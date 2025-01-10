import speech_recognition as sr# it is a library that contanins various modules like recognizer,audio_file(for working with audio files) , microphone(for usig the microphone)


import os # it is a module that manages all the path in localy ststem . this module is used in line no 58
# The os module is a standard Python library for interacting with the operating system, providing functions to work with directories, files, and other system-level feature
import threading # it is a tool recog voice while playing video maily used to run multiple files

# pip install mtranslate
import mtranslate
from mtranslate import translate

# pip install colorma -> to used to beautify the terminal
from colorama import Fore,Style,init
#ting might not work out of the box in the terminal.

init(autoreset=True)  # This initializes the colorama library with autoreset=True.

def print_loop():
    while True: # infinite loop
        print(Fore.GREEN +Style.BRIGHT + " \rI am Listening...",end =" ",flush=True)
        print(Style.RESET_ALL,end="",flush=True)
        
        # This resets any text styles applied earlier (like Fore.GREEN) to ensure that the next print statement doesn't carry over the green color


def Translate_hindi_to_english(text):
    english_text = translate(text,"en-us")
    return english_text
    
#  english_text = translate(text, "en-us"): This calls the translate function from the mtranslate library, which translates the text from its original language to English ("en-us").
   
def listen():
    recognizer = sr.Recognizer()
    #  This creates an instance ( means creating an specific object from class ) of the Recognizer class from the speech_recognition library. The Recognizer class is used to process audio and convert it into text.
    # Recognizer is the class that is designed to recognize speech.
    # recognizer is the instance (object) of that class, meaning it's an actual working recognizer that you can use to recognize speech.
    
    recognizer.dynamic_energy_threshold = True

    recognizer.energy_threshold =40000
    recognizer.dynamic_energy_adjustment_damping = 0.010
    recognizer.dynamic_energy_ratio = 1.0
    # recognizer.pause_threshold = 0.3 # means jab me 0.3 sec ke ruki to pura ho gaya mera bolna 
    recognizer.operation_timeout = None
    recognizer.non_speaking_duration = 0.3 # jab tak bola nahi 
    recognizer.pause_threshold = .9  # Sets the pause duration in seconds that the recognizer waits for before considering speech to be finished



# When using with, you don’t need to manually open and close the microphone; it’s automatically cleaned up after use, even if errors occur.
    with sr.Microphone() as source :
        # source is a variable now i think 
        recognizer.adjust_for_ambient_noise(source,duration=0.5) # source is the microphone object that was defined earlier. It's passed to the adjust_for_ambient_noise method, so the recognizer knows from which source it should listen and adjust for background noise
        while True:
            print(Fore.GREEN + " I am Listning....",end="",flush=True)
            try:
                # agar me kush na bolu to error aega to us error ko na mane to 
                # (try) use kara 
                audio = recognizer.listen(source,timeout=None)
                print("\r" + Fore.LIGHTBLACK_EX + Style.BRIGHT + " Got it Sir ,  I am Recognising....", end="",flush=True) # here \r is used to overwrite the line I am listening
                recognizer_text = recognizer.recognize_google(audio).lower()
                if recognizer_text:
                    trans_text = Translate_hindi_to_english(recognizer_text)
                    print("\r" + Fore.LIGHTYELLOW_EX + " Mr. ManasModi :" +Fore.GREEN+Style.BRIGHT+ trans_text)
                    return trans_text
                else:
                    return ""
           
            except sr.UnknownValueError:
                recognizer_text = ""
            finally: # ye pakka honi chiye  
                print("\r", end="",flush=True)  # \r means erase

            os.system("cls" if os.name == "nt" else "clear") 
            # If the OS is Windows (os.name == "nt"), it uses the command "cls" to clear the terminal
            # So, when the code runs and reaches this point, it tells your terminal to clear the screen if you're using Windows. For other operating systems, such as Linux or macOS, the clear command is used instead:


            # threading part 
            listen_thread = threading.Thread(target=listen)
            print_thread = threading.Thread(target=print_loop)

            listen_thread.start()
            print_thread.start()
            listen_thread.join()
            print_thread.join()
while True:
     x=listen()
     if(x=='exit'):
        print('\r')
        break