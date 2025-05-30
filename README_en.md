# AquaTrioPico

**AquaTrioPico** is a simple automatic watering system for three plants using one water tank. It is powered by a **PicoPi** board and controls three water pumps via relays, based on real-time soil moisture readings.

## Features

- Waters three separate pots
- Real-time soil moisture monitoring
- Pump activation only when moisture drops below threshold
- Low power consumption – suitable for continuous use
- Optional OLED display or manual control

## Required Components

- PicoPi
- 3x DC water pump 3–5V
- 3x relay module
- 3x soil moisture sensor (analog or digital)
- Water tank
- Breadboard MB102 + jumper wires
- (Optional) OLED I2C display
- (Optional) 3D printed enclosure

## Folder Structure

```
AquaTrioPico/
├── firmware/         # Source code (MicroPython or Arduino)
├── hardware/         # Wiring diagrams, pinout, photos
├── 3d-print/         # STL files for the enclosure
├── docs/             # Photos, diagrams, usage documentation
├── LICENSE           # License file
└── README.md         # This file
```

## License

MIT License
