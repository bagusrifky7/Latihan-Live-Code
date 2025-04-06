print('Welcome to Calories Calculator                  ')
print('                                                ')
print('List of food: Rice, Chicken, Apple, Banana, Egg ')
print('List of workout: Running, Walking, Cycling, Yoga')
print('                                                ')


class calorie_caculator:
    #Atribut berisi dict dari makanan dan aktivitas serta dict kosong untuk input list
    def __init__(self): 
        self.food_calorie = {
            'rice': 200,
            'chicken': 250,
            'apple': 95,
            'banana': 105,
            'egg': 78
        }
        self.activity_burn_per_hour = {
            'running': 600,
            'walking': 250,
            'cycling': 500,
            'yoga': 200
        }
        self.list_food = {}
        self.list_activity = {}

    # Method untuk log makanan
    def log_food(self, *args, **kwargs):
        for food in args:
            for f, q in kwargs.items(): # Double loop untuk mengakses tuple args dan dict kwargs
                if food in self.food_calorie and food == f:
                    quantity_count = q['quantity'] * self.food_calorie[food]
                    self.list_food.update({food : quantity_count})

        # .values() digunakan untuk mengakses elemen dari dict keys         
        total_food = sum(self.list_food.values()) 
        print(f'Total calories from food: {total_food}')
    
    # Method untuk log aktivitas 
    def log_activity(self, *args, **kwargs):
        for activities in args:
            for a, d in kwargs.items(): # Double loop untuk mengakses tuple args dan dict kwargs
                if activities in self.activity_burn_per_hour and activities == a:
                    duration_count = (d['duration'] / 60) * self.activity_burn_per_hour[activities]
                    self.list_activity.update({activities : duration_count})
        
        total_activities = sum(self.list_activity.values())
        print(f'Total calories burn from activities: {total_activities}')

    # Method untuk perhitungan kalori dari log makanan dan aktivitas    
    def cal_net_calories(self):
        cal_net = sum(self.list_food.values()) - sum(self.list_activity.values())
        
        if cal_net > 0:
            print(f'Surplus: {cal_net}')
        elif cal_net < 0:
            print(f'Deficit: {int(abs(cal_net))}')
    
    def running_app(self):
        while True:
            print('Menu')
            print('1. Log food')
            print('2. Log activities')
            print('3. Total calories')
            print('4. Exit')
            print('')
            
            choice = input('Input menu: ')

            try:
                if choice == '1': # Menu 1
                    input_food = input('Log food: ').lower()
                    if input_food not in self.food_calorie: #Jika input tidak ada di dalam dict food_calorie
                        raise ValueError
                    else:
                        args = {input_food}
                        input_quantity = int(input('Quantity: '))
                        kwargs = {input_food : {'quantity' : input_quantity}}
                        self.log_food(*args, **kwargs)
            
                elif choice == '2': # Menu 2
                    input_activities = input('Log activities: ').lower()
                    if input_activities not in self.activity_burn_per_hour:
                        raise ValueError
                    else:
                        input_duration = int(input('Duration: '))
                        args = {input_activities}
                        kwargs = {input_activities : {'duration' : input_duration}}
                        self.log_activity(*args, **kwargs)

                elif choice == '3': # Menu 3
                    if not self.list_food and not self.list_activity: #Jika belum log keduanya
                        print('No log for activities or foods yet')
                    elif not self.list_activity: # Jika belum log activity
                        print('No log activities yet')
                    elif not self.list_food: # Jika belum log makanan
                        print('No log food yet')
                    else:
                        self.cal_net_calories()

                elif choice == '4': # Menu 4
                    print('Thank you for using the calculator')
                    break 
                
                else: 
                    raise ValueError
            # Digunakan agar program lebih seamless    
            except ValueError:
                print('Error: Invalid input')
            
            print('                                     ')


# Jalankan aplikasi
if __name__ == '__main__':
    calculator = calorie_caculator()
    calculator.running_app()


