print('=========================================================')
print('                                                         ')
print('                  Walmart Shopping App                   ')
print('                                                         ')
print('=========================================================')
print('                                                         ')
print('                                                         ')


class shopping_cart():
    def __init__(self):
        self.list_cart = {}

    def add_items(self, **add_item):
        for item,price in add_item.items():
            self.list_cart.update({item : price})

    def remove_items(self, *remove_item):
        for item in remove_item:
            if item in self.list_cart:
                print(f'Removed: {item}')
                del self.list_cart[item]

    
    def view_cart(self):
        print(f'Items in cart:')
        for item,price in self.list_cart.items():
            print(f'- {item} : {price}')
    
    def checkout(self):
        total = 0
        for item, price in self.list_cart.items():
            total += price
        
        print(f'Total : {total}')
    
    def running_app(self):
        while True:
            print('Menu:')
            print('1. Add item to your cart')
            print('2. Remove item for your cart')
            print('3. Display shopping cart')
            print('4. Checkout')
            print('5. Exit')
            print('                                             ')
            
            pilihan = input('Pilihan: ')
            
            try:

                if pilihan == '1':
                    things = input('Enter item you want to buy: ').title()
                    price  = int(input('Enter price of the item: '))
                    add_item = {things : price}
                    self.add_items(**add_item)
                    print(f'Item {things} succesfully added')
                
                elif pilihan == '2':
                    if not self.list_cart:
                        print('No items in the cart')
                    else:
                        remove = input('Enter item you want to remove: ').title()
                        remove_item = {remove}
                        if not remove in self.list_cart:
                            print('Item not in the cart')
                        else:
                            self.remove_items(*remove_item)

                elif pilihan == '3':
                    if not self.list_cart:
                        print('There\'s no items in the cart')
                    else:
                        self.view_cart()
                
                elif pilihan == '4':
                    if not self.list_cart:
                        print('No items in the cart yet')
                    else:
                        self.checkout()
                
                elif pilihan == '5':
                    print('Thank you for using Walmart App')
                    break
                
                else:
                    raise ValueError
            
            except ValueError:
                print('Error: Invalid input')
            print('')

if __name__ == '__main__':
    walmart = shopping_cart()
    walmart.running_app()
