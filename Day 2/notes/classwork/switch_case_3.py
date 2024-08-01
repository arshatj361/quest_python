#Repeat the problem 2 for multiple orders. In each order the customer will order one food item only.

veg_items = {
    1 : 'Mysuru Filter Coffee',
    2 : 'Yummy Idly-vada',
    3 : 'Worlds soft Mysuru Mailari Dosa',
    4 : 'Bhupal Special Poha',
    5 : 'Bengaluru tamato-peanuts Upama'
}
nonveg_items = {
    1 : 'Egg Pokoda',
    2 : 'Chicken Biryani',
    3 : 'Fish Fry',
    4 : 'Mutton Masala'
}
food_types = {
    1 : veg_items,
    2 : nonveg_items
}
food_menu = {
    1 : '1:Coffee 2:Idly-Vada 3:Dosa 4:Poha 5:Upama',
    2 : '1:Egg Pokoda 2:Chicken Biryani 3:Fish Fry'
}

print('Welcome to our hotel The Taste')
while True:
    user_choice = int(input('1:Veg 2:Non-Veg \t Your choice please: ')) 
    items = food_menu.get(user_choice, 'Invalid')
    if items == 'Invalid':
        print('Invalid choice entered')
        break
    print(items)
    food_item_number = int(input('Enter item number that you wish have:'))

    print('Your ' + food_types.get(user_choice).get(food_item_number) + ' is here')
    user_choice = int(input('Do you wish to have more: Press 1 if yes: '))
    if user_choice != 1:
        break
print('Thank you, Visit again')