"# iouapp"

Environment Setup
1. Download and install latest version of python:
    - https://www.python.org/downloads/
2. Install pip (package installer for python):
    - https://pip.pypa.io/en/stable/getting-started/
3. Install flask web server package:
    - https://pypi.org/project/Flask/
4. Download and install Mysql db server:
    - https://dev.mysql.com/downloads/installer/
5. Download and install GIT client:
    - https://git-scm.com/downloads

Setup Code
1. Create account on Github
2. Code repository:
    - https://github.com/pangaea/iouapp
3. Create working directory and run clone command from it:
    - git clone https://github.com/pangaea/iouapp.git
4. Add SSH cert to git (only needed for submitting)
    - https://docs.github.com/en/authentication/connecting-to-github-with-ssh

Initial setup
1. Open mySQL Workbench query console
2. Copy entire contents of database/init.sql and paste into console
3. Execute to create all database entities
4. Copy config-sample.json to config.json
5. Update settings to match your local development env.
6. From the project root directory run:
    - python app.py
7. Open browser and navigate to:
    - http://localhost:5000/

Database migrations
- add_notes_field_to_iou.sql : Adds 'notes' field to iou table.
    
Troubleshooting
- On Windows, if Git isn't using the SSH key, make sure OpenSSH is installed and Git know about it (update path as needed):
    - git config --global core.sshCommand C:/Windows/System32/OpenSSH/ssh.exe
