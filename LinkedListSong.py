#made 19/03/2026
class SongNode: #bluprint for every node
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist
        self.prev = None
        self.next = None

class Playlist(): #uses SongNode to make lis
    def __init__(self):
        self.head = None #when a new list is made it has nothing in it
        self.tail = None
        self.current = None
    def add_song(self, title, artist):#when the function in called
        node = SongNode(title, artist) #it makes a node with the inputs
        if not self.head: #if its the first node to be made (Head = None)
            self.head = self.tail = self.current = node #the node is the head, tail, and current
        else: #if its not the first node
            node.prev = self.tail #assigns the current tail node as the previous in the new node
            self.tail.next = node #assigns the new node as the next in the current tail node
            self.tail = node #makes the new node the tail
    def show_current(self): #displays current song
        if self.current:#if there is a current song
            print(f"Currently playing: {self.current.title} - by - {self.current.artist}")
    def next_track(self): #Goes to next song
        if self.current and self.current.next: #if their is a current song and a valid next song
            self.current=self.current.next #set the current song to the next one
    def prev_track(self): #Goes to previous song
        if self.current and self.current.prev: #if theres a current song and a valid previous
            self.current = self.current.prev #set the current song to the previous

my_vibe = Playlist()

my_vibe.add_song("Bohemian Rapsody","The Queens")
my_vibe.add_song("Mr. Blue Sky","Electronic Light Orchestra")
my_vibe.add_song("Money for Nothing","Dire Straits")

my_vibe.show_current()

my_vibe.next_track()
my_vibe.next_track()
my_vibe.prev_track()

my_vibe.show_current()