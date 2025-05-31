import argparse
from core import anonymity, firewall, port_monitor, scan_defense, bypass
from utils import logger

def main():
    parser = argparse.ArgumentParser(description="Predator - Advanced Privacy & Security Tool")

    parser.add_argument('--anon', action='store_true', help='Activate anonymity features (Tor, MAC, DNS)')
    parser.add_argument('--firewall', action='store_true', help='Manage firewall rules')
    parser.add_argument('--port-monitor', action='store_true', help='Monitor open ports and strange connections')
    parser.add_argument('--scan-defense', action='store_true', help='Activate scan defense (Nmap, masscan detection)')
    parser.add_argument('--bypass', action='store_true', help='Enable censorship bypass tools')

    args = parser.parse_args()

    logger.log("Predator started")

    if args.anon:
        logger.log("Activating anonymity features...")
        anonymity.run()

    if args.firewall:
        logger.log("Managing firewall...")
        firewall.run()

    if args.port_monitor:
        logger.log("Starting port monitor...")
        port_monitor.run()

    if args.scan_defense:
        logger.log("Activating scan defense...")
        scan_defense.run()

    if args.bypass:
        logger.log("Enabling bypass tools...")
        bypass.run()

    if not any(vars(args).values()):
        parser.print_help()

if __name__ == '__main__':
    main()
