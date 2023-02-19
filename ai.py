import os
import playsound
import speech_recognition as ai
from random import randrange
from gtts import gTTS
import pyttsx3

nome_in = ["come ti chiami", "chi sei"]                          
nome_out = ["Il mio nome..è..Christina", "Sono..Christina"]
speciale_in = ["organizzazione","El psy congroo"]
speciale_out = ["Bentornato...Ocarin"]
battuta_in = ["raccontami una barzelletta", "dimmi una barzelletta", "fammi ridere", "fammi divertire"]
battuta_out = ["Che cosa hanno in comune un televisore e una formica?......Le antenne!", "Qual è la pianta più puzzolente?......Quella dei piedi!",
               "Che cos'è una zebra?......Un cavallo evaso dal carcere!", "Sapete perché il pomodoro non riesce a dormire?......Perché l’insalata...russa!",
               "Qual'è il colmo per un matematico?......Abitare in una frazione di potenza", "Se sentite delle sirene avvicinarsi non vi preoccupate.......ho appena arrestato il PC!",
               "Due tirchi scommettono 20 euro per chi resta più a lungo sott'acqua:......ritrovati i due cadaveri!",
               "Un fantasmino si sveglia perché aveva fatto un incubo, va dalla mamma e la mamma gli dice: madonna tesoro! sei pallidissimo",
               "Che cosa fa un pittore al polo nord?......un affresco!"]

engine = pyttsx3.init()

#inizio funzione
#in questa funzione andrà a settare la API di google con la lingua italiana e creerà un file mp3 da rimuovere se già esiste altrimenti verrà creato per memorizzare ciò che dovrà dire

def speak(text):
    tts = gTTS(text = text, lang = "it")
    filename = "voce.mp3"
    if os.path.exists(filename):
        os.remove(filename)
    tts.save(filename)
    playsound.playsound(filename)

#fine funzione

#inizio funzione
#in questa funzione prenderemo come input il microfono e assocerà ciò detto da noi a una variabile audio e poi mi stamperà a video ciò che ho detto o un errore

def get_audio():
    r = ai.Recognizer()
    with ai.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 1)                 #riduce i rumori ambientali
        audio = r.listen(source)
        result = ""
        try:
            result = r.recognize_google(audio, language="it")
            print(result)
        except Exception as e:
            engine.say("Non..ho..capito")
            engine.runAndWait()
    return result

#fine funzione

#qui assegnerà ciò detto da noi in una variabile e prenderà randomicamente dalla lista delle risposte una risposte e la assocerà a una variabile e parlerà

while True:
    text_in = get_audio()
    text_in = text_in.lower()
    text_out = text_in
    if text_in != None and text_in != "":
            if text_in in nome_in:
                ran = randrange(len(nome_out))
                text_out = nome_out[ran]
                engine.say(text_out)
                engine.runAndWait()
            elif text_in in speciale_in:
                ran = randrange(len(speciale_out))
                text_out = speciale_out[ran]
                engine.say(text_out)
                engine.runAndWait()
            elif text_in in battuta_in:
                ran = randrange(len(battuta_out))
                text_out = battuta_out[ran]
                engine.say(text_out)
                engine.runAndWait()
            else:
                engine.say("Purtroppo non ho ancora imparato a rispondere a questa domanda...scusami")
                engine.runAndWait()
