# -*- coding: utf-8 -*-
import PySimpleGUI as sg
import main

layout= [[sg.Text('原始目录', size=(15, 1), auto_size_text=False, justification='right'),
        sg.InputText(key='-From Folder-'), sg.FolderBrowse()],
        [sg.Text('转换后目录', size=(15, 1), auto_size_text=False, justification='right'),
        sg.InputText(key='-To Folder-'), sg.FolderBrowse()],[sg.Btn('确定', key='_CONFIRM_'), sg.Cancel()]]

# Create the Window
window = sg.Window('数据处理', layout)

# Create the event loop
while True:
    event, values = window.read()
    if event == '_CONFIRM_':
        try:
            main.editAll(str(values['-From Folder-']),str(values['-To Folder-']))
            sg.popup('文档转换成功')
        except:
            sg.popup('转换出错')
    if event in (None, 'Cancel'):
        # User closed the Window or hit the Cancel button
        break
    print(f'Event: {event}')
    print(str(values))

window.close()
