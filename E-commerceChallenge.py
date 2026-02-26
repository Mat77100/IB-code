#26/02/2026
#OOP challange E-commerce price sorter
import random


class product():
    def __init__(self,name,price,digital,):
        self.name = name
        self.price = price
        self.digital = digital
    def GetName(self):
        return self.name
    def GetPrice(self):
        return self.price
    def IsDigital(self):
        return self.digital

class PhysicalProduct(product):
    def __init__(self, name, price, digital,ShippingCost):
        super().__init__(name, price, digital)
        self.ShippingCost = ShippingCost
        self.price += self.ShippingCost
    def GetShippingCost(self):
        return self.ShippingCost

#list was genarated by GPT
productlist = ["Wireless Bluetooth Headphones", "Stainless Steel Water Bottle", "Gaming Laptop", "Mechanical Keyboard", "Smartphone Case", "LED Desk Lamp", "Running Shoes", "Yoga Mat", "Digital Camera", "Portable Charger", "Coffee Maker", "Electric Toothbrush", "Backpack", "Smartwatch", "Sunglasses", "Winter Jacket", "Office Chair", "Mountain Bike", "Cookware Set", "Action Figure", "Board Game", "Bluetooth Speaker", "External Hard Drive", "USB Flash Drive", "Graphic T-Shirt", "Jeans", "Sneakers", "Tablet", "Monitor", "Printer", "Desk Organizer", "Fitness Tracker", "Hair Dryer", "Air Fryer", "Blender", "Vacuum Cleaner", "Electric Kettle", "Notebook", "Pen Set", "Smart TV", "HDMI Cable", "Router", "Microphone", "Webcam", "Tripod", "Guitar", "Piano Keyboard", "Drum Set", "Paint Set", "Sketchbook", "Lego Set", "RC Car", "Drone", "Flashlight", "Tool Kit", "Hammer", "Screwdriver Set", "Wrench Set", "Tennis Racket", "Football", "Basketball", "Camping Tent", "Sleeping Bag", "Hiking Boots", "Grill", "BBQ Tool Set", "Lawn Mower", "Garden Hose", "Plant Pot", "Sofa", "Dining Table", "Bed Frame", "Mattress", "Pillow", "Blanket", "Curtains", "Wall Clock", "Picture Frame", "Bookshelf", "Car Vacuum", "Dash Cam", "Car Seat Cover", "Motorcycle Helmet", "Skateboard", "Roller Skates", "Ice Skates", "Swimsuit", "Beach Towel", "Umbrella", "Raincoat", "Suitcase", "Travel Pillow", "Makeup Kit", "Lipstick", "Perfume", "Shampoo", "Conditioner", "Body Lotion", "Hand Soap", "Laundry Detergent", "Dishwasher Pods", "Paper Towels", "Toilet Paper", "Food Storage Containers", "Cutlery Set", "Dinner Plates", "Wine Glasses", "Water Filter", "Iron", "Ironing Board", "First Aid Kit", "Thermometer", "Blood Pressure Monitor", "Baby Stroller", "Baby Monitor", "Pet Bed", "Dog Leash", "Cat Tree", "Fish Tank", "Bird Cage", "Smart Doorbell", "Security Camera", "Smoke Detector", "Carbon Monoxide Detector", "Extension Cord", "Power Strip", "Surge Protector", "Laptop Stand", "Mouse Pad", "Desk Fan", "Space Heater", "Air Purifier", "Humidifier", "Dehumidifier", "Electric Blanket", "Watering Can", "Garden Shovel", "Rake", "Pressure Washer", "Car Wax", "Windshield Wipers", "Fuel Can", "Jump Starter", "Binoculars", "Compass", "Map", "Cookbook", "Novel", "Puzzle", "Card Game", "Smart Light Bulb", "VR Headset", "Streaming Device", "Router Modem Combo", "NAS Storage", "Graphics Tablet", "3D Printer", "Filament Spool", "Soldering Iron", "Raspberry Pi", "Arduino Kit", "VR Gloves", "Projector", "Projector Screen", "Electric Scooter", "Helmet Camera", "Fishing Rod", "Tackle Box", "Kayak", "Life Jacket", "Surfboard", "Snowboard", "Ski Goggles", "Climbing Harness", "Dumbbell Set", "Barbell", "Treadmill", "Exercise Bike", "Resistance Bands", "Foam Roller", "Massager", "Essential Oil Diffuser", "Alarm Clock", "Wall Art", "Candle Set", "Jewelry Box", "Necklace", "Watch", "Wallet", "Belt", "Gloves", "Scarf", "Hat", "Suit", "Dress", "Blazer", "Tie", "Sandals", "Slippers", "Bathrobe", "Shower Curtain", "Toothpaste", "Mouthwash", "Floss", "Razor", "Shaving Cream", "Nail Clippers", "Hair Straightener", "Curling Iron", "Mirror", "Step Ladder", "Toolbox", "Storage Bin", "Filing Cabinet", "Whiteboard", "Bulletin Board", "Calculator", "Label Maker", "Glue Gun", "Tape Measure", "Level Tool", "Stud Finder", "Chainsaw", "Leaf Blower", "Snow Shovel", "Fire Pit", "Patio Chair", "Hammock", "Inflatable Pool", "Hot Plate", "Slow Cooker", "Rice Cooker", "Toaster", "Microwave", "Refrigerator", "Freezer", "Dish Rack", "Knife Set", "Cutting Board", "Apron", "Oven Mitts", "Spice Rack", "Tea Kettle", "Mug Set", "Water Bottle Carrier"]
mixedproducts=[]

for i in range(0,len(productlist)):
    if random.randint(1,2) == 1:
        mixedproducts.append(product(productlist[i],round(random.uniform(1,100),2),True))
    else:
        mixedproducts.append(PhysicalProduct(productlist[i],round(random.uniform(1,100),2),False,round(random.uniform(4,30),2)))

for i in range(len(mixedproducts)):
    min_idx = i
    for j in range(i+1,len(mixedproducts)):
        if mixedproducts[j].GetPrice() < mixedproducts[min_idx].GetPrice():
            min_idx = j
        if min_idx != i:
            mixedproducts[i],mixedproducts[min_idx] = mixedproducts[min_idx],mixedproducts[i]


for product in mixedproducts:
    if product.IsDigital():
        output = str(product.GetName())
        output = output + "--->" + str(product.GetPrice())
    else:
        output = str(product.GetName())
        output = output + "--->" + str(product.GetPrice())
    print(output)