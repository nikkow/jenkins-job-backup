# Jenkins Job Backup
Quick tool to back up the jobs configured on a Jenkins instance.

## How to use?

First, you need to make sure that Python version 2.7.0+ is installed on your machine. To proceed, run the simple command:

	python --version
	
If something comes out, good. Python is installed. If you get an error message saying that `python` is not found, please install it first.

Then, open the script `jenkins-backup.py` using your favorite editor and edit the configuration section. 

| Variable | Meaning | Example |
|---|---|---|
| `JENKINS_URL` | The root URL of your Jenkins instance (no port, no path). Please make sure that the URL is accessible from the maching you intend to run the script from. | e.g. `https://ci.mycompany.com`|
| `JENKINS_PORT` | This variable speaks for itself. Indicates the port Jenkins runs on. | e.g. `8080`|
| `OUTPUT_DIR` | The destination path of the backups without trailing slash. It can either be a absolute path, or a path relative to the script execution directory. If the path does not exists, the script will try to create it. | e.g. `/home/nikkow/backups/jenkins`|

Now you're ready to go! Open your favorite terminal, `cd` to the directory containing `jenkins-backup.py` and run:

	python jenkins-backup.py
	
That's it. 

## Note

As always, this script is provided **as is** ... I'm not responsible for anything you or this script might do to your files, backups, etc... 