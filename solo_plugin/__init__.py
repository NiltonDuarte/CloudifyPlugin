# import the ctx object
from cloudify import ctx
# import the operation decorator
from cloudify.decorators import operation

ctx.logger.info(dir(ctx.node))
ctx.logger.info(dir(ctx))