# 🚀 Cosmic Terminal

A cross-language coding adventure game written in C++ and Python!

## 🌟 Overview

Cosmic Terminal is a console-based game where you play as a hacker trying to compromise a spaceship's systems by solving programming challenges. The game combines:

- **C++**: Core game engine, terminal rendering, and input handling
- **Python**: Challenge generation and solution verification system
- **Cross-language bridge**: Seamless communication between C++ and Python

## 🎮 Gameplay

1. **Objective**: Hack through 5 security levels of a spaceship
2. **Challenges**: Solve Python coding problems at each level
3. **Progression**: Advance to next level upon successful solution
4. **Victory**: Complete all levels to take control of the ship!

## 🛠️ Installation

### Prerequisites
- C++17 compatible compiler (GCC, Clang, MSVC)
- CMake 3.12+
- Python 3.8+
- Python development headers

### Build Instructions

```bash
# Clone and setup
git clone <repository-url>
cd cosmic-terminal

# Create build directory
mkdir build && cd build

# Configure with CMake
cmake ..

# Build the project
cmake --build .

# Run the game
./cosmic_terminal