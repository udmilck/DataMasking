# -*- coding: utf-8 -*-
import PySimpleGUI as sg

# Create some widgets
# text = sg.Text("待处理文档路径")
# text_entry = sg.FilesBrowse()
layout= [[sg.FileBrowse('打开图片',key='filebrowser',target='image_shape'),sg.InputText('',key='image_shape',disabled=True)]]
# ok_btn = sg.Button('OK')
# cancel_btn = sg.Button('Cancel')
# layout = [[text, text_entry],
#           [ok_btn, cancel_btn]]

# Create the Window
window = sg.Window('Hello PySimpleGUI', layout)

# Create the event loop
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        # User closed the Window or hit the Cancel button
        break
    print(f'Event: {event}')
    print(str(values))

window.close()
