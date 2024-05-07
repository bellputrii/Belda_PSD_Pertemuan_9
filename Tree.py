class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def remove_child(self, child):
        self.children.remove(child)
        child.parent = None

    def display_tree(self, prefix="", level=0):
        indent = "    " * level
        print(indent + prefix + self.data)
        for child in self.children:
            child_is_last = child == self.children[-1]
            child_prefix = "└── " if child_is_last else "└── "
            child.display_tree(child_prefix, level + 1)

print("-- SILSILAH KELUARGA -- \n")
kakek_nenek = Tree("Kakek/Nenek")
bibi_paman = Tree("Bibi/Paman")
rista = Tree("Rista")
sabya = Tree("Sabya")
budi = Tree("Budi")
ravito = Tree("Ravito")
atta = Tree("Atta")
sinta = Tree("Sinta")
meira = Tree("Meira")
arta = Tree("Arta")
tri = Tree("Tri")
azam = Tree("Azam")
fani = Tree("Fani")
khasya = Tree("Khasya")
ibu_ayah = Tree("Ibu/Ayah")
manda = Tree("Manda")
vero = Tree("Vero")
nica = Tree("Nica")
belda = Tree("Belda")
faza = Tree("Faza")
zahirah = Tree("Zahirah")
pram = Tree("Pram")
fairuz = Tree("Fairuz")
canaya = Tree("Canaya")
mono = Tree("Mono")
surya = Tree("Surya")


kakek_nenek.add_child(bibi_paman)
rista.add_child(sabya)
sabya.add_child(budi)
bibi_paman.add_child(ravito)
ravito.add_child(atta)
atta.add_child(sinta)
bibi_paman.add_child(meira)
meira.add_child(arta)
arta.add_child(tri)
bibi_paman.add_child(azam)
azam.add_child(fani)
fani.add_child(khasya)
kakek_nenek.add_child(ibu_ayah)
ibu_ayah.add_child(manda)
manda.add_child(vero)
vero.add_child(nica)
ibu_ayah.add_child(belda)
belda.add_child(faza)
faza.add_child(zahirah)
belda.add_child(pram)
pram.add_child(fairuz)
ibu_ayah.add_child(canaya)
canaya.add_child(mono)
mono.add_child(surya)


kakek_nenek.display_tree()
