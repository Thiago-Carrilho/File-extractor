import PySimpleGUI as sg
from extractor import extract_archive

sg.theme('Black')

label1 = sg.Text("Select Archive:")
input1 = sg.Input()
choose1 = sg.FilesBrowse("Browse", key="archive")

label2 = sg.Text("Select dest dir:")
input2 = sg.Input()
choose2 = sg.FilesBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("Archive Extractor",
                   layout=[[label1, input1, choose1],
                           [label2, input2, choose2],
                           [extract_button, output_label]])
while True:
    event, values = window.read()
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepath,dest_dir)
    window["output"].update(value="Extraction Completed!")

window.close()
