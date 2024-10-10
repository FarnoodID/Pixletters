# Pixletters
A Python program to help solving [Pixletters](https://pixletters.com/), where players must guess a hidden five-letter word based on feedback from their guesses. The program provides visual representations of letters using pixel art, helping players determine which letters are correct and in the right position.

## Features
- **Word Selection**: The program uses a predefined list of words stored in `allwords.txt`.
- **Pixel Representation**: Each letter is represented by a pixel matrix, allowing for a unique visual feedback mechanism.
- **Feedback Processing**: After each guess, players input feedback using:
  - `2`: Indicates that the letter has pixels in the specified positions.
  - `0`: Indicates that the letter does not have pixels in the specified positions.
  - `1`: Indicates that there is no information about the pixel for now (the status of that position is unknown).
  - Players can also input individual letters that have been confirmed as correct.

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.

### Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/FarnoodID/PixLetters.git
   ```
2. Navigate to the project directory:
   ```bash
   cd PixLetters
   ```
### Usage
1. Run the program:
   ```bash
   python pixletters.py
   ```
2. The program will prompt you to enter your guesses and feedback.
3. Use the word "Titer" as your first guess for optimal results.
4. Enter your results using the specified format:
   - Example: ``22220 02220 r 10001 22222``
     - Each entry corresponds to a row of pixels, providing feedback on which pixels are filled (``2``), not filled (``0``), or unknown (``1``). ``r`` means the third letter is "r".
## Example Interaction
  - If you enter ``22220``, it means that the first letter has pixels filled in the first four positions but not in the last position.
  - If you find a letter that is confirmed as correct, you can enter it directly.
  - Each subsequent input corresponds to the next row of pixels.
## Additional Notes
  - The program will display the number of available words after each input.
  - To see all possible words at any time, type ``best``.
## How It Works
The program maintains a list of potential words and filters them based on user input and feedback. Each letter's validity is checked against the current guesses, allowing for refined guesses in subsequent rounds.
## Pixel Art Representation
Each letter is represented by a unique pixel matrix defined in the code. This visual representation enhances user interaction and provides immediate feedback on letter placement.
