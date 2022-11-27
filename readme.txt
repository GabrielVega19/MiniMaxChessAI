there are a couple requirements to run the code from this project 
1. First you must have rust installed on your computer
2. You must have python installed on your computer
3. You must create a virtual environment in the project directory and install the requirements from the .txt file
    a. "python3 -m venv venv" to create
    b. "source venv/bin/activate" to activate
    c. "pip install -r requirements.txt"
4. You must go into the root directory for the library that we used and then install the library 
    a. "cd Library/gym-chess"
    b. you must type "pip install -e ."
5. You can then do into the root directory for the project and run the program
    a. "python3 main.py"

There is two branches for this project the main branch which is the implementation that allowes you to play against the AI and the
statAnalysis branch which runs the AI against a bot that chooses random moves a certain number of times and then prints out the 
results of the games