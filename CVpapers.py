lenet - 5 for handwritten digits 
image 32 * 32 * 1-> filter 5 * 5 * 1 -> avg pool f = 2 s = 2 ->filter 5*5*1 -> avg pooling f = 2 s = 2 -> filter 5*5*16 -> dense layer -> dense layer -> softmax
alexnet 227 * 227 * 3
filter 55 * 55 * 96 ->  
vgg - 16 weighted layers 
conv 3  83 s =1 max_pool  = 2*2 , s=2
image-> conv 64 * 2-> pool -> conv 2-> pool -> conv *3 ->pool->conv * 3 -> pool ->conv*3
deep networks are bad due to loseing gradient residual block
a -> linear -> relu -> linera -> relu -> output.
residual block : skiping a layer 
  al -> (skip linear and reau) -> al + linear -> relu 
  
