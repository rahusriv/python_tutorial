from netmiko import ConnectHandler

iosv_l2 = {
    #'device_type':'cisco_ios',
    'device_type':'linux',
    'ip':'127.0.0.1',
    'username':'rahul',
    'password':'rahul12'
}

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('ls')
print(output)

#config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
#output = net_connect.send_config_set(config_commands)
#print(output)

#for n in range(2,22):
#    print("Creating vlan "+ str(n))
#    config_commands = ['vlan '+str(n), 'name Python_VLAN '+str(n)]
#    output = net_connect.send_config_set(config_commands)
#    print(output)

