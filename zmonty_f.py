def get_options_list(field, control_value=None, **kwargs):
    
    options = []    
          
    if not control_value:
        options = [('', 'Please Select Above')]
        return options    
    
    
    if control_value == 'A11A':
        options.append(('111A', '111A'))
    
    if control_value == 'B22B':
        options.append(('222B', '222B'))
        
    if control_value == 'C33C':
        options.append(('333C', '333C'))
    
    if control_value == 'D44D':
        options.append(('444D', '444D'))
    
    return options
