# import the ctx object
from cloudify import ctx
# import the operation decorator
from cloudify.decorators import operation
from common import *

@operation
def create(**kwargs):
  ctx.logger.info("switch_create")
  solo_config = ctx.node.properties["solo_config"]
  
  datapathId = ctx.node.properties["datapathId"]
  controllerIp = ctx.node.properties["controllerIp"]
  controllerPort = ctx.node.properties["controllerPort"]
  openflowVersion = ctx.node.properties["openflowVersion"]
  physicalDevice = ctx.node.properties["physicalDevice"]
  vNetworkName = ctx.node.properties["vNetworkName"]
  ctx.logger.info(dir(ctx))
  ctx.logger.info(dir(ctx.node))
  ctx.logger.info(dir(ctx.instance))
   

@operation
def delete(**kwargs):
  ctx.logger.info("switch_delete")
  solo_config = ctx.node.properties["solo_config"]