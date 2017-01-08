# -*- coding: utf-8 -*-
"""
http://stackoverflow.com/questions/466345/converting-string-into-datetime
"""
from datetime import datetime
now = datetime.today()
nice_time = datetime.strftime(now, '%A %B %d, %Y')
print nice_time
