'''
pip install kivy

pip install kivy.deps.sdl2

python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
'''

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()