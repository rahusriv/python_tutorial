from netmiko import ConnectHandler

iosv_l2 = {
    #'device_type':'cisco_ios',
    #'device_type'='generic_termserver_telnet'
    'device_type':'linux',
    'ip':'127.0.0.1',
    'username':'rahul',
    'password':'mastlappyubuntu12',
    #'port':2000

}

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('ls')
if("folder2" in output):
    print("Command successful")
else:
    print("command did not succed")
print(output)

print(type(output))


res = net_connect.is_alive()
print(type(res))
print(res)

#print(type(output))
#print("abc\n def\n")
#commands = ['mkdir abc']
#output = net_connect.send_config_set(config_commands=commands, delay_factor=100)
#print(output)

#for n in range(2,22):
#    print("Creating vlan "+ str(n))
#    config_commands = ['vlan '+str(n), 'name Python_VLAN '+str(n)]
#    output = net_connect.send_config_set(config_commands)
#    print(output)

