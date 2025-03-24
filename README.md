# 🏰 Castle War

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green?logo=pygame)

**Castle War** is a head-to-head 2D strategy game built with **Pygame**. Spawn units, manage resources, and destroy your enemy's barracks in an epic pixel-art battle!


---

## 🎮 Gameplay Overview

You and your opponent each control a side of the screen with:

- **Barracks** – Spawn your army here.
- **Mines** – Generate resources using workers.
- **Towers** – Auto-fire on nearby enemies.
- **Walls** – Defend your structures.

Balance offense and defense while managing your gold to overwhelm your opponent!

---

## 🧩 Project Structure

```
.
├── main.py               # Main game loop and mechanics
├── loading_assets.py     # Loads sprites and animations
├── constants.py          # Game constants and settings
└── assets/               # All image and animation assets
```

---

## 🕹️ Controls

(Current controls are likely via UI interaction or hotkeys. Customize this once control bindings are finalized.)

---

## 📦 Installation

### Requirements

- Python 3.x
- Pygame

Install dependencies:

```bash
pip install pygame
```

### Run the Game

```bash
python main.py
```

---

## 📁 Assets

Make sure the following folders exist within your `assets/` directory:

- `assets/sky.png`
- `assets/ground.png`
- `assets/control.jpg`
- `assets/melee/left/`
- `assets/melee/right/`
- (Add other folders like `worker/`, `ranged/` as needed)

---

## 🧠 Features

- Real-time unit spawning and movement
- Resource gathering and gold management
- Defensive structures with auto-attack
- Modular codebase for easy expansion

---

## 🛠️ Future Enhancements

- 🎵 Sound effects and music
- 🧠 Smarter enemy AI
- 🧍‍♂️ Single-player campaign mode
- 🌐 Online multiplayer
- 💬 In-game tutorial and help screen

---
