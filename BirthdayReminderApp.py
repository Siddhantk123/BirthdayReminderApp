Dict = {} #dictonary to store birthday

while True:

    print("-----Birthday Adder-----\n")
    print("1.Show birthday")
    print("2.Add to birthday list")
    print("3.Exit")
    choice =input("Enter your choice from 1,2,3 \n")
    choice=int(choice)
    if choice == 1:
        if len(Dict) == 0:
            print("Nothing to show")
        else:
            name=input("enter the name of the person to look for birthday \n")
            birthday=Dict.get(name,"No data found")
            print(birthday)
    elif choice == 2:
        name=input("Enter the Name \n")
        date=input("Enter birthday \n")
        Dict[name] = date # way to add key and value to dict
        print("Birthday Added")
    elif choice == 3:
        print("---exiting program---")
        break
    else:
        print("Choose a valid option")            




