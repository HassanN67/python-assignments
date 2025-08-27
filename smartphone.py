# Activity 1
# Base Class
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours
    
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number} 📞")
    
    def charge(self, hours):
        self.battery_life += hours
        print(f"{self.brand} {self.model} charged for {hours} hours. Battery life: {self.battery_life}h")

# Inherited Class
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_life, cooling_system):
        super().__init__(brand, model, battery_life)  # inherit attributes from Smartphone
        self.cooling_system = cooling_system
    
    def play_game(self, game):
        print(f"{self.brand} {self.model} is playing {game} 🎮 with {self.cooling_system} cooling system!")

# Example usage:
phone1 = Smartphone("Apple", "iPhone 15", 20)
gaming_phone = GamingPhone("Asus", "ROG Phone 7", 15, "liquid-cooling")

phone1.call("123-456-789")
phone1.charge(2)

gaming_phone.call("987-654-321")
gaming_phone.play_game("PUBG Mobile")
