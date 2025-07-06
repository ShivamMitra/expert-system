# 🏠 Expert-System – Smart Home Energy Management

A lightweight Python expert system that helps you **monitor and control household devices**—lights, fans and common appliances—while keeping track of estimated energy use. The single-file implementation (`energy management.py`) offers an interactive, menu-driven CLI that can be extended into larger IoT or rule-based projects.:contentReference[oaicite:0]{index=0}

---

## 🎯 Key Features

| Capability | Details |
|------------|---------|
| **Device control** | Switch lights 💡, fan 🌬️ and named appliances on/off individually. |
| **Critical-load safety** | Prevents accidental shutdown of refrigerator, geyser & heater. |
| **Occupancy simulation** | Randomly toggles “room occupied” state to test automation logic. |
| **Energy accounting** | Adds a small kWh cost every time a device state changes. |
| **Single-file, zero deps** | Uses only Python `random`—no external libraries required. |

---

## 🛠️ Installation


1 – Clone the repo
```
git clone https://github.com/ShivamMitra/expert-system.git
cd expert-system
```
2 – Run with Python ≥ 3.8
```
python "energy management.py"
Tip: On Windows, surround the filename with quotes (there’s a space).
Rename the file if you prefer: mv "energy management.py" energy_management.py
```


## 🚀 Quick Start
---
*** Energy Management System Menu ***
1. Turn On Lights     5. Turn On Appliance
2. Turn Off Lights    6. Turn Off Appliance
3. Turn On Fan        7. Simulate Room Occupancy
4. Turn Off Fan       8. Display Energy Consumption
9. Exit
---

Example session:
```
Enter your choices separated by space (1-9): 1 5
Lights turned on.
Enter the appliance name: TV
TV turned on.

Enter your choices separated by space (1-9): 8
Total Energy Consumed: 0.87 kWh
```


## 📂 Project Structure
```
expert-system/
└── energy management.py   # Core expert-system logic
Feel free to add:


README.md        # ← you are here
requirements.txt # (empty – uses only stdlib)
tests/           # unit tests
```


## 🧩 How It Works

1.State variables keep track of switch positions, appliance map and cumulative kWh.

2.Menu loop parses a space-separated list so you can batch commands.

3.Rules (if/elif chains) enforce critical-load protection and update energy stats.

4.Random occupancy lets you prototype presence-based automation without sensors.


## Extend it by:

1.Replacing the random occupancy stub with PIR / camera input.

2.Exposing functions as a REST API (e.g., using FastAPI) for mobile apps.

3.Persisting energy_consumed to a database or InfluxDB for dashboards.

4.Adding rule-weights or fuzzy logic for smarter decisions.



## 🧪 Testing
```

Sample pytest skeleton (create in tests/test_basic.py):


from energy_management import EnergyManagementSystem

def test_light_toggle():
    sys = EnergyManagementSystem()
    sys.turn_on_lights()
    assert sys.lights_on
    sys.turn_off_lights()
    assert not sys.lights_on
```


