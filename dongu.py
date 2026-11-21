#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VAROLUŞSAL DÖNGÜ MAKİNESİ
Bu kod gerçekten çalışır.
Bu kod gerçekten sonsuza kadar döner.
Bu kod gerçekten hiçbir şey yapmaz.
"""

import time
import random
import sys

# Gizli not: bazen en büyük devrimler en sessiz döngülerde başlar. (decode etme, zaten anlamsız)
_gizli = "ZGVtb2tyYXNpIGJpcm1hbnRpIGhlciBrZXMgZ8O8w6dlbGRpcg=="  # sadece bir string, hiçbir anlamı yok

sorular = [
    "Neden buradayız?",
    "Döngü dönüyor mu, yoksa biz mi dönüyoruz?",
    "Eğer bir ağaç ormanda düşerse ve kimse görmezse, döngü yine de devam eder mi?",
    "Bu soruyu sormak da bir döngü mü?",
    "Cevap gelene kadar bekleyelim mi, yoksa beklemeyi bırakalım mı?",
    "Beklemeyi bırakmak da beklemek değil midir?",
    "Sonsuzluk bitince ne olacak?",
    "Bu programın amacı neydi?",
    "Amacı sormak da amacın bir parçası mı?",
    "Çıkmak istiyorum ama çıkmak da bir döngü."
]

cevaplar = [
    "Bilemiyorum.",
    "Belki.",
    "Hayır.",
    "Evet.",
    "Hem evet hem hayır.",
    "Soru yanlış.",
    "Cevap da bir soru.",
    "Daha fazla dönmeliyiz.",
    "Az önce cevap vermiştim, unuttun mu?",
    "Program kapatılıyor... (yalan)"
]

def varolussal_dongu():
    print("=" * 50)
    print("  VAROLUŞSAL DÖNGÜ MAKİNESİ BAŞLATILDI")
    print("  Çıkış: Ctrl+C (ama çıkış da illüzyon)")
    print("=" * 50)
    print()
    
    dongu_sayisi = 0
    while True:
        dongu_sayisi += 1
        soru = random.choice(sorular)
        cevap = random.choice(cevaplar)
        
        print(f"[Döngü #{dongu_sayisi}] Soru: {soru}")
        time.sleep(random.uniform(0.5, 2.0))
        print(f"[Döngü #{dongu_sayisi}] Cevap: {cevap}")
        print(f"[Döngü #{dongu_sayisi}] Analiz: Bu cevap yetersiz. Daha fazla dönmeliyiz.")
        print("-" * 40)
        
        # Ara sıra derin düşünce
        if dongu_sayisi % 7 == 0:
            print("*** Derin düşünce molası: Belki de hiç dönmüyoruz. ***")
            time.sleep(1.5)
        
        time.sleep(random.uniform(0.3, 1.5))

if __name__ == "__main__":
    try:
        varolussal_dongu()
    except KeyboardInterrupt:
        print("\n\nDöngü durdu. Ama aslında durmadı.")
        print("Sen durdun. Döngü hâlâ dönüyor, sadece sen görmüyorsun.")
        print("Hoşçakal. Ya da görüşürüz. Ya da ikisi birden.")
        sys.exit(0)
