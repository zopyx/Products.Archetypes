REQUEST = context.REQUEST
SESSION = REQUEST.SESSION
    
if not hasattr(context, 'isTemporary'):
    id = context.getId()
    referrer = REQUEST.get('HTTP_REFERER', context.aq_parent.absolute_url())
    cflag = SESSION.get('__creation_flag__', {})
    cflag.update({id:referrer})
    SESSION.set('__creation_flag__', cflag)