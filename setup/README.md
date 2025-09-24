<h1>
  <span class="headline">Setup</span>
  <span class="subhead"></span>
</h1>

## Setup

Open your Terminal application and navigate to the **`./buggy-flask-app-starter`** directory:

```bash
cd ./buggy-flask-app-starter
```

Install dependencies:

```bash
pipenv install -r requirements.txt
```

Activate the virtual environment:

```bash
pipenv shell
```

Run the application:
   
```bash
python app.py
```

  or 

```bash
pipenv run python app.py
```

In your browser, send a request to `localhost:5000` to hit the `index` route.

Open the contents of the directory in VSCode:

```bash
code .
```

To deactivate the virtual environment when you're done, simply type:

```bash
exit
```