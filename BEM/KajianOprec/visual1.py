df = pd.read_csv("/content/gdrive/MyDrive/BEM /oprec_cleaned.csv")

# Define the mappings and conditions for each target value
mappings = {
    'Pergerakan': [
        'Akspro (Aksi dan Propaganda)',
        'Sokre (Sosial Kreatif)',
        'Ajarmas (Advokasi dan Jejaring Masyarakat)'
    ],
    'Analisis': [
        'Anstrat (Analisis Isu Strategis)',
        'Andal (Analisis Data dan Produk Digital)',
    ],
    'Kemahasiswaan': [
        'Kesmen (Kesehatan Mental)',
        'Adkesma (Advokasi dan Kesejahteraan Mahasiswa)',
        'PPK (Pengenbangan Potensi dan Karier)',
        'PPK (Pengembangan Potensi dan Karier)',
        'Panorama (Pengembangan Inovasi dan Karya Mahasiswa)',
        'Ekraf (Ekonomi Kreatif)'
    ],
    'Kemasyarakatan': [
        'Sosmas (Sosial dan Masyarakat)',
        'PDM (Pengembangan Desa Mitra)'
    ],
    'Relasi': [
        'Kolabin (Kolaborasi Internal)',
        'KOLABIN (Kolaborasi Internal)',
        'Hublu (Hubungan Luar)'
    ],
    'Sekretaris Jenderal' : [
        'PSDM (Pengembangan Sumber Daya Manusia)',
        'Sekkab (Sekretaris Kabinet)',
        'Medinfo (Media dan Informasi)',
        'Keuangan'
    ]
}

      ##### CHECK UNIQUE #####
# # Create a condition for rows that don't match any of the options in the mappings
# no_match_condition = ~df['Biro/Kementerian Pilihan 1'].isin([option for options in mappings.values() for option in options])

# # Print the values that don't fit any conditions above
# no_match_values = df[no_match_condition]['Biro/Kementerian Pilihan 1'].unique()
# print("Values that don't fit any conditions:")
# for value in no_match_values:
#     print(value)


# Initialize a dictionary to store counts
counts = {}

# Loop through the mappings and conditions, apply transformations, and store counts
for target_value, options in mappings.items():
    condition = df['Biro/Kementerian Pilihan 1'].isin(options)
    df.loc[condition, 'Biro/Kementerian Pilihan 1'] = target_value
    count = condition.sum()
    counts[target_value] = count
    print(f"{target_value}: {count}")

# Sort the counts in descending order
sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=False))

# Create a horizontal bar chart to visualize the counts
plt.figure(figsize=(10, 6))
plt.barh(list(sorted_counts.keys()), list(sorted_counts.values()))
plt.xlabel('Jumlah Pendaftar')
plt.ylabel('Bidang')
plt.title('Pendaftar per Bidang - Pilihan 1')
plt.tight_layout()

# Show the horizontal bar chart
plt.show()







#### no 3 #####
# Disini
df = pd.read_csv("/content/gdrive/MyDrive/BEM /oprec_cleaned.csv")

# Define the mappings and conditions for each target value
mappings = {
    'Pergerakan': [
        'Akspro (Aksi dan Propaganda)',
        'Sokre (Sosial Kreatif)',
        'Ajarmas (Advokasi dan Jejaring Masyarakat)'
    ],
    'Analisis': [
        'Anstrat (Analisis Isu Strategis)',
        'Andal (Analisis Data dan Produk Digital)',
    ],
    'Kemahasiswaan': [
        'Kesmen (Kesehatan Mental)',
        'Adkesma (Advokasi dan Kesejahteraan Mahasiswa)',
        'PPK (Pengenbangan Potensi dan Karier)',
        'PPK (Pengembangan Potensi dan Karier)',
        'Panorama (Pengembangan Inovasi dan Karya Mahasiswa)',
        'Ekraf (Ekonomi Kreatif)'
    ],
    'Kemasyarakatan': [
        'Sosmas (Sosial dan Masyarakat)',
        'PDM (Pengembangan Desa Mitra)'
    ],
    'Relasi': [
        'Kolabin (Kolaborasi Internal)',
        'KOLABIN (Kolaborasi Internal)',
        'Hublu (Hubungan Luar)'
    ],
    'Sekretaris Jenderal' : [
        'PSDM (Pengembangan Sumber Daya Manusia)',
        'Sekkab (Sekretaris Kabinet)',
        'Medinfo (Media dan Informasi)',
        'Keuangan'
    ]
}

# Initialize a dictionary to store counts
counts1 = {}
counts2 = {}

# Loop through the mappings and conditions, apply transformations, and store counts
for target_value, options in mappings.items():
    condition = df['Biro/Kementerian Pilihan 1'].isin(options)
    df.loc[condition, 'Biro/Kementerian Pilihan 1'] = target_value
    count = condition.sum()
    counts1[target_value] = count

print() 

for target_value, options in mappings.items():
    condition = df['Biro/Kementerian Pilihan 2'].isin(options)
    df.loc[condition, 'Biro/Kementerian Pilihan 2'] = target_value
    count = condition.sum()
    counts2[target_value] = count


sorted_counts1 = dict(sorted(counts1.items(), key=lambda item: item[1], reverse=False))
sorted_counts2 = dict(sorted(counts2.items(), key=lambda item: item[1], reverse=False))

# Select the top 3 values from sorted_counts1 and sorted_counts2
top3_counts1 = dict(list(sorted_counts1.items())[:3])
top3_counts2 = dict(list(sorted_counts2.items())[:3])

# Create a horizontal bar chart to visualize the top 3 counts for Pilihan 1
plt.figure(figsize=(10, 6))
plt.barh(list(top3_counts1.keys()), list(top3_counts1.values()))
plt.xlabel('Jumlah Pendaftar')
plt.ylabel('Bidang')
plt.title('Top 3 Pendaftar per Bidang - Pilihan 1')
plt.tight_layout()

# Show the horizontal bar chart for Pilihan 1
plt.show()

# Create a horizontal bar chart to visualize the top 3 counts for Pilihan 2
plt.figure(figsize=(10, 6))
plt.barh(list(top3_counts2.keys()), list(top3_counts2.values()))
plt.xlabel('Jumlah Pendaftar')
plt.ylabel('Bidang')
plt.title('Top 3 Pendaftar per Bidang - Pilihan 2')
plt.tight_layout()

# Show the horizontal bar chart for Pilihan 2
plt.show()
