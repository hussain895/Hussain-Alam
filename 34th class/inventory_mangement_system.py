Inventory = {}

while True:
   print("\n-----------------------------------------------------------------Inventory Mangement System-------------------------------------------------")
   print("1 . Add The Items ")
   print("2 . View The Items ")
   print("3 . Search The Item ")
   print("4 . Update The Item ")
   print("5 . Remove The Item ")
   print("6 . Exit ")

   choice =input("Select The Option (1-6) : ")

   if choice == "1":
    name = input("Add The Items : ")
    quantity = input("Quantity : ")
    Inventory[name] = quantity
    print("\n Add Successfully")


   elif choice == "2":
     if not Inventory:
       print("Inventory Is Empty ")
     else:
       for key, value in Inventory.items():
         print(key , ":" , value)

   elif choice == "3":
       name = input("Enter The Item To Search ")
       if name in Inventory:
        print(name , "Quantity" , Inventory[name])
       else:
        print("Product Is Not Found")
     
   elif choice == "4":
     name = input("Enter The Item To Update ")
     if name in Inventory:
       qty = input("Add New Quantity ")
       Inventory[name] = qty
       print("The Quantity Of The Item Is Updated")
     else:
       print("Product Is Not Found")
   
   elif choice == "5":
     name = input("Entet The Item To Remove ")
     if name in Inventory:
       del Inventory[name]
       print("The Item Is Delected Successfully ")
     else:
       print("Product Is Not Found ")

   elif choice == "6":
     print("Exit")
     break

   else:
     print("Invalid Option ")     