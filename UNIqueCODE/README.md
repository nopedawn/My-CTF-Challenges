## Judul Soal
UNIqueCODE


## Deskripsi
Just some random unicode decrypting hidden file inside, I know you can solve this.


## Penyelesaian

Ekstrak file `chall.png` kemudian cari file bernama `UNI`

```bash
$ binwalk -e chall.png
```

File gambar berisi string unicode, setelah di ekstrak menggunakan `binwalk` akan terdapat banyak string `字0漢` pada file bernama `UNI`

```bash
$ cat UNI
```

Jika kita perhatikan lagi flagnya ternyata bilangan desimal, kita bisa decrypt dengan script [solver.py](./solver.py) yang kita susun berikut,

- Statement awal kita gunakan untuk membuka file `UNI` dengan akses read `r`, lalu baca isi filenya dengan fungsi `read()`

- Pada variabel `repl` dengan statement untuk mereplace string `字0漢` yang akan diganti dengan string berisikan enter " "

- Buat variabel `flag` berisi string kosong, untuk menampung flag

- Statement for mem-parsing setiap isi dari variabel `repl` akan diubah ke tipe data Python List untuk mendapatkan representasi string yang spesifik, dengan fungsi `chr()` lalu tampilkan flagnya.


## Metode Penyelesaian Lain

Bisa menggunakan webtools untuk decryptnya, https://www.asciitohex.com/ kemudian hilangkan string `字0漢` ganti menjadi spasi, didapatlah flagnya.


## FLAG
`Hackfest0x06{y34h_y0u_c0mpl3tl3ly_d3crypt_th1s_ch4ll3ng3}`
