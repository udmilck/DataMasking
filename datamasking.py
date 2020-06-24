# -*- coding: utf-8 -*-
import PySimpleGUI as sg
import main

layout= [[sg.Text('待转换文档目录', size=(15, 1), auto_size_text=False, justification='right'),
        sg.InputText(key='-From Folder-'), sg.FolderBrowse()],
        [sg.Text('转换后文档目录', size=(15, 1), auto_size_text=False, justification='right'),
        sg.InputText(key='-To Folder-'), sg.FolderBrowse()],[sg.Btn('开始处理', key='_CONFIRM_'),sg.Btn('结束', key='_quit_')]]

# Create the Window
window = sg.Window('数据脱敏', layout)

# Create the event loop
while True:
    event, values = window.read()
    if event == '_CONFIRM_':
        try:
            main.editAll(str(values['-From Folder-']),str(values['-To Folder-']))
            sg.popup('文档脱敏成功')
        except:
            sg.popup('处理出错，请检查文档')
    if event == '_quit_':
        break
    if event in (None, 'Cancel'):
        # User closed the Window or hit the Cancel button
        break
    # print(f'Event: {event}')
    # print(str(values))

window.close()
