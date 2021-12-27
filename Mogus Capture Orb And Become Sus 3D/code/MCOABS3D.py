import os
import tkinter as tk
import random
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Filename, WindowProperties
import simplepbr
import gltf

window = tk.Tk()

def run():
    SusOrb = os.environ.get("SusOrb")
    panda = Filename.fromOsSpecific(os.path.join(f'{SusOrb}\\sprites\\world\\world.gltf'))
    panda2 = Filename.fromOsSpecific(os.path.join(f'{SusOrb}\\sprites\\mogus\\mogus.gltf'))
    panda3 = Filename.fromOsSpecific(os.path.join(f'{SusOrb}\\sprites\\orb\\orb.gltf'))
    panda4 = Filename.fromOsSpecific(os.path.join(f'{SusOrb}\\sprites\\resbutton\\resbutton.gltf'))
    panda5 = Filename.fromOsSpecific(os.path.join(f'{SusOrb}\\sprites\\killbutton\\killbutton.gltf'))
    panda6 = Filename.fromOsSpecific(os.path.join(f'{SusOrb}\\sprites\\mogcorpse\\mogcorpse.gltf'))

    class MyApp(ShowBase):
        def __init__(self):
            ShowBase.__init__(self)
            props = WindowProperties()
            props.setTitle("Mogus Capture Orb And Become Sus 3D")
            self.win.requestProperties(props)
            self.setBackgroundColor(0, 0, 255)
            class World():
                self.scene = self.loader.loadModel(panda)
                self.scene.reparentTo(self.render)
                self.scene.setScale(7, 7, 1)
                self.scene.setPos(0, 50, 0)
            class Orb():
                a = random.randint(-30, 30)
                b = random.randint(20, 80)
                self.scene = self.loader.loadModel(panda3)
                self.scene.reparentTo(self.render)
                self.scene.setScale(1, 1, 1)
                self.scene.setPos(a, b, 1)
            class Res():
                self.scene = self.loader.loadModel(panda4)
                self.scene.reparentTo(self.render)
                self.scene.setScale(1, 1, 1)
                self.scene.setPos(-40, 50, 0)
            class Kill():
                self.scene = self.loader.loadModel(panda5)
                self.scene.reparentTo(self.render)
                self.scene.setScale(1, 1, 1)
                self.scene.setPos(40, 50, 0)
            simplepbr.init()

    app = MyApp()
    app.run()

button = tk.Button(
    window,
    text="Click to start!",
    command=run
)

button.pack()

window.mainloop()