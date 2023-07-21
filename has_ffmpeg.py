from shutil import which

def has_ffmpeg():
    return which("ffmpeg") is not None
