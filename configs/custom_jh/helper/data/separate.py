#train과 test 8:2 비율

import os 
import shutil

dataset_path='/content/drive/MyDrive/Colab Notebooks/MMClassification/configs/custom_jh/helper/data'
dir_name=['공인본','대구개인본']
folder=['train','test','val']

for x in folder:
  for y in dir_name:
    file_lst=os.listdir(os.path.join(dataset_path,y))
    out_dir=os.path.join(dataset_path,x)+'/'+y
    if not os.path.exists(out_dir):
      os.mkdir(out_dir)
    if x=='train':

      file_lst1=[file_lst[i] for i in range(0,int(len(file_lst)*0.8)-1)]
      
      #file_lst1=[file_lst[i] for i in range(0,int(len(file_lst)*0.4)-1)]
      for k in file_lst1:
        shutil.copy(os.path.join(dataset_path,y)+'/'+k,out_dir)
    elif x=='test' or x=='val':
      file_lst2=[file_lst[i] for i in range(int(len(file_lst)*0.8),len(file_lst)-1)]
      #file_lst2=[file_lst[i] for i in range(int(len(file_lst)*0.4),int(len(file_lst)*0.7))]
      for k in file_lst2:
        shutil.copy(os.path.join(dataset_path,y)+'/'+k,out_dir)



    

        