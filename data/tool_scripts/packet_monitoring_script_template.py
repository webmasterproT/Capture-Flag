import json
import socket
import struct
from scapy.all import sniff, IP, TCP, UDP

# Load shared dependencies and configurations
with open('data/config_defaults.json') as config_defaults_file:
    CONFIG_DEFAULTS = json.load(config_defaults_file)
with open('data/packet_monitoring_filters.json') as filters_file:
    PACKET_MONITORING_FILTERS = json.load(filters_file)
with open('data/user_activity_logs.json') as logs_file:
    USER_ACTIVITY_LOGS = json.load(logs_file)

API_KEY = CONFIG_DEFAULTS['API_KEY']

# Define the packet processing function
def process_packet(packet):
    # Extract packet details
    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    src_port = packet[TCP].sport if TCP in packet else None
    dst_port = packet[TCP].dport if TCP in packet else None
    protocol = packet.sprintf("%IP.proto%")

    # Log the packet details
    log_entry = {
        'src_ip': src_ip,
        'dst_ip': dst_ip,
        'src_port': src_port,
        'dst_port': dst_port,
        'protocol': protocol
    }
    USER_ACTIVITY_LOGS.append(log_entry)

    # Check for any monitoring filters
    for filter_rule in PACKET_MONITORING_FILTERS:
        if all(filter_rule[key] == log_entry[key] for key in filter_rule):
            # Trigger an alert or take action based on the filter rule
            handle_alert(filter_rule, log_entry)

# Define the alert handling function
def handle_alert(filter_rule, log_entry):
    # Placeholder for handling alerts based on filter matches
    print(f"Alert triggered by rule {filter_rule['name']}: {log_entry}")

# Define the packet sniffing function
def start_packet_sniffing(interface=None, filter=None):
    # Start sniffing packets on the given interface with the provided filter
    sniff(iface=interface, filter=filter, prn=process_packet, store=0)

# Save logs to file
def save_logs():
    with open('data/user_activity_logs.json', 'w') as logs_file:
        json.dump(USER_ACTIVITY_LOGS, logs_file, indent=4)

# Main function to start the packet monitoring script
if __name__ == "__main__":
    try:
        # Start packet sniffing on the default interface with no filter
        start_packet_sniffing()
    except KeyboardInterrupt:
        # Save logs when the script is stopped
        save_logs()
        print("Packet monitoring stopped. Logs have been saved.")