from pydub import AudioSegment
from pydub.playback import play
from pydub.effects import normalize, low_pass_filter, high_pass_filter

def improve_audio_quality(input_file, output_file):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Normalize audio levels
    normalized_audio = normalize(audio)

    # Apply low-pass and high-pass filters
    filtered_audio = high_pass_filter(low_pass_filter(normalized_audio, 500), 1000)

    # Export the improved audio
    filtered_audio.export(output_file, format="wav")

    print("Audio quality improvement complete.")

# Example usage
input_file = "input_audio.wav"
output_file = "improved_audio.wav"
improve_audio_quality(input_file, output_file)