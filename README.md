## Install Virtual Env
> pip install virtualenv # for Windows
> pip3 install virtualenv # for Mac/Linux

## Create Virtual Env
> virtualenv venv
>
or
> python -m venv venv
>>

## MacOs or Linux
> source venv/bin/activate
>>
or
>
## Windows
> source venv/Scripts/activate

## Run tests
> python3 -m pytest -v tests/test_google_search.py # Mac/Linux
> pytest -v tests/test_google_search.py # Windows