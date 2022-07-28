
# MAC_changer
💻It`s little script, which can  change your MAC address on LINUX.💻
## Description
This script to changes your MAC address by using the following commands: 

 1. `ifconfig 'interface' down`
 2. `ifconfig interface hw ether 'new mac address' `
 3. `ifconfig 'interface' up`
 ## Usage
Run the script in your terminal with parameters which you can find below.
`python3 MAC_changer.py *parameters*`

### Parameters:
 1. **[NECESSARY]**  `-i eth0`  - after  "-i" write your interface, which MAC address will be changed. 

> EXAMPLE: `python3 MAC_changer.py -i eth0`
> ![enter image description here](https://i.imgur.com/kYFWCc5.png)

 2. **[OPTIONAL]**  `-m 00:11:22:33:44:66` - after "-m" write the new MAC address . If you will not write this parameter, the address will be random generated. 

> EXAMPLE: `python3 MAC_changer.py -i eth0 -m 00:11:22:33:44:66` 
> ![enter image description here](https://i.imgur.com/K89AhNZ.png)

 3. **[OPTIONAL]**  `-t time` - where time is (1s - seconds, 1m - minutes, 1h - hours). This function let the script change the MAC address every time, that you wrote in. The MAC addresses will be random generated. 

> EXAMPLE: `python3 MAC_changer.py -i eth0 -t 1m`
![enter image description here](https://i.imgur.com/K0toiCd.png)
> ![enter image description here](https://i.imgur.com/tB6EgPx.png)
## Help
For more information you can use: `python3 MAC_changer.py --help`
