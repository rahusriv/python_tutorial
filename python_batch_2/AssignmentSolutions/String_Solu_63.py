ip_address = input("Enter an ip address :")

ip_address = ip_address.strip()

#ip_address = ip_address.lstrip("0")
count =0
for c in ip_address:
    if(c == "0"):
        count = count +1
    else:
        break

result = ip_address[count:]
print(ip_address)
print(result)