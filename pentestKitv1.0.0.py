#! /usr/bin/env python3
import socket
import os

def banner():

	print("█   █ █   █ ███  ███  █   █ █████     ████ █████  ███     ████  █████ █   █ █████ █████  ████ █████    █   █ ███ █████   ")
	print("█░ █ ░██  █░ █░░█ ░░░ █░  █░ ░█░░░   █ ░░░░█░░░░░█ ░░░    █░░░█ █░░░░░██  █░ ░█░░░█░░░░░█ ░░░░ ░█░░░   █░ █ ░ █░░ ░█░░░  ")
	print("███ ░ █░█ █░░█░░█░ ██░█████░░ █░░░░   ███░░████░░█░ ░░░   ████░░████░░█░█ █░░ █░░░████░░░███░░░ █░░░░  ███ ░ ░█░░░ █░░░░ ")
	print("█░░█ ░█░░██░░█░░█░░ █░█░░░█░░ █░░      ░░█ █░░░░ █░░      █░░░░ █░░░░ █░░██░░ █░░ █░░░░   ░░█   █░░    █░░█ ░ █░░  █░░   ")
	print("█░░░█ █░░ █░███░ ███ ░█░░░█░░ █░░    ████░░█████░ ███     █░░░░░█████░█░░ █░░ █░░ █████░████░░  █░░    █░░░█ ███░  █░░   ")
	print(" ░░  ░ ░░  ░░░░░  ░░░ ░░░  ░░  ░░     ░░░░ ░░░░░░  ░░░     ░░    ░░░░░ ░░  ░░  ░░  ░░░░░ ░░░░ ░  ░░     ░░  ░ ░░░   ░░   ")
	print("  ░   ░ ░   ░ ░░░  ░░░  ░   ░   ░      ░░░░  ░░░░░  ░░░     ░     ░░░░░ ░   ░   ░   ░░░░░ ░░░░    ░      ░   ░ ░░░   ░   ")

	version = "version: 1.0.0"
	print(version.center(120))

def clear():

	os.system("cls" if os.name == "nt" else "clear")

def menu():

	while True:

		clear()
		banner()
		print("\n[1] Network Scanner")

		try:

			choice = input("\n[+] Select Tool: ")

			if choice == "1":

				networkScanner()

			else:

				print("\n[-]Please enter valid option")

		except KeyboardInterrupt:

			print("\nGoodbye")
			break

def networkScanner():

	target = input("\n[+] Enter IP: ")

	try:

		for port in range(1,65535):

			with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
				
				sock.settimeout(1)

				results = sock.connect_ex((target, port))

				if results == 0:

					print(f"Port {port} is open.")

				sock.close()

	except KeyboardInterrupt:
		print("\nGoodbye")

if __name__ == "__main__":

	menu()
