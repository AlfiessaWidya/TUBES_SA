def knapsack_brute_force(value, berat, kapasitas):
    num_item = len(value)
    max_value = 0
    subset_terbaik = []

    # Hasilkan semua kemungkinan himpunan bagian dari item
    for i in range(2**num_item):
        subset = []
        total_value = 0
        total_berat = 0

        # Periksa setiap bit item dalam representasi biner dari i
        for j in range(num_item):
            if (i >> j) & 1:
                subset.append(j)
                total_value += value[j]
                total_berat += berat[j]
        # Uperbarui subset terbaik jika memiliki nilai dan bobot yang lebih tinggi dalam kapasitas
        if total_berat <= kapasitas and total_value > max_value:
            max_value = total_value
            subset_terbaik = subset

    return max_value, subset_terbaik

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
optimal_value, item_terpilih = knapsack_brute_force(value, berat, kapasitas)
print("Kapasitas\t:", kapasitas)
print("Optimal value\t:", optimal_value)
print("Item terpilih\t:", item_terpilih)