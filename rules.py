from datetime import datetime
def detect_bruteforce(failed_login):
    alert_file = open("alerts/alert.txt","a")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for ip,count in failed_login .items():
        if count >= 3:
            alert_file.write(f"{current_time} [CRITICAL] Possible Brute Force Attack from {ip} ({count} failed logins)\n")
    alert_file.close()

def detect_port_scan(port_scan):
    alert_file = open("alerts/alert.txt","a")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for ip,count in port_scan.items():
        if count>=2:
            alert_file.write(f"{current_time}[WARNING] Possible Port Scan from {ip} ({count} port scan events)\n")
    alert_file.close()