# coding:utf-8
'''simple file test'''
file = open("myfile","w")
file.write("First line with necessary newline charactor\n")
file.write("Second line to write to the file\n")
file.close()
file = open("myfile","r")
line1 = file.readline()
line2 = file.readline()
print(line1,line2)
file.close()

import os
os.remove("myfile")
