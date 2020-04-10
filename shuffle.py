from sklearn.model_selection import train_test_split
import glob,os,pathlib
import shutil,random

folder_path='/home/shanto/Documents/TigerITML/Labeled Numberplate voc'
train_path='/home/shanto/Documents/TigerITML/images/train'
test_path='/home/shanto/Documents/TigerITML/images/test'


file_names=[file.split('/')[-1] for file in glob.glob(os.path.join(folder_path,"*.xml"))]
label=[0 for file in range(len(file_names))]
#random.shuffle(file_names)

# for file in glob.glob(os.path.join(folder_path,"*.txt")):
#     print()

# file_list = list(pathlib.Path(folder_path).glob("*.jpg"))
# print(file_list)

os.makedirs(train_path,exist_ok=True)
os.makedirs(test_path,exist_ok=True)

X_train, X_test, y_train, y_test = train_test_split(file_names, label, test_size=0.2,shuffle=True)

print("Total : {}, Train : {}, Test : {}".format(len(file_names),len(X_train),len(X_test)))

for train in X_train:
    base_name=train.split('.')[0]
    shutil.copy(os.path.join(folder_path,train),train_path)
    shutil.copy(os.path.join(folder_path,base_name+'.jpg'),train_path)

for test in X_test:
    base_name=test.split('.')[0]
    shutil.copy(os.path.join(folder_path,test),test_path)
    shutil.copy(os.path.join(folder_path,base_name+'.jpg'),test_path)