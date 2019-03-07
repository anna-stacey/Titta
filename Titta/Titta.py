# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 08:39:57 2018

@author: Marcus
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 14:16:59 2018

@author: Marcus
"""

from psychopy import core

def get_defaults(et_name):
    if et_name == 'Tobii4C':
        import Tobii4C as settings
        settings.eye_tracker_name = 'Tobii4C'
    elif et_name == 'Spectrum':
        import Spectrum as settings
        settings.eye_tracker_name = 'Spectrum'        
    elif et_name == 'Nano':
        import Nano as settings
        settings.eye_tracker_name = 'Nano'        
    else:
        print('eye tracker type not supported')
        core.quit()
    return settings
    
    
class Connect(object):   
    def __init__(self, in_arg='dummy'):
        '''  in_arg can be either string with eye tracker name
        or 'settings' generated by calling (and optionally modifying)
        the output from get_defaults()
        '''
        
        if isinstance(in_arg, str):
            if 'dummy' in in_arg:
                import Tobii_dummy
                self.__class__ = Tobii_dummy.Connect
                self.__class__.__init__(self)  
            else:            
                import Tobii
                self.__class__ = Tobii.myTobii
                self.__class__.__init__(self, in_arg)
        else:
            import Tobii
            self.__class__ = Tobii.myTobii
            self.__class__.__init__(self, in_arg)
            
            
        

