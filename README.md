# 🇮🇩 BahasaNusantara

> Interpreter Python dengan sintaks Bahasa Indonesia — dirancang untuk edukasi, developer lokal, dan pemula programming.

[![PyPI Version](https://img.shields.io/pypi/v/bahasa-nusantara)](https://pypi.org/project/bahasa-nusantara)
[![Python Versions](https://img.shields.io/pypi/pyversions/bahasa-nusantara)](https://pypi.org/project/bahasa-nusantara)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/bahasa-nusantara)](https://pypi.org/project/bahasa-nusantara)

---

## ✨ Apa itu BahasaNusantara?
**BahasaNusantara** adalah interpreter alternatif Python yang memungkinkan kamu menulis kode dengan **sintaks Bahasa Indonesia**, namun tetap kompatibel dengan semua library Python.  
Dirancang untuk mempermudah pembelajaran programming bagi pelajar dan pemula di Indonesia.

---

## 🚀 Fitur Unggulan

- 🔤 Translasi otomatis keyword Python → Bahasa Indonesia
- 📚 Kompatibel dengan pustaka Python (NumPy, Pandas, scikit-learn, dll.)
- 🖥️ Mode REPL interaktif seperti Python asli (BETA)
- 🌈 Output berwarna & error dalam Bahasa Indonesia
- ⚡ Performa tinggi (langsung eksekusi, tanpa file sementara)
- 📄 Dukungan file `.nus`
- 🔧 CLI Commands: `jalankan`, `run`, `nus`, `bahasa-nusantara`

---

## ⚙️ Instalasi

### 🔸 Dari PyPI
```bash
pip install bahasa-nusantara
```

### 🔸 Dari Source
```bash
git clone https://github.com/daffa-aditya-p/bahasa-nusantara.git
cd bahasa-nusantara
pip install .
```

---

## 📥 Contoh Kode `.nus`

```nus
fungsi halo_dunia(nama):
    tulis("🌍 Halo,", nama)
    tulis("Selamat datang di BahasaNusantara!")
    kembali benar

fungsi main():
    nama = tanya("Siapa nama Anda? ")
    halo_dunia(nama)

    angka_list = [1, 2, 3, 4, 5]
    tulis("Panjang list:", panjang(angka_list))
    tulis("Angka acak:", acak(angka_list))

jika __name__ == "__main__":
    main()
```

🧪 Jalankan dengan:
```bash
jalankan main.nus
```

---

## 🔄 Sintaks Indonesia ke Python

| Bahasa Indonesia | Python |
|------------------|--------|
| fungsi | def |
| kembali | return |
| jika | if |
| jika_lainnya | elif |
| lainnya | else |
| untuk | for |
| dalam | in |
| selama | while |
| selesai | break |
| teruskan | continue |
| tulis | print |
| tanya | input |
| gunakan | import |
| dari | from |
| sebagai | as |
| benar | True |
| salah | False |
| kosong | None |
| dan | and |
| atau | or |
| bukan | not |
| panjang() | len() |
| tipe() | type() |
| acak() | random.choice() |

---

## 💡 Contoh Lanjutan

### Web Scraping
```nus
gunakan requests
dari bs4 gunakan BeautifulSoup

fungsi ambil_judul(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    tulis("Judul:", soup.title.string)
```

### Machine Learning
```nus
dari sklearn.linear_model gunakan LinearRegression

fungsi main():
    model = LinearRegression()
    model.fit([[1], [2], [3]], [2, 4, 6])
    tulis("Prediksi:", model.predict([[4]]))
```

### GUI Tkinter
```nus
dari tkinter gunakan Tk, Label

fungsi main():
    jendela = Tk()
    Label(jendela, text="Halo Dunia!").pack()
    jendela.mainloop()
```

---

## 🧑‍🏫 Panduan Pemula

1. Buat file `halo.nus`
2. Tulis kode dengan sintaks Bahasa Indonesia
3. Jalankan pakai `jalankan halo.nus`
4. Eksplorasi pustaka Python yang kamu suka

---

## 🛣️ Roadmap & Kontribusi

**Fitur selanjutnya:**

- [ ] Highlight error interaktif
- [ ] Modul belajar otomatis
- [ ] Ekstensi VSCode
- [ ] Dukungan runtime Web (browser)

**Ingin kontribusi?** Fork repo ini, push branch baru, dan buat Pull Request. Tambahkan contoh `.nus` jika kamu menambah keyword baru.

---

## ❓ FAQ

**Q: Apakah ini interpreter baru?**  
A: Ini adalah wrapper Python, bukan pengganti CPython.

**Q: Bisa pakai semua library Python?**  
A: Ya! Karena kamu tetap menjalankan Python asli.

**Q: Aman untuk pemula dan sekolah?**  
A: Sangat aman. Dibuat khusus untuk edukasi.

---

## 👤 Tentang Penulis

**Nama:** Daffa Aditya Pratama  
**Email:** [daffaadityp@proton.me](mailto:daffaadityp@proton.me)  
**GitHub:** [@daffa-aditya-p](https://github.com/daffa-aditya-p)

---

## ⭐ Dukung Proyek Ini!

Beri ⭐ di GitHub dan bantu sebarkan ke teman, guru, atau komunitasmu.  
Mari bersama tingkatkan akses belajar programming di Indonesia 🇮🇩

---
