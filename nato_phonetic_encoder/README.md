# NATO Phonetic Alphabet Encoder

This Python script utilizes the NATO phonetic alphabet to encode words into their corresponding phonetic codes.

## Usage

1. **Install Dependencies**

   Ensure you have Python installed on your system. Additionally, install the required `pandas` library using pip:

```code
> pip install pandas
```

2. **Run the Script**

Execute the script `nato_encoder.py` using Python. It will prompt you to enter a word, and then it will output the corresponding NATO phonetic codes.

python nato_encoder.py

3. **Input**

Enter the word you want to encode when prompted. Only alphabetic characters are considered; any non-alphabetic characters will be ignored.

4. **Output**

The script will return the NATO phonetic codes corresponding to the input word.

## Script Details

- **Reading Data**

The script reads the NATO phonetic alphabet data from the provided CSV file `nato_phonetic_alphabet.csv`.

- **Dictionary Creation**

It creates a dictionary where each letter is a key mapped to its corresponding phonetic code, using the data read from the CSV file.

- **Encoding Function**

The function `natoEncoder(text)` takes a word as input and returns a list of NATO phonetic codes. It converts the input word to uppercase, retrieves the phonetic codes for each letter from the dictionary, and returns them as a list.

## Files

- **nato_encoder.py**: The Python script implementing the NATO phonetic alphabet encoder.
- **nato_phonetic_alphabet.csv**: The CSV file containing the NATO phonetic alphabet data.
