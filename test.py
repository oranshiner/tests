from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os

# Set folder path
folder_path = "C:\\Users\\HOME\\Desktop\\Projects\\AutoVideo\\samples"

# Get all video and audio files
video_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]
audio_files = [f for f in os.listdir(folder_path) if f.endswith('.mp3')]

# Load audio
audio = AudioFileClip(os.path.join(folder_path, audio_files[0]))

# Load and process videos
video_clips = []
for video_file in video_files:
    clip = VideoFileClip(os.path.join(folder_path, video_file))
    clip = clip.set_audio(audio.subclip(0, clip.duration))  # Set audio to the video
    video_clips.append(clip)

# Concatenate and export
final_video = concatenate_videoclips(video_clips)
final_video = final_video.set_audio(audio.subclip(0, final_video.duration))  # Final audio setting
final_video.write_videofile("final_video.mp4", audio_codec="aac")