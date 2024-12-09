
# Offline Speller Interface Using Blink Detection

## Overview
This project involves the creation of a simple offline "speller" interface that uses blinking to select letters of the alphabet. The interface displays letters in a loop, records the timestamps of each letter's display, and decodes user inputs based on blink data collected via an EEG electrode.

The project is designed as part of a cognitive science end-year project and consists of:
1. A program for displaying letters of the alphabet and logging timestamps.
2. A decoding algorithm to match blink data with displayed letters.
3. A report summarizing the project process, analysis, and findings.

---

## Features
- **Letter Display Program**:
  - Displays letters of the alphabet sequentially in a loop.
  - Logs the timestamps of each letter's display in a file (`litery_czas.txt`).
  - Includes both text-based and GUI-based versions (e.g., Tkinter, Pygame).

- **Blink Data Decoding**:
  - Analyzes EEG blink data to identify selected letters.
  - Matches blink timestamps with letter display times.

- **Report**:
  - Detailed documentation of methods, results, and improvements.

---

## Installation
### Prerequisites
- Python 3.7 or higher
- Required Python libraries:
  - `time`
  - `tba...`
  - `numpy`
  - `matplotlib`
  - `pandas` (optional, for data processing)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/KWojtowicz/Speller---Human-Computer-Interface.git
   cd Speller---Human-Computer-Interface
   ```
2. Install dependencies (use a virtual environment if preferred):
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
### Letter Display Program

- **Text-based version**:

- **GUI version (Tkinter)**:



### Decoding Blink Data
1. Collect blink data during the letter display session using the provided EEG setup.
2. Run the Jupyter Notebook for decoding:
   ```bash
   jupyter notebook decode_blinks.ipynb
   ```
3. Follow the instructions in the notebook to process and decode the blink data.

---

## File Structure




## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
- Course instructor @ratajczykd

---

## Contact
For questions or feedback, feel free to reach out at [kamil.k.woj@gmail.com].
