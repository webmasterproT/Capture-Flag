```python
import json
import socket
from scapy.all import sniff
from utils.constants import PACKET_MONITORING_FILTERS
from utils.helpers import log_activity, load_json_data
from ai_integration import analyze_packet_for_threats

def packet_callback(packet):
    """
    Callback function that gets called every time a packet is sniffed.
    """
    try:
        # Convert packet to a more readable format if necessary
        packet_info = {
            'source': packet.sprintf('%IP.src%'),
            'destination': packet.sprintf('%IP.dst%'),
            'protocol': packet.sprintf('%IP.proto%')
        }
        
        # Log packet information
        log_activity('Packet received: {}'.format(json.dumps(packet_info)))
        
        # Analyze packet for potential threats
        threat_info = analyze_packet_for_threats(packet)
        if threat_info:
            log_activity('Threat detected: {}'.format(json.dumps(threat_info)))
        
        # Here you can add more logic based on the packet analysis
        # For example, you can trigger alerts, block traffic, etc.
        
    except Exception as e:
        log_activity('Error processing packet: {}'.format(str(e)))

def start_packet_monitoring():
    """
    Start monitoring network packets based on the filters defined in PACKET_MONITORING_FILTERS.
    """
    filters = load_json_data(PACKET_MONITORING_FILTERS)
    sniff_filter = filters.get('sniff_filter', '')
    
    try:
        log_activity('Starting packet monitoring with filter: {}'.format(sniff_filter))
        sniff(filter=sniff_filter, prn=packet_callback, store=0)
    except Exception as e:
        log_activity('Error starting packet monitoring: {}'.format(str(e)))

if __name__ == "__main__":
    start_packet_monitoring()
```