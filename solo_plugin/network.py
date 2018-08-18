# import the ctx object
from cloudify import ctx
# import the operation decorator
from cloudify.decorators import operation
from common import *
import time

@operation
def create(**kwargs):
  ctx.logger.info("network_create")
  for rel in ctx.instance.relationships:
    ctx.logger.info(rel.node.properties)
  solo_config = ctx.node.properties["solo_config"]
  vNetName = str(ctx.node.properties["vNetworkName"])
  urlPath = "/vnet"
  data = {"vNets" : [{"vNetworkName": vNetName}]}
  ctx.logger.info(data)
  response = REST.post(urlPath, data, solo_config)
  #ctx.logger.info(response.json())


@operation
def delete(**kwargs):
  ctx.logger.info("network_delete")
  solo_config = ctx.node.properties["solo_config"]
  vNetName = str(ctx.node.properties["vNetworkName"])
  urlPath = "/vnet/network/{}".format(vNetName)
  response = REST.delete(urlPath, solo_config)
  #ctx.logger.info(response.json())
