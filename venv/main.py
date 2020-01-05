"""program for translating arabic characters into roman arabic script"""

import os

#importing pydub for audio
from pydub import AudioSegment
from pydub.playback import play

#importing lebanese module stuff
from lebanese import breakdown_lebanese
from breakdown_lebanese import arabic_break_down
from lebanese import lebanese_to_roman
from lebanese_to_roman import arabic_to_roman_replace

#importing kivy stuff
import kivy
kivy.require('1.11.1') # replace with your current kivy version !
#from kivy.config import Config
#Config.set('modules', 'screen', 'phone_samsung_galaxy_s5')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.core.window import Window

import kivy

kivy.require('1.11.1')  # replace with your current kivy version !
# from kivy.config import Config
# Config.set('modules', 'screen', 'phone_samsung_galaxy_s5')
from kivy.app import App

class TranslatorWidget(Widget):
    lebanese_arabic_text_input = ObjectProperty()

    #import arabic_reshaper
    #from bidi.algorithm import get_display
    #def get_mirrored_arabic(arabic):
     #   arabic_words = arabic
      #  reshaped_text = arabic_reshaper.reshape(arabic_words)
       # bidi_text = get_display(reshaped_text)
        #return bidi_text

    #test_word = StringProperty("")
    #value = StringProperty("")

class MyApp(App):
    def build(self):
        Window.bind(on_key_down=self.key_action)
    def key_action(self, *args):
        print("got a key event: %s" % list(args))
        last_button = args[len(args)-2]
        print(last_button)
        #from lebanese.arabic_direction import get_mirrored_arabic
        #arabic_input = last_button
        #arabic_input = get_mirrored_arabic(arabic_input)
        #if last_button != None:
         #   Window.bind(on_key_down=self.key_action(<kivy.core.window.window_sdl2.WindowSDL object at 0x040431B8>, 276, 80, None, []))
            #force_left(<kivy.core.window.window_sdl2.WindowSDL object at 0x040431B8>, 276, 80, None, [])
    #def force_left(self, window, key, scancode, codepoint, modifiers):
     #   Window.bind(on_key_down=self.
      #      on_key_down= (self, window, key, scancode, codepoint, modifiers)
       #     return

    import arabic_reshaper
    from bidi.algorithm import get_display
    def get_mirrored_arabic(arabic):
        arabic_words = arabic
        reshaped_text = arabic_reshaper.reshape(arabic_words)
        bidi_text = get_display(reshaped_text)
        return bidi_text
   # def build(self):
     #   return TranslatorWidget()

if __name__ == '__main__':
    MyApp().run()
