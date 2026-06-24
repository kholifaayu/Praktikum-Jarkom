# Laporan Praktikum modul 5

# Tujuan Praktikum
dapat menginvestigasi cara kerja protokol UDP menggunakan Wireshark

# jawab pertanyaan 
1. Berapa banyak field pada header UDP? Sebutkan namanya!
Header UDP memiliki 4 field, yaitu:

Source Port (Port Sumber)
Destination Port (Port Tujuan)
Length (Panjang)
Checksum

2. Perhatikan informasi “content field” pada paket yang Anda pilih di pertanyaan 1. Berapa
panjang (dalam satuan byte) masing-masing “field” yang terdapat pada header UDP?
jawab: 8 byte.

3. Nilai yang tertera pada ”Length” menyatakan nilai apa? Verfikasi jawaban Anda melalui
paket UDP pada trace.
jawab: Field Length menyatakan jumlah byte keseluruhan segmen UDP, yaitu:

Panjang Header UDP + Panjang Data (Payload)

Karena header UDP selalu 8 byte, maka:

Payload = Length - 8

4. Berapa jumlah maksimum byte yang dapat disertakan dalam payload UDP? (Petunjuk:
jawaban untuk pertanyaan ini dapat ditentukan dari jawaban Anda untuk pertanyaan 2)
jawab:payload UDP maksimum adalah 65.527 byte.

5. Berapa nomor port terbesar yang dapat menjadi port sumber? (Petunjuk: lihat petunjuk
pada pertanyaan 4)
jawab:nomor port terbesar adalah 65535.

6. Berapa nomor protokol untuk UDP? Berikan jawaban Anda dalam notasi heksadesimal dan
desimal. Untuk menjawab pertanyaan ini, Anda harus melihat ke bagian ”Protocol” pada
datagram IP yang mengandung segmen UDP.
jawab:
Pada header IPv4, nilai Protocol untuk UDP adalah:

Desimal: 17
Heksadesimal: 0x11

7. Pasangan paket UDP yang saya temukan adalah Frame 470 dan Frame 472. Frame 470 merupakan DNS Query yang dikirim dari host 192.168.1.109 ke server DNS 68.87.71.226 menggunakan source port 1051 dan destination port 53. Frame 472 merupakan DNS Response yang dikirim kembali dari 68.87.71.226 ke 192.168.1.109 dengan source port 53 dan destination port 1051. Hal ini menunjukkan bahwa Frame 472 adalah balasan terhadap Frame 470 karena alamat IP dan nomor port pada kedua paket saling bertukar serta jenis paket berubah dari query menjadi response.

![hasil gambar](../assets/image/modul%205.1.png)


