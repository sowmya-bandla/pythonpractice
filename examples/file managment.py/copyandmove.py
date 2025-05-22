import shutil
shutil.copy('example.txt', 'dup.txt')
#checking copy of file 
with open('dup.txt', 'r') as file:
    con=file.read()
    print(con)


#moving file 
shutil.move('dup.txt', 'new_folder/dup.txt')