> 学习目标：
>
> - TensorFlow和Pandas的一些基本操作
> - 使用TensorFlow高级API

# 第3节 使用TensorFlow工具包

## 3.1. 层次结构
- 层次结构

  ![image-20181109153904778](assets/image-20181109153904778.png)
  **图 1. TensorFlow 工具包层次结构。**

| 工具包                         | 说明                   |
| ------------------------------ | ---------------------- |
| Estimator (tf.estimator)       | 高级 OOP API。         |
| tf.layers/tf.losses/tf.metrics | 用于常见模型组件的库。 |
| TensorFlow                     | 低级 API               |


- TF由下面两个组件组成
  - 图协议缓冲区
  - 执行图的运行时
  > 这两个组件类似于Java编译器和JVM



## 3.2. tf.estimator API

```tf.estimator```与scikit-learn API兼容。

```python
import tensorflow as tf

# Set up a linear classifier.
classifier = tf.estimator.LinearClassifier()

# Train the model on some example data.
classifier.train(input_fn=train_input_fn, steps=2000)

# Use it to predict.
predictions = classifier.predict(input_fn=predict_input_fn)
```





编程参看[first_step_with_tensorflow.ipynb](../code/first_step_with_tensorflow.ipynb)

