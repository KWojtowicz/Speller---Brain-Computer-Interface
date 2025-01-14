
# Offline Speller Interface Using Blink Detection

_Grabowska J. & Wojtowicz K., Human-Computer Interaction, Faculty of Psychology and Cognitive Sciences, Adam Mickiewicz University, 2024/2025_

## Overview
This project involves the creation of a simple offline "speller" interface that uses blinking to select letters of the alphabet. The interface displays letters in a loop, records the timestamps of each letter's display, and decodes user inputs based on blink data collected via an OpenBCI EEG electrode.

The project is designed as part of a cognitive science end-year project and consists of:
1. A program for displaying letters of the alphabet and logging timestamps.
2. A decoding algorithm to match blink data with displayed letters.
3. A report summarizing the project process, analysis, and findings.

---

## Features
- **Letter Display Program** ([letter_displayer.py](letter_displayer.py)):
  - Displays letters of the alphabet sequentially in a loop using tkinter GUI.
  - Logs the timestamps of each letter's display in a file ([`litery_czas.txt`](Data/litery_czas.txt)).

- **Blink Data Decoding** ([EEG_Blinks_Data_Decoder.ipynb](EEG_Blinks_Data_Decoder.ipynb)):
  - Analyzes EEG data to identify blinks based on based on filtration from [BLINKER Documentation](https://vislab.github.io/EEG-Blinks/).
  - Matches blink timestamps with letter display times.

- **Report** ([Project_Report.md](Project_Report.md)):
  - Documentation of methods, results, and improvements.

---

## Installation
### Prerequisites
- Python 3.7 or higher
- Required Python libraries:
  - `time`
  - `tkinter`
  - `numpy`
  - `matplotlib`
  - `pandas`
  - `aseegg`

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
2. Install aseegg library (use a virtual environment if preferred):
    ```bash
   pip install ./Libraries/aseegg.py
   ```
---

## Usage
### Letter Display Program


- **GUI version (Tkinter)**:



### Decoding Blink Data
1. Collect blink data during the letter display session using preferred single channel EEG setup.
2. Open the Jupyter Notebook:
   ```bash
   jupyter notebook EEG_Blinks_Data_Decoder.ipynb
   ```
3. Select file path for your letters timestamps and EEG data record

---


## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
- Course instructor @ratajczykd

---

## Contact
For questions or feedback, feel free to reach out at [kamil.k.woj@gmail.com].
