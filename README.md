# 🎼 Musical Floor with Raspberry Pi  

This project is a **musical floor instrument** built using infrared obstacle sensors and a Raspberry Pi.  
The floor is designed to look like **piano keys**, with each key assigned to one sensor.  
When a person steps on a key, the Raspberry Pi plays the corresponding note through a speaker.  

Additionally, there are **two control buttons** that allow the user to switch between different instrument modes:  
- 🎹 Piano  
- 🔔 Bells  
- 🎶 Flute  
- 🎸 Guitar  

---

## ⚙️ Components Used  
- **Raspberry Pi** (any model with GPIO support)  
- **8 Infrared Obstacle Detection Sensors (IR sensors)**  
- **2 Push Buttons (for instrument selection)**  
- **Speaker connected to Raspberry Pi**  
- Jumper wires and breadboard  

---

## 🎶 How It Works  
1. The floor is designed like piano keys, each equipped with an infrared sensor.  
2. When someone steps on a key, the sensor detects the movement.  
3. The Raspberry Pi processes the signal and plays the correct note based on the selected instrument.  
4. Two push buttons allow the user to switch between instrument modes (Piano, Bells, Flute, Guitar).  

---

## 🖥️ Software Setup  
1. Prepare Raspberry Pi with **Raspberry Pi OS**.  
2. Install required Python libraries for sound playback (`pygame` recommended):  
   ```bash
   sudo apt update
   sudo apt install python3-pygame
   ```  
3. Clone the project repository:  
   ```bash
   git clone https://github.com/YourUsername/musical-floor.git
   cd musical-floor
   ```  
4. Run the program:  
   ```bash
   python3 musical_floor.py
   ```  

---

## 📁 Project Structure  
```
musical-floor/
│── musical_floor.py   # Main code
│── sounds/            # Sound files for Piano, Bells, Flute, Guitar
│── README.md          # Project description
```

---

## 🎯 Features  
- 8-key musical floor designed like a piano  
- 4 different instrument modes (Piano, Bells, Flute, Guitar)  
- Two buttons to easily switch instrument type  
- Fun, interactive experience for kids and adults  
- Expandable with more keys or more instruments  

---

## 🚀 Future Improvements  
- Add LED lights that match the instrument mode  
- Bluetooth/WiFi support for wireless speakers  
- Record & playback functionality  

---

## 👤 Author  
Created by **Soheil Ahmadi**  
