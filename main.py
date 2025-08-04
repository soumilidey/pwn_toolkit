#importing modules
import argparse
from modules.recon import cutie
from modules.portscanner import potato
from modules.webscanner import tomato
from modules.bruteforce import onion

def banner():
    print(r"""
 _________ __ _________     _______________________  _________________
7     7  V  V  7     7     7      7     7     7  7  7  7  7  7      7
|  -  |  |  |  |  _  |     !__  __|  7  |  7  |  |  |   __|  !__  __!
|  ___|  !  !  |  7  |       7  7 |  |  |  |  |  !__|     |  | 7  7  
|  7  |        |  |  |       |  | |  !  |  !  |     |  7  |  | |  |  
!__!  !________!__!__!       !__! !_____!_____!_____!__!__!__! !__!  
                                                                     
_____________     __________________________________  ____           
7  _  7  7  7     7     7     7  7  7        7  7  7  7  7           
|   __|  !  |     |  ___|  7  |  |  |  _  _  |  |  |  |  |           
|  _  !_   _!     !__   |  |  |  |  |  7  7  |  |  !__|  |           
|  7  |7   7      7     |  !  |  !  |  |  |  |  |     |  |           
!_____!!___!      !_____!_____!_____!__!__!__!__!_____!__!           
Red Team Toolkit | by Soumili
    """)

def main():
    banner()
    parser = argparse.ArgumentParser(description="Pwn Toolkit: Red Team Toolkit")
    
    subparsers = parser.add_subparsers(dest="command", help="Available modules")

    # Recon Module
    cutie = subparsers.add_parser("recon", help="Perform reconnaissance")
    cutie.add_argument("-t", "--target", required=True, help="Target domain/IP")

    # Port Scan Module
    potato = subparsers.add_parser("portscan", help="Scan for open ports")
    potato.add_argument("-t", "--target", required=True, help="Target IP/hostname")

    # Web Vulnerability Module
    tomato = subparsers.add_parser("webvulnerability", help="Check for web vulnerabilities")
    tomato.add_argument("-u", "--url", required=True, help="Target URL")

    # Password Attack Module
    onion = subparsers.add_parser("password", help="Brute-force password attack")
    onion.add_argument("-l", "--login", required=True, help="Login URL or SSH IP")
    onion.add_argument("-u", "--user", required=True, help="Username")
    onion.add_argument("-w", "--wordlist", required=True, help="Path to word list")


    args = parser.parse_args()

    if args.command == "recon":
        cutie(args.target)
    elif args.command == "portscan":
        potato(args.target)
    elif args.command == "webvulnerabilities":
        tomato(args.url)
    elif args.command == "password":
        onion(args.login, args.user, args.wordlist)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

