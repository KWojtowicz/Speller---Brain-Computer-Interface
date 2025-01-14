# **Project Report: Blink-Based Speller Interface**
_Grabowska J. & Wojtowicz K., Human-Computer Interaction, Faculty of Psychology and Cognitive Sciences, Adam Mickiewicz University, 2024/2025_

## **1. Task Description**
The goal of the project was to develop a simple offline "speller" interface that uses blinking to select letters of the alphabet. The interface displays letters in a loop, records the timestamps of each letter's display, and decodes user inputs based on blink data collected via an OpenBCI EEG electrode. The project was carried out in two-person groups and included the following tasks:

- Developing a program to display alphabet letters in a loop (polish alphabet).
- Collecting single channel OpenBCI EEG data.
- Creating an algorithm to decode recorded EEG data and match recorded blinks with letters.
- Preparing a report documenting the project.

---

## **2. Selected Methods**

### **a) Letter Display**
To display alphabet letters in a loop, the **Tkinter** library was used to create a simple graphical user interface. Each letter was displayed for 1 second and their timestamps were recorded using Unix time format in the `litery_czas.txt` file.

Data recording:
```python
with open("Data/litery_czas.txt", "a") as myfile:
        myfile.write(current_letter + ', ' + str(time.time()) + '\n')
```

### **b) Blink Detection and Data Filtration**
The EEG signals collected during letter display were analyzed to detect blinks. The following methods were applied:

1. **Signal Filtering:**
   - A bandpass filter in the range of 1–20 Hz was applied to reduce noise and isolate blink-related signals.
   - Filtering was implemented using the provided `aseegg` module.

2. **Blink Detection:**
   - A threshold for the signal was calculated.
   - First, intervals during which the signal is greater than `signal mean + 1.5 * standard deviations` were determined. 
   - The intervals form the potential blinks. Then intervals were narrowed only only to potential blinks that are longer than 50 ms and are at least 50 ms apart.
   - These criteria should eliminate small rapid eye movements without eliminating actual blinks.

**Filtration and detection was based on [BLINKER Documentation](https://vislab.github.io/EEG-Blinks/).**

### **c) Letter Decoding**
Blink timestamps were compared with the letter display time intervals recorded in `litery_czas.txt`. Matching data was saved as list of letters `blinked_letters`.

---

## **3. Analysis and Results**
 
### **a) Detected blinks**
The collected EEG data were filtered and analyzed for blink signal. Results:
- Detected blinks timestamps: `[1734081761.3918755,
 1734081768.407744,
 1734081780.4984891,
 1734081781.5211663,
 1734081786.4954152,
 1734081795.5597646,
 1734081813.6475134,
 1734081816.671228,
 1734081817.6932497,
 1734081823.7379277,
 1734081832.7105572,
 1734081833.7340474,
 1734081847.825498,
 1734081848.8444574,
 1734081851.8201602,
 1734081858.841068,
 1734081860.8908377,
 1734081861.912717,
 1734081862.93318,
 1734081863.91526,
 1734081873.904448,
 1734081879.9956002,
 1734081889.9935217,
 1734081891.022148,
 1734081892.0383708,
 1734081893.0148077,
 1734081894.0404255,
 1734081895.0614529,
 1734081897.0615914,
 1734081898.0858688,
 1734081899.0587494,
 1734081903.0580156,
 1734081910.1267376,
 1734081928.2138608,
 1734081937.2344208,
 1734081938.252507,
 1734081939.2307842,
 1734081940.2531123,
 1734081942.2977166,
 1734081943.275237,
 1734081944.2998807,
 1734081945.274155,
 1734081955.3638103]
`
- Corresponding letters: `['O',
'T',
 'Ę',
 'H',
 'Ć',
 'U',
 'Ł',
 'B',
 'Ż',
 'A',
 'I',
 'M',
 'U',
 'Ł',
 'Ż',
 'Ć',
 'F',
 'Ń',
 'Ó',
 'Z',
 'P',
 'M',
 'U',
 'J',
 'L',
 'Ł',
 'G',
 'Ę',
 'H',
 'Ź']`

### **b) Result Analysis**
Although signals resembling blinks were detected, synchronizing these signals with the letter timestamps did not provide a meaningful result. The decoded letters did not correspond to any Polish word. This outcome highlights the need for further improvements in both signal recording and filtration algorithms.

---

## **4. Problems and Limitations**

- **Noise in EEG Signal:** There was a limited accuracy in blink detection due to high noise levels in the EEG signal. Low quality of recorded data resulted in an inaccurate blinks detection and incorrect letter identification. 

---

## **5. Possible Improvements**

- **Enhanced Signal Filtering:** Using advanced methods like filtration based on machine learning alogorithms could improve blink detection.
- **EEG upgrade and subject isolation:** 
Using a more accurate EEG device and isolating the subject from potential electromagnetic interference from the environment could improve the signal used for analysis.

---
