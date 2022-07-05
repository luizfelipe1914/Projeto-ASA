#!/usr/bin/env python3

from pathlib import Path
import json

def main():
	try:
		with open("config.json", "r") as config:
			configuration = json.loads(config.read())
			config.close()

	except Exception as err:
		print(err)


	direta = open("db.mg.asa.br.external", "r")
	reversa = open("db.reverso.mg.asa.br.external", "r")
	data_direta = direta.readlines()
	data_reversa = reversa.readlines()

	data_direta = data_direta.replace(f"SERIAL", f"{configuration['SERIAL']}")
	data_reversa = data_reversa.replace(f"SERIAL", f"{configuration['SERIAL']}")
	configuration.pop("SERIAL")
	
	direta.close()
	reversa.close()

	for c in configuration.keys():
		data_direta = data_direta.replace(f"{c}", f"{configuration[c]}")
		temp = configuration[c].split('.')
		data_reversa = data_reversa.replace(f"{c}", f"{temp[3]}")
	
	direta = open("db.mg.asa.br.external", "w")
	reversa = open("db.reverso.mg.asa.br.external", "w")
	direta.write(data_direta)
	reversa.write(data_reversa)

if __name__ == '__main__':
	main()
