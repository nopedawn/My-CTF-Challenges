## Transfer

## Description
Rekan saya mencoba men-transfer beberapa file, tetapi beberapa file tersebut ter-encode, bisakah kamu mencari tahu apa isi file tersebut.


## Solving
- Diberikan sebuah challenge packet capture, berisi packet traffic FTP (File Transfer Protocol)

- Cek Statistics > Protocol Hierarchy > Terdapat traffic FTP > dan juga Line-based text data

- Lalu lakukan Display filter > Search `ftp` > `ftp-data`

- Ada 3 file ber-ekstensi `.txt` ketiga file txt tersebut jika di cek bytesnya berisi string base64

- Langsung saja Follow TCP Stream > Save As > `index1.txt` `index2.txt` `index3.txt`

- Jika di decode ketiga file tersebut ternyata ber-signature `.png`, lakukan dengan menggunakan bash dan buat script automasinya

```bash
for i in {1..3}
do
	cat index$i.txt | base64 -d > image$i.png
done

```

- Flag terdapat pada file `index2.txt` setelah di decode ke `.png`


## FLAG
`Hackfest0x06{k1nd4_4wfuL_ftp_tr4ff1c5_1snt_1t}`
