# import the ctx object
from cloudify import ctx # pylint: disable=import-error
# import the operation decorator
from cloudify.decorators import operation # pylint: disable=import-error
from common import REST
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
  dummy = REST.post(urlPath, data, solo_config)
  #ctx.logger.info(response.json())


@operation
def delete(**kwargs):
  ctx.logger.info("network_delete")
  solo_config = ctx.node.properties["solo_config"]
  vNetName = str(ctx.node.properties["vNetworkName"])
  urlPath = "/vnet/network/{}".format(vNetName)
  dummy = REST.delete(urlPath, solo_config)
  #ctx.logger.info(response.json())
