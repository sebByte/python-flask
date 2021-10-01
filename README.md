## Boilerplate for Python Flask project, deployable to Heroku

- Intended for use on VSCode Docker devcontainer

### Setup
- Make sure you have Docker and the Visual Studio Code extension _Remote - Containers_ (id: ms-vscode-remote.remote-containers) installed locally
- Clone this repo
- Open folder in Visual Studio Code, it should suggest to open in container. If not, choose _Remote-Containers: Reopen Folder in Container_ from the Command Palette
- Install dependencies with `pip install -r requirements.txt`
- Try running the app with `flask run`, it shoult open in your browser (VSCode will tell you the URL)

## Deplyment to Heroku
- The `Procfile`, `wsgi.py` and `runtime.txt` are user by heroku to run the app.
- Try running the app locally using these file with `heroku local` (it should work just as well as `flask run`)
- 