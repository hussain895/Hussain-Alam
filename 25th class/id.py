log = 'IP:192.168.1.22 [STATUS=404] ENDPOINT="/api/vi/users" TIME=0.452s'

ip = log[log.index(":")+1 : log.index(" ")]
status = log[log.index("=")+1 : log.index("]" , log.index("="))]
endpoint = log.split('"')[1]
time = log[59:65]
time_float = float(time[-5:-1])

print("IP : " , ip)
print("Status : " , status)
print("Endpoint : " , endpoint)
print("Time  : " , time_float)
print(type(time_float))


if status > "400":
    print("The Status Is Greator Than 400")
else:
    print("The Status Is Less Than 400")
