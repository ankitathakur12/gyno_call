import subprocess
import sys
import shutil
import os
# from ..gynochat.settings import upload_video_path, result_dir, BASE_DIR
from django.conf import settings


# envDir = os.path.sys.executable.replace('.exe', '')
# directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(directory)


# directory = r"C:\Users\ankit\PycharmProjects\GynoCall"
# directory = os.path.join(settings.BASE_DIR)
# print(directory)
parent_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
print(parent_directory )


def f(face_file_path, audio_file_path):
    # if result_dir.exists():
    #     shutil.rmtree(result_dir)
    # os.mkdir(result_dir)



    # ffmpeg -i lip_sync_1_aud.mp4 -ab 160k -ac 2 -ar 44100 -vn lip_sync_1_aud.wav
    subprocess.run(['ffmpeg', '-i', str(audio_file_path),
                    '-ab', '180k', '-ac', '2', '-ar', '44100', '-vn',
                    str('sample_data/input_audio.wav')], capture_output=False)


    # cd Wav2Lip && python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face "/content/lip_sync_1_face.mp4" --audio "/content/lip_sync_1_aud.wav"
    # os.chdir('http://127.0.0.1:8000/Wav2Lip')

    os.chdir(parent_directory)


    subprocess.run(["new_env/Scripts/python", 'gynochat/Wav2Lip/inference.py', '--checkpoint_path',
                    'gynochat/Wav2Lip/checkpoints/wav2lip_gan.pth', '--face',
                    str(face_file_path), '--audio', str(audio_file_path), '--outfile', str('gynochat/static/result_voice.mp4'),'--fps', '60'],
                    capture_output=False)

    file_name = 'input_audio.wav'
    file_path = os.path.join(settings.BASE_DIR, 'sample_data', file_name)
    # file_path = "sample_data/input_audio.wav"
    if os.path.isfile(file_path):
        os.remove(file_path)


    return 'done!'