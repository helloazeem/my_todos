import FreeSimpleGUI as SGui
from zip_extrator import extract_archive

SGui.theme("Black")

label1 = SGui.Text("Select Archive")
input1 = SGui.Input()
choose_button1 = SGui.FileBrowse("Choose", key="archive")

label2 = SGui.Text("Select Dest Dir")
input2 = SGui.Input()
choose_button2 = SGui.FolderBrowse("Choose", key="folder")

extract_button = SGui.Button("Extract")
output_label = SGui.Text(key="output", text_color= "green")

window = SGui.Window("Archive Extractor",
                     layout=[[label1, input1, choose_button1],
                     [label2, input2, choose_button2],
                     [extract_button, output_label]])


while True:
    event, values = window.read()
    print(event, values)
    archive_path = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archive_path, dest_dir)
    window["output"].update(value="Extraction Complete")

window.close()