#structurede array
import numpy as np
#defining dtype with field names and types
student_dtype = np.dtype([
    ('stno', 'i4'),
    ('stname', 'U8'),
    ('subj1', 'f8'),
    ('subj2', 'f8'),
    ('subj3', 'f8'),
    ('ttlmarks', 'f8'),
    ('avg', 'f4'),
    ('grade', 'U2')
])

#creating array using dtype
raw_data= [
    (1, 'abc', 76.5, 83, 65 ),
    (2,'def', 99,74,37.5),
    (3,'tyu',88,90,31.5)
]

# Prepare the structured array with calculated fields
students=np.empty(len(raw_data), dtype=student_dtype)

for i,(stno,stname,subj1,subj2,subj3) in enumerate(raw_data):
    ttlmarks=subj1+subj2+subj3
    avg = ttlmarks / 3

    if avg >= 90:
        grade = "A"
    elif avg >=80:
        grade = 'B'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    students[i]=(stno, stname, subj1, subj2, subj3, ttlmarks, avg, grade)

#write to a file
with open('student_details.txt', 'w') as file:
    file.write('stno  stname     subj1  subj2  subj3  ttlmarks   avg             garde\n')
    for s in students:
        file.write(f"{s['stno']}      {s['stname']:10}  {s['subj1']}  {s['subj2']}  {s['subj3']}   {s['ttlmarks']}     {s['avg']:.2f}   {s['grade']}\n")


#reading 
with open('student_details.txt', 'r') as file:
   for line in file:
       print(line.strip())