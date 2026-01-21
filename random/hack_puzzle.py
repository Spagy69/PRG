import time
import random
import sys
import os

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'
    WHITE = '\033[97m'

class Effects:
    @staticmethod
    def type_writer(text, speed=0.03, color=Colors.GREEN):
        sys.stdout.write(color)
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        sys.stdout.write(Colors.END + "\n")

    @staticmethod
    def loading_bar(description="Processing", duration=3):
        print(f"{Colors.YELLOW}{description}{Colors.END}")
        width = 40
        for i in range(width + 1):
            percent = int((i / width) * 100)
            bar = "█" * i + "-" * (width - i)
            sys.stdout.write(f"\r[{bar}] {percent}%")
            sys.stdout.flush()
            time.sleep(duration / width)
        print()
    

    @staticmethod
    def hack_animation(text="HACKING"):
        chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
        final_text = str(text)
        current_text = [""] * len(final_text)
        
        for i in range(len(final_text)):
            for _ in range(5):
                temp_text = "".join(current_text[:i]) + random.choice(chars)
                sys.stdout.write(f"\r{Colors.RED}{temp_text}{Colors.END}")
                sys.stdout.flush()
                time.sleep(0.05)
            current_text[i] = final_text[i]
            
        sys.stdout.write(f"\r{Colors.RED}{final_text}{Colors.END}\n")

    @staticmethod
    def generate_random_mac():
        return ":".join(["{:02x}".format(random.randint(0, 255)) for _ in range(6)]).upper()


class GameState:
    def __init__(self):
        self.connected_ssid = None
        self.location = "~"
        self.inventory = {}  # cracked passwords
        self.files = {
            "~": [],
            "~/downloads": []
        }
        self.available_ssids = [
            {"SSID": "SkolaVDF_Zamestnanci", "security": "WPA2", "signal": "90%", "cracked": False, "password": None},
            {"SSID": "Kozak_Hotspot", "security": "WPA2", "signal": "45%", "cracked": False, "password": "ty_jses_karel_zejo"},
            {"SSID": "Guest_WiFi", "security": "OPEN", "signal": "100%", "cracked": True, "password": ""}
        ]
        self.network_devices = {
            "Kozak_Hotspot": [
                {"ip": "192.168.1.1", "alias": "Router_Gateway"},
                {"ip": "192.168.1.67", "alias": "Kozak_Laptop"},
                {"ip": "192.168.1.69", "alias": "Kozak_Vibrator"}
            ]
        }
        self.target_defeated = False

    def get_prompt(self):
        host = "hacker@kali"
        path = self.location
        if self.connected_ssid:
            return f"{Colors.GREEN}{host}{Colors.END}:{Colors.BLUE}{path}{Colors.END} ({Colors.YELLOW}{self.connected_ssid}{Colors.END})$ "
        return f"{Colors.GREEN}{host}{Colors.END}:{Colors.BLUE}{path}{Colors.END}$ "

class Game:
    def __init__(self):
        self.state = GameState()
        self.running = True

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_help(self):
        print(f"\n{Colors.BOLD}Available Commands:{Colors.END}")
        print(f"  {Colors.CYAN}nmcli dev wifi list{Colors.END}            - List available WiFi networks")
        print(f"  {Colors.CYAN}bruteforce <SSID>{Colors.END}              - Attempt to crack a WiFi password")
        print(f"  {Colors.CYAN}nmcli dev wifi connect <SSID> password <PWD>{Colors.END} - Connect to a network")
        print(f"  {Colors.CYAN}ls{Colors.END}                               - List files in current directory")
        print(f"  {Colors.CYAN}cd <dir>{Colors.END}                         - Change directory")
        print(f"  {Colors.CYAN}cat <file>{Colors.END}                       - Read file content")
        print(f"  {Colors.CYAN}scan{Colors.END}                             - Scan network for devices (requires connection)")
        print(f"  {Colors.CYAN}ddos <IP>{Colors.END}                        - Launch DDoS attack on target IP")
        print(f"  {Colors.CYAN}exit{Colors.END}                             - Exit game")
        print(f"  {Colors.CYAN}help{Colors.END}                             - Show this help message\n")

    def run(self):
        self.clear()
        Effects.type_writer("Initializing Kali Linux...", 0.05)
        Effects.loading_bar("Loading Modules")
        print(f"{Colors.GREEN}System Ready.{Colors.END}\n")
        self.print_help()
        print(f"{Colors.RED}Your only goal is to hack Kozák! Good luck!{Colors.END}")
        print(f"{Colors.RED}WARNING! This is only a simulation, no real hacking will be done :D{Colors.END}")

        while self.running:
            try:
                command_str = input(self.state.get_prompt()).strip()
                if not command_str:
                    continue
                self.process_command(command_str)
            except KeyboardInterrupt:
                print("\nExiting...")
                self.running = False


    def process_command(self, command_str):
        parts = command_str.split()
        cmd = parts[0].lower()

        if cmd == "help":
            self.print_help()

        elif cmd == "exit":
            self.running = False

        elif cmd == "ls":
            current_files = self.state.files.get(self.state.location, [])
            if not current_files:
                print("total 0")
            else:
                for f in current_files:
                    print(f"{f}")

        elif cmd == "cd":
            if len(parts) < 2:
                self.state.location = "~"
                return
            
            target = parts[1]
            if target == "..":
                if self.state.location != "~":
                    self.state.location = "~"
            elif target == "downloads":
                if self.state.location == "~":
                    self.state.location = "~/downloads"
                else:
                    print(f"bash: cd: {target}: No such file or directory")
            elif target == "~":
                 self.state.location = "~"
            else:
                 print(f"bash: cd: {target}: No such file or directory")

        elif cmd == "cat":
            if len(parts) < 2:
                print("Usage: cat <filename>")
                return
            filename = parts[1]
            files_in_dir = self.state.files.get(self.state.location, [])
            if filename in files_in_dir:
                if filename.endswith(".txt"):
                    for ssid_data in self.state.available_ssids:
                        if f"password_{ssid_data['SSID']}.txt" == filename:
                             print(f"\nPassword for {ssid_data['SSID']}: {ssid_data['password']}\n")
                             return
                print(f"Contents of {filename}...")
            else:
                print(f"cat: {filename}: No such file or directory")

        elif cmd == "nmcli":

            if len(parts) >= 4 and parts[1] == "dev" and parts[2] == "wifi" and parts[3] == "list":
                print(f"{Colors.BOLD}SSID             MODE   CHAN  RATE       SIGNAL  BARS  SECURITY{Colors.END}")
                print("---------------------------------------------------------------")
                for net in self.state.available_ssids:
                   bars = "▂▄▆█" if net['signal'] == "100%" else "▂▄▆_"
                   print(f"{net['SSID']:<16} Infra  11    54 Mbit/s  {net['signal']:<7} {bars}  {net['security']}")
                print()
            
            elif len(parts) >= 6 and parts[1] == "dev" and parts[2] == "wifi" and parts[3] == "connect":
                try:
                    ssid_index = 4
                    ssid = parts[ssid_index]
                    
                    if "password" in parts:
                        pwd_index = parts.index("password") + 1
                        if pwd_index < len(parts):
                            password = parts[pwd_index]
                        else:
                             print("Error: Missing password argument.")
                             return
                    else:
                        print("Error: Usage: nmcli dev wifi connect <SSID> password <PASSWORD>")
                        return

                    ssid = ssid.strip('"').strip("'")
                    password = password.strip('"').strip("'")

                    target_net = next((n for n in self.state.available_ssids if n['SSID'] == ssid), None)
                    if target_net:
                        if target_net['password'] == password:
                            Effects.loading_bar("Connecting", 2)
                            print(f"{Colors.GREEN}Successfully connected to {ssid}.{Colors.END}")
                            self.state.connected_ssid = ssid
                        else:
                            print(f"{Colors.RED}Error: Connection activation failed: 802.1X supplicant failed{Colors.END}")
                    else:
                        print(f"Error: SSID '{ssid}' not found.")

                except ValueError:
                     print("Error: Usage logic error.")

            else:
                print("Usage: nmcli dev wifi [list|connect]")

        elif cmd == "bruteforce":
            if len(parts) < 2:
                print("Usage: bruteforce <SSID>")
                return
            
            target_ssid = parts[1]
            target_net = next((n for n in self.state.available_ssids if n['SSID'] == target_ssid), None)
            
            if target_net:
                if target_net['security'] == "OPEN":
                    print("Network is OPEN. No password needed.")
                    return

                print(f"{Colors.YELLOW}Initializing Bruteforce attack on {target_ssid}...{Colors.END}")
                time.sleep(5)
                Effects.hack_animation(f"CRACKING HASH {target_ssid}...")
                Effects.loading_bar("Testing dictionary keys", 4)
                
                print(f"{Colors.GREEN}SUCCESS! Password found.{Colors.END}")
                print("Saving to file...")
                
                filename = f"password_{target_ssid}.txt"
                if filename not in self.state.files["~/downloads"]:
                     self.state.files["~/downloads"].append(filename)
                
                print(f"{Colors.CYAN}Password saved to ~/downloads/{filename}{Colors.END}")
                
            else:
                 print(f"Error: SSID '{target_ssid}' not found.")

        elif cmd == "scan":
            if not self.state.connected_ssid:
                print(f"{Colors.RED}Error: You are not connected to any network.{Colors.END}")
                return
            
            print(f"Scanning network {self.state.connected_ssid}...")
            Effects.loading_bar("Scanning Subnet 192.168.1.0/24", 3)
            
            devices = self.state.network_devices.get(self.state.connected_ssid, [])
            if devices:
                print(f"\n{Colors.BOLD}IP ADDRESS       MAC ADDRESS         ALIAS{Colors.END}")
                print("--------------------------------------------------------")
                for dev in devices:
                    print(f"{dev['ip']:<16} {Effects.generate_random_mac()}   {dev['alias']}")
                print()
            else:
                print("No devices found.")

        elif cmd == "ddos":
            if len(parts) < 2:
                print("Usage: ddos <IP>")
                return
            
            target_ip = parts[1]
            
            valid_target = False
            devices = self.state.network_devices.get(self.state.connected_ssid, [])
            for dev in devices:
                if dev['ip'] == target_ip and dev['alias'] == "Kozak_Laptop":
                    valid_target = True
                    break
            
            if valid_target:
                print(f"{Colors.RED}INITIATING DDoS ATTACK ON {target_ip} (Kozak_Laptop)...{Colors.END}")
                time.sleep(1)
                print("Allocating botnet...")
                time.sleep(1)
                print("Bots connected: 69,420")
                Effects.loading_bar("FLOODING PACKETS", 5)
                
                # DDoS Visuals
                for _ in range(15):
                    print(f"{Colors.RED}SENDING PACKET -> {target_ip} [SIZE=65535] [TTL=128]{Colors.END}")
                    time.sleep(0.1)
                
                print(f"\n{Colors.GREEN}TARGET DOWN! CONNECTION TIMEOUT.{Colors.END}")
                time.sleep(1)
                self.show_victory()
                self.running = False
            else:
                 print(f"Pinging {target_ip}...")
                 time.sleep(2)
                 print(f"{target_ip} is active but DDoS had no visible effect (Wrong target?).")

        elif cmd == "goat": # ístr eg xdddd
            self.show_victory()
            print("Takhle jsi to neměl udělat :D ale řešení je řešení že xd")

        else:
            print(f"Command '{cmd}' not found. Type 'help' for a list of commands.")

    def show_victory(self):
        print(f"\n{Colors.YELLOW}{Colors.BOLD}MISSION ACCOMPLISHED! KOZÁK HAS BEEN DEFEATED.{Colors.END}\n")
        goat_art = r"""
        
                      ___.
                     //  \\
                    ((   ''
                     \\__,
                    /6 (%)\,
                   (__/:";,;\--____----_
                    ;; :';,:';`;,';,;';`,`_
                      ;:,;;';';,;':,';';,-Y\
                       ;,;,;';';,;':;';'; Z/
                       / ;,';';,;';,;';;'
                      / / |';/~~~~~\';;'
                     ( K  | |      || |
                      \_\ | |      || |
                       \Z | |      || |
                          L_|      LL_|
                          LW/      LLW/
        
        KOZÁK IS WATCHING YOU. >:)
        """
        print(f"{Colors.RED}{goat_art}{Colors.END}")
        print(f"{Colors.RED}I hope you enjoyed this puzzle game! :D{Colors.END}")
        input("Press Enter to finish...")

if __name__ == "__main__":
    game = Game()
    game.run()
