import os
import pathlib
import sqlite3

direct = input("Enter Directory: ")
def countlines(directory = direct, lines=0, ext="*", skip_blank=False):
    filelist = []
    rootlist = []
    
    for root, dirs, files in os.walk(directory):
        # loop through the files
        rootlist.append(root)
        for filename in files:
            
            file = os.path.join(root, filename)
            filelist.append(file)
            
            try:
                with open(file, "r", encoding="utf-8") as f:
                    if skip_blank:
                        
                        new_lines = len([i for i in f.readlines() if i.strip()])
                        # print("reading lines")
                        for i in range(new_lines):
                            print("reading lines")
                    else:
                        
                        new_lines = len(f.readlines())

                    
                    lines = lines + new_lines
                # print(file,"------>",new_lines)
            except:
                pass
    
    return f"In this folder, there are {len(filelist)} files, and have lines {lines} of code in it."
# call the function
value = countlines(direct,ext="*", skip_blank=True)

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''insert into data values (?)''',(value,))
conn.commit()

print(value)