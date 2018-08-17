# import the ctx object
from cloudify import ctx
# import the operation decorator
from cloudify.decorators import operation
from common import *
import requests
import json
import time

@operation
def create(**kwargs):
  ctx.logger.info("my_start-")
  #for key, value in ctx.node.properties.iteritems():
  # ctx.logger.info([key, value])
  vNetName = str(ctx.node.properties["vNet_name"])
  urlPath = "/vnet"
  data = {"vNets" : [{"vNetworkName": vNetName}]}
  ctx.logger.info(data)
  solo_config = ctx.node.properties["solo_config"]
  response = REST.post(urlPath, data, solo_config)
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
def delete(**kwargs):
  ctx.logger.info("my_stop-")
  vNetName = str(ctx.node.properties["vNet_name"])
  urlPath = "/vnet/network/{}".format(vNetName)
  solo_config = ctx.node.properties["solo_config"]
  response = REST.delete(urlPath, solo_config)
  ctx.logger.info(response.json())
