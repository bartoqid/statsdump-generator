from get_tsf import get_tsf
from get_status import get_status
from download_stats import download_stats
from get_api_key import get_key
import getpass
import time

#Enter username
firewall_admin = input("Please Enter firewall username: ")

#Enter password for firewall
firewall_password = getpass.getpass("Please enter firewall password: ")

def generate_tsf(firewall_ip):

    global firewall_admin
    global firewall_password

    firewall_ip = firewall_ip.rstrip('\n')

    api_key = get_key(firewall_ip, firewall_admin, firewall_password)
    job_id = get_tsf(firewall_ip, api_key)
    status_progress = (get_status(firewall_ip, api_key, job_id))

    while status_progress[0] != "FIN":
        time.sleep(5)
        print("Waiting for device: " + firewall_ip + " TSF to be generated")
        print("Job ID: " + job_id + " Status: " + status_progress[0] + " Progress : " + status_progress[1] + "%\n")
        status_progress = (get_status(firewall_ip, api_key, job_id))
    else:
        size = download_stats(firewall_ip, api_key, job_id)
        print("Successfully transferred " + str(size) + " Bytes\n")