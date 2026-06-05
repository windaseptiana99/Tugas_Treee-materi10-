class Node:
    def __init__(self, nama):
        self.nama = nama
        self.children = []

    def tambah_anak(self, child):
        self.children.append(child)


def tampilkan_menu(node, level=0):
    print("  " * level + "- " + node.nama)

    for child in node.children:
        tampilkan_menu(child, level + 1)



menu_restoran = Node("Menu Restoran")

makanan_pembuka = Node("Makanan Pembuka")
makanan_utama = Node("Makanan Utama")
makanan_penutup = Node("Makanan Penutup")

menu_restoran.tambah_anak(makanan_pembuka)
menu_restoran.tambah_anak(makanan_utama)
menu_restoran.tambah_anak(makanan_penutup)

makanan_pembuka.tambah_anak(Node("Sup Ayam"))
makanan_pembuka.tambah_anak(Node("Salad Buah"))
makanan_pembuka.tambah_anak(node("fruty cake"))


makanan_utama.tambah_anak(Node("Nasi Goreng"))
makanan_utama.tambah_anak(Node("Mie Goreng"))
makanan_utama.tambah_anak(Node("Ayam Bakar"))
makanan_utama.tambah_anak(node("nasi liwet"))

makanan_penutup.tambah_anak(Node("Es Krim"))
makanan_penutup.tambah_anak(Node("Puding Coklat"))
makanan_penutup.tambah_anak(Node("cake"))

tampilkan_menu(menu_restoran)