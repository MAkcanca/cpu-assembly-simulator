## Bilgisayar Mimarisi - CPU Assembly Register Simulator
2020 yılında Eskişehir Osmangazi Üniversitesi Matematik ve Bilgisayar Bölümü'nde verilen Bilgisayar Mimarisi 1 dersi için hazırladığım CPU Assembly Register simülasyonudur.

Desteklediği komutlar
---
- LOAD
- MOV
- ADD
- STO
- **Indirect addressing, Direct addressing, Immediate addressing**

### CPU sınıfı
---
CPU(Komutlar [], memory={}, pc=1)
komutlar array tipinde, memory dict tipinde, pc int tipinde alınır.
Komut dizisi formatı şu şekildedir:
`komutlar = ["LOAD 123", "MOV AL,12", "STO @5"]`
Memory sözlük formatı şu şekildedir:
`memory = {"123": "10", "5": "123", "12":"314"}`
Sınıf objesi oluşturulduktan sonra calistir() fonksiyonuyla simülasyon başlatılabilir.
```
from cpu_sim import CPU
islemci1 = CPU(komutlar, memory=memory, pc=1)
islemci1.calistir()
```
Çıktı
```
PC: 1 MAR: None MBR: None IR: None ACC: None AL: None BL: None
PC: 2 MAR: 1 MBR: I1 IR: I1 ACC: None AL: None BL: None
PC: 2 MAR: 123 MBR: I1 IR: I1 ACC: 10 AL: None BL: None
PC: 3 MAR: 2 MBR: I2 IR: I2 ACC: 10 AL: None BL: None
PC: 3 MAR: 12 MBR: 314 IR: I2 ACC: 10 AL: 314 BL: None
PC: 4 MAR: 3 MBR: I3 IR: I3 ACC: 10 AL: 314 BL: None
PC: 4 MAR: 5 MBR: 123 IR: I3 ACC: 10 AL: 314 BL: None
PC: 4 MAR: 123 MBR: 123 IR: I3 ACC: 10 AL: 314 BL: None
PC: 5 MAR: 4 MBR: I4 IR: I4 ACC: 10 AL: 314 BL: None
```

---

Hatalar içerebilir, test edilmemiştir.