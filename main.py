def checkage(friend):
    for f in friend.items():
        if f[1] >= 20:
            print(f[0],f[1])

friend = {'somchai':17,'somsak':15, 'sompong':21}

checkage(friend)