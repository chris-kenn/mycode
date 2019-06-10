#!/usr/bin/env python3

my_list = [ "192.168.0.5", 5060, "UP" ]
# Print IP
print("The first item in the list (IP): " + my_list[0] )
# Print port
print("The second item in the list (port): " + str(my_list[1]) )
# Print state
print("The last item in the list (state): " + my_list[2] )

# Add new list
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
# Print out statement
print(f"When I {new_list[5]} into IP address {new_list[3]} or {new_list[4]} I am unable to ping ports {new_list[0]}, {new_list[1]}, or {new_list[2]}. ")

