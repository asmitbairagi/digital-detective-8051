# Mission 5 — Number Systems and Data Representation

## 1. Objective
To understand different number systems, perform conversions between them, and learn how computers represent text using character encodings.

## 2. Number Systems
I studied four number systems:

- **Binary (Base 2):** Uses digits 0 and 1.
- **Octal (Base 8):** Uses digits 0–7.
- **Decimal (Base 10):** Uses digits 0–9.
- **Hexadecimal (Base 16):** Uses digits 0–9 and letters A–F.

## 3. Manual Conversions

Some conversions I practised:

- Binary to decimal: \(1101_2 = 13_{10}\)
- Decimal to binary: \(19_{10} = 10011_2\)
- Binary to hexadecimal: \(10101111_2 = AF_{16}\)
- Hexadecimal to decimal: \(3C_{16} = 60_{10}\)
- Hexadecimal to decimal: \(7B_{16} = 123_{10}\)
- Binary to octal: \(1101011_2 = 153_8\)
- Decimal to binary: \(45_{10} = 101101_2\)

## 4. Python Conversion Functions

I explored the following built-in Python functions:

- `bin(n)` — Converts an integer to binary.
- `oct(n)` — Converts an integer to octal.
- `hex(n)` — Converts an integer to hexadecimal.
- `int(value, base)` — Converts a number represented as a string in a specified base into a decimal integer.

I verified conversions using Python's interactive interpreter.

## 5. Number Converter Program

I created `number_converter.py` to convert:
- Decimal numbers into binary, octal, and hexadecimal.
- Binary, octal, and hexadecimal inputs into decimal.

I tested the program using decimal values 10, 45, and 60.

I also tested reverse conversions using:
- Binary: `101101`
- Octal: `55`
- Hexadecimal: `2d`

All three represent decimal 45.

## 6. ASCII and UTF-8

**ASCII:**
- Originally uses 7 bits and represents 128 characters.
- `A` has decimal value 65.
- `a` has decimal value 97.

**UTF-8:**
- Supports characters from many languages, symbols, and emojis.
- Uses 1–4 bytes per Unicode code point.
- Is backward-compatible with ASCII.

UTF-8 is more useful for modern applications because it supports a much wider range of characters.

## 7. Challenges and Learning

I learned how to convert numbers between different bases and verify my answers using Python. I also understood how character encoding allows computers to represent text.

One important learning was that Python's conversion functions return different data types: `bin()`, `oct()`, and `hex()` return strings, while `int()` returns an integer.

## 8. Files and Evidence

- `number_converter.py` — Python number conversion program.
- `README.md` — Mission documentation.

## 9. Commit Details

- Commit message: `Complete Mission 5`
- Branch: `main`