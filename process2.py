file1 = open("test1.txt",'r')
Lines = file1.readlines()
file2 = open("text2.txt", 'w')

res = ""
tmp_str = ""
count = 0
for line in Lines: 
    tmp = "("
    line = line.split("bag")
    #print(line)
    tmp += '"' + ''.join(line[0][:-1]) + '", list{'

    for i in range(1,len(line)-1):
        s = line[i].split(" ")
        num = s[-4]
        s = s[-3:-1]
        tmp += "(" + num + ',"'+' '.join(s)+'")'
        if(i < len(line)-2):
            tmp += ","
    tmp += '}),'
    print(tmp)
    res += tmp
    
file2.writelines(res)