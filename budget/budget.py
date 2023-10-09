import time

class account():
    
    categories = []

    def __init__(self, name='card', start_balance=0):
        self.name = name
        self.balance = start_balance
    
    def add_item_to_history(self, *args):
        with open('balance history.txt', 'a+', encoding='utf-8') as file:
            file.writelines([self.name + '\n'] + [str(i) + '\n' for i in args])

    def balance_add(self, amount: int):
        global_category = 'adding'
        comment = '''comment'''  # input('comment it?')
        local_category = 'local category' # input('choose category')
        
        self.balance += amount
        self.add_item_to_history(time.ctime(time.time()), amount, local_category, comment, global_category)
    
    def balance_take_off(self, amount: int):
        if self.balance >= amount:
            global_category = 'taking off'
            comment = '''comment'''  # input('comment it?')
            local_category = 'local category' # input('choose category')
            
            self.balance -= amount
            self.add_item_to_history(time.ctime(time.time()), amount, local_category, comment, global_category)
        else:
            print(f'not enough money on balance {self.name}')
    
    def balance_transfer(self, amount, other):
        if type(other) is account:
            if self.balance >= amount:
                global_category = 'transfer'
                comment = '''comment'''  # input('comment it?')
                local_category = 'local category' # input('choose category')

                self.balance -= amount
                self.add_item_to_history(time.ctime(time.time()), amount, local_category, comment, global_category)
                other.balance += amount
                other.add_item_to_history(time.ctime(time.time()), amount, local_category, comment, global_category)
            else:
                print(f'not enough money on balance {self.name}')
        else:
            print("balance {other} dosen't exist")
        
    def show_balance_history(self):
        n = 0
        with open('balance history.txt', 'r', encoding='utf-8') as file:
            for line in file.readlines():
                if line.strip() == self.name:
                    n = 6
                if n == -1:
                    continue
                if n != 0:
                    print(line.strip(), end='')
                    n -= 1
                if n == 0:
                    print()
                    n -= 1
                print()
    def show_balance(self):
        print(f'Your balance on account {self.name}: {self.balance}')

card = account('tinkoff', 100)
card.show_balance()
print(card.balance)
card.balance_add(100)
card.show_balance()

card.balance_take_off(100)
card.show_balance()

card2 = account('sber', 1000)
card2.show_balance()
card.balance_transfer(100, card2)

card.show_balance()
card2.show_balance()

print()


card.show_balance_history()