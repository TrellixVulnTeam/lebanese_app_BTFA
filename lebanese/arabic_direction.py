import kivy.app
import kivy.uix.label


#text_to_be_reshaped = ''
#reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)

#def left_arrow_press()


import arabic_reshaper
from bidi.algorithm import get_display
def get_mirrored_arabic(arabic):
    arabic_words = arabic
    reshaped_text = arabic_reshaper.reshape(arabic_words)
    bidi_text = get_display(reshaped_text)
    return bidi_text

#def get_mirrored_arabic(arabic):
 #   arabic_words = arabic
    #print(arabic_words)
 #   reshaped_text = arabic_reshaper.reshape(arabic_words)
#    bidi_text = bidi.algorithm.get_display(reshaped_text)
  #  return bidi_text



##import arabic_reshaper
#import bidi.algorithm
#class TestApp(kivy.app.App):
 #   def build(self):
  #      reshaped_text = arabic_reshaper.reshape("بسم الله")
   #     bidi_text = bidi.algorithm.get_display(reshaped_text)
    #    return kivy.uix.label.Label(text=bidi_text, font_name="font/arial")
#
#testApp = TestApp()
#testApp.run()