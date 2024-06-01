# Tic Tac Toe Game and Calculator Application

This repository contains two projects: a simple Tic Tac Toe game and a basic Calculator application, both built using PySide6 for the GUI.

## Tic Tac Toe Game

A simple Tic Tac Toe game supporting two modes: Player vs Player and Player vs CPU.

### Features

- Two game modes: Player vs Player and Player vs CPU.
- Dynamic color-changing buttons.
- Font customization upon game restart.
- Display of the current player's turn.
- Detection of win and draw conditions.
- Restart game functionality.
- About section with creator information.

### Installation

1. Clone the repository


2. Install the required dependencies:
    ```bash
    pip install PySide6
    ```

3. Ensure you have the `window.ui` file in the `tic-tac-toe` directory.

### Usage

1. Run the application:
    ```bash
    python main.py
    ```

2. Choose a game mode using the radio buttons.

3. Play the game by clicking on the buttons representing the grid.

4. Use the "Restart" button to reset the game. The font will change to "Viner Hand ITC" with size 50.

5. Change the button colors using the "Change Color" button.

6. View the creator's information using the "About" button.

## Calculator Application

A basic calculator application supporting basic arithmetic operations and several scientific functions.

### Features

- Basic arithmetic operations: addition, subtraction, multiplication, division.
- Scientific functions: square root, logarithm, sine, cosine, tangent, cotangent.
- Clear functionality to reset the input.
- Decimal point support.
- Results display.

### Installation

1. Navigate to the calculator directory:
    ```bash
    cd ../calculator
    ```

2. Install the required dependencies:
    ```bash
    pip install PySide6
    ```

3. Ensure you have the `mainwindow.ui` file in the `calculator` directory.

### Usage

1. Run the application:
    ```bash
    python main.py
    ```

2. Use the buttons to perform calculations:
    - Click digit buttons (0-9) to input numbers.
    - Click operation buttons (+, -, *, /) to perform arithmetic operations.
    - Click function buttons (sqrt, log, sin, cos, tan, cot) for scientific calculations.
    - Click the decimal point button (.) to add a decimal point.
    - Click the clear button (C) to reset the input.
    - Click the equal button (=) to calculate the result.

