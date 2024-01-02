# TRAVEL AGENCY MANAGEMENT SYSTEM

# Note: Password for administrator access is 120804

def book_package(indiv):
    code=input('Enter package code (eg: B1): ')
    n=int(input('Enter number of passengers: '))
    val=[]
    details=[]
    num=0
    minor=0
    for i in range(n):
        name=input('Enter passenger name: ')
        age=int(input('Enter passenger age: '))
        if age<12:
            num+=1
            minor+=0.5*indiv[code.upper()][2]
        phone=input('Enter contact number (05xxxxxxxx): ')
        while len(phone)!=10:
            print('Invalid contact number')
            phone=input('Enter contact number (05xxxxxxxx): ')
        ppn=input('Enter passport number: ')
        val=[code.upper(),name.upper(),age,phone]
        details+=[ppn.upper(),name.upper(),age,phone]
        bookings[ppn.upper()]=val
    print('\n__________BOOKING SUMMARY__________')
    print('\nDestination:',indiv[code.upper()][0])
    print('Duration:',indiv[code.upper()][1])
    print('Number of passengers:',n)
    print('Total cost:',(n-num)*indiv[code.upper()][2]+minor,'AED')
    print('Passenger details:',details)
    print('\n********************************************************************************************************\nThank you for booking with Beyond Borders Tours & Travels\nTo confirm your booking kindly transfer the said amount to the following bank account:\n\nBeneficiary: BEYOND BORDERS TOURS & TRAVELS\nBank: ABCD Bank, Abu Dhabi, UAE\nIBAN: AE123400000987612300012\n\n********************************************************************************************************')
#<theme code><package number>:[Destination, duration, cost(pp), description]
indiv={'B1':['Seychelles','3 nights',7999,'Stay at Hilton Northlome'],'B2':['Maldives','3 nights',4599,'Stay at Kurumathi Maldives'],'B3':['Thailand','5 nights',3439,'Stay at Hilton Arcadia Resort'],'S1':['Dubai','1 night',1499,'Stay at Atlantis, The Palm'],'S2':['Fujairah','1 night',810,'Water sports and trekking'],'S3':['Abu Dhabi','2 nights',2175,'Stay at Anantara Eastern Mangroves'],'A1':['Bali','5 nights',3599,'Water sports combo'],'A2':['Thailand','6 nights',3950,'Exploring the wildlife'],'A3':['Croatia','6 nights',4500,'Boat picnic excursion'],'H1':['Vietnam','6 nights',6500,'Temple and museum tours'],'H2':['Jordan','5 nights',5590,'Visit to ruins of Petra'],'H3':['Rome','3 nights',3700,'Colosseum and palace tour']} 
#<package number>:[Destination, duration,  travel dates, available spots, cost(pp)]
group={'G1':['Sri Lanka','15 days','12-26 Jan 2022',15,6900],'G2':['Europe','11 days','18-28 Jan 2022',10,12500],'G3':['Switzerland','06 days','21-26 Jan 2022',16,4500],'G4':['Russia','10 days','02-11 Feb 2022',12,10500],'G5':['Iceland','10 days','09-18 Feb 2022',10,15400],'G6':['Singapore','05 days','21-25 Feb 2022',24,3500]}
bookings={}

while True:
    print('\nWelcome to Beyond Borders Tours & Travels')
    print('1. Admistrator access')
    print('2. User access')
    print('3. Exit')
    c1=int(input('Enter option number: '))
    if c1==1:
        pwd=input('Enter password: ')
        if pwd=='120804':
            print('\n1. Add packages')
            print('2. Delete packages')
            print('3. Edit package details')
            print('4. View bookings')
            print('5. Delete a booking')
            c2=int(input('Enter choice: '))
            if c2==1:
                print('\n1. Add independent package')
                print('2. Add group package')
                ch=int(input('Enter choice: '))
                if ch==1:
                    n=int(input('Enter number of packages to be added: '))
                    val=[]
                    for i in range(n):
                        code=input('Enter package code: ')
                        dst=input('Enter destination: ')
                        dur=input('Enter duration(in nights): ')
                        cost=int(input('Enter cost(pp): '))
                        desc=input('Enter description: ')
                        val=[dst.title(),dur.lower(),cost,desc.title()]
                        indiv[code.upper()]=val
                        print(indiv)
                elif ch==2:
                    n=int(input('Enter number of packages to be added: '))
                    val=[]
                    for i in range(n):
                        code=input('Enter package code: ')
                        dst=input('Enter destination: ')
                        dur=input('Enter duration(in days): ')
                        dates=input('Enter travel dates(xx-xx Mon Year): ')
                        avl=int(input('Enter number of available spots: '))
                        cost=int(input('Enter cost(pp): '))
                        val=[dst.title(),dur.lower(),dates.title(),avl,cost]
                        group[code.upper()]=val
                        print(group)
                else:
                    print('Invalid option')
            elif c2==2:
                print('\n1. Delete independent package')
                print('2. Delete group package')
                ch=int(input('Enter choice: '))
                if ch==1:
                    k=list(indiv.keys())
                    code=input('Enter package code: ')
                    if code.upper() in k:
                        del indiv[code.upper()]
                        print(indiv)
                    else:
                        print('Invalid package code')
                elif ch==2:
                    k=list(group.keys())
                    code=input('Enter package code: ')
                    if code.upper() in k:
                        del group[code.upper()]
                        print(group)
                    else:
                        print('Invalid package code')
                else:
                    print('Invalid option')
            elif c2==3:
                print('\n1. Edit independent package details')
                print('2. Edit group package details')
                ch=int(input('Enter choice: '))
                if ch==1:
                    print('1. Change duration')
                    print('2. Change cost per person')
                    print('3. Change description')
                    ch=int(input('Enter choice: '))
                    if ch==1:
                        code=input('Enter package code: ')
                        if code.upper() in list(indiv.keys()):
                            dur=input('Enter revised duration(in nights): ')
                            indiv[code.upper()][1]=dur
                            print(indiv)
                        else:
                            print('Invalid package code')
                    elif ch==2:
                        code=input('Enter package code: ')
                        if code.upper() in list(indiv.keys()):
                            cost=int(input('Enter revised cost per person: '))
                            indiv[code.upper()][2]=cost
                            print(indiv)
                        else:
                            print('Invalid package code')
                    elif ch==3:
                        code=input('Enter package code: ')
                        if code.upper() in list(indiv.keys()):
                            desc=input('Enter revised description: ')
                            indiv[code.upper()][3]=desc
                            print(indiv)
                        else:
                            print('Invalid package code')
                    else:
                        print('Invalid option')
                elif ch==2:
                    print('1. Change duration')
                    print('2. Change travel dates')
                    print('3. Change availabilty')
                    print('4. Change cost per person')
                    if ch==1:
                        code=input('Enter package code: ')
                        if code.upper() in list(group.keys()):
                            dur=input('Enter revised duration(in days): ')
                            group[code.upper()][1]=dur
                            print(group)
                        else:
                            print('Invalid package code')
                    elif ch==2:
                        code=input('Enter package code: ')
                        if code.upper() in list(group.keys()):
                            dates=input('Enter revised travel dates(xx-xx Mon Year): ')
                            group[code.upper()][2]=dates
                            print(group)
                        else:
                            print('Invalid package code')
                    elif ch==3:
                        code=input('Enter package code: ')
                        if code.upper() in list(group.keys()):
                            avl=input('Enter revised number of available spots: ')
                            group[code.upper()][3]=avl
                            print(group)
                        else:
                            print('Invalid package code')
                    elif ch==4:
                        code=input('Enter package code: ')
                        if code.upper() in list(group.keys()):
                            cost=input('Enter revised cost per person: ')
                            group[code.upper()][4]=cost
                            print(group)
                        else:
                            print('Invalid package code')
                    else:
                        print('Invalid option')
                else:
                    print('Invalid option')
            elif c2==4:
                k=list(bookings.keys())
                print('\n%-14s'%'Package booked','%-14s'%'Passport No.','%-15s'%'Name','%-8s'%'Age','%-14s'%'Contact number')
                for i in k:
                    print('%-14s'%bookings[i][0],'%-14s'%i,'%-15s'%bookings[i][1],'%-8s'%bookings[i][2],'%-14s'%bookings[i][3])
            elif c2==5:
                ppn=input('Enter passport number to be deleted: ')
                k=list(bookings.keys())
                for i in k:
                    if i==ppn.upper():
                        del bookings[i]
                        break
                else:
                    print('Booking does not exist')
            else:
                print('Invalid option')
        else:
            print('Incorrect password')
            print('1. Return to main menu')
            print('2. Exit')
            c2=int(input('Enter choice: '))
            if c2==1:
                continue
            else:
                break
            
    elif c1==2:
        print('\nExplore the world with specially curated holiday packages by Beyond Borders Tours & Travels')
        print('1. Independent packages')
        print('2. Group packages')
        print('(Children below the age of 12 years will be charged 50% of the listed price)')
        c2=int(input('\nEnter option number: '))
        if c2==1:
            print('\n1. Holiday packages by theme')
            print('2. Holiday packages by destination')
            print('3. Holiday packages by number of nights')
            print('4. Holiday packages by budget')
            print('5. Display all holiday packages')
            c3=int(input('Enter option number: '))
            if c3==1: #Holiday packages by theme
                print('\nDesired theme of holiday:')
                print('1. Beach')
                print('2. Staycation')
                print('3. Adventure')
                print('4. Art, History and Culture')
                ch=int(input('Enter choice: '))
                if ch==1:
                    k=list(indiv.keys())
                    print('\n%-4s'%'Code','%-11s'%'Destination','%-10s'%'Duration','%-11s'%'Cost(PP)','%-25s'%'Description')
                    for i in k:
                        if i[0]=='B':
                            print('%-4s'%i,'%-11s'%indiv[i][0],'%-10s'%indiv[i][1],'%-5s'%indiv[i][2],'AED\t','%-25s'%indiv[i][3])
                    print('\n1. Book a package')
                    print('2. Return to main menu')
                    print('3. Exit')
                    ch=int(input('Enter choice: '))
                    if ch==1:
                        book_package(indiv)
                    elif ch==2:
                        continue
                    elif ch==3:
                        break
                    else:
                        print('Invalid option')
                elif ch==2:
                    k=list(indiv.keys())
                    print('\n%-4s'%'Code','%-11s'%'Destination','%-10s'%'Duration','%-15s'%'Cost(PP)','%-25s'%'Description')
                    for i in k:
                        if i[0]=='S':
                            print('%-4s'%i,'%-11s'%indiv[i][0],'%-10s'%indiv[i][1],'%-5s'%indiv[i][2],'AED\t','%-25s'%indiv[i][3])
                    print('\n1. Book a package')
                    print('2. Return to main menu')
                    print('3. Exit')
                    ch=int(input('Enter choice: '))
                    if ch==1:
                        book_package(indiv)
                    elif ch==2:
                        continue
                    elif ch==3:
                        break
                    else:
                        print('Invalid option')
                elif ch==3:
                    k=list(indiv.keys())
                    print('\n%-4s'%'Code','%-11s'%'Destination','%-10s'%'Duration','%-15s'%'Cost(PP)','%-25s'%'Description')
                    for i in k:
                        if i[0]=='A':
                            print('%-4s'%i,'%-11s'%indiv[i][0],'%-10s'%indiv[i][1],'%-5s'%indiv[i][2],'AED\t','%-25s'%indiv[i][3])
                    print('\n1. Book a package')
                    print('2. Return to main menu')
                    print('3. Exit')
                    ch=int(input('Enter choice: '))
                    if ch==1:
                        book_package(indiv)
                    elif ch==2:
                        continue
                    elif ch==3:
                        break
                    else:
                        print('Invalid option')
                elif ch==4:
                    k=list(indiv.keys())
                    print('\n%-4s'%'Code','%-11s'%'Destination','%-10s'%'Duration','%-15s'%'Cost(PP)','%-25s'%'Description')
                    for i in k:
                        if i[0]=='H':
                            print('%-4s'%i,'%-11s'%indiv[i][0],'%-10s'%indiv[i][1],'%-5s'%indiv[i][2],'AED\t','%-25s'%indiv[i][3])
                    print('\n1. Book a package')
                    print('2. Return to main menu')
                    print('3. Exit')
                    ch=int(input('Enter choice: '))
                    if ch==1:
                        book_package(indiv)
                    elif ch==2:
                        continue
                    elif ch==3:
                        break
                    else:
                        print('Invalid option')
                else:
                    print('Invalid option')
            elif c3==2: #Holiday packages by destination
                d=input('\nEnter desired destination: ')
                k=list(indiv.keys())
                flag=0
                for i in k:
                    x=indiv[i][0]
                    if x.upper()==d.upper().strip():
                        print('\n%-4s'%'Code','%-11s'%'Destination','%-10s'%'Duration','%-15s'%'Cost(PP)','%-25s'%'Description')
                        print('%-4s'%i,'%-11s'%indiv[i][0],'%-10s'%indiv[i][1],'%-5s'%indiv[i][2],'AED\t','%-25s'%indiv[i][3])
                        flag=1
                if flag==0:
                    print('No packages found')
                    print('\n1. Return to main menu')
                    print('2. Exit')
                    ch=int(input('Enter choice: '))
                    if ch==2:
                        continue
                    elif ch==3:
                        break
                    else:
                        print('Invalid option') 
                else:
                    print('\n1. Book a package')
                    print('2. Return to main menu')
                    print('3. Exit')
                    ch=int(input('Enter choice: '))
                    if ch==1:
                        book_package(indiv)
                    elif ch==2:
                        continue
                    elif ch==3:
                        break
                    else:
                        print('Invalid option')
            elif c3==3: #Holiday packages by number of nights
                nts=int(input('\nEnter number of nights: '))
                k=list(indiv.keys())
                flag=0
                for i in k:
                    if indiv[i][1]==str(nts)+' nights' or indiv[i][1]==str(nts)+' night':
                        print('\n%-4s'%'Code','%-11s'%'Destination','%-10s'%'Duration','%-15s'%'Cost(PP)','%-25s'%'Description')
                        print('%-4s'%i,'%-11s'%indiv[i][0],'%-10s'%indiv[i][1],'%-5s'%indiv[i][2],'AED\t','%-25s'%indiv[i][3])
                        flag=1
                if flag==0:
                    print('No packages found')
                    print('\n1. Return to main menu')
                    print('2. Exit')
                    ch=int(input('Enter choice: '))
                    if ch==2:
                        continue
                    elif ch==3:
                        break
                    else:
                        print('Invalid option') 
                else:
                    print('\n1. Book a package')
                    print('2. Return to main menu')
                    print('3. Exit')
                    ch=int(input('Enter choice: '))
                    if ch==1:
                        book_package(indiv)
                    elif ch==2:
                        continue
                    elif ch==3:
                        break
                    else:
                        print('Invalid option')
            elif c3==4: #Holiday packages by budget
                print('\nChoose category of packages: ')
                print('1. Budget tours')
                print('2. Getaway deals')
                print('3. Luxury escapes')
                ch=int(input('Enter choice: '))
                if ch==1:
                    k=list(indiv.keys())
                    print('\n%-4s'%'Code','%-11s'%'Destination','%-10s'%'Duration','%-15s'%'Cost(PP)','%-25s'%'Description')    
                    for i in k:
                        if indiv[i][2]<=3000:
                            print('%-4s'%i,'%-11s'%indiv[i][0],'%-10s'%indiv[i][1],'%-5s'%indiv[i][2],'AED\t','%-25s'%indiv[i][3])
                    print('\n1. Book a package')
                    print('2. Return to main menu')
                    print('3. Exit')
                    ch=int(input('Enter choice: '))
                    if ch==1:
                        book_package(indiv)
                    elif ch==2:
                        continue
                    elif ch==3:
                        break
                    else:
                        print('Invalid option')
                elif ch==2:
                    k=list(indiv.keys())
                    print('\n%-4s'%'Code','%-11s'%'Destination','%-10s'%'Duration','%-15s'%'Cost(PP)','%-25s'%'Description')    
                    for i in k:
                        if 3000<indiv[i][2]<=6000:
                            print('%-4s'%i,'%-11s'%indiv[i][0],'%-10s'%indiv[i][1],'%-5s'%indiv[i][2],'AED\t','%-25s'%indiv[i][3])
                    print('\n1. Book a package')
                    print('2. Return to main menu')
                    print('3. Exit')
                    ch=int(input('Enter choice: '))
                    if ch==1:
                        book_package(indiv)
                    elif ch==2:
                        continue
                    elif ch==3:
                        break
                    else:
                        print('Invalid option')
                elif ch==3:
                    k=list(indiv.keys())
                    print('\n%-4s'%'Code','%-11s'%'Destination','%-10s'%'Duration','%-15s'%'Cost(PP)','%-25s'%'Description')    
                    for i in k:
                        if 6000<indiv[i][2]:
                            print('%-4s'%i,'%-11s'%indiv[i][0],'%-10s'%indiv[i][1],'%-5s'%indiv[i][2],'AED\t','%-25s'%indiv[i][3])
                    print('\n1. Book a package')
                    print('2. Return to main menu')
                    print('3. Exit')
                    ch=int(input('Enter choice: '))
                    if ch==1:
                        book_package(indiv)
                    elif ch==2:
                        continue
                    elif ch==3:
                        break
                    else:
                        print('Invalid option')
                else:
                    print('Invalid option')
            elif c3==5:
                k=list(indiv.keys())
                print('\n%-4s'%'Code','%-11s'%'Destination','%-10s'%'Duration','%-15s'%'Cost(PP)','%-25s'%'Description')
                for i in k:
                    print('%-4s'%i,'%-11s'%indiv[i][0],'%-10s'%indiv[i][1],'%-5s'%indiv[i][2],'AED\t','%-25s'%indiv[i][3])
                print('\n1. Book a package')
                print('2. Return to main menu')
                print('3. Exit')
                ch=int(input('Enter choice: '))
                if ch==1:
                    book_package(indiv)
                elif ch==2:
                    continue
                elif ch==3:
                    break
                else:
                    print('Invalid option')
            else:
                print('Invalid option')
        elif c2==2:
            k=list(group.keys())
            print('\n%-4s'%'Code','%-13s'%'Destination','%-12s'%'Duration','%-15s'%'Travel dates','%-17s'%'Available spots','%-10s'%'Cost(PP)')
            for i in k:
                print('%-4s'%i,'%-13s'%group[i][0],'%-12s'%group[i][1],'%-20s'%group[i][2],'%-12s'%group[i][3],'%6s'%group[i][4],'AED')
            print('\n1. Book a package')
            print('2. Return to main menu')
            print('3. Exit')
            ch=int(input('Enter choice: '))
            if ch==1:
                code=input('Enter package code (eg: G1): ')
                n=int(input('Enter number of passengers: '))
                val=[]
                details=[]
                for i in range(n):
                    name=input('Enter passenger name: ')
                    age=int(input('Enter passenger age: '))
                    phone=int(input('Enter contact number (05xxxxxxxx): '))
                    ppn=input('Enter passport number: ')
                    val=[code.upper(),name.upper(),age,phone]
                    details+=[ppn.upper(),name.upper(),age,phone]
                    bookings[ppn.upper()]=val
                print('\nBOOKING SUMMARY:')
                print('\nDestination:',group[code.upper()][0])
                print('Duration:',group[code.upper()][1])
                print('Travel dates:',group[code.upper()][2])
                print('Number of passengers:',n)
                print('Total cost:',n*group[code.upper()][4],'AED')
                print('Passenger details:',details)
                print('\nThank you for booking with Beyond Borders Tours & Travels\nTo confirm your booking kindly transfer the said amount to the following bank account:\n\nBeneficiary: BEYOND BORDERS TOURS & TRAVELS\nBank: ABCD Bank, Abu Dhabi, UAE\nIBAN: AE123400000987612300012\n')
                group[code.upper()][3]-=n
            elif ch==2:
                continue
            elif ch==3:
                break
            else:
                print('Invalid option')
    elif c1==3:
        break
    else:
        print('Invalid option')
    
                    
                        
                        
            
                        
                            
      
            
        