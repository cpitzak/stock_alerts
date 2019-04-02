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

# Example Ouput:
Note: The alerts.ini is just an example. These aren't values that I use or recommend. Personally, I'd want JPM and WFC to be 15% less than the graham number. You can update the graham_number.py calculator to do this or create another calculation python file for less_than_graham_number.
<pre>
2019-04-01 17:37:33,539 INFO Running COST with alerts: ['pe_ratio']
2019-04-01 17:37:34,219 INFO FAILED pe_ratio message: COST: P/E ratio 31.35, expected P/E: 15.0
2019-04-01 17:37:34,219 INFO Running USB with alerts: ['graham_number']
2019-04-01 17:37:35,123 INFO FAILED graham_number message: USB Graham Number is $43.14, C: $49.07. H: $49.14, L: $48.3
2019-04-01 17:37:35,123 INFO Running MCO with alerts: ['pe_ratio']
2019-04-01 17:37:35,789 INFO FAILED pe_ratio message: MCO: P/E ratio 27.37, expected P/E: 15.0
2019-04-01 17:37:35,789 INFO Running VRSN with alerts: ['peter_lynch_value']
2019-04-01 17:37:36,707 INFO FAILED peter_lynch_value message: VRSN: Peter Lynch Value is $60.64, C: $185.96. H: $186.12, L: $182.11
2019-04-01 17:37:36,707 INFO Running WFC with alerts: ['graham_number']
2019-04-01 17:37:37,594 INFO PASSED graham_number message: WFC Graham Number is $52.25, C: $48.81. H: $48.9, L: $48.17
2019-04-01 17:37:37,595 INFO Running BAC with alerts: ['price']
2019-04-01 17:37:37,854 INFO FAILED price message: BAC Expected Price is $22.89, C: $28.54. H: $28.74, L: $27.85
2019-04-01 17:37:37,854 INFO Running HD with alerts: ['pe_ratio', 'peter_lynch_value']
2019-04-01 17:37:38,516 INFO FAILED pe_ratio message: HD: P/E ratio 22.21, expected P/E: 15.0
2019-04-01 17:37:39,413 INFO FAILED peter_lynch_value message: HD: Peter Lynch Value is $134.53, C: $195.64. H: $195.9, L: $192.85
2019-04-01 17:37:39,413 INFO Running JPM with alerts: ['graham_number']
2019-04-01 17:37:40,324 INFO PASSED graham_number message: JPM Graham Number is $104.22, C: $104.64. H: $104.68, L: $102.12
WFC Graham Number is $52.25, C: $48.81. H: $48.9, L: $48.17
JPM Graham Number is $104.22, C: $104.64. H: $104.68, L: $102.12
</pre>