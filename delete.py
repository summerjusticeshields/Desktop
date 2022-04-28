x = input ('Type "duck" or "goose": ')
count = 0

while x != 'goose':
        
    count += 1
    print (input ('Type "duck" or "goose": '))

    if x == 'goose':
        print(count)
