import sys
from generate_dump import generate_dump
from ip_addr_valid import ip_addr_valid
from ip_reach import ip_reach
from ip_file_valid import ip_file_valid
from create_threads import create_threads
from generate_tsf import generate_tsf

choice = input("Enter 1 for Stats Dump and Enter 2 for Tech Support File.\nEnter 1 or 2:")
while (choice != '1') and (choice != '2'):
    choice = input("Dude, come one! Enter 1 for Stats Dump and Enter 2 for Tech Support File.\nEnter 1 or 2:")

if choice == '1':
    # Saving the list of ip address in in ip.txt to a variable
    ip_list = ip_file_valid()

    # verifying the validity of each ip address in the list
    try:
        ip_addr_valid(ip_list)

    except KeyboardInterrupt:
        print("\n\n* Program aborted by user. Exiting...\n")
        sys.exit()

    # Verifying the reachablity of each IP address in the list
    try:
        ip_reach(ip_list)

    except KeyboardInterrupt:
        print("\n\n* Program aborted by user. Exiting...\n")
        sys.exit()

    create_threads(ip_list, generate_dump)

elif choice == '2':
    # Saving the list of ip address in in ip.txt to a variable
    ip_list = ip_file_valid()

    # verifying the validity of each ip address in the list
    try:
        ip_addr_valid(ip_list)

    except KeyboardInterrupt:
        print("\n\n* Program aborted by user. Exiting...\n")
        sys.exit()

    # Verifying the reachablity of each IP address in the list
    try:
        ip_reach(ip_list)

    except KeyboardInterrupt:
        print("\n\n* Program aborted by user. Exiting...\n")
        sys.exit()

    create_threads(ip_list, generate_tsf)

#Calling thrteads creation function for one or multiple ssh connections
#create_threads(ip_list, generate_dump)

#End of program