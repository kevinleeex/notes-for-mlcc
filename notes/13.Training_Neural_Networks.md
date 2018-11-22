学习目标：

- 了解反向传播算法

## 训练神经网络

**反向传播算法(Back propagation)**是最常见的一种神经网络训练算法，一个直观的可视化的例子：[反向传播直观解释](https://google-developers.appspot.com/machine-learning/crash-course/backprop-scroll/)

### 失败案例(Failure Cases)

下面展示了几种常见的BP出错的情况

- **梯度消失**

  靠近输入层(较低层)的梯度可能会变得非常小。在深度网络中，计算这些梯度时，可能会涉及许多小项的乘积。

  当较低层的梯度逐渐消失到0时，这些层的训练速度会非常缓慢，甚至停止训练。

  **ReLU激活函数有助于防止梯度消失。**

- **梯度爆炸**

  如果网络中的权重过大，则在较低层的梯度会涉及许多大项的乘积。在这种情况下，梯度就会爆炸：梯度过大会导致模型难以收敛。

  **批标准化(Batch-Nomalization)可以降低学习速率，有助于防止梯度爆炸。**

- **ReLU单元消失**

  一旦ReLU单元的加权和低于0，ReLU单元就可能会停滞。它会输出对网络没有任何贡献的0激活，而梯度在反向传播算法期间将无法再从中流过。梯度的来源被切断，ReLU的输入可能无法作出足够的改变来使加权和恢复到0以上。

  **降低学习速率有助于防止ReLU单元消失**。
### Dropout正则化

**丢弃(Dropout)**是另一种形式的正则化，可用于神经网络。工作原理是，在梯度下降法的**每一步**中随机丢弃一些网络单元。丢弃得越多，正则化效果越强：

- **0.0:** 无丢弃正则化
- **1.0**: 丢弃所有内容，模型学不到任何内容
- **0.0~1.0**之间的值更有用

### 最佳实践(Best Practices)

- ReLU
- Batch-Normalization
- Small Learning Rate
- Dropout

编程参见[improving_nn_performance.ipynb](../code/improving_nn_performance.ipynb)