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
  ctx.logger.info("ctx: "+str(dir(ctx)))
  ctx.logger.info("ctx.node: "+str(dir(ctx.node)))
  ctx.logger.info("ctx.instance: "+str(dir(ctx.instance)))
  for rel in ctx.instance.relationships:
    ctx.logger.info("rel: "+str(dir(rel)))
    ctx.logger.info("rel.target: "+str(dir(rel.target)))
    ctx.logger.info("rel.type: "+str(rel.type))
    ctx.logger.info("rel.target.node.properties: "+str(rel.target.node.properties))
   

@operation
def delete(**kwargs):
  ctx.logger.info("switch_delete")
  solo_config = ctx.node.properties["solo_config"]