# AquaTrioPico

**AquaTrioPico** to prosty system automatycznego podlewania 3 roślin z jednego zbiornika, oparty na **PicoPi** i przekaźnikach sterujących trzema pompkami wodnymi. System działa na podstawie bieżących odczytów wilgotności gleby.

## Funkcje

- Podlewanie trzech oddzielnych doniczek
- Pomiar wilgotności gleby w czasie rzeczywistym
- Aktywacja pompki tylko przy niskiej wilgotności
- Niskie zużycie energii – przystosowany do pracy ciągłej
- Możliwość rozbudowy o wyświetlacz OLED lub sterowanie ręczne

## Wymagane komponenty

- PicoPi
- 3x pompka wodna DC 3–5V
- 3x przekaźnik
- 3x czujnik wilgotności gleby (analogowy lub cyfrowy)
- Zbiornik na wodę
- Breadboard MB102 + przewody
- (Opcjonalnie) Wyświetlacz OLED I2C
- (Opcjonalnie) Obudowa z drukarki 3D

## Struktura folderów

```
AquaTrioPico/
├── firmware/         # Kod źródłowy (MicroPython lub Arduino)
├── hardware/         # Schematy, pinout, zdjęcia
├── 3d-print/         # Modele STL obudowy
├── docs/             # Zdjęcia, diagramy, dokumentacja użytkownika
├── LICENSE           # Licencja
└── README.md         # Ten plik
```

## Licencja

Licencja MIT
