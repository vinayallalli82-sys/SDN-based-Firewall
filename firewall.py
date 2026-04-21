from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()


blocked_pairs = [
    ("10.0.0.1", "10.0.0.2"),
]

def _handle_PacketIn(event):
    packet = event.parsed
    ip = packet.find('ipv4')

    
    if not ip:
        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        event.connection.send(msg)
        return

    src = str(ip.srcip)
    dst = str(ip.dstip)

    log.info(f"Packet: {src} -> {dst}")

   
    if (src, dst) in blocked_pairs:
        log.info("BLOCKED")
        return

  
    msg = of.ofp_flow_mod()
    msg.match = of.ofp_match.from_packet(packet)
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

    log.info("ALLOWED → flow installed")


def launch():
    log.info("Firewall module loaded")
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
