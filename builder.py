# hello_psg.py

import PySimpleGUI as sg
import os
import subprocess

branchselect = [[sg.Text("Paste github link to sm64pc repo and branch")],[sg.In(),sg.In(size=(7, 1))],[sg.Text("And type the name of repo folder")],[sg.In()],[sg.Text('modelpack folder (optional)')],[sg.In(),sg.FolderBrowse()],[sg.Text('Texture pack folder (optional)')],[sg.In(),sg.FolderBrowse()],[sg.Button("Ok")]]
buildoptions = [[sg.Text('specify build flags and jobs, you can see possible flags on your repo\'s wiki, if you use modelpack, use MODELPACK=1, if you use texturepack, use EXTERNAL_DATA=1')],[sg.InputText(),sg.Button('Build')]]
baseromselect = [[sg.Text("Select baserom of sm64 with extension .z64")],[
        sg.Text("baserom:"),
        sg.In(),
        sg.FileBrowse(),

    ],[sg.Button("Ok")]]
buildfinish = [[sg.Text('If you see this message and the game did not launch for like 2 minutes after the message appeared, that means that build failed.')],[sg.Button('Ok')]]



# Create the window
window = sg.Window("SM64 pc builder", branchselect)


# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Ok" or event == sg.WIN_CLOSED:
        branchname=values[1]
        os.system('git clone "'+values[0]+'" "'+values[2]+'" --branch='+values[1])
        os.system('cp -r "'+values[3]+'/actors" "'+values[2]+'" && cp -r "'+values[3]+'/src" "'+values[2]+'"')
        repofolder=values[2]
        texturepack=values[4]
        window.close()
        window = sg.Window("baserom", baseromselect)
        
        while True:
            event, values = window.read()
            if event == 'Ok' or event == sg.WIN_CLOSED: 
                baseromfolder=values[0]
                window.close()
                window = sg.Window('build options', buildoptions)
                event, values = window.read()
                if event == 'Build' or event == sg.WIN_CLOSED:
                    buildflags = values[0]
                    print(buildflags)
                    window.close
                    break



    window.close()


    os.system('cp '+'"'+baseromfolder+'"'+" "+'"'+repofolder+'/baserom.us.z64"')
    os.system('cd "'+repofolder+'" && make '+buildflags)
    os.system('cp -r "'+texturepack+'/gfx" "'+repofolder+'/build/us_pc/res"')
    window = sg.Window('Build finished!', buildfinish)
    with open('builds.txt', 'r') as blist:
        builds = blist.read()
    with open ('builds.txt', 'w') as bwrite:
        bwrite.write(repofolder+'\n'+builds)
    os.system('./"'+repofolder+'/build/us_pc/sm64.us.f3dex2e"')



        

        



