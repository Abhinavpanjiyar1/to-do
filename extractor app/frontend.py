import PySimpleGUI as aa
from backend import extract_archive

aa.theme("black")

label1 = aa.Text("select archive:")
input1 = aa.Input()
choose_button1 = aa.FileBrowse("choose", key = "archive")


label2 = aa.Text("select dest dir:")
input2 = aa.Input()
choose_button2 = aa.FolderBrowse("choose", key = "folder")

extract_button = aa.Button('Extract')
output_label = aa.Text(key = 'output', text_color='red')

window = aa.Window('Archive Extractor',
                   layout = [[label1, input1, choose_button1],
                   [label2, input2, choose_button2],
                   [extract_button, output_label]])
while True:
    event, values = window.read()
    print(event, values)
    archivepath = values['archive']
    dest_dir = values['folder']
    extract_archive(archivepath, dest_dir)
    window["output"].update(value = "extraction completed")


window.close()


