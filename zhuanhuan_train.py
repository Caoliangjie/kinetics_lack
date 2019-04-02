import csv
with open('diff_train.csv', 'w+',newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    with open('diff_train.txt', 'r',encoding='utf-8') as filein:
        for line in filein:
            for i in range(len(line)):
              if (line[i]=='0')and(line[i-1]=='_')and(line[i+1]=='0'):
                print(line[:i-1])
                line_list = line[0:i-1].strip('\n').split('\t')
            #print(line)
                spamwriter.writerow(line_list)
                break
#现将txt转成csv文件，这里顺便保存的时候先把后面的时间去除了。
