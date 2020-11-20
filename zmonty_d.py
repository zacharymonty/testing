def get_options_list(field, control_value=None, **kwargs):
    
    options = []    
          
    if not control_value:
        options = [('', 'Please Select Above')]
        return options    
    
    
    if control_value == 'A1A1':
        options.append(('11AA', '11AA'))
    
    if control_value == 'B2B2':
        options.append(('22BB', '22BB'))
        
    if control_value == 'C3C3':
        options.append(('33CC', '33CC'))
    
    if control_value == 'D4D4':
        options.append(('44DD', '44DD'))
    
    return options
