## Siomay DUMPling


## Description

Menurut ku memiliki catatan akan sangat membantu


## Challenge & Password

[chall.zip](https://mega.nz/file/dmJlxaRK#GMtprhcj3B66LxxNR0xFfjhuQygRJ1KgHFgdfPg-mZc) `_nih09871234P4S5w0rdnya_gAN`


## Solving

Gunakan [Volatility Framework](https://www.volatilityfoundation.org/releases) untuk menganalisa dump file

Cek profile dari dump file

> `volatility -f chall.raw imageinfo`

Terdapat suggested profile hasil imageinfo, gunakan profile yang lebih dominan yaitu `Win7SP1x64`

Kemudian analisa dengan cetak semua proses lists yang sedang berjalan menggunakan profile `Win7SP1x64`

> `volatility -f chall.raw pslist --profile=Win7SP1x64`

Dan terdapat beberapa proses running dan salah satunya `notepad.exe` dengan PID `2412`, lalu analisa proses tersebut jika terdapat suatu data text

> `volatility -f chall.raw --profile=Win7SP1x64 memdump --dump-dir=./ -p 2412`

Hasil dump akan berupa file dengan nama PID dari proses tersebut `2412.dmp`

Kemudian cek isi string nya, dan ditemukan berupa data text QR ASCII

> `strings -e l  ./2412.dmp | grep "X."`

Simpan string QR ASCII tersebut ke dalam file `.txt`, lalu convert menjadi file Image menggunakan Python, berikut solvernya [solver.py](./solver.py)

Setelah didapat menjadi QR Image, kemudian scan.


## FLAG
`Hackfest0x06{banh_banh_beli_siomay_sebaskom_ajah_:joy:}`
