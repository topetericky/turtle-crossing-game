# 🐢 Turtle Crossing Game

A classic arcade-style game built with Python using the turtle graphics module. Inspired by *Frogger*, the player controls a turtle that must cross a busy road while avoiding randomly generated cars. With each successful crossing, the game speeds up and the level increases.

---

## 🎮 Gameplay Features

- Use the **Up Arrow** key to move the turtle forward.
- Cars are randomly generated and move from right to left.
- Each time the turtle reaches the top, the level increases and car speed ramps up.
- Collision with a car ends the game with a "Game Over" screen.

---

## 📁 Project Structure
turtle-crossing-game/
├── main.py # Main game loop and screen setup
├── player.py # Player movement and finish line logic
├── car_manager.py # Car generation, movement, and speed logic
├── scoreboard.py # Score tracking and level display

---

## 💻 Techniques Used

- **Python 3**
- `turtle` (for graphics and animation)
- `random` (for car positioning and generation)
- Object-Oriented Programming (classes and inheritance)
- Basic game loop and collision detection
