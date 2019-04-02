## Stock Alerts

This program will read from a list of stocks you are watching and check if they meet the criteria you are interested in.

I made the program  in a way that lets you "dropin" your calculation and then reference it in alerts.ini. Technically speaking this is the "strategy design pattern".
To do this you create your *calculation python file* following the rules in **Add Your Own Calculation** below. Then you use it in the alerts.ini. Take a look at how I did *pe_ratio.py*, *price.py*, *graham_number.py*, *peter_lynch_value.py* to get an idea of how to do that. And look at alerts.ini to see how I used those calculations.

# Setup
1.  conda create -n alerts python=3.6 anaconda
2. Activate your conda environment:
    1. Windows: activate tenk
    2. Linux: source activate tenk

# Run the program
`python stock_alerts.py`

# Add Your Own Calculation
1. In the alerts folder create a python file
2. In your python file create a method with this signature: def run(self, ticker)
    1. This method must return a dictionary with this format: { 'pass': bool_value, 'messsage': 'this is what you decide to output if your calculation passed' }
3. In your python file create: def __init__(self)
    1. In this method read from the alert.ini to get what your calculator needs (i.e. in my P/E ratio calculator I decided to read a pe_ratio field so I could specify the pe_ratio)
  
# Add Tickers
1. Open alerts/alerts.ini
2. Look through the ones I included:
    1. You'll see that the tickers are surrounded by []
    2. You'll see **alerts:** what comes after this is the python file names (separated by commas) of the calculation you created
3. Create a section for your ticker and either use the calcuation you created or use the calculations I created
