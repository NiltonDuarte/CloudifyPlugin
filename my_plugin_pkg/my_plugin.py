# import the ctx object
from cloudify import ctx
# import the operation decorator
from cloudify.decorators import operation
import requests
import json

@operation
def start(**kwargs):
  ctx.logger.info("my_starting")
  vNetName = str(ctx.node.properties["vNet_name"])
  url = "http://"+ctx.node.properties["server_ip"]+":"+str(ctx.node.properties["server_port"])+"/overlay/orchestrator/v1/vnet"
  ctx.logger.info(url)
  data = {"vNets" : [{"vNetworkName": vNetName}]}
  ctx.logger.info(data)
  data_json = json.dumps(data)
  headers = {'Content-type': 'application/json'}
  #url = 'http://httpbin.org/post'
  response = requests.post(url, data=data_json, headers=headers, auth=('karaf','karaf'))
  ctx.logger.info(response.json())
  #print response

@operation
def stop():
  pass
#create_Vnet('teste')
