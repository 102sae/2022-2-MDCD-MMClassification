#meta안에 .txt파일에 write
import os

#class_name=['공인본','증도가']
dataset_path='/content/drive/MyDrive/Colab Notebooks/MMClassification/configs/custom_jh/helper/data'
folder_name=['train','test','val']

for x in folder_name:
  
    file_lst=os.listdir(os.path.join(dataset_path,x)+'/'+'공인본')
    file_lst2=os.listdir(os.path.join(dataset_path,x)+'/'+'증도가')
    out_path=os.path.join(dataset_path,'meta')
    with open(out_path+'/'+x+'.txt','w',encoding='utf-8')as f:
      f.truncate()
      for x in file_lst:
        f.write('공인본/'+x+' 0'+'\n')
      for x in file_lst2:
        f.write('증도가/'+x+' 1'+'\n')

      f.close()

