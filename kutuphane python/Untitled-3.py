class Kutuphane:
    def __init__(self):
        self.file = open("book.txt", "a+")
        self.books = []


    def kitap_listele(self):
        print("*** Kitap Listesi ***")
        for kitap in self.books:
            print(f"{kitap[0]} , {kitap[1]} , {kitap[2]} ,{kitap[3]}")

    def kitap_ekle(self):
        adi = input("Kitap Adı: ")
        yazar = input("Yazar: ")
        yayin_yili = input("Yayın Yılı: ")
        sayfa_sayisi = input("Sayfa Sayısı: ")
        yeni_kitap = [adi, yazar, yayin_yili, sayfa_sayisi]
        self.books.append(yeni_kitap)
        self.file.write(f"{adi},{yazar},{yayin_yili},{sayfa_sayisi}\n")
        print("Kitap eklendi.")

    def kitap_sil(self):
        adi = input("Silinecek kitabın adı: ")
        self.books = [kitap for kitap in self.books if kitap[0] != adi]
        print("Kitap silindi.")

def main():
    lib = Kutuphane()
    while True:
        print("\n*** MENÜ ***")
        print("1) Kitapları Listele")
        print("2) Kitap Ekle")
        print("3) Kitap Sil")
        print("q) Çıkış")
        secim = input("Seçiminizi yapın: ")

        if secim == '1':
            lib.kitap_listele()
        elif secim == '2':
            lib.kitap_ekle()
        elif secim == '3':
            lib.kitap_sil()
        elif secim == 'q':
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
