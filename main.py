def project2():
    print('What action do you want to perform?')
    print('*Add new member (A) ')
    print('*Choosing the best member (C)')
    print('*Member update (U)')
    inp = input(': ')
    if inp == 'A':
        name = input('enter name: ')
        age = int(input('enter age:'))
        level = input('enter level: ')
        dicti[name] = [age , level]
        project2()

    elif inp == 'C':
        print(dicti)
        lis = []
        for i in dicti:
            num = dicti.get(i)[0]
            lis.append(num)
        maxi = max(lis)
        mini = min(lis)
        av = (maxi + mini)/2
        
        if int(maxi +mini )%2 != 0:
            av+=1
        choose = []
        for i in dicti:
            num = dicti.get(i)[0]
            if num <= av:
                choose.append(i)
        i =1
        best_ch = dicti.get(choose[0])[1]
        m_name = choose[0]
        while i < len(choose):
            if best_ch<dicti.get(choose[i])[1]:

                best =  dicti.get(choose[i])
                best_ch = dicti.get(choose[i])[1]
                m_name = choose[i]
            elif dicti.get(m_name)[1] == dicti.get(choose[i])[1]:
                if  dicti.get(m_name)[0] > dicti.get(choose[i])[0]:
                    best =  dicti.get(choose[i])
                    best_ch = dicti.get(choose[i])[1]
                    m_name = choose[i]
            i +=1
        print(best)
        print(m_name)
        del dicti[m_name]
        print(dicti)
        project2()

    elif inp == "U":
        name = input('Enter the member name :  ')
        level = input('Enter the member level :  ')
        dicti[name] = [dicti.get(name)[0] , level]
        print(dicti)
        project2()


dicti = {}
project2()