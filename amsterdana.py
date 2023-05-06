#!/usr/bin/python
print="""

                                       _       
                    _                 | |      
 _____ ____   ___ _| |_ _____  ____ __| |_____ 
(____ |    \ /___|_   _) ___ |/ ___) _  (____ |
/ ___ | | | |___ | | |_| ____| |  ( (_| / ___ |
\_____|_|_|_(___/   \__)_____)_|   \____\_____|
                                               



"""
import nmap

# Criando um objeto nmap
nm = nmap.PortScanner()

# Variável com o endereço IP ou URL
ip = input('Digite o endereço IP ou URL: ')

# Escaneando o endereço IP ou URL
nm.scan(ip, arguments='-A -T4')

# Imprimindo informações
print('='60)
print('Informações do Host: ' + ip)
print('='60)
print('Status do Host: ' + nm[ip].state())
print('='60)
for protocolo in nm[ip].all_protocols():
    print('Portas abertas para o protocolo ' + protocolo + ': ')
    lista = nm[ip][protocolo].keys()
    lista.sort()
    for porta in lista:
        print('porta: ' + str(porta) + '\t\t Estado: ' + nm[ip][protocolo][porta]['state'])

print('='60)
print('Serviços detectados: ')
for servico in nm[ip]['tcp']:
    print('Porta: ' + str(servico) + '\t\t Serviço: ' + nm[ip]['tcp'][servico]['name'])

print('='60)
print('Informações do SO: ')
print('SO: ' + nm[ip].hostname())
print('Fabricante: ' + nm[ip].vendor())
print('Versão: ' + nm[ip].os_version())
print('Família: ' + nm[ip].os_family())
print('='60)