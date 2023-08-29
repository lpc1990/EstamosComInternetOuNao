from ping3 import ping, verbose_ping

# Ping simples
hostname = "www.google.com"
response_time = ping(hostname)
if response_time is not None:
    print(f"Ping response time for {hostname}: {response_time:.2f} ms")
else:
    print(f"Failed to ping {hostname}")

# Ping com mais detalhes
verbose_ping(hostname, count=4)