from pytube import YouTube

SAVE_PATH = './static/'

class VideoProcessing:
    def __init__(self) -> None:
        pass
    
    def get_video(url):
        try: 
            yt = YouTube(url) 
        except: 
            print("Connection Error") 
            
        yt = yt.streams.filter(file_extension='mp4').get_lowest_resolution()
        
        try: 
            yt.download(output_path=SAVE_PATH, filename='downloaded-video.mp4')
        except: 
            print("Some Error!") 
            
        print("Download Success")
                  
        
