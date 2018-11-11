
import shutil
import os
#from BackEnd.Controller import ConnectionToNeo4j, vari, AyeshAudioRecorder
from Controller import ConnectionToNeo4j, vari, AyeshAudioRecorder


def silence_detect1(QNumber):

    #Passing parameters
    sessionNumber = vari.sessionId
    userId = vari.userId


    outputFile = AyeshAudioRecorder.Audio_recording()


    from pydub import AudioSegment, silence
    path = '../Database/Audio/'+outputFile
    print(path)
    # os.chdir(path)
    # files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    # oldest = files[0]
    # print(oldest)
    # path1 = path + '/' + oldest
    # print(path1)
    myaudio = AudioSegment.from_wav(path)  # 'audio/output14.wav'

    silence = silence.detect_silence(myaudio, min_silence_len=1000, silence_thresh=-30)
    # start and the end point of silence and display number of silent part in brackets
    # convert to sec
    silence = [((start / 1000), (stop / 1000)) for start, stop in silence]
    #1 Start and end points of silence parts in milliseconds
    print('#1 Start and end points of silence parts in milliseconds')
    print(silence)

    #2 Gap between start and the end point of the each silent part of the audio
    silence_gap = [(((stop) - (start)) / 1000) for start, stop in silence]
    print('#2 Gap between start and the end point of the each silent part of the audio')
    print(silence_gap)

    #3 identify silence parts with more than 3 milliseconds
    silence_gap2 = sorted(i for i in silence_gap if i >= 0.003)
    print('#3 identify silence parts with more than 3 milliseconds')
    print(silence_gap2)

    #convert the silent parts with milisecons to seconds
    silence_gap_list = [i * 1000 for i in silence_gap2]
    #4 silence gaps with three decimal places
    myFormattedList2 = ['%.3f' % elem for elem in silence_gap_list]
    print('#4 silent gaps in seconds with 3 decimal places')
    print(myFormattedList2)

    totalSilent=list(map(float,myFormattedList2))
    sumOfsilents = sum(totalSilent)
    print('#5 summation of all silent parts that are having more than 3 seconds')
    print(sumOfsilents)
    marksForsilents=round(25-(sumOfsilents*1.25))
    print('#6 marks for the silent part for a question')
    print(marksForsilents)

#After detecting the silence part of the audio clip it willmove to another folder vikum shold get the audio clip from that new folder.
    #path2 = 'D:/New Research/SmartInterviewer-Code/BackEnd/Database/movedAudio'
    #shutil.move(path1, path2)

    #passed from sarindi



    #------------------------------------------------------------
    string = "voiceq"
    questionNumber =QNumber
    questionOutput = string + str(questionNumber)
    print(questionOutput)
    print(type(questionOutput))

    #----------------------------------------------------
    qnumber = questionOutput
    voiceMark = str(marksForsilents)

    ConnectionToNeo4j.getQuestionNumberToSave(userId,sessionNumber,qnumber)




    ConnectionToNeo4j.saveVoiceMarks(userId,sessionNumber,qnumber, voiceMark)

    print(ConnectionToNeo4j.saveVoiceMarks(userId,sessionNumber,qnumber, voiceMark))

# silence_detect1(1)
