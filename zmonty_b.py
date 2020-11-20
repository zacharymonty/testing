def get_options_list(field, control_value=None, **kwargs):
    
    options = []    
          
    if not control_value:
        options = [('', 'Please Select Above')]
        return options    
    
    
    if control_value == 'AAAA':
        options.append(('1111', '1111'))
    
    if control_value == 'BBBB':
        options.append(('2222', '2222'))
        
    if control_value == 'CCCC':
        options.append(('3333', '3333'))
    
    if control_value == 'DDDD':
        options.append(('4444', '4444'))
    
    return options
