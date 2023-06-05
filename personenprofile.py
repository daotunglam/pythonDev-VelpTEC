names = ["Kai", "John", "Emily", "Michael", "Sophia", "Benjamin"]


def personenprofile():
    dic = {}
    for name in names:
        dic[name] = len(name)

    maxNameLength = max(list(dic.values()))
    minNameLength = min(list(dic.values()))

    longestName = ''
    shortestName = ''
    for name in names:
        if len(name) == maxNameLength:
            longestName = name
        if len(name) == minNameLength:
            shortestName = name

    return shortestName, longestName, dic

shortestName, longestName, dic = personenprofile()
print('dic: ', dic)
print('shortestName: ', shortestName)
print('longestName: ', longestName)
