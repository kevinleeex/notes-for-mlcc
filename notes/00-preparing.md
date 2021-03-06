# 第0节 前提准备(Preparing)

## 0.1. Pandas 使用入门

机器学习速成课程中的编程练习使用 [Pandas](http://pandas.pydata.org/) 库来操控数据集。如果您不熟悉 Pandas，建议您先学习[Pandas 简介](https://colab.research.google.com/notebooks/mlcc/intro_to_pandas.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=pandas-colab&hl=zh-cn)教程，该教程介绍了练习中使用的主要 Pandas 功能。编程参看[hello_pandas.ipynb](./hello_pandas.ipynb)

## 0.2. 低阶 TensorFlow 基础知识

机器学习速成课程中的编程练习使用 TensorFlow 的高阶 [tf.estimator API](https://www.tensorflow.org/api_docs/python/tf/estimator/Estimator) 来配置模型。如果您有兴趣从头开始构建 TensorFlow 模型，请学习以下教程：

- [TensorFlow Hello World](https://colab.research.google.com/notebooks/mlcc/hello_world.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=helloworld-colab&hl=zh-cn)：在低阶 TensorFlow 中编码的“Hello World”。编程参看[hello_tf.ipynb](../code/hello_tf.ipynb)
- [TensorFlow 编程概念](https://colab.research.google.com/notebooks/mlcc/tensorflow_programming_concepts.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=tfprogconcepts-colab&hl=zh-cn)：演示了 TensorFlow 应用中的基本组件：张量、指令、图和会话。
- [创建和操控张量](https://colab.research.google.com/notebooks/mlcc/creating_and_manipulating_tensors.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=tensors-colab&hl=zh-cn)：张量快速入门 - TensorFlow 编程中的核心概念。此外，还回顾了线性代数中的矩阵加法和乘法概念。编程参看[tensors_in_tf.ipynb](../code/tensors_in_tf.ipynb)

## 0.3. 主要概念和工具

机器学习速成课程中介绍并应用了以下概念和工具。有关详情，请参阅链接的资源。

### 0.3.1. 数学

#### 代数

- [变量](https://www.khanacademy.org/math/algebra/introduction-to-algebra/alg1-intro-to-variables/v/what-is-a-variable)、[系数](https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-equivalent-exp/cc-6th-parts-of-expressions/v/expression-terms-factors-and-coefficients)和[函数](https://www.khanacademy.org/math/algebra/algebra-functions)
- [线性方程式](https://wikipedia.org/wiki/Linear_equation)，例如 y=b+w1x1+w2x2
- [对数](https://wikipedia.org/wiki/Logarithm)和对数方程式，例如 y=ln(1+ez)
- [S 型函数](https://wikipedia.org/wiki/Sigmoid_function)

#### 线性代数

- [张量和张量等级](https://www.tensorflow.org/programmers_guide/tensors)
- [矩阵乘法](https://wikipedia.org/wiki/Matrix_multiplication)

#### 三角学

- [Tanh](https://reference.wolfram.com/language/ref/Tanh.html)（作为[激活函数](https://developers.google.com/machine-learning/glossary#activation_function)进行讲解，无需提前掌握相关知识）

#### 统计信息

- [均值、中间值、离群值](https://www.khanacademy.org/math/probability/data-distributions-a1/summarizing-center-distributions/v/mean-median-and-mode)和[标准偏差](https://wikipedia.org/wiki/Standard_deviation)
- 能够读懂[直方图](https://wikipedia.org/wiki/Histogram)

#### 微积分（可选，适合高级主题）

- [导数](https://wikipedia.org/wiki/Derivative)概念（您不必真正计算导数）
- [梯度](https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/gradient-and-directional-derivatives/v/gradient)或斜率
- [偏导数](https://wikipedia.org/wiki/Partial_derivative)（与梯度紧密相关）
- [链式法则](https://wikipedia.org/wiki/Chain_rule)（带您全面了解用于训练神经网络的[反向传播算法](https://developers.google.com/machine-learning/crash-course/backprop-scroll/)）

## 0.4. Python 编程

### 0.4.1. 基础 Python

[Python 教程](https://docs.python.org/3/tutorial/)中介绍了以下 Python 基础知识：

- [定义和调用函数](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)：使用位置和[关键字](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)参数
- [字典](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)、[列表](https://docs.python.org/3/tutorial/introduction.html#lists)、[集合](https://docs.python.org/3/tutorial/datastructures.html#sets)（创建、访问和迭代）
- [`for` 循环](https://docs.python.org/3/tutorial/controlflow.html#for-statements)：包含多个迭代器变量的 `for` 循环（例如 `for a, b in [(1,2), (3,4)]`）
- [`if/else` 条件块](https://docs.python.org/3/tutorial/controlflow.html#if-statements)和[条件表达式](https://docs.python.org/2.5/whatsnew/pep-308.html)
- [字符串格式](https://docs.python.org/3/tutorial/inputoutput.html#old-string-formatting)（例如 `'%.2f' % 3.14`）
- 变量、赋值、[基本数据类型](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)（`int`、`float`、`bool`、`str`）
- [`pass` 语句](https://docs.python.org/3/tutorial/controlflow.html#pass-statements)

### 0.4.2. 中级 Python

[Python 教程](https://docs.python.org/3/tutorial/)还介绍了以下更高级的 Python 功能：

- [列表推导式](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Lambda 函数](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)

## 0.5. 第三方 Python 库

机器学习速成课程代码示例使用了第三方库提供的以下功能。无需提前熟悉这些库；您可以在需要时查询相关内容。

### 0.5.1. [Matplotlib](http://matplotlib.org/contents.html)（适合数据可视化）

- [`pyplot`](http://matplotlib.org/api/pyplot_api.html) 模块
- [`cm`](http://matplotlib.org/api/cm_api.html) 模块
- [`gridspec`](http://matplotlib.org/api/gridspec_api.html) 模块

### 0.5.2. [Seaborn](http://seaborn.pydata.org/index.html)（适合热图）

- [`heatmap`](http://seaborn.pydata.org/generated/seaborn.heatmap.html) 函数

### 0.5.3. [Pandas](http://pandas.pydata.org/)（适合数据处理）

- [`DataFrame`](http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe) 类

### 0.5.4. [NumPy](http://www.numpy.org/)（适合低阶数学运算）

- [`linspace`](https://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.linspace.html) 函数
- [`random`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.random.html#numpy.random.random) 函数
- [`array`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html) 函数
- [`arange`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html) 函数

### 0.5.5. [scikit-learn](http://scikit-learn.org/)（适合评估指标）

- [metrics](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics) 模块

## 0.6. Bash 终端/云端控制台

要在本地计算机上或云端控制台中运行编程练习，您应该能熟练使用命令行：

- [Bash 参考手册](https://tiswww.case.edu/php/chet/bash/bashref.html)
- [Bash 快速参考表](https://github.com/LeCoupa/awesome-cheatsheets/blob/master/languages/bash.sh)
- [了解 Shell](http://www.learnshell.org/)



## 导航

[返回目录](../README.md) | 上一节 | [下一节 01-Framing](./01-framing.md)

