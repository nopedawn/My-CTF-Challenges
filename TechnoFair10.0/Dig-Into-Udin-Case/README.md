# Dig Into Udin Case

Description:
```
Udin menerima pekerjaan, akhir-akhir ini dia menerima job sebagai Email Analyzer dengan jobdesk analisis pesan email, suatu hari dia berhadapan dengan client yang melampirkan email berisi penyuluhan auth dari perusahaan tidak dikenal, atau mungkin saja itu semacam email phising? Alhasil dia kewalahan setelah berupaya mencari tahu sendiri informasi tersebut dengan mengidetifikasi lampiran email yang telah dia unduh. Kini Udin meminta untuk mengidentifikasi hasil dump PC-nya dengan mencari tahu beberapa informasi tentang Offset, nama serta email perusahaannya dan kapan waktu asli email terkirim.


Flag Format: TechnoFairCTF{Offset_Nama Perusahaan_Email_d/m/Y-H:M:S}
```

[Chall](https://mega.nz/file/on5E2ChC#_GJeJkqpMIksW3XvmZt0H4mVPzNOOc8z7jQ745lahBM)

Password: `P455w0rd-f0r-TH15-Ch4LL-@#!`

Ketentuan:
> - `Offset` = Offset/Inode tersebut
> - `Nama Perusahaan` = nama perusahaannya
> - `Email` = nama email perusahaannya
> - `d/m/Y-H:M:S` = (Hari/Bulan/Tahun-Jam:Menit:Detik) waktu asli email terkirim

Contoh:
`TechnoFairCTF{0xffff31337_ZoneTravel_admin-center@zonetravel.com_24/08/2023-02:16:30}`

Flag:
`TechnoFairCTF{0xffffa09fbabcd1c8_DeliverBox_support-division@deliverbox.com_05/07/2023-08:49:12}`

Author: jsbach#7151