import scapy.all as scapy

arp_request_packet=scapy.ARP(pdst="10.0.2.1/24")
broadcast_packet=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
combined_packet=broadcast_packet/arp_request_packet
(answered_list,unanswered_list)=scapy.srp(combined_packet,timeout=1)
answered_list.summary();

