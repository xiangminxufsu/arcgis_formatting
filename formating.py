#formating the file to meet arcgis standard
import os
import re

#keep only a-Z and _ remove all the rest
def handler(line):
    matched = re.findall(r'(?:[^\r\n,"]|"(?:\\.|[^"])*")+', line)
    newlist = []
    for x in matched:
        newx=''
        for i in x:
            if re.match('^[A-Za-z0-9_]',i):
                newx=newx+i
                pass
            else:
                pass
                if newx is not '' and newx[-1]!='_':
                    newx=newx+'_'
        if newx[-1]=='_':newx = newx[:-1]
        newlist.append(newx)
    rt = ','.join(newlist) + '\r\n'
    return rt
        
def main(dir,newdir):
    ori_f = open(dir,'rb')
    des_f = open(newdir,'wb')

    firstline=ori_f.readline()
    #print firstline
    newline = handler(firstline)
    des_f.write(newline)

    for line in ori_f:
        des_f.write(line)
        
    ori_f.close()
    des_f.close()

if __name__ == '__main__':
    dir = r'C:\\Users\\GIS_tech\\Desktop\\66county\\merged_file\\final_track.csv'
    assert os.path.exists(dir)
    newdir=r'C:\\Users\\GIS_tech\\Desktop\\66county\\merged_file\\newfinal_track.csv'
    main(dir,newdir)