from websocket_server import WebsocketServer

# Called for every client connecting (after handshake)
def new_client(client, server):
	print("New client connected and was given id %d" % client['id'])
	server.send_message_to_all("Hey all, a new client has joined us")


# Called for every client disconnecting
def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
	if len(message) > 200:
		message = message[:200]+'..'
	print("Client(%d) said: %s" % (client['id'], message))

	if(message=='list_clients'):
		for obj in server.clients:
			print(obj)

	print(message[0:4])
	if(message[0:4]=='tell'):
		parts = message.split(',')

		tell_part = parts[0].split(':')
		id = int(tell_part[1])

		for obj in server.clients:
			if obj["id"]==id:
				sendto = obj
				break

		text_part = parts[1].split(':')
		text = text_part[1]

		server.send_message(sendto,text)











PORT=5012
server = WebsocketServer(host='192.168.2.3' ,port = PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
