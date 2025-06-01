import logging
from logging.handlers import TimedRotatingFileHandler
import torch
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from transformers import pipeline
import secrets
from functools import lru_cache
from config import settings
import sys
from pathlib import Path
import time


# 1. 设置天级别日志轮转
def setup_logging():
    """配置天级别轮转的日志系统"""
    log_dir = Path(settings.LOG_DIR)
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "text_classification.log"

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    file_handler = TimedRotatingFileHandler(
        filename=log_file,
        when="midnight",
        interval=1,
        backupCount=settings.LOG_RETENTION_DAYS,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    file_handler.suffix = "%Y-%m-%d.log"

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(settings.LOG_LEVEL)

    # 清除现有处理器
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


# 初始化日志
setup_logging()
logger = logging.getLogger(__name__)


# 2. 自动重启装饰器
def auto_restart(max_retries=3, delay=5):
    """自动重启装饰器"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    retries += 1
                    logger.error(f"程序崩溃 (尝试 {retries}/{max_retries}): {str(e)}")
                    if retries < max_retries:
                        logger.info(f"{delay}秒后重启...")
                        time.sleep(delay)
            logger.critical("达到最大重启次数，程序终止")
            sys.exit(1)

        return wrapper

    return decorator


# 创建FastAPI应用
app = FastAPI(
    title="文本分类API", description="提供文本分类服务的API接口", version="1.0.0"
)

security = HTTPBasic()


# 请求模型
class TextClassificationRequest(BaseModel):
    text: str


# 响应模型
class TextClassificationResponse(BaseModel):
    message: str
    label: str
    score: float


# 缓存模型加载
@lru_cache(maxsize=1)
def load_classifier():
    try:
        classifier = pipeline(
            task="text-classification",
            model=settings.MODEL_PATH,
            truncation=True,
            max_length=512,
            torch_dtype=torch.float16,
            device="cuda" if torch.cuda.is_available() else "cpu",
            use_fast=True,
        )
        logger.info("模型加载成功")
        return classifier
    except Exception as e:
        logger.error(f"模型加载失败: {str(e)}")
        raise


# 验证用户凭证
def verify_credentials(credentials: HTTPBasicCredentials):
    correct_username = secrets.compare_digest(
        credentials.username.encode("utf8"), settings.API_USERNAME.encode("utf8")
    )
    correct_password = secrets.compare_digest(
        credentials.password.encode("utf8"), settings.API_PASSWORD.encode("utf8")
    )
    if not (correct_username and correct_password):
        logger.warning(f"无效的登录尝试: {credentials.username}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效的用户名或密码",
            headers={"WWW-Authenticate": "Basic"},
        )


# 加载分类器
classifier = load_classifier()


@app.post("/text_classification", response_model=TextClassificationResponse)
async def classify_text(
    request: TextClassificationRequest,
    credentials: HTTPBasicCredentials = Depends(security),
):
    """文本分类端点"""
    try:
        verify_credentials(credentials)
        logger.info(f"处理文本分类请求，文本长度: {len(request.text)}")

        pipe_result = classifier(request.text)
        label = pipe_result[0]["label"]
        score = float(pipe_result[0]["score"])

        return TextClassificationResponse(message="请求成功", label=label, score=score)
    except Exception as e:
        logger.error(f"处理请求时出错: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="处理请求时发生错误",
        )


# 3. 程序入口点，包含自动重启逻辑
@auto_restart(max_retries=settings.MAX_RETRIES, delay=settings.RESTART_DELAY)
def run_server():
    import uvicorn

    logger.info(f"启动服务，监听 {settings.HOST}:{settings.PORT}")
    uvicorn.run(
        app,
        host=settings.HOST,
        port=settings.PORT,
        workers=settings.WORKERS,
        log_config=None,  # 禁用uvicorn默认日志，使用我们的配置
    )


if __name__ == "__main__":
    # 添加启动日志
    logger.info("=" * 50)
    logger.info("应用程序启动")
    logger.info(f"日志级别: {settings.LOG_LEVEL}")
    logger.info(f"日志保留天数: {settings.LOG_RETENTION_DAYS}")
    logger.info(f"最大重启次数: {settings.MAX_RETRIES}")
    logger.info("=" * 50)

    try:
        run_server()
    except KeyboardInterrupt:
        logger.info("接收到中断信号，程序正常退出")
    except Exception as e:
        logger.critical(f"未捕获的异常导致程序退出: {str(e)}", exc_info=True)
