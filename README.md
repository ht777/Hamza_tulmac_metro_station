 İstanbul Metro Rota Simülasyonu

 1. Proje Başlığı ve Kısa Açıklama
**İstanbul Metro Rota Simülasyonu**, İstanbul'un farklı hatlarını temsil eden istasyonlar arasında, iki farklı rota bulma algoritması kullanarak (BFS ve A*) en az aktarmalı ve en hızlı rotayı tespit etmeyi amaçlayan bir projedir. Bu simülasyon, gerçek dünya ulaşım problemlerine algoritmik çözümler üretme ve grafik veri yapılarıyla çalışma becerilerini geliştirmeyi hedefler.

2. Kullanılan Teknolojiler ve Kütüphaneler
- Python 3:** Projenin geliştirilmesinde kullanılan ana programlama dilidir. Python'un okunabilirliği ve geniş ekosistemi, bu tür simülasyon projelerinde tercih edilme nedenlerinden biridir.
- heapq:** A* algoritmasında, öncelik sıralaması yaparak en düşük maliyetli (süre bazında) rotayı hızlıca seçmek için kullanılan yerleşik kütüphanedir. Bu kütüphane, algoritmanın verimliliğini artırmak amacıyla minimum yığını (min-heap) yönetir.
- collections:**  
- deque:** BFS algoritmasında, FIFO (First-In-First-Out) prensibine göre istasyonları sıraya koymak ve hızlıca erişmek için kullanılır. Bu yapı, kuyruk işlemlerinde yüksek performans sağlar.  
- defaultdict:** Metro ağı içerisindeki istasyonları ve hatları organize etmek için kullanılır. Anahtar bulunmadığında otomatik olarak varsayılan liste üretir; bu sayede istasyon ekleme işlemleri daha temiz ve hata payı düşük şekilde gerçekleşir.
- typing:** Kodun daha okunabilir ve anlaşılabilir olması için tip belirtimleri (type hints) sağlar; bu, özellikle büyük projelerde hata ayıklamayı kolaylaştırır.

 3. Algoritmaların Çalışma Mantığı
  BFS (Breadth-First Search) Algoritması
- **Nasıl Çalışır?**  
  BFS algoritması, başlangıç istasyonundan itibaren, komşu istasyonları katman katman ziyaret eder. Bir kuyruk veri yapısı (deque) kullanarak, ilk olarak en yakın komşuları işleme alır ve daha sonra sırayla tüm istasyonları ziyaret eder. İlk bulunan hedef istasyon, en az aktarmalı yani en kısa istasyon sayısına sahip rota olarak kabul edilir.
- **Neden Kullanıldı?**  
  Metro ağında, aktarma sayısının minimum olduğu bir rota kullanıcılar için pratik ve tercih edilir olduğundan, BFS algoritması bu probleme doğal bir çözüm sunar. Algoritmanın garantilediği en kısa yol bulma özelliği, rotanın aktarma sayısı bazında optimize edilmesine olanak tanır.

 A* Algoritması
- **Nasıl Çalışır?**  
  A* algoritması, her adımda f(n) = g(n) + h(n) fonksiyonunu kullanır:
  - **g(n):** Başlangıç istasyonundan mevcut istasyona kadar geçen gerçek toplam süre.
  - **h(n):** Hedefe olan tahmini süre (bu projede uygun bir tahmin bulunmadığından 0 değeri kullanılarak algoritma, Dijkstra algoritması gibi çalışır).
  
  Öncelik kuyruğu (heapq) yardımıyla, her adımda en düşük f(n) değerine sahip rota seçilir. Böylece, geçiş süreleri göz önüne alınarak en hızlı rota belirlenir.
- **Neden Kullanıldı?**  
  Metro ağında, kullanıcıların zaman açısından en verimli rotayı bulabilmesi önemlidir. A* algoritması, hem gerçek süre hesaplaması (g) hem de (bu örnekte) basitleştirilmiş bir tahmin (h = 0) kullanarak, en hızlı ve zaman açısından optimum rotayı hızlıca bulmaya yardımcı olur. Bu, özellikle yoğun hat transferlerinin ve farklı güzergahların bulunduğu durumlarda pratik bir çözüm sunar.

4. Örnek Kullanım ve Test Sonuçları
Projede örnek olarak İstanbul temalı üç farklı hat üzerinden (Kırmızı, Mavi, Turuncu) test senaryoları gerçekleştirilmiştir:

- Senaryo 1: Yenikapı'dan Levent'e** 
 - **BFS Algoritması:** En az aktarmalı (istasyon sayısı bazında) rota tespit edilmiştir.
 - **A\* Algoritması:** Toplam geçiş süresi hesaplanarak, en hızlı rota belirlenmiştir.
  
- Senaryo 2: Kadıköy'den Maltepe'ye**
  - Her iki algoritma da, farklı hatlar arası transferleri göz önünde bulundurarak doğru ve mantıklı rota sonuçları üretmiştir.
  
- Senaryo 3: Maltepe'den Yenikapı'ya**
  - Transfer noktaları (örneğin; Taksim-Sultanahmet, Şişli-Üsküdar, Eminönü-Bostancı) üzerinden yapılan hesaplamalarla, algoritmalar kullanıcıya en uygun rotayı sunmuştur.

Test senaryoları çalıştırıldığında, algoritmalar ekrana rota bilgilerini (istasyon isimleri) ve toplam geçiş süresini (dakika bazında) başarılı bir şekilde yazdırmaktadır.

 5. Projeyi Geliştirme Fikirleri
- **Gerçek Veri Entegrasyonu:**  
  İstanbul'un gerçek metro hatlarını ve istasyon verilerini kullanarak, daha kapsamlı bir metro ağı simülasyonu oluşturulabilir. Canlı trafik veya bakım bilgileri de entegre edilerek, dinamik rota hesaplamaları yapılabilir.
  
- **Görselleştirme:**  
  Matplotlib, Plotly veya benzeri grafik kütüphaneleri ile, metro hatlarının ve rotaların harita üzerinde görselleştirilmesi sağlanabilir. Bu, kullanıcı deneyimini artırır ve simülasyonun anlaşılmasını kolaylaştırır.
  
- **Mobil ve Web Uygulaması:**  
  Projenin backend'ine entegre edilebilecek interaktif bir kullanıcı arayüzü geliştirilerek, kullanıcıların gerçek zamanlı rota sorgulaması yapması mümkün hale getirilebilir.
  
- **Alternatif Rota Algoritmaları:**  
  Çok kriterli optimizasyon, Dijkstra’nın varyasyonları veya genetik algoritmalar gibi ek yöntemler araştırılarak, farklı koşullar altında en uygun rotanın belirlenmesi sağlanabilir.
  
- **Ek Özellikler:**  
  Bilet fiyatı hesaplaması, bekleme süreleri ve aktarma süreleri gibi ek parametreler eklenerek, daha gerçekçi bir simülasyon ortaya konulabilir.




