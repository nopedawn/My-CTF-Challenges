from moviepy.editor import VideoFileClip, AudioFileClip

def add_audio_to_video(video_path, audio_path, output_path):
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)

    video = video.set_audio(audio)
    video.write_videofile(output_path, codec='libx264', audio_codec='aac')

    print(f"Audio berhasil ditambahkan ke video. Hasil disimpan sebagai {output_path}.")

video_path = 'output_video.mp4'
audio_path = 'audio.mp3'
output_path = 'video_with_audio.mp4'

add_audio_to_video(video_path, audio_path, output_path)
