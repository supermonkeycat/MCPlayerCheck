from mcstatus import JavaServer

serverip = input("Enter the ip of the server: ")
serverport = input("Enter the port of the server (leave blank for default 25565): ")

if not serverport:
  serverport = 25565
else:
  serverport = int(serverport)

print(f"Attempting to connect to {serverip}:{serverport}...")

try:
  server = JavaServer.lookup(f"{serverip}:{serverport}")
  status = server.status()
  print("Connected!")
  print(f"The server has {status.players.online} player(s) online out of {status.players.max} max.")

  if status.players.sample:
    print("Online Players:")
    for player in status.players.sample:
      print(f"- {player.name}")
  else:
    print("No players online.")
except Exception as e:
  print(f"Could not connect to the server: {e}")
