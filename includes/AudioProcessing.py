import moviepy.editor as mp


AUDIO_PATH = './static/downloaded-audio.wav'
VIDEO_PATH = './static/downloaded-video.mp4'
class AudioProcessing:
    def __init__(self) -> None:
        pass
    
    def get_audio():
        clip = mp.VideoFileClip(filename=VIDEO_PATH)
        
        clip.audio.write_audiofile(AUDIO_PATH)
        