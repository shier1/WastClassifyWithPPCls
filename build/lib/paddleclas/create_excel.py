from tokenize import Triple
import pandas as pd

# mobilenetv2_cbam_train = pd.DataFrame(columns=['epoch', 'top1', 'loss'])
# mobilenetv2_cbam_val = pd.DataFrame(columns=['epoch', 'top1', 'loss'])

# mobilenetv2_train = pd.DataFrame(columns=['epoch', 'top1', 'loss'])
# mobilenetv2_val = pd.DataFrame(columns=['epoch', 'top1', 'loss'])



# with open('mobilenetv2/Train_avg_top1.txt', 'r') as f:
#     for line in f:
#         top1 = eval(line.split(' ')[6].strip(','))
#         loss = eval(line.split(' ')[-1])
#         epoch = eval(line.split('/')[2].split(' ')[-1])
#         mobilenetv2_train=mobilenetv2_train.append({'epoch':epoch, 'top1':top1, 'loss':loss}, ignore_index=True)
        

# with open('mobilenetv2/Val_avg_top1.txt', 'r') as f:
#     for line in f:
#         top1 = eval(line.split(' ')[-1])
#         loss = eval(line.split(' ')[-3].rstrip(','))
#         epoch = eval(line.split('][')[1].split(' ')[-1])
#         mobilenetv2_val=mobilenetv2_val.append({'epoch':epoch, 'top1':top1, 'loss':loss}, ignore_index=True)


# with open('mobilenetv2_cbam/Train_avg_top1.txt', 'r') as f:
#     for line in f:
#         top1 = eval(line.split(' ')[6].strip(','))
#         loss = eval(line.split(' ')[-1])
#         epoch = eval(line.split('/')[2].split(' ')[-1])
#         mobilenetv2_cbam_train=mobilenetv2_cbam_train.append({'epoch':epoch, 'top1':top1, 'loss':loss}, ignore_index=True)

# with open('mobilenetv2_cbam/Val_avg_top1.txt', 'r') as f:
#     for line in f:
#         top1 = eval(line.split(' ')[-1])
#         loss = eval(line.split(' ')[-3].rstrip(','))
#         epoch = eval(line.split('][')[1].split(' ')[-1])
#         mobilenetv2_cbam_val=mobilenetv2_cbam_val.append({'epoch':epoch, 'top1':top1, 'loss':loss}, ignore_index=True)


# mobilenetv2_cbam_train.to_excel('mobilenetv2_cbam_train.xls')
# mobilenetv2_cbam_val.to_excel('mobilenetv2_cbam_val.xls')
# mobilenetv2_train.to_excel('mobilenetv2_train.xls')
# mobilenetv2_val.to_excel('mobilenetv2_val.xls')

mobilenetv1_train = pd.DataFrame(columns=['epoch', 'top1', 'loss'])
mobilenetv1_val = pd.DataFrame(columns=['epoch', 'top1', 'loss'])

with open('mobilenetv1/Train_avg_top1.txt', 'r') as f:
    for line in f:
        top1 = eval(line.split(' ')[6].strip(','))
        loss = eval(line.split(' ')[-1])
        epoch = eval(line.split('/')[2].split(' ')[-1])
        mobilenetv1_train=mobilenetv1_train.append({'epoch':epoch, 'top1':top1, 'loss':loss}, ignore_index=True)

with open('mobilenetv1/Val_avg_top1.txt', 'r') as f:
    for line in f:
        top1 = eval(line.split(' ')[-1])
        loss = eval(line.split(' ')[-3].rstrip(','))
        epoch = eval(line.split('][')[1].split(' ')[-1])
        mobilenetv1_val=mobilenetv1_val.append({'epoch':epoch, 'top1':top1, 'loss':loss}, ignore_index=True)

mobilenetv1_train.to_excel('mobilenetv1_train.xls')
mobilenetv1_val.to_excel('mobilenetv1_val.xls')