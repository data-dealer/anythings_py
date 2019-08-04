# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 09:05:19 2018

@author: User
"""

import xlsxwriter

# Note the file extension should be .xlsm.
workbook = xlsxwriter.Workbook('macros2.xlsm')
worksheet = workbook.add_worksheet()

worksheet.set_column('A:A', 30)

# Add the VBA project binary.
workbook.add_vba_project('./vbaProject.bin')

# Show text for the end user.
worksheet.write('A3', 'Press the button to say hello.')

# Add a button tied to a macro in the VBA project.
worksheet.insert_button('B3', {'macro': 'say_hello',
                               'caption': 'Press Me',
                               'width': 80,
                               'height': 30})

workbook.close()






import xlsxwriter

# Note the file extension should be .xlsm.
workbook = xlsxwriter.Workbook('macros.xlsm')
worksheet = workbook.add_worksheet()

worksheet.set_column('A:A', 30)

# Add the VBA project binary.
workbook.add_vba_project('./vbaProject.bin')

# Show text for the end user.
worksheet.write('A3', 'Press the button to say hello.')

# Add a button tied to a macro in the VBA project.
worksheet.insert_button('B3', {'macro':   'say_hello',
                               'caption': 'Press Me',
                               'width':   80,
                               'height':  30})

workbook.close()