import sys
import string
import os
import re


def word2list(mydir, mylist):  # Read the txt file, and put every word into my list.
    with open(mydir,'r',encoding='utf-8') as f:
        lines = f.readlines()

        for i in range(0,lines.__len__(),1):
            for word in lines[i].split():
                word=word.strip(string.whitespace)
                mylist.append(word)
        return mylist


def wordCounter(t, p):
    for i in list1:
        if i in list2:
            # print(i)
            t = int(t) + 1

    # print("===============")

    for j in list2:
        if j in list1:
            # print(j)
            p = int(p) + 1

    return t, p


def getOverlapRatio(root_title_dir, root_artic_dir, list1, list2):
    for root, dirs, files in os.walk(root_title_dir):
        for i in files:

            title_dir = root+i
            pattern = re.compile(r'\d+')
            num = pattern.findall(i)
            list1 = word2list(title_dir, list1)  # t

            artic_dir = root_artic_dir+"artic_"+num[0]+".txt"
            list2 = word2list(artic_dir, list2)

            count_t = 0 # How many t shown in p
            count_p = 0 # How many p shown in t
            count_t, count_p = wordCounter(count_t, count_p)

            # t 与 p 的重合度 = [count(t) + count(p)] / [length(t) + length(p)]
            OverlapRatio = float(count_t+count_p) / (len(list1)+len(list2))
            print("文章" + num[0] + "的重合度为：" + str(OverlapRatio))


            list1 = []
            list2 = []

if __name__ == "__main__":
    list1 = []
    list2 = []
    root_title_dir = "/Users/qianqian/Desktop/articles/title/"
    root_artic_dir = "/Users/qianqian/Desktop/articles/artic/"

    getOverlapRatio(root_title_dir, root_artic_dir, list1, list2)

# OUTPUT:
# 文章11495的重合度为：0.05625
# 文章12822的重合度为：0.14240506329113925
# 文章5977的重合度为：0.0677710843373494
# 文章15195的重合度为：0.07588532883642496
# 文章16488的重合度为：0.04838709677419355
# 文章9181的重合度为：0.058365758754863814
# 文章17796的重合度为：0.0273224043715847
# 文章5963的重合度为：0.08333333333333333
# 文章12188的重合度为：0.08211678832116788
# 文章13296的重合度为：0.05039193729003359
# 文章7812的重合度为：0.06484149855907781
# 文章11481的重合度为：0.061391541609822645
# 文章10947的重合度为：0.052878965922444184
# 文章3484的重合度为：0.09297520661157024

