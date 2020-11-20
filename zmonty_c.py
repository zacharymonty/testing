def get_options_list(field, control_value=None, **kwargs):
    
    options = []    
          
    if not control_value:
        options = [('', 'Please Select Above')]
        return options    
    
    
    if control_value == '1111':
        options.append(('A1A1', 'A1A1'))
    
    if control_value == '2222':
        options.append(('B2B2', 'B2B2'))
        
    if control_value == '3333':
        options.append(('C3C3', 'C3C3'))
    
    if control_value == '4444':
        options.append(('D4D4', '4444'))
    
    return options
