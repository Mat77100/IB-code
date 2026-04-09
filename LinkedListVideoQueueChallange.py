import webbrowser 

class node():
    def __init__(self,link,title):
        self.link = link
        self.title = title
        self.next = None
        self.prev = None

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.total = 0
    def add_vid(self,link,title):
        video = node(link, title)
        if not self.head:
            self.head = self.tail = self.current = video
        else:
            video.prev = self.tail
            self.tail.next = video
            self.tail = video
        self.total += 1
    def currentVideo(self):
        print("Current video: ",self.current.link)
        webbrowser.open(self.current.link)
    def nextVid(self):
        if self.current and self.current.next:
            self.current = self.current.next
            self.currentVideo()
        else:
            print("this is the end of the queue")
    def prevVid(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            self.currentVideo()
        else:
            print("this is the start of the queue")
    def removeVideo(self,Deleteindex):
        SelectedNode = self.head
        index = 0
        while index != Deleteindex:
            if index == self.total + 1:
                return
            else:
                SelectedNode = SelectedNode.next
        SelectedNode.prev.next = SelectedNode.next
        SelectedNode.next.prev = SelectedNode.prev
        self.total -= 1


Video_queue = Queue()

def menu():
    print("Current Video Queue:")
    TempArr = []
    Selected = Queue.head
    for i in range (0, Video_queue.total+1):
        TempArr.append(Selected.Title)
        Selected = Selected.next
    print("⇋".join(TempArr))
    print()
    print("Menu: (input one of these to perform an action)")
    print("1 -- Add a video")
    print("2 -- Show the currently playing")
    print("3 -- Go to next")
    print("4 -- Go to previous")
    print("5 -- Delete a video")
    action = 0
    while action < 1 or action > 5:
        try:
            action = input("Awating input (1 - 5)>> ")
        except:
            print("invalid")
    if action == 1:
        Queue.add_vid(input("Title: "),input("Link: "))
        menu()
    elif action == 2:

    elif action == 3:

    elif action == 4:

    elif action == 5:
