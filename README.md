# HashCrackr 🚀

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/ghazal-fyzt/HashCracker?style=flat-square)

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Implementation](#implementation)
- [Getting Started](#getting-started)
- [Credits](#credits)

## Overview 🚀

HashCrackr is a Python-based tool designed to perform brute-force attacks on hashed passwords. Utilizing the SHA256 hashing algorithm, HashCrackr efficiently maps hashed passwords back to their original 4-digit numeric formats. This tool is particularly useful for educational purposes, demonstrating the vulnerabilities of simple password schemes and the importance of strong password practices in cybersecurity.

## Features 🔍

- **Brute-Force Attack**: Attempts all possible 4-digit numeric combinations (0000 to 9999) to crack hashed passwords.
- **SHA256 Support**: Utilizes the SHA256 hashing algorithm to match and reverse-engineer hashed passwords.
- **CSV Handling**: Reads input CSV files containing names and hashed passwords, and outputs cracked passwords in a new CSV file.
- **Extensible Design**: Easily add support for additional hash functions or more complex password formats.
- **Command-Line Interface**: Simple and straightforward CLI for ease of use.

## Implementation 🛠️

HashCrackr operates by generating a rainbow table of all possible 4-digit numeric passwords and their corresponding SHA256 hashes. It then compares the hashes from the input file against this table to identify and retrieve the original passwords.

### **Key Components:**

1. **Input Handling**:
    - Reads a CSV file (`input.csv`) with two columns: `name` and `hashed_password`.
    - Stores the names and hashed passwords in separate lists for processing.

2. **Rainbow Table Generation**:
    - Iterates through all possible 4-digit combinations (0000 to 9999).
    - Hashes each combination using SHA256 and stores the hash-password pair in a dictionary.

3. **Password Cracking**:
    - Compares each hashed password from the input against the rainbow table.
    - If a match is found, the original password is retrieved and stored.

4. **Output Generation**:
    - Writes the cracked passwords along with the corresponding names to an output CSV file (`output.csv`).

## Getting Started 🛠️

### **Prerequisites**

- **Operating System:** Windows, macOS, or Linux
- **Python:** Version 3.8 or higher

### **Installation**

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/ghazal-fyzt/HashCracker.git
    cd HashCracker
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### **Usage**

1. **Prepare Your Input CSV:**

    Ensure your `input.csv` is formatted with two columns: `name` and `hashed_password`.


2. **Run the Script:**

    ```bash
    python hash_crackr.py input.csv output.csv
    ```

3. **Check the Output:**

    The `output.csv` will contain the names and their cracked passwords.


## Credits 👏

This project was part of the final project for one of Jadi's courses in Introduction to Python. Special thanks to Jadi Mirmirani for their guidance and support.

[Visit jadijadi's GitHub](https://github.com/jadijadi)


