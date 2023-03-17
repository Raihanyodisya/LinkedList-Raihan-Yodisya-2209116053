class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.history = []

    # CREATE
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.append_history("add", data)
            return
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node
        self.append_history("add", data)

    # READ
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_node
        print("None")

    # UPDATE
    def update(self, old_value, new_value):
        current_node = self.head
        while current_node:
            if current_node.data == old_value:
                current_node.data = new_value
                self.append_history("update", (old_value, new_value))
                return
            current_node = current_node.next_node
        print(f"{old_value} not found in the list.")

    # DELETE
    def delete_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next_node
            self.append_history("remove", data)
            return
        current_node = self.head
        while current_node.next_node:
            if current_node.next_node.data == data:
                current_node.next_node = current_node.next_node.next_node
                self.append_history("remove", data)
                return
            current_node = current_node.next_node
        print(f"{data} not found in the list.")

    def display_history(self):
        if not self.history:
            print("Anda Belum Melakukan Apapun")
        else:
            print("Riwayat Yang Anda Lakukan:")
            for operation in self.history:
                if operation[0] == "add":
                    print(f"Gitar Yang Ditambah : {operation[1]}")
                elif operation[0] == "remove":
                    print(f"Gitar Yang Dihapus : {operation[1]}")

    def append_history(self, operation, data):
        self.history.append((operation, data))

# MENU
def menu():
    # print("Selamat Datang Admin Toko Khusus Gitar")
    print("1. Menambahkan Merk Gitar")
    print("2. Melihat Daftar Gitar Yang Tersedia")
    print("3. Mengedit / Mengubah Daftar Gitar Yang Tersedia")
    print("4. Menghapus Daftar Gitar Yang Tersedia")
    print("5. Riwayat Daftar Gitar Yang Tersedia")
    print("0. Keluar")

# MAIN PROGRAM
linked_list = LinkedList()

while True:
    menu()
    choice = input("Masukkan Pilihan Anda : ")

    if choice == "1":
        data = input("Isi Merk Gitar Baru : ")
        linked_list.append(data)
    elif choice == "2":
        linked_list.print_list()
    elif choice == "3":
        old_value = input("Merk Gitar Lama : ")
        new_value = input("Merk Gitar Baru : ")
        linked_list.update(old_value, new_value)
    elif choice == "4":
        data = input("Merk Gitar Yang Ingin Dihapus: ")
        linked_list.delete_by_value(data)
    elif choice == "5":
        linked_list.display_history()
    elif choice == "0":
        print("Selamat Tinggal")
        break
    else:
        print("Pilihan Tidak Tersedia, Coba Lagi")