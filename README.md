Amazon functional E2E automation project using POM, Python, Selenium and Webdriver Manager
- What tools / frameworks would you use for AT?
```
POM
Selenium
Python
Webdriver_manager
Faker
```
- What would be used for each tool?
```
POM - Used to organize the code and make it cleaner and adding small blocks of code helping in the maintenance and reusability of the code.
Selenium - Free open-source testing framework that has a huge community around the entire world. It supports multiple programming langagues, it supports differents browsers, (...)
Webdriver_manager - Library that provides the way to automatically manage drivers for different browsers. This way we don't need to manually add/update drivers binaries.
Faker - Library to generate random info like name, address, email, phone number, (...)
```
- What parts of the app you would apply AT to?
```
To decide what should be automated or not I follow these steps:
 - Complexity
 - Frequency the user runs that particular scenario
 - Time to run it manually vs implementing the automation
 - Subjectiveness 
 - (...)
```

### Install requirements
- for Mac/Linux
```
pip3 install -r requirements.txt
```
- for Windows
```
pip install -r requirements.txt
```


### Install Virtual Env
- for Mac/Linux
```
pip3 install virtualenv
```
- for Windows
```
pip install virtualenv
```


### Create Virtual Env
- for Mac/Linux
```
python3 -m venv venv
```
- for Windows
```
virtualenv venv
```


### Activate Virtual Env
- for Mac/Linux
```
source venv/bin/activate
```
- for Windows
```
source venv/Scripts/activate
```


### Run tests
- for Mac/Linux
```
python3 -m pytest -v tests/...py
```
- for Windows
```
pytest -v tests/...py
```