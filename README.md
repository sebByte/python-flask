## Boilerplate for Python Flask project, deployable to Heroku

- Intended for use on VSCode Docker devcontainer

### Setup
- Make sure you have Docker and the Visual Studio Code extension _Remote - Containers_ (id: ms-vscode-remote.remote-containers) installed locally.
- Clone this repo.
- Open folder in Visual Studio Code, it should suggest to open in container. If not, choose _Remote-Containers: Reopen Folder in Container_ from the Command Palette.
- Install dependencies with `pip install -r requirements.txt`
- Try running the app with `flask run` in the VSCode terminal, it shoult open in your browser (VSCode will tell you the URL)

## Deplyment to Heroku
- The files _Procfile_, _wsgi.py_ and _runtime.txt_ contain all info heroku needs to run the app.
- Create the heroku app with `heroku create` in the VSCode terminal.
- Try running the app locally  with `heroku local` (basically the same as `flask run`, but now we want to make sure heroku can start the app as well.)
- Deploy with `git push heroku main` (or `master` if that's the name of your main branch)
- Wait for the deploy script to run, then visit the deployed app in your browser!