import sys
import string
import os
import re


def word2list(mydir, mylist):  # Read the txt file, and put every word into my list.
    try:
        with open(mydir,'r',encoding='utf-8') as f:
            lines = f.readlines()
            for i in range(0,lines.__len__(),1):
                for word in lines[i].split():
                    word=word.strip(string.whitespace)
                    mylist.append(word)
            return mylist

    except (IOError, TypeError):
        pass



def wordCounter(t, p, list1, list2):

    try:
        for i in list1:
            if i in list2:
                t = int(t) + 1
        for j in list2:
            if j in list1:
                p = int(p) + 1
        return t, p
    except (IOError, TypeError):
        pass

def getOverlapRatio(root_title_dir, root_artic_dir, list1, list2):

    temp_title_dir_list = []
    try:
        for root, dirs, files in os.walk(root_title_dir):
            for i in files:
                title_dir = root+i
                temp_title_dir_list.append(title_dir)

        print(len(temp_title_dir_list)) # 10986 个

    except (IOError, TypeError):
        pass


    try:
        # for root, dirs, files in os.walk(root_title_dir):
        #     for i in files:
        #         title_dir = root+i
        #         pattern1 = re.compile(r'\d+')
        #         num1 = pattern1.findall(i)
        #         list1 = word2list(title_dir, list1)  # t

        #         print(title_dir)

        for i in range(100):
            print(temp_title_dir_list[i])
            list1 = word2list(temp_title_dir_list[i], list1)
            print(list1)

            for root, dirs, files in os.walk(root_artic_dir):
                for j in files:
                    artic_dir = root+j
                    pattern2 = re.compile(r'\d+')
                    num2 = pattern2.findall(j)
                    list2 = word2list(artic_dir, list2)


                    count_t = 0 # How many t shown in p
                    count_p = 0 # How many p shown in t
                    count_t, count_p = wordCounter(count_t, count_p, list1, list2)

                    print("count_t: " + str(count_t))
                    print("count_p: " + str(count_p))

                    # t 与 p 的重合度 = [count(t) + count(p)] / [length(t) + length(p)]
                    OverlapRatio = float(count_t+count_p) / (len(list1)+len(list2))
                    print("标题" + temp_title_dir_list[i] + "对应文章" + num2[0] + "的重合度为：" + str(OverlapRatio))


                    list2 = []
            list1 = []

    except (IOError, TypeError):
        pass


if __name__ == "__main__":
    list1 = []
    list2 = []
    root_title_dir = "/Users/qianqian/Desktop/articles/title/"
    root_artic_dir = "/Users/qianqian/Desktop/articles/artic/"

    getOverlapRatio(root_title_dir, root_artic_dir, list1, list2)


#OUTPUT:
# count_t: 1
# count_p: 1
# 标题/Users/qianqian/Desktop/articles/title/title_15195.txt对应文章18645的重合度为：0.0038022813688212928
# count_t: 0
# count_p: 0
# 标题/Users/qianqian/Desktop/articles/title/title_15195.txt对应文章17576的重合度为：0.0
# count_t: 0
# count_p: 0
# 标题/Users/qianqian/Desktop/articles/title/title_15195.txt对应文章16668的重合度为：0.0
# count_t: 0
# count_p: 0
# 标题/Users/qianqian/Desktop/articles/title/title_15195.txt对应文章1587的重合度为：0.0
# count_t: 0
# count_p: 0
# 标题/Users/qianqian/Desktop/articles/title/title_15195.txt对应文章948的重合度为：0.0
# count_t: 0
# count_p: 0
# 标题/Users/qianqian/Desktop/articles/title/title_15195.txt对应文章18123的重合度为：0.0
# count_t: 0
# count_p: 0
# 标题/Users/qianqian/Desktop/articles/title/title_15195.txt对应文章790的重合度为：0.0
# count_t: 0
# count_p: 0
# 标题/Users/qianqian/Desktop/articles/title/title_15195.txt对应文章13076的重合度为：0.0
# count_t: 1
# count_p: 2
# 标题/Users/qianqian/Desktop/articles/title/title_15195.txt对应文章24的重合度为：0.003592814371257485