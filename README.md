## Simple Streamlit App

This project demonstrates how to create an interactive web app using Streamlit. Users can select a number from a slider, view the selection, generate random data, and see it visualized in a line chart.

### Features

* Select a number using a slider
* Display the selected number
* Generate a random DataFrame with 50 rows and 3 columns
* Display the DataFrame
* Visualize the DataFrame with a line chart

### Installation

**Prerequisites**

* Python 3.7 or higher
* pip (Python package installer)

**Steps**

1. **Clone the repository (if using Git):**

   ```bash
   git clone https://github.com/abdulwahed-mans/Streamlit.git
   cd Streamlit
   ```

2. **Create and activate a virtual environment:**

   **Windows (Command Prompt):**

   ```bash
   python -m venv myenv
   myenv\Scripts\activate
   ```

   **Windows (PowerShell):**

   ```bash
   python -m venv myenv
   .\myenv\Scripts\Activate
   ```

3. **Install required packages:**

   * If you have a `requirements.txt` file:

     ```bash
     pip install -r requirements.txt
     ```

   * If no `requirements.txt` file:

     ```bash
     pip install streamlit pandas numpy
     ```

### Usage

1. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

2. **Open your web browser:**

   * The app will automatically open in your default browser once the server is running.
   * If not, visit `http://localhost:8501` in your browser.

### File Structure

```
├── myenv/           # Virtual environment directory
├── app.py            # The main Python script for the Streamlit app
├── README.md        # This README file
└── requirements.txt # Python packages required for the project
```

### License

This project is licensed under the MIT License (see the LICENSE file for details).

### Acknowledgments

* Streamlit Documentation
* Pandas Documentation
* NumPy Documentation
