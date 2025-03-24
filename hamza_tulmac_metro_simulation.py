from collections import defaultdict, deque
import heapq
from typing import Dict, List, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        # Her istasyon için (komşu istasyon, geçiş süresi) bilgilerini tutar.
        self.komsular: List[Tuple['Istasyon', int]] = []

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int) -> None:
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """
        BFS algoritması kullanılarak istasyon sayısı bazında en az aktarmalı (en kısa) rotayı bulur.
        1. Başlangıç ve hedef istasyonların varlığını kontrol eder.
        2. deque ile kuyruk oluşturulur.
        3. Ziyaret edilen istasyonlar takip edilerek hedefe ulaşılırsa rota döndürülür.
        4. Rotayı bulamazsa None döner.
        """
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        kuyruk = deque([(baslangic, [baslangic])])
        ziyaret_edilen = set([baslangic.idx])
        
        while kuyruk:
            mevcut, rota = kuyruk.popleft()
            if mevcut == hedef:
                return rota
            for komsu, _ in mevcut.komsular:
                if komsu.idx not in ziyaret_edilen:
                    ziyaret_edilen.add(komsu.idx)
                    kuyruk.append((komsu, rota + [komsu]))
        return None

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """
        A* algoritması (heuristic 0 alınarak Dijkstra gibi çalışır) ile en hızlı (dakika bazında en kısa süreli) rotayı bulur.
        1. Başlangıç ve hedef istasyonların varlığını kontrol eder.
        2. heapq ile öncelik kuyruğu oluşturulur.
        3. Her adımda toplam süre güncellenir; hedefe ulaşıldığında rota ve toplam süre döndürülür.
        4. Rota bulunamazsa None döner.
        """
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        # Öncelik kuyruğu: (toplam_sure + heuristic, benzersiz id, mevcut istasyon, rota)
        pq = [(0, id(baslangic), baslangic, [baslangic])]
        ziyaret_edilen: Dict[str, int] = {}
        
        while pq:
            toplam_sure, _, mevcut, rota = heapq.heappop(pq)
            if mevcut == hedef:
                return (rota, toplam_sure)
            if mevcut.idx in ziyaret_edilen and ziyaret_edilen[mevcut.idx] <= toplam_sure:
                continue
            ziyaret_edilen[mevcut.idx] = toplam_sure
            for komsu, sure in mevcut.komsular:
                yeni_sure = toplam_sure + sure
                heuristic = 0  # Uygun heuristic kullanılmadığından 0 değeri
                heapq.heappush(pq, (yeni_sure + heuristic, id(komsu), komsu, rota + [komsu]))
        return None

# Örnek İstanbul Metro Ağı kurulumu ve test senaryoları
if __name__ == "__main__":
    metro = MetroAgi()
    
    # Kırmızı Hat: Taksim, Beyoğlu, Şişli, Levent
    metro.istasyon_ekle("K1", "Taksim", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Beyoğlu", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Şişli", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "Levent", "Kırmızı Hat")
    
    # Mavi Hat: Yenikapı, Sultanahmet, Sirkeci, Eminönü
    metro.istasyon_ekle("M1", "Yenikapı", "Mavi Hat")
    metro.istasyon_ekle("M2", "Sultanahmet", "Mavi Hat")  # Transfer noktası
    metro.istasyon_ekle("M3", "Sirkeci", "Mavi Hat")
    metro.istasyon_ekle("M4", "Eminönü", "Mavi Hat")
    
    # Turuncu Hat: Kadıköy, Üsküdar, Bostancı, Maltepe
    metro.istasyon_ekle("T1", "Kadıköy", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Üsküdar", "Turuncu Hat")  # Transfer noktası
    metro.istasyon_ekle("T3", "Bostancı", "Turuncu Hat")  # Transfer noktası
    metro.istasyon_ekle("T4", "Maltepe", "Turuncu Hat")
    
    # Hat içi bağlantılar
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Taksim -> Beyoğlu
    metro.baglanti_ekle("K2", "K3", 6)  # Beyoğlu -> Şişli
    metro.baglanti_ekle("K3", "K4", 8)  # Şişli -> Levent
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # Yenikapı -> Sultanahmet
    metro.baglanti_ekle("M2", "M3", 3)  # Sultanahmet -> Sirkeci
    metro.baglanti_ekle("M3", "M4", 4)  # Sirkeci -> Eminönü
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Kadıköy -> Üsküdar
    metro.baglanti_ekle("T2", "T3", 9)  # Üsküdar -> Bostancı
    metro.baglanti_ekle("T3", "T4", 5)  # Bostancı -> Maltepe
    
    # Transfer bağlantıları (farklı hatlardaki istasyonlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Taksim (Kırmızı) <-> Sultanahmet (Mavi)
    metro.baglanti_ekle("K3", "T2", 3)  # Şişli (Kırmızı) <-> Üsküdar (Turuncu)
    metro.baglanti_ekle("M4", "T3", 2)  # Eminönü (Mavi) <-> Bostancı (Turuncu)
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: Yenikapı'dan Levent'e
    print("\n1. Yenikapı'dan Levent'e:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    else:
        print("Rota bulunamadı!")
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    else:
        print("Rota bulunamadı!")
    
    # Senaryo 2: Kadıköy'den Maltepe'ye
    print("\n2. Kadıköy'den Maltepe'ye:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    else:
        print("Rota bulunamadı!")
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    else:
        print("Rota bulunamadı!")
    
    # Senaryo 3: Maltepe'den Yenikapı'ya
    print("\n3. Maltepe'den Yenikapı'ya:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    else:
        print("Rota bulunamadı!")
    
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    else:
        print("Rota bulunamadı!")
