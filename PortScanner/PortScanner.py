import socket
import sys
import time
import datetime

def scan_host(host, port, r_code=1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        code = s.connect_ex((host, port))
        if code == 0:
            r_code = code
        s.close()
    except Exception, e:
        pass
    return r_code
	
def main():
	host = ''
	min_port = int(raw_input('Min port: '))
	max_port = int(raw_input('Max port: '))
	try:
		host = raw_input("[*] Enter Target Host Address: ")
	except KeyboardInterrupt:
		print "[*] User Requested An Interrupt."
		print "[*] Application Shutting Down"
		sys.exit(1)
	hostip = socket.gethostbyname(host)
	print "\n[*] Host = " + host
	print "\n[*] IP = " + hostip
	print "\n[*] Scanning Started At " + time.strftime("%H:%M:%S")
	start_time = datetime.datetime.now()
	for port in range(min_port, max_port, 1):
		try:
			response = scan_host(host, port)
			if response == 0:
				print "[*] Port " + port + ": Open"
		except Exception, e:
			pass
	stop_time = datetime.datetime.now()
	duration = stop_time - start_time
	print "\n[*] Scanning Finished At" + time.strftime("%H:%M:%S") + " ..."
	print "[*] Scanning Duration: " + duration + " ..."
