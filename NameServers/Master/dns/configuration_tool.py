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

	direta = Path(r"db.mg.asa.br.external")
	reversa = Path(r"db.reverso.mg.asa.br.external")
	data_direta = direta.read_text()
	data_reversa = reversa.read_text()

	data_direta = data_direta.replace(f"SERIAL", f"{configuration['SERIAL']}")
	data_reversa = data_reversa.replace(f"SERIAL", f"{configuration['SERIAL']}")
	configuration.pop("SERIAL")
	
	for c in configuration.keys():
		data_direta = data_direta.replace(f"{c}", f"{configuration[c]}")
		temp = configuration[c].split('.')
		data_reversa = data_reversa.replace(f"{c}", f"{temp[3]}")
	direta.write_text(data_direta)
	reversa.write_text(data_reversa)

if __name__ == '__main__':
	main()
