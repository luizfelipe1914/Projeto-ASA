#!/usr/bin/env python3

import json

"""
	load_data -> Essa função recebe como parâmetro o arquivo json, efetua sua leitura
	e retorna um dicionário contendo os dados.
"""
def load_data(config):
    data = ""
    try:
        with open(config, "r") as configuration:
            data = json.loads(configuration.read())
            configuration.close()
    except Exception as err:
        print(err)
    return data

"""
	replace_data_direct_zone -> Essa função recebe como parâmetros o arquivo da zona de pesquisa direta
	e um dicionário contendos os dados. Ela efetua a leitura do arquivo de zona e substitui algumas
 	plaravras(chaves do dicionário) pelos seus valores. Ex. {'APACHE2':'172.25.0.11'}, a função irá buscar
	no texto lido do arquivo a palavra APACHE2, em seguida a substituirá por 172.25.0.11. É retornada uma string
	com os devidos valores.
"""
def replace_data_direct_zone(zone, data):
	direct_data = ""
	try:
		with open(zone, "r") as direct:
			direct_data = direct.read()
			direct.close()
	except Exception as err:
		print(err)
	for d in data.keys():
		direct_data = direct_data.replace(d, data[d])
	return direct_data

"""
	replace_data_reverse_zone -> Essa função recebe como parâmetros o arquivo da zona de pesquisa reversa
	e um dicionário contendos os dados. Ela efetua a leitura do arquivo de zona e substitui algumas
 	plaravras(chaves do dicionário) pelos seus valores(último octeto do endereço IPv4). 
  	Ex. {'APACHE2':'172.25.0.11'}, a função irá buscar no texto lido do arquivo a palavra APACHE2, 
    em seguida, a substituirá por 11. É retornada uma string com os devidos valores
"""

def replace_data_reverse_zone(zone, data):
	try:
		with open(zone, "r") as reverse:
			reverse_data = reverse.read()
			reverse.close()
	except Exception as err:
		print(err)
	reverse_data = reverse_data.replace("SERIAL", f"{data['SERIAL']}")
	for d in data.keys():
		if(d != "SERIAL"):
			reverse_data = reverse_data.replace(f"{d}", f"{data[d].split('.')[3]}")
	return reverse_data

"""
	write_data -> recebe como parâmetros os arquivos de zona direta e reversa e as strings
	com os devidos valores, efetua a gravação destas nos arquivos de zona.
"""
def write_data(direct, reverse, direct_zone, reverse_zone):
    try:
        with open(direct_zone, "w") as dz:
            dz.write(direct)
    except Exception as err:
        print(err)
    try:
        with open(reverse_zone, "w") as rz:
            rz.write(reverse)
    except Exception as err:
        print(err)
    

def main():
    
	js = load_data("config.json")
	dz = replace_data_direct_zone("db.mg.asa.br.external", js)
	rz = replace_data_reverse_zone("db.reverso.mg.asa.br.external", js)
	#print(js)
	print(dz)
	print(rz)
	write_data(dz, rz, "db.mg.asa.br.external", "db.reverso.mg.asa.br.external")
	
if __name__ == '__main__':
	main()
