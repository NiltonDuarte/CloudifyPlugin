# import the ctx object
from cloudify import ctx
# import the operation decorator
from cloudify.decorators import operation
import requests
import json
import time

@operation
def start(**kwargs):
  ctx.logger.info("my_start-"+str(kwargs))
  vNetName = str(ctx.node.properties["vNet_name"])
  restURL = "http://"+ctx.node.properties["server_ip"]+":"+str(ctx.node.properties["server_port"])+"/overlay/orchestrator/v1"
  url = restURL +"/vnet"
  ctx.logger.info(url)
  data = {"vNets" : [{"vNetworkName": vNetName}]}
  ctx.logger.info(data)
  data_json = json.dumps(data)
  headers = {'Content-type': 'application/json'}
  #url = 'http://httpbin.org/post'
  response = requests.post(url, data=data_json, headers=headers, auth=('karaf','karaf'))
  ctx.logger.info(response.json())
  """
  getURL = restURL + "/vnet/network/" + vNetName
  reqCode = -1
  max_count = 20
  count = 0
  while not reqCode == 200:
    if count > max_count:
      #throw
      return
    count += 1
    time.sleep(0.2)
    response = requests.get(getURL, headers=headers, auth=('karaf','karaf'))
    reqCode = response.status_code
    ctx.logger.info("req_status_code:"+str(reqCode))
  """

@operation
def stop(**kwargs):
  ctx.logger.info("my_stop-"+str(kwargs))
  vNetName = str(ctx.node.properties["vNet_name"])
  restURL = "http://"+ctx.node.properties["server_ip"]+":"+str(ctx.node.properties["server_port"])+"/overlay/orchestrator/v1"
  url = restURL +"/vnet/network/"+vNetName
  ctx.logger.info(url)
  headers = {'Accept': 'application/json'}
  response = requests.delete(url, headers=headers, auth=('karaf','karaf'))
  #ctx.logger.info(response.json())

@operation
def delete(**kwargs):
  stop(kwargs)

