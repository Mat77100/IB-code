class Doll:
    # i have yet to add comments
    
    def __init__(self,name,greeting_style="Hello"):
        self.name = name
        self.greeting_style=greeting_style
    
    def say_hello(self):
        print(f"{self.greeting_style}, I am {self.name}")
    
arthur = Doll("Arthur")
John = Doll("John", greeting_style="Hey folks")
machine0110 = Doll("machine0110", greeting_style="01100010 01100101 01100101 01100010 00100000 01100010 01101111 01101111 01110000")

arthur.say_hello()
John.say_hello()
machine0110.say_hello()