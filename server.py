import socket
from binascii import hexlify

def print_server_machine_info():
    host_name = socket.gethostname()
    ip_address_server = socket.gethostbyname(host_name)
    packed_ip_address_server = socket.inet_aton(ip_address_server)
    print ("Server:")
    print ("    Host name: %s" %host_name)
    print ("    IP address (Dez): %s" %ip_address_server)
    print ("    IP address (Hex): %s" %(hexlify(packed_ip_address_server)))
    print ("")

def get_client_machine_info():
    eingabe_port = input("Geben Sie ihren Port ein")
    if eingabe_port != int:
        eingabe_port = input("Geben Sie ihren Port ein")
    remote_host = 'www.amazon.de'                                                          #client-programm#
    ip_address_client = socket.gethostbyname(remote_host)
    packed_ip_address_client = socket.inet_aton(ip_address_client)
    try:
        print ("Client:")
        print ("    Trying to connect to: %s" %(remote_host))
        print ("    IP address of %s (Dez): %s" %(remote_host, ip_address_client))
        print ("    IP address of %s (Hex): %s" %(remote_host, hexlify(packed_ip_address_client)))
    except socket.error as err_msg:
        print ("%s: %s" %(remote_host, err_msg))
if __name__ == '__main__':
    print_server_machine_info()

    get_client_machine_info()
