#python program 3



expense_dict = {   #use to store values in key: value pairs
  "item": [],
  "amount": [],
  
}
mylist = expense_dict['amount']
myiist2 = expense_dict['item']

# use while loop for continuos user inputing
i=0
while i<2:
    

    user_item = input('enter the name of item   ')
    #add the item in the disc
    expense_dict['item'].append(user_item)
    
    #add amount of that item
    user_amount = input('enter the amount of item   ')
    expense_dict['amount'].append(user_amount)
    i+=1
    
    
 # function to show data in dicitionay by for loop
def show_expense():
    
    print("your expen expenses")
    for y in range(2):
        print('your item name ---------------------------: '+ myiist2[y] )
        print("--------------------amount of that item--",mylist[y])
        
            
#printing the result to console            
print( show_expense())

            
 
