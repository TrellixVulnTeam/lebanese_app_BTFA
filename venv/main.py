"""program for translating arabic characters into roman arabic script"""

#ADD ًَ ُ ٌ ٍ ِ ْ ّ SUPPORT

import os

#importing pydub for audio
from pydub import AudioSegment
from pydub.playback import play

#importing lebanese module stuff
from lebanese import breakdown_lebanese
from breakdown_lebanese import arabic_break_down
from lebanese import lebanese_to_roman
from lebanese_to_roman import arabic_to_roman_replace


import kivy.app
import kivy.uix.label
import kivy.uix.button
import kivy.uix.textinput
import kivy.uix.boxlayout
import kivy.uix.image
import kivy.uix.floatlayout
import arabic_reshaper
import bidi.algorithm
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty, StringProperty

class Ar_text(TextInput):
    max_chars = NumericProperty(1000000)  # maximum character allowed
    str = StringProperty()

    def __init__(self, **kwargs):
        super(Ar_text, self).__init__(**kwargs)
        self.text = bidi.algorithm.get_display(arabic_reshaper.reshape("اطبع شيئاً"))

    def insert_text(self, substring, from_undo=False):
        if not from_undo and (len(self.text) + len(substring) > self.max_chars):
            return

        self.str = self.str+substring
        self.text = bidi.algorithm.get_display(arabic_reshaper.reshape(self.str))
        substring = ""
        super(Ar_text, self).insert_text(substring, from_undo)
        print("A", self.str)

    def do_backspace(self, from_undo=False, mode='bkspc'):
        self.str = self.str[0:len(self.str)-1]
        self.text = bidi.algorithm.get_display(arabic_reshaper.reshape(self.str))
        print("B", self.str)

class MyApp(kivy.app.App):

    def build(self):

        #getting float_layout
        float_layout = kivy.uix.floatlayout.FloatLayout()
        background_image = kivy.uix.image.Image(source='C:/Users/natha/PycharmProjects/translator/venv/images/background.png')
        background_image.allow_stretch = True
        float_layout.add_widget(background_image)


        #boxLayout = kivy.uix.boxlayout.BoxLayout(orientation="vertical")
        # label = kivy.uix.label.Label(text=bidi_text, font_name="arial")
        #boxLayout.add_widget(label)

        """def check_text(self):
            if first_typed != "":
                print("testing")
                def set_last_text(self, *args):
                    last_typed = ""
                    last_typed = arabic_input
                    return print("another test")
            else:

                first_typed = ""

                return first_typed"""

    # reshaping arabic

        def get_bidi_text(self, *args):
            typed_text = "بسم اللَّه"
            reshaped_text = arabic_reshaper.reshape(typed_text)
            bidi_text = bidi.algorithm.get_display(reshaped_text)
            return bidi_text

        #on_text: self.your_variable = self.text

       # memory_var =

      #  def new_typed_text(self, *args):
       #     self.arabic_input = typed_text.text

         #   self.memory_var = self.arabic_input

        #arabic inputbox on_text=get_bidi_text(self) text=get_bidi_text(self)
        arabic_input = Ar_text(text=" ", font_name='C:/Users/natha/PycharmProjects/translator/lebanese/font/bahij yakout-regular.ttf', id='arabic_input', size_hint=(.8, .2),
                             pos_hint={'center_x': .5, 'center_y': .78}, multiline=False, font_size='22dp', text_language='ar_LB',
                             background_color=[1, 1, 1, 1], foreground_color=[0, 0, 0, 1])

        float_layout.add_widget(arabic_input)

        #adding the explainers
        characters_label = kivy.uix.label.Label(text='Characters', size_hint=[1,.2], font_size= '16dp', pos_hint={'x': -0.45, 'y': 0.19}, color=[0, 0, 1, 1])
        float_layout.add_widget(characters_label)

        current_bugs = kivy.uix.textinput.TextInput(text='CURRENT BUGS \n* \n*missing phenetics\n*\n*', font_name="C:/Windows/Fonts/arial.ttf", id='current_bugs', size_hint=(.3, .3),
                             pos_hint={'center_x': .8, 'center_y': .5}, multiline=True, font_size='16dp',
                             background_color=[1, 1, 1, 1], foreground_color=[0, 0, 0, 1])
        float_layout.add_widget(current_bugs)

        future_updates = kivy.uix.textinput.TextInput(text='FUTURE UPDATE\n*add arabic vowels \n*add phenetics\n*add dictionary of audio clips\n*mobile support', font_name="C:/Windows/Fonts/arial.ttf", id='future_updates', size_hint=(.3, .3),
                             pos_hint={'center_x': .2, 'center_y': .5}, multiline=True, font_size='16dp',
                             background_color=[1, 1, 1, 1], foreground_color=[0, 0, 0, 1])
        float_layout.add_widget(future_updates)

        #adding arabic label at top of screen
        arabic_label = kivy.uix.label.Label(text="Input arabic word to have it translated: ", size_hint=[1, .2], font_size='24dp',
                                            pos_hint={'x': 0, 'y': .8}, font_name='C:/Windows/Fonts/arial.ttf')
        float_layout.add_widget(arabic_label)

        #adding the output box that the translated arabic goes to.
        arabic_output_box = Ar_text(size_hint=[.8, .2], pos_hint={'center_x': .5, 'center_y': .22}, multiline=True, text="", font_size='22dp',
                                font_name='C:/Users/natha/PycharmProjects/translator/lebanese/font/bahij yakout-regular.ttf', id='output_box')
        float_layout.add_widget(arabic_output_box)



        # adding the button
        arabic_convert_button = kivy.uix.button.Button(text='Convert!', on_release=lambda x: arabic_translator(self),
                                                       size_hint=[.2, .3],
                                                       pos_hint={'center_x': .5, 'center_y': .5})
        float_layout.add_widget(arabic_convert_button)

        # this function is for the button below, its position is important so as to allow it to load
        def arabic_translator(self, *args):
            # print('test from the button!')
            press_enter = "\n"
            equals = " = "
            arabic_output = breakdown_lebanese.arabic_break_down(arabic_input.text) + press_enter
            arabic_output += lebanese_to_roman.arabic_to_roman_replace(arabic_input.text) + equals + arabic_input.text + press_enter
            arabic_output += lebanese_to_roman.get_word_breakdown(arabic_input.text) + press_enter
            arabic_output += lebanese_to_roman.get_new_roman_string(arabic_input.text) + press_enter
            print(arabic_output)

            arabic_output_box.text = arabic_output

            return arabic_output_box.text
            #= arabic_output

        #  if len(test_word) != None:
        #     text = arabic_input
        # on_text_validate:

        #


        # some_label.text = ' button pushed!'
        # button = kivy.uix.button.Button(text=bidi_text, font_name="arial")
        #boxLayout.add_widget(button)


        return float_layout
"""
    FloatLayout:
    font_name: 'ariel'
    # here is your background



# here you can add other widgets and place their positions, like so:






"""

if __name__ == '__main__':
    MyApp().run()