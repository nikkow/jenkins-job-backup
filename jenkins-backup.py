#!/usr/bin/python
#
# Jenkins Backup Tools
# --------------------
# Command line tool to perform a backup of all the jobs
# configured on a Jenkins instance.
# This was tested with 2.7.10.
# See https://github.com/nikkow/jenkins-job-backup
#
import urllib2
import json
import os

# Configuration
# -------------
# Configure the variables below to match your jenkins
# installtion. Please make sure that this script will
# be able to access your instance (rights, network...).
JENKINS_URL = "https://your.jenkins.instance"
JENKINS_PORT = "8080"
OUTPUT_DIR = "Backup-Jenkins"

# ----- DO NOT EDIT BELOW ----- #
def loadJobs():
    # Loading the configuration straigt from the instance.
    JENKINS_BUILT_API_URL = "%s:%s/api/json" % (JENKINS_URL, JENKINS_PORT)
    print("Grabbing Jenkins Config from %s" % JENKINS_BUILT_API_URL)
    print("")
    instance_cfg = urllib2.urlopen(JENKINS_BUILT_API_URL).read()
    instance_cfg = json.loads(instance_cfg)

    # Extracting jobs from loaded response.
    print("%d job(s) found." % len(instance_cfg['jobs']))
    print("")
    return instance_cfg['jobs']

if __name__ == '__main__':
    jobs = loadJobs()

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for idx, job in enumerate(jobs):
        print("Backing-up job %d/%d: %s" % ((idx + 1), len(jobs), job['name']))
        job_cfg = urllib2.urlopen("%s/config.xml" % job['url']).read()
        save_path = "%s/%s-config.xml" % (OUTPUT_DIR, job['name'])
        f = open(save_path, "w")
        f.write(job_cfg)
        f.close()
        print("Saved to %s" % save_path)
        print("")

    print("All jobs are backed up!")
    print("Exiting.")
    print("")
