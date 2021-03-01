# def print_string(suffix):
#     a='fast'

#     if suffix:
#         print('add suffix')
#         a+='campus'
#         return

#     print(a)


# print_string(1)

################################

# a='FastCampus'
# a.index('C')

###############################

# a=[1,2,3]
# a.pop()
# a[1]=4

##############################

# immutable=(1,2,3)
# immutable[1]=4

##############################

# a=['b','c','d','a']
# a.reverse()
# ''.join(a).index('dc')

##############################

# a=['alghost', 'fastcampus']
# b={'alghost': 1, 'fastcampus': 2}

# if 'a' in a:
#     print(1)
# elif 'al' in a and 'alghost' in b:
#     print(2)
# elif 'al' in a or 1 in b:
#     print(3)
# elif 'al' in a or 'alghost' in b:
#     print(4)
# else:
#     print(1)

################################

# a = [1, 2, 3]
# b = (4, 5, 6)
# a.pop()
# a.append(b)
# print(len(a))

##################################

# a = '"FastCampus" 프로그래밍 유치원 완주반\n\t시작합니다'
# a = "\"FastCampus\" 프로그래밍 유치원 완주반\n\t시작합니다"
# a = " ".join(["FastCampus", "프로그래밍", "유치원", "완주반"]) + "\n\t시작합니다"
# a = '''"FastCampus" 프로그래밍 유치원 완주반\n\t시작합니다'''
# print(a)

###############################

# result=5+4
# alghost=result/3
# print(alghost)

##############################

# a=['Fast', 'Slow', '3', '21']
# a.append('Campus')
# a.insert(2, '77')
# a.reverse
# print(','.join(a[:3]))
# print(a)

###############################

# for elem in range(10):
#     print(elem)

################################

# def flatten(results):

#     rows=[]

#     for row in results:

#         cells=[]

#         for cell in row:

#             cells.append(cell)

#         rows.append(tuple(cells))

#     return tuple(rows)

# print(flatten([[1,2,3], [4,5,6]]))

#################################

# a={'name': 'kaden', 'company': 'fastcampus'}

# for e in a.values():
#     print(e)

# for _, e in a.items():
#     print(e)

# for k in a:
#     print(a[k])

# for k in a.keys():
#     print(k)

####################################

# print([1,2,3,1,2,3])
# print([1,2,3]*2)
# print([1,2,3]+[1,2,3])
# print([1,2,3].append([1,2,3]))

# print([1,2,3,1,2,3]!=[1,2,3].append([1,2,3]))

####################################

# a, b, c = ('4', 2, 'a')
# print((int(a) + b)*c)

###################################

# a = 'Fastcampus'
# print(a[2:5].upper())

###################################

# a = list(range(10))

# while a:
#     cur = a.pop()
#     rem = cur % 3
#     if rem == 0:
#         print(0, end='')
#         continue
#         print(0, end-'')
#     elif rem == 1:
#         print(1, end='')
#     else:
#         print(2)
#         break
#     print(' ', end='')

#################################

# print(int((10//3)/2)*1.3)

################################

# a = 'Preschool'
# sep = ','
# print(sep.join(a[3:].replace('oo', 'aa').split()))

###############################

# a = []

# for i in range(10):
#     if i % 3 == 0:
#         a.append(i)

# print(str(max(a))+str(min(a)))

################################

# a = 'fastcampus'
# b = 'python'
# print(b[:a.find('c')].replace('p', 'c').upper())

################################

# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]

# a.append(b[2:][1])
# a.append(b[:3][2])
# print(a[2:5])

##################################

# a = [1, 3, 4, 9, 11, 0]
# a.sort()
# a.reverse()
# print(a.index(3))

##################################

# def print_filter(string):
#     if 'skip' in string:
#         print('Skip')
#         return
#     print(string)/


# print_filter('skip c')

###################################

# def filter_malformed_email(data):
#     for k, v in list(data.items()):
#         # check @
#         if '@' not in v:
#             del data[k]
#             continue

#         if not 5 <= len(k) <= 10:
#             del data[k]

#     return data


# data = {'kaden': 'kaden@fastcampus.com',
#         'olivia': 'olivia.com', 'bob': 'bob@gmail.com'}
# print(filter_malformed_email(data))

################################

# def _print(m):
#     for (key, value) in m.items():
#         for values in value:
#             print(str(key)+' '+str(values))
#     return


# a = {'first': [1, 2, 3], 'second': [4, 5, 6]}
# _print(a)

###############################


################################

# def slice2_str_add(a, b):
#     result = str(a[0])+str(a[1])+str(b[0])+str(b[1])
#     return result


# print(slice2_str_add([1, 2, 3], [4, 5, 6]))
# print(slice2_str_add(['a', 'b', 'c'], ['d', 'e', 'f']))

###############################

def count_words(sentlist):
    ready_words = []
    for onesent in sentlist:
        words_in_onesent_list = onesent.split()
        low_word_list = []
        for oneword in words_in_onesent_list:
            low_word = oneword.lower()
            low_word_list.append(low_word)
        ready_words.append(low_word_list)
    wordsdict = {}
    for one_ready_word in ready_words:
        dict_d = dict.fromkeys(one_ready_word)
        wordsdict.update(dict_d)
    print(wordsdict)


print(count_words(["Running notebook pipelines",
                   "The Jupyter Notebook", "the Python itself"]))
print(count_words(["패스트캠퍼스", "유치원 완주반 1", "유치원  "]))
