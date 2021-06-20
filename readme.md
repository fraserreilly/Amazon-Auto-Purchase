# Amazon Auto Purchase
This script checks if items are available on amazon and purchases them when they become available.

## Getting Started
### Requirements:
- Python 3
- Selenium (`pip install selenium`)
- Chrome WebDriver
- Credentials stored in enviroment variables

## Running the script
- Run `python main.py`. A new headless chrome window will be opened (you can check this by removing `options.headless = True` and logs will be displayed within your terminal.
- Do whatever you want, the script will run until it's closed, if it crashes it will be displayed in the cli.
- If the item is avaiable and purchased it will be displayed in the cli and the script will close.
