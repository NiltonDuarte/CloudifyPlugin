# import the ctx object
from cloudify import ctx
# import the operation decorator
from cloudify.decorators import operation
import requests
import json

@operation
def start():
  vNetName = ctx.node.properties["vNet_name"]
  url = ctx.node.properties["server_ip"]+":"+ctx.node.properties["server_port"]
  data = {"vNets" : [{"vNetworkName": vNetName}]}
  data_json = json.dumps(data)
  headers = {'Content-type': 'application/json'}
  #url = 'http://httpbin.org/post'
  response = requests.post(url, data=data_json, headers=headers)
  #print response

@operation
def stop():
  pass
#create_Vnet('teste')