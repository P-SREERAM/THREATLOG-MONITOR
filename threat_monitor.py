import rules 
def count_failed_logins():
    failed_login = {}
    file = open("logs/sample.log","r")
    for line in file:
        line = line.strip()
        if "FAILED_LOGIN" in line:
            parts = line.split()
            ip = parts[-1]
            if ip in failed_login:
                failed_login[ip] += 1
            else:
                failed_login[ip] = 1
    file.close()
    return failed_login

def count_port_scan():
    port_scan = {}
    file = open("logs/sample.log","r")
    for line in file:
        line = line.strip()
        if "PORT_SCAN" in line:
            part = line.split()
            ip = part[-1]
            if ip in port_scan:
                port_scan[ip] += 1
            else:
                port_scan[ip] = 1
    file.close()
    return port_scan

port_scan = count_port_scan()
failed_logins = count_failed_logins()
rules.detect_bruteforce(failed_logins)
rules.detect_port_scan(port_scan)

