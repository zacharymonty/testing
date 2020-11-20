def get_options_list(field, control_value=None, **kwargs):
    
    options = []    
          
    if not control_value:
        options = [('', 'Please Select Above')]
        return options    
    
    
    if control_value == '11AA':
        options.append(('A11A', 'A11A'))
    
    if control_value == '22BB':
        options.append(('B22B', 'B22B'))
        
    if control_value == '33CC':
        options.append(('C33C', 'C33C'))
    
    if control_value == '44DD':
        options.append(('D44D', 'D44D'))
    
    return options
