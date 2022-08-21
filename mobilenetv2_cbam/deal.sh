cat train.log|grep "Train" > Train_top1.txt
cat Train_top1.txt |grep "Avg" > Train_avg_top1.txt
rm Train_top1.txt

cat train.log|grep "Eval" > Val_top1.txt
cat Val_top1.txt |grep "Avg" > Val_avg_top1.txt
rm Val_top1.txt

