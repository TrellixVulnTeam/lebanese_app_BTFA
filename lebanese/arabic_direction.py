import kivy.app
import kivy.uix.label


#text_to_be_reshaped = ''
#reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)

#def left_arrow_press()
def arabic_left(current_string, current_key):
    new_string = current_string
    if len(new_string) != None:

    #if new_string == old_string:

        new_string = new_string.insert(0, current_key)
        return_string = "".join(new_string)
        return return_string
    #old_string = new_string


"""
import arabic_reshaper
import bidi
from bidi.algorithm import get_display
def get_mirrored_arabic(arabic):
    arabic_words = arabic
    arabic_memory = arabic

    if arabic == None:
        return ""
    if arabic != None and len(arabic) > 0:
        arabic_words = arabic[len(arabic)-1]
        mytext = bidi.algorithm.get_display(arabic_reshaper.reshape(arabic_words))
        mytext = arabic_memory + mytext
        return mytext
    #reshaped_text = arabic_reshaper.reshape(arabic_words)
    #bidi_text = get_display(reshaped_text)
    #return bidi_text

    mytext = bidi.algorithm.get_display(arabic_reshaper.reshape(arabic_words))
    mytext = arabic_memory + mytext
    return mytext

"""
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