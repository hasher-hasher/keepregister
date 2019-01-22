### Install Virtualenv
Virtualenv is the best way to isolate your python environment from the python which is used for the system to run. **It is highly recomended to use virtualenv**
#### Install with pip
```bash
$ sudo pip install virtualenv
```
#### Install with apt-get (Debian based)
```bash
$ sudo apt-get install python3-virtualenv
```
#### Create the virtualenv
```bash
$ mkdir myproject
$ cd myproject
$ virtualenv venv
New python executable in venv/bin/python
Installing setuptools, pip............done.
```

#### Activate virtualenv
```bash
$ . venv/bin/activate
```

### Install locally
On the project folder and with virtualenv running, run ``` pip install --editable . ``` to install locally the app. Now whenever the virtualenv is running the keepregister app will be available

### Run Locally
``` $ keepregister file.txt "Today i realised that i like unicorns" ```
