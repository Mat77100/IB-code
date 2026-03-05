#05/03/2026
import tkinter as tk
class TicketNode:
    def __init__(self,number):
        self.ticket_number = number #The Data
        self.next_person = None #The pointer to next person

class TicketCounter:
    def __init__(self):
        self.ticketNum = 0
        self.first_person = None
    def TakeTicket(self):
        self.ticketNum += 1
        new_node = TicketNode(self.ticketNum)
        if not self.first_person: # if no nodes
            self.first_person = new_node #make a new one
            print(f"Ticket number {self.ticketNum} has been taken")
            return
        
        last = self.first_person
        while last.next_person:
            last = last.next_person
        last.next_person = new_node
        print(f"Ticket number {self.ticketNum} has been taken")
    def serve_next_customer(self):
        if not self.first_person: #if queue is empty
            print("No one is in line")
            return
        print(f"Currently serving ticket number {self.first_person.ticket_number}")
        self.first_person = self.first_person.next_person #next person in line becomes the first


pharmacy_line = TicketCounter()
root = tk.Tk()
tk.Button(root,text="Take ticket",command=pharmacy_line.TakeTicket).pack()
tk.Button(root,text="Serve next customer",command=pharmacy_line.serve_next_customer).pack()
root.mainloop()