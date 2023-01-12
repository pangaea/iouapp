"# iouapp"

Environment Setup
- Download and install latest version of python:
    https://www.python.org/downloads/
- Install pip (package installer for python):
    https://pip.pypa.io/en/stable/getting-started/
- Install flask web server package:
    https://pypi.org/project/Flask/
- Download and install Mysql db server:
    https://dev.mysql.com/downloads/installer/
- Download and install GIT client:
    https://git-scm.com/downloads

Setup Code
- Create account on Github
- Code repository:
    https://github.com/pangaea/iouapp
- Create working directory and run clone command from it:
    git clone https://github.com/pangaea/iouapp.git
- Add SSH cert to git (only needed for submitting)
    https://docs.github.com/en/authentication/connecting-to-github-with-ssh

Initial setup
- Open mySQL Workbench query console
- Copy entire contents of init.sql and paste into console
- Execute to create all database entities
- Copy config-sample.json to config.json
- Update settings to match your local development env.
- From the project root directory run:
    python app.py
- Open browser and navigate to:
    http://localhost:5000/
    
Troubleshooting
- On Windows, if Git isn't using the SSH key, make sure OpenSSH is installed and Git know about it (update path as needed):
    git config --global core.sshCommand C:/Windows/System32/OpenSSH/ssh.exe
