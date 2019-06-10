#!/usr/bin/env python3

proto = ['ssh', 'http', 'https']
protoa = ['ssh', 'http', 'https']
print(proto)
# print(proto[1])
proto.append('dns') # Add to end of list
protoa.append('dns') # Add to end of list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # common ports
proto.extend(proto2)
print(proto)
protoa.append(proto2)
print (protoa)

# proto.extend('dns')
# print(proto)


