import wmi
import socket
import psutil

def obter_interface_rede_ativa():
    interfaces = psutil.net_if_stats()
    for interface, status in interfaces.items():
        # Verifica se a interface está ativa
        if status.isup:
            return interface


# Obtém o nome da interface e o endereço IP da interface de rede ativa


# if nome_interface_ativa:
#     print("A interface de rede ativa é:", nome_interface_ativa)
# else:
#     print("Nenhuma interface de rede ativa encontrada.")


def obter_endereco_ip_por_nome_interface():
    nome_interface_ativa = obter_interface_rede_ativa()
    interfaces = psutil.net_if_addrs()
    for interface, enderecos in interfaces.items():
        if interface == nome_interface_ativa:
            for endereco in enderecos:
                if endereco.family == socket.AF_INET:
                    # print(endereco.family, socket.AF_INET)
                    return endereco.address, nome_interface_ativa
    return None  # Retorna None se a interface não for encontrada ou não tiver um endereço IPv4

def change_dns_to_google(interface_ip):
    dns_servers = ["8.8.8.8", "8.8.4.4"]  # Altere para seus servidores DNS desejados
    c = wmi.WMI()
    for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
        for ip_info in interface.IPAddress:
            if ip_info == interface_ip:
                # Configurar os servidores DNS
                interface.SetDNSServerSearchOrder(DNSServerSearchOrder=dns_servers)
                return "ok"
            else:
                return "not ok"
    print(f"Não foi possível encontrar uma interface com o IP {interface_ip}")

def change_dns_to_dhcp(interface_ip):
    c = wmi.WMI()
    for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
        for ip_info in interface.IPAddress:
            if ip_info == interface_ip:
                # Configurar o DNS para automático (DHCP)
                interface.SetDNSServerSearchOrder()
                return "ok"
            else:
                return "not ok"
    print(f"Não foi possível encontrar uma interface com o nome {interface_ip}.")

# Nome do endereço IP da interface de rede que você deseja modificar
# interface_ip = endereco_ip_rede_ativa  # Substitua pelo IP da sua interface

# Lista de servidores DNS que você deseja configurar


# change_dns_to_google(interface_ip, dns_servers)
# change_dns_to_dhcp(interface_ip)