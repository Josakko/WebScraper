#!/bin/bash
read -p "Enter MAC address: " mac_address

read -p "Enter interface name: " interface_name

cd " 'replace this whit path of main.py' "
python3 main.py -i "$interface_name" -m "$mac_address"
