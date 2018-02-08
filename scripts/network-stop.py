from cloudify import ctx

ctx.logger.info('---> NETWORK {} is stopping...'.format(str(ctx.node.name)))
