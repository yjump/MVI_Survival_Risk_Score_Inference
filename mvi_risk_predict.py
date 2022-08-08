import pandas as pd
import numpy as np

train_df = pd.read_csv('./Input_Patient_Info.csv')
train_feature_df = train_df[["MVI_Stage","MVI_Area_Stage","Tumor_Diameter","Liver_Cirrhosis"]]
train_y_df = train_df[["Death_Flag","Survival_Months"]]

#List of tuples
aux = [(e1,e2) for e1,e2 in train_y_df.values]
#Structured array
new_train_y = np.array(aux, dtype=[('Status', '?'), ('Survival_in_Months', 'float32')])

import torch
from torch import nn

x_train = train_feature_df.values.astype('float32')
y_train_time = train_y_df["Survival_Months"].values.astype('float32')
y_train_flag = train_y_df["Death_Flag"].values.astype('float32')  

net = nn.Sequential(
    nn.Linear(4, 20),
    nn.BatchNorm1d(20),
    nn.Tanh(),
    nn.Dropout(0.8),
    nn.Linear(20, 1),
    nn.Tanh(),
    nn.Dropout(0.8),
    )


net.load_state_dict(torch.load('./ai_model_best.pt'))
train_x = torch.from_numpy(x_train)
train_y_time = torch.from_numpy(y_train_time)
train_y_flag = torch.from_numpy(y_train_flag)
net.eval()
pred = net(train_x)
pred = pred.detach().numpy()
train_df['MVI_AI_Risk']=np.array(pred) 
train_df.to_csv('./Output_Patient_Info_with_Risk_Score.csv',index=False)
print("The output file of the patients' survival risk scores has been written!")

