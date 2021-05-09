import torch
from torch import autograd, nn
import sys, getopt

num_series = []
for i in range(1,11):
    num_series.append(i)

batch_size = 1 #number of samples processed before the model is updated
seq_len = i-1 #length of the input that will be fed to the network
input_size = i
hidden_size = i+3

#define embedding
embedding = nn.Embedding(input_size, hidden_size)

rnn = torch.nn.RNN(
    input_size =input_size+3, #The number of expected features in the input 
    hidden_size=hidden_size, #The number of features in the hidden state 
    num_layers=1, #Number of recurrent layers.
    nonlinearity='tanh' #The non-linearity to use.

)

input = autograd.Variable(
    torch.LongTensor(num_series[:-1]).view(seq_len,batch_size)
)

target = autograd.Variable(
    torch.LongTensor(num_series[1:]).view(seq_len,batch_size)
)

print('input', input)
print('target', target)

parameters = rnn.parameters()
optimizer = torch.optim.Adam(parameters)


def decode_output(tensor):
    decoded = []
    str_tensor=str(tensor)
    i=0
    while(i!=len(str_tensor)):
        if(str_tensor[i].isdigit()):
            if(str_tensor[i+1].isdigit()):
                decoded.append(int(str_tensor[i]+str_tensor[i+1]))
                i=i+1
            else:
                decoded.append(int(str_tensor[i]))
        i=i+1
    print('Next number in given series: ', decoded[-1])
    print('\n')

def train():
    epoch = 0
    while True:
        embedded_input = embedding(input)
        state = autograd.Variable(torch.zeros(1,batch_size, hidden_size))
        out, state = rnn(embedded_input, state)
        out_unembedded = out.view(-1, hidden_size)
        misc, pred = out_unembedded.max(1)
        loss = torch.nn.functional.nll_loss(out_unembedded,target.view(-1))
        if epoch % 50 == 0:
            print('epoch',epoch)
            print('input', input.data.view(1,-1))
            print('target', target.data.view(1,-1))
            print ('pred ', pred.data.view(1,-1))
            print('loss',loss.data.view(1,-1))
        rnn.zero_grad()
        loss.backward()
        optimizer.step()
        if(epoch == i*350):
            break
        epoch +=1

def predict(new_series):
    print('Given number sequence: ',new_series)
    new_input = autograd.Variable(
    torch.LongTensor(new_series).view(len(new_series),batch_size)
    )
    embedded_input = embedding(new_input)
    state = autograd.Variable(torch.zeros(1,batch_size, hidden_size))
    out, state = rnn(embedded_input, state)
    out_unembedded = out.view(-1, hidden_size)
    misc,prediction = out_unembedded.max(1)
    print('new prediction', prediction)
    decode_output(prediction)

def predictions():
    
    print('\n')
    series_01 = [1,2,3]
    predict(series_01)

    #shorter sequence -> usually worse prediction
    series_02 = [3,4]
    predict(series_02)

    series_03 = [6,7,8,9]
    predict(series_03)

    series_04 = [1,2,3,4,5,6,7]
    predict(series_04)



if __name__ == "__main__":
   train()
   predictions()
