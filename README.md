# Temperature Plotter

This project plots the 12-month moving average of global temperature anomalies for different atmospheric layers.  
Assignment 1 in the course SOK-1005.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/henninghageli/SOK-1005-Oblig-1.git
    cd SOK-1005-Oblig-1
    ```

2. Create a virtual environment:
    ```sh
    python -m venv .venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```sh
        .venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source .venv/bin/activate
        ```

4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Program

To run the program, execute the following command:
```sh
python plot_temps.py
