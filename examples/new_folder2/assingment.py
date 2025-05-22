'''#creating files
with open('filea.txt', 'w') as file:
    file.write('This is data in filea.\n')
    file.write('self practice')

with open('fileb.txt', 'w') as file:
    file.write("This is data in fileb")

#reading files
with open('filea.txt', 'r') as file:
    content1 = file.read()
    print(content1)

with open('filea.txt', 'r') as file:
    content2 = file.read()
    print(content2)


##merging two files into third file
#opening file1 and file2
with open('filea.txt', 'r') as file1, open('fileb.txt', 'r') as file2:
    content1=file1.read()
    content2=file2.read()
#merging two files into new file
with open('merged.txt', 'w') as merged_file:
    merged_file.write(content1)
    merged_file.write('\n')
    merged_file.write(content2)
#reading new file
with open('merged.txt', 'r') as file:
    con=file.read()
    print(con)
#merging two files line by line
with open('filea.txt') as f1, open('fileb.txt') as f2, open('merge.txt', 'w') as mf:
    for line in f1:
        mf.write(line)
    mf.write('\n')
    for line in f2:
        mf.write(line)
'''

#copying content from one file to another
import shutil
shutil.copy('merged.txt', 'dup_merged.txt')
#reading
with open('dup_merged.txt', 'r') as file:
    cont=file.read()
    print(cont)

