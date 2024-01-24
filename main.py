import random 

decorations = {
"chair": 20,
"table": 50,
"computer": 1200,
"couch": 400,
}

items = {
    "bone": 15,
    "wooden hammer": 20,
    "orb": 300, 
    "broken sword": 55
}

class Player:
    def __init__(self, username):
        self.username = username 
        self.cash = 50000
        self.level = 0
        self.current_exp = 0 
        self.exp_until_next_level = 50    
        self.inv = []    
        self.owns_house = False
        
    def display_attributes(self):
        print(f"""
User: {self.username}
Cash: {self.cash}
Inv: {self.inv_view()}
Lvl: {self.level}
Exp: {self.current_exp}
Exp to lvl: {self.exp_until_next_level}
              """)

    def inv_view(self):
        if not self.inv:
            return "[Inventory empty]"
        else:
            return f"\n- " + '\n- '.join(self.inv)
    
    def gamble(self, amount):
        if self.cash >= int(amount):
            gamb = random.randint(1, 100)
            if gamb >= 50:
                print("You won!")
                dbl_amnt = float(amount) * 2
                self.cash += dbl_amnt
                print(f"You made ${dbl_amnt:.2f}")
            else:
                print("You lost...")
                print(f"${amount} was removed from your wallet.")

    def decorate_house(self):
        if self.owns_house == False:
            print("You do not own a home yet.")
            print("you need $40000 to buy one.")
            if self.cash >= 40000:
                print("I see you have enough...")
                choice = input("Buy house (y/n)")
                if choice == "y":
                    self.cash -= 40000
                    self.owns_house = True
                    print("You have purchased a house!")
            else:
                print("You turn down the offer.")
        else:    
            for item, value in decorations.items():
                print(f"[{item}] - [{value}]")
            choice = input("Input: ")
            if choice in decorations:
                self.cash -= decorations[choice]
                print(f"You have added {choice} to your house.")
            else:
                print("That item is not in the decorations list.\nPlease select another. ")
        
    def farm_exp(self):
        print("You enter the wilderness...")
        amount_of_gold = random.randint(1, 75)

        print("You slay a goblin")
        print(f"You obtain ${amount_of_gold}")
        
        self.cash += amount_of_gold
        
        ran_item = random.choice(list(items.keys()))
        chance_for_item = random.randint(1, 100)
        if chance_for_item >= 50:
            print(f"you obtain a {ran_item}")
            self.inv.append(ran_item)
         
    def use_auction_house(self):
        autction_items = {"cloth": 25, "poison darts": 15, "fire dagger": 1500, "chicken cage": 30, "random pet": 2700}
        items = []
        for _ in range(3):
            random_items_from_auc_list = random.choice(list(autction_items))
            items.append(random_items_from_auc_list)
            
        for item in items:
            print(f"- {item}")
        choice = input("Would you like to buy any of the current items?: ")
        if choice in items:
             print(f"You get {choice}")
             self.inv.append(autction_items[choice])

def main():
    print("Welcome to life sim 728")
    username = input("What is your desired username: ")
    running = True 
    player = Player(username)
    while running: 
        print("""
What would you like to do?
1. Build house
2. Farm exp
3. Gamble
4. View stats
5. auct
6. Exit
              """)
        choice = input("Input: ")
        if choice == "1":
            player.decorate_house()
        elif choice == "2":
            player.farm_exp()
        elif choice == "3":
            print(f"You currently have {player.cash} dollars.")
            amount = input("How much would you like to gamble?: ")
            player.gamble(amount)
        elif choice == "4":
            player.display_attributes()
        elif choice == "5":
            player.use_auction_house()
        elif choice == "6":
            running = False
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()