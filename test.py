from gtts import gTTS

print('11')
tts = gTTS(text = '요즈음 들어 활동량이나 의욕이 많이 떨어지셨습니까?', lang = 'ko', slow = False)
tts.save('survey_2.mp3')