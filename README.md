# Python 数据科学

## 介绍
b站 AI日日新 不定期更新使用Python框架完成机器学习、深度学习、数据科学任务。配套视频见[b站合集](https://www.bilibili.com/video/BV1pHd8YiERd/?spm_id_from=333.1387.homepage.video_card.click&vd_source=06eafedcfca50f6eabb7b3d6b61ecfe3)


## python的windows环境

1. 下载[python3.10](https://www.python.org/downloads/release/python-31011/)，注意选择`Windows installer (64-bit)`，在安装指引中记得勾选将python添加到路径
2. 安装目前最流行的编辑器 [vs code](https://code.visualstudio.com/Download#)，在安装指引中记得将vs code添加到path路径，并开启右键打开文件夹功能，按照安装提示完成安装后即可打开该软件，然后你需要安装 `Chinese (Simplified)` 【汉化插件】、`python`【微软官方python语言支持】、`Ruff`【格式化和语法】、`Material Icon Theme`【文件标签】、`jupyter`【notebook支持】
3. 安装完以上两个工具就已经ok了，然后我们新建一个文件夹，然后在文件夹内右键选择vs code打开。接着选择左上角的`查看` --> `终端`可以在打开的窗口运行命令
4. pip命令是python自带的包管理工具，我们需要替换pip源来提升下载速度，请运行如下命令更换源：`pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple`
5. 然后请再安装`uv`，它是比pip更快更强大的包管理工具，运行如下命令：`pip install uv`。然后让我们创建一个虚拟环境：`uv venv`，并且你可以初始化项目：`uv init`，还有使用与pip兼容的安装命令`uv pip install <your_package>`，或者你可以使用`uv add <your_package>`安装。因为uv的镜像配置跟pip不一致，你可以参考我当前项目下的`pyproject.toml`为当前项目配置镜像源，还有更多功能请前往[uv官网](https://docs.astral.sh/uv/)查看
6. 你可以使用 `uv sync` 命令同步本项目的依赖


## 自然语言处理
### 文本分类
文本分类是将文本划分为不同的类别的任务，例如垃圾邮件过滤、新闻文章分类等。我们将使用transformers框架来完成文本分类，它可以非常轻松的训练多种领域的模型，是我们必须学习的库，对应的notebook在[notebooks/文本分类.ipynb](notebooks/文本分类.ipynb)

### 实体识别
实体识别，也称为命名实体识别（Named Entity Recognition，简称NER），是自然语言处理（NLP）的一个组成部分，用于识别文本中具有特定意义的实体。这些实体可以包括人名、地名、机构名、专有名词等，并且还可能涵盖时间、数量和其他预定义类别。我们同样将使用transformers框架来完成实体识别。对应的notebook在[notebooks/实体识别.ipynb](notebooks/实体识别.ipynb)

### 端到端文本生成
端到端文本生成（Text-to-Text Generation） 是一种自然语言处理（NLP）任务，其核心目标是将一段输入文本自动转换为另一段输出文本。这种转换可以是对原文的改写、总结、翻译、问答、复述等多种形式。对应的notebook在[notebooks/端到端文本生成.ipynb](notebooks/端到端文本生成.ipynb)



## 计算机视觉
### 图像分类
图像分类被用来开发图像识别应用程序，这些程序可以识别动物、植物、汽车车型、水果、蔬菜等，并且像iPhone这样的智能手机也利用这项技术实现照片的自动分类功能。对应的notebook在[notebooks/图像分类.ipynb](notebooks/图像分类.ipynb)

### 视频分类
视频分类能够帮助在线视频平台自动识别上传视频的内容类型，如体育、音乐、电影等，从而实现高效的视频管理和快速检索。对应的notebook在[notebooks/视频分类.ipynb](notebooks/视频分类.ipynb)




## 表格中的机器学习
### 聚类
聚类作为一种无监督学习方法，在多个领域有着广泛的应用。例如，在图像处理领域，聚类被用作图像分割的重要方法之一，除了图像处理之外，聚类分析还在文本挖掘、生物信息学等多个领域发挥了重要作用。对应的notebook在[notebooks/聚类.ipynb](notebooks/聚类.ipynb)

### 分类
分类的作用主要是将输入数据分配到预定义的类别中。这种分类任务是监督学习的一种形式。数字格式分类的核心作用是通过对数值型数据的学习和建模，预测新数据所属的类别。例如：金融领域 ：根据用户的信用评分（数值型数据）判断其贷款申请是否通过（高风险/低风险）。对应的notebook在[notebooks/分类.ipynb](notebooks/分类.ipynb)

### 回归
回归在机器学习的回归问题中有着广泛的应用，这些应用涵盖了多个领域。例如，可以使用回归模型来进行财务绩效预测、能耗预测以及制造工艺参数的预测等。对应的notebook在[notebooks/回归.ipynb](notebooks/回归.ipynb)

### 时间序列预测
时间序列预测的作用主要体现在通过对历史数据的分析来推测未来的趋势和模式。在实际应用中，时间序列预测被广泛用于多个领域，例如金融市场、经济预测、物联网数据处理、库存管理和生产调度等。对应的notebook在[notebooks/时间序列预测.ipynb](notebooks/时间序列预测.ipynb)



## 常用框架
### transformers库
[transformers库](https://hf-mirror.com/docs/transformers/index)。Transformers库能够完成多种自然语言处理（NLP）任务，包括但不限于文本生成、命名实体识别、情感分析、翻译、摘要等。此外，Transformers库不仅限于NLP领域，它还包含了用于计算机视觉任务的现代卷积网络等模型。通过使用Transformers库提供的pipeline函数，可以方便地执行上述任务，同时也支持用户深入定制和开发新的模型应用

### sklearn库
[Sklearn（scikit-learn）](https://scikit-learn.org/stable/index.html)是一个功能强大的机器学习库，能够完成多种任务，主要包括以下几类：
1. 回归 ：用于预测连续值的输出，比如房价预测或温度预测等
2. 聚类 ：将数据划分为不同的群组，使得同一群组内的数据相似度较高，而不同群组之间的差异较大。例如客户分群分析
3. 降维 ：减少数据集的变量数量，同时保留尽可能多的信息，常用于可视化和加速计算。例如主成分分析（PCA）
4. 分类 ：通过已有的带标签数据训练模型，对新数据进行类别预测。例如，判断一封邮件是否为垃圾邮件

### autogluon库
[AutoGluon](https://auto.gluon.ai/stable/index.html)库能够完成多种机器学习任务，包括但不限于：
1. 自动预处理 ：在处理数据时，AutoGluon可以自动识别任务类型，并对特征进行预处理，简化了数据准备阶段的工作
2. 超参数调优 ：AutoGluon能自动进行超参数调优，使得开发者无需深入理解每一种算法的细节也能构建高效的模型
3. 模型选择与集成 ：AutoGluon能够在多个不同类型的机器学习模型中进行选择，并根据问题的性质自动进行模型的组合与集成，以提高预测性能


## 论文
### resnet论文
[Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)

### transformer论文
[Attention Is All You Need](https://arxiv.org/abs/1706.03762)

### bert论文
[BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)

### T5论文
[Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683)

### vllm论文
[Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)

### sglang论文
[SGLang: Efficient Execution of Structured Language Model Programs](https://arxiv.org/abs/2312.07104)

### dinov2论文
[DINOv2: Learning Robust Visual Features without Supervision](https://arxiv.org/abs/2304.07193)

### lert论文
[LERT: A Linguistically-motivated Pre-trained Language Model](https://arxiv.org/abs/2211.05344)

### mengzi系列论文
[Mengzi: Towards Lightweight yet Ingenious Pre-trained Models for Chinese](https://arxiv.org/abs/2110.06696)

### 随机森林论文
[Random Forests](https://link.springer.com/article/10.1023/A:1010933404324)