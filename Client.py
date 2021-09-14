#HTTP Client

#Imports
import http.client

#get http server ip
http_server = "127.0.0.1"

#create a connection
conn = http.client.HTTPConnection(http_server,8080)


while True:
    cmd = input('INPUT : [ex. "GET "secret.html or "GET grp2.html"]: ')
    # cmd = ['GET', "secret.html"]
    cmd = cmd.split()

    if cmd[0] == 'end': #type "end" to end client side connection
        break
    
    #request command to server
    conn.request(cmd[0], cmd[1])

    #get response from server
    rsp = conn.getresponse()
    
    #print server response and data
    print(rsp.status, rsp.reason)
    data_received = rsp.read()
    print(data_received)
    
conn.close()