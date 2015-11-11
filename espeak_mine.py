#!/usr/bin/env python2
import subprocess as sp
import time



def  question():
    sp.call("espeak 'Welcome to the question maker, do you want to play? '", shell=True)
    time.sleep(1.5)
    sp.call("espeak ' All questions will be fifty points'",shell=True) 
    time.sleep(1.5)
    sp.call("espeak 'if you got them right '",shell=True)
    time.sleep(1.5)
    sp.call("espeak 'you will have five seconds to answer the questions'",shell=True)
    time.sleep(1.5)
    sp.call("espeak 'First question, name one MLG item '",shell=True)
    time.sleep(3)
    sp.call("espeak 'Question one done, the answers could  be three sixty no scope'",shell=True)
    time.sleep(1.5)
    sp.call("espeak 'Or illuminati, or oooh baby a triple and airhorns and baby lumi'",shell=True)
    time.sleep(1.5)
    sp.call("espeak 'If you got this right, good job, thheeeeeeeee end baba'",shell=True)

def name():
    sp.call("espeak 'Hello, my name is espeak'",shell=True)
    time.sleep(1.5)
    sp.call("espeak 'What is your name?'",shell=True)
    time.sleep(0.5)
    name = input("espeak 'What is your name? '")
    time.sleep(0.5)
    sp.call("espeak 'Hello, '",shell=True)
    time.sleep(0.25)
    sp.call("espeak" + " '" + name + "'",shell=True)

