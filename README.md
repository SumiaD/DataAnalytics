## Data used

Get and analyze corona statistics in Germany from https://api.corona-zahlen.org.

Alternatively, get corona statistics in the US from https://covidtracking.com/data/api.

## How to get started?

#### Data Platform Appliance

Clone the project from this repository, open Jupyter Notebook *api_requests.ipynb* and try to install the libraries. The most libraries should be preinstalled, therefore to save your time only install the ones that are missing in the appliance (you will see which ones are missing in the error message):

```bash
pip install <PACKAGE>
```

Alternatively, you can install all the packages from the requirements list, already installed packages will be automatically omitted by pip (but this still can take longer):

```bash
pip install -r data-analytics/requirements.txt
```

#### VS Studio Code

Clone the project from this repository and then creeate & activate the virtual environment:

```bash
python3 -m venv data-analytics/.myvenv
source data-analytics/.myvenv/bin/activate
```

Install the requirements:

```bash
pip install -r data-analytics/requirements.txt
```

Select the .myvenv as your interpreter:

Command Palette > Select Interpreter > Enter interpreter path > Select the .myenv from this project

Select your .myenv as your Kernel.

> **TIP**: If your VS Studio Code has troubles assigning your new environment as your Kernel, create a new Jupyter Notebook file - then you should be able to select your .myvenv as your Kernel.

You are all set! Now you should be able to reproduce each step in the Jupyter Notebook.

Once you are done with the analysis, deactivate the environment:

```bash
deactivate
```

## Chart Outputs

![Cases](/assets/charts/cases.png)

![Cases by State](/assets/charts/cases_by_state.png)

![Hospitalization Cases by State](/assets/charts/hospitalization7days_by_state.png)

![Historic Hospitalization Cases by State](/assets/charts/hospitalization7days_by_state_history.png)

![Recovered by State](/assets/charts/recovered_by_state_history.png)

