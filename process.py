file1 = open("test1.txt",'r')
Lines = file1.readlines()
file2 = open("text2.txt", 'w')

res = ""
tmp_str = ""
for line in Lines: 
    #print(line)
    s = line.strip('\n')
    #s = s.split(" ")
    res += s + ","
    
    
file2.writelines(res)