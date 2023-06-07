from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from gtts import gTTS
from os import listdir, path
import numpy as np
from .forms import FileForm
import os
import shutil
from .functions import f
import http
import openai
import os
from dotenv import load_dotenv, find_dotenv
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

conn = http.client.HTTPSConnection("api.openai.com")
openai.api_key = os.getenv('CHAT_GPT_KEY')


# openai.api_key = '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'


class Newchat(TemplateView):
    template_name ='chat.html'


    def get(self, request):
        print(request)
        gyno_name = "Dr. Aspi Arora"
        first_response = "Greetings! I'm here to assist you. Please feel free to ask any questions you may have. "
        context = {"gyno_name":gyno_name,"first_response":first_response}
        return render(request, self.template_name, context)

    def post(self, request):
        print(request)

        prompt = request.POST['prompt'] #+ str("\n\n###\n\n")
        print(prompt)
        response = openai.ChatCompletion.create(
            model= "gpt-3.5-turbo",
            temperature=1,
            max_tokens=100 ,
            top_p=1,
            frequency_penalty=0.75,
            presence_penalty=0,
            messages=[
                {"role": "system", "content": "You are a helpful asistant."},
                {"role": "user", "content": "Answer under 50 words: "+prompt},
            ]
        ).choices[0]["message"]['content']
        # response = "Greetings! I'm here to assist you. Please feel free to ask any questions you may have. "
        print(response)
        directory_path = os.path.join(settings.BASE_DIR, 'sample_data')
        if os.path.exists(directory_path):
            print("folder is exists")
        else:
            print("folder is not exists")


        tts = gTTS(response)
        print(tts)


        output_file = os.path.join(settings.BASE_DIR, 'sample_data', 'input_audio.wav')

        tts.save(output_file)
        print("New TTS output saved as", output_file)

        context = {'response_by_AI': response}
        print(context)

        if request.method == 'POST':

            face_file_path = 'gynochat/sample_data/input_video.mp4'
            audio_file_path = 'gynochat/sample_data/input_audio.wav'
            print('_' * 10, f(face_file_path, audio_file_path))


        return JsonResponse(context)





