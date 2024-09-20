import logging
logger = logging.getLogger('base')

def create_model(opt, mask=0):
    model = opt['model']
    frame_num = opt['gop']
    from .IBSN import Model_VSN as M

    m = M(opt, mask=mask)
    logger.info('Model [{:s}] is created.'.format(m.__class__.__name__))
    return m