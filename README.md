## Running this project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
python -m venv venv
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source venv/bin/activate
```
for windows:
```
.\venv\scripts\activate
```

Then install the project dependencies with

```
pip install -r requirements.txt
```

Now you can run the project with this command

```
python manage.py runserver
```

**Note** Feel free to customize this Repo according to your project's specific details and structure. Providing clear and comprehensive information will help users and contributors engage with your project more effectively.
