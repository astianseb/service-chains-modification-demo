from cloudify import ctx

ctx.logger.info('---> VNF {} is stopping...'.format(str(ctx.node.name)))
