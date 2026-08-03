# Currency Converter

## Description

A simple command-line currency converter built with Python. This project uses an exchange rate API to convert an amount from one currency to another in real time.

## Features

* Supports multiple world currencies
* Simple terminal interface
* Uses a personal API key provided by the user

## Requirements

* Python 3.10+
* `requests` library

Install the required library:

```bash
pip install requests
```

## Setup

1. Clone this repository:

```bash
git clone https://github.com/your-username/currency-converter.git
cd Currency-Converter
```

2. Open the Python file.

3. Replace:

```python
api_key = "api.key"
```

with your own API key.

You can get a free API key from **https://www.exchangerate-api.com**, which is also the API used in this project.

## Example

**Input 1**

```text
300 GBP
```

**Input 2**

```text
EUR
```

**Output**

```text
300 GBP equals 350.33 EUR
```

> **Note:** This example was generated using the exchange rate on **3 August 2026, 1:35 PM GMT**.

## Technologies Used

* Python
* Requests
* REST API
* JSON

## Future Improvements

* Exchange rate history
* Save conversion history
