# Sequence-to-Sequence-Learning

In this project we will be teaching a neural network to End-to-End Learning with English.


![encode_decode](https://cloud.githubusercontent.com/assets/27130785/26065105/2318bc24-39a8-11e7-84c3-4a9c0c484cbe.png)






[KEY: > input, = target, < output]
> who wants this ?
= who wants this ?
< who wants this ?

This is made possible by the simple but powerful idea of the `sequence to sequence network <http://arxiv.org/abs/1409.3215>`__, in which two recurrent neural networks work together to transform one sequence to another. An encoder network condenses an input sequence into a vector, and a decoder network unfolds that vector into a new sequence.

To improve upon this model we'll use an `attention mechanism <https://arxiv.org/abs/1409.0473>`__, which lets the decoder learn to focus over a specific range of the input sequence.

**Recommended Reading:**

I assume you have at least installed PyTorch, know Python, and
understand Tensors.
And for more, read the papers that introduced these topics:
-  `Learning Phrase Representations using RNN Encoder-Decoder for
   Statistical Machine Translation <http://arxiv.org/abs/1406.1078>`__
-  `Sequence to Sequence Learning with Neural
   Networks <http://arxiv.org/abs/1409.3215>`__
-  `Neural Machine Translation by Jointly Learning to Align and
   Translate <https://arxiv.org/abs/1409.0473>`__
-  `A Neural Conversational Model <http://arxiv.org/abs/1506.05869>`__
