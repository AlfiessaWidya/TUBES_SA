def knapsack_greedy(berat, value, kapasitas):
    # Hitung rasio nilai ke berat untuk setiap item
    rasio = []
    for i in range(len(berat)):
        total_rasio = value[i] / berat[i]
        rasio.append((total_rasio, i))

    # Urutkan item dalam urutan menurun dari rasio nilai ke berat
    rasio.sort(reverse=True)
    
    total_value = 0
    total_berat = 0
    item_dipilih = []
    
    for total_rasio, index in rasio:
        item_berat = berat[index]
        
        # periksa apakah menambahkan item melebihi kapasitas
        if total_berat + item_berat <= kapasitas:
            total_value += value[index]
            total_berat += item_berat
            item_dipilih.append(index)
    
    return total_value, item_dipilih
 
 # read data
file = open(r'E:\Kuliah\SEMESTER 4\SA\Tubes\file.txt', 'r')
read = file.read()
file.close()
masukan = read.split()
arr = list(map(int, masukan))

# deklarasi berat, nilai, dan kapasitas dengan array kosong
berat = []
value = []
kapasitas = []

# deklarasi n data untuk mensplit inputan 
n = 5
# deklarasi i dan j untuk inital state perulangan
i = 0
j = 0
# membagi masukan sebanyak 3 berupa berat, nilai, dan kapasitas
for i in range(n):
    berat.append(arr[i])
i+=1
for j in range(n):
    value.append(arr[i+j])
j+=1
kapasitas = arr[i+j]

# print nilai optimal dan item yang dipilih
optimal_value, item_terpilih = knapsack_greedy(berat, value, kapasitas)
print("Kapasitas\t:", kapasitas)
print("Optimal value\t:", optimal_value)
print("Item terpilih\t:", item_terpilih)