def update_allowed_ips(allowed_ips):
    new_ip = input("Enter new IP address: ")
    allowed_ips.append(new_ip)
    return allowed_ips


server_ip = ("192", "168", "1", "10")

allowed_ips = ["192.168.1.5", "192.168.1.6"]

print("Server IP:", ".".join(server_ip))
print("Allowed IPs:", allowed_ips)

allowed_ips = update_allowed_ips(allowed_ips)

print("\nUpdated Configuration:")
print("Server IP:", ".".join(server_ip))
print("Allowed IPs:", allowed_ips)