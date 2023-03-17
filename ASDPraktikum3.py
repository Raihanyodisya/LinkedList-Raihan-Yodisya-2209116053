# import os
# os.system('clear')

# class Manusia:
#     def __init__(self, nama, ttl, nim):
#         self.nama = nama 
#         self.ttl = ttl
#         self.nim = nim

#     def aktivitas(self):
#         print(self.nama + " Sedang Gitaran")


# manusia1 = Manusia("Neymar", "Miaubaru, 50 Oktober 2029", "011")

# manusia1.nama = "Caesar"
# manusia1.ttl = "Samarinda, 30 Februari 2000"
# manusia1.nim = 68

# print(manusia1.nama)
# print(manusia1.ttl)
# print(manusia1.nim)

# manusia1.aktivitas()

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None 

#     def tambahdepan(self, value):
#         if self.head is None:
#             self.head = Node(value)

#         else:
#             nodebaru = Node(value)
#             nodebaru.next = self.head
#             self.head = nodebaru

#     def printlist(self):
#         if self.head is None:
#             print("Linked List Kosong")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data,end="=>")
#                 n = n.next

# listnya = LinkedList()

# listnya.tambahdepan(10)
# listnya.tambahdepan(15)
# listnya.tambahdepan(12000)
# listnya.tambahdepan(1000)
# listnya.tambahdepan(5678)
# listnya.tambahdepan(1234)
# listnya.tambahdepan(500000000)
# listnya.tambahdepan(111)
# listnya.tambahdepan(20)
# listnya.tambahdepan(19)
# listnya.tambahdepan(18)
# listnya.tambahdepan(17)
# listnya.tambahdepan(16)
# listnya.tambahdepan(14)
# listnya.tambahdepan(12)
# listnya.tambahdepan(13)
# listnya.tambahdepan(11)
# listnya.depan()

# listnya.printlist()