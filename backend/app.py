# from flask import Flask, request, jsonify, send_from_directory
# from flask_cors import CORS
# from pydub import AudioSegment
# from pydub.effects import normalize
# from pydub.utils import which
# import os
# import numpy as np
# import noisereduce as nr

# # ================= FFmpeg Setup =================
# AudioSegment.converter = which("ffmpeg")
# AudioSegment.ffprobe = which("ffprobe")

# # ================= Flask Setup =================
# app = Flask(__name__)
# CORS(app)

# UPLOAD_FOLDER = "uploads"
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# # ================= Home Route =================
# @app.route("/")
# def home():
#     return "Backend Running Successfully!"

# # ================= Upload & Enhance Route =================
# @app.route("/upload", methods=["POST"])
# def upload_file():
#     if "audio" not in request.files:
#         return jsonify({"error": "No file uploaded"}), 400

#     file = request.files["audio"]
#     if file.filename == "":
#         return jsonify({"error": "Empty filename"}), 400

#     input_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(input_path)

#     try:
#         # Load audio
#         audio = AudioSegment.from_file(input_path)

#         # Normalize audio
#         audio = normalize(audio)

#         # Convert to numpy array
#         samples = np.array(audio.get_array_of_samples(), dtype=np.float32)

#         # Handle stereo audio
#         if audio.channels > 1:
#             samples = samples.reshape((-1, audio.channels))
#             samples = samples.mean(axis=1)  # mix to mono for noise reduction

#         # Take first 0.5 sec as noise profile
#         noise_sample = samples[:int(0.5 * audio.frame_rate)]

#         # Apply noise reduction
#         reduced_noise = nr.reduce_noise(
#             y=samples,
#             y_noise=noise_sample,
#             sr=audio.frame_rate,
#             prop_decrease=0.9
#         )

#         # Convert back to AudioSegment
#         enhanced_audio = AudioSegment(
#             reduced_noise.astype(np.int16).tobytes(),
#             frame_rate=audio.frame_rate,
#             sample_width=2,  # int16 = 2 bytes
#             channels=1 if audio.channels == 1 else audio.channels
#         )

#         # Save enhanced file
#         filename_without_ext = os.path.splitext(file.filename)[0]
#         output_filename = f"enhanced_{filename_without_ext}.wav"
#         output_path = os.path.join(UPLOAD_FOLDER, output_filename)
#         enhanced_audio.export(output_path, format="wav")

#         return jsonify({
#             "message": "Audio enhanced successfully!",
#             "file": output_filename
#         })

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# # ================= Download Route =================
# @app.route("/uploads/<filename>")
# def download_file(filename):
#     return send_from_directory(UPLOAD_FOLDER, filename)

# # ================= Run Server =================
# if __name__ == "__main__":
#     app.run(debug=True)


# #UPLOADS BUT SPPED INCREASES 






from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from pydub import AudioSegment
from pydub.effects import normalize
from pydub.utils import which
import os
import numpy as np
import noisereduce as nr

AudioSegment.converter = which("ffmpeg")
AudioSegment.ffprobe = which("ffprobe")

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def home():
    return "Backend Running Successfully!"

@app.route("/upload", methods=["POST"])
def upload_file():
    if "audio" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["audio"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_path)

    try:
        audio = AudioSegment.from_file(input_path)
        audio = normalize(audio)

        samples = np.array(audio.get_array_of_samples())

        if audio.channels == 2:
            samples = samples.reshape((-1, 2))
            mono = samples.mean(axis=1)
        else:
            mono = samples

        mono = mono.astype(np.float32)

        noise_sample = mono[:int(0.5 * audio.frame_rate)]

        reduced_noise = nr.reduce_noise(
            y=mono,
            y_noise=noise_sample,
            sr=audio.frame_rate,
            prop_decrease=0.9
        )

        reduced_noise = np.clip(reduced_noise, -32768, 32767).astype(np.int16)

        enhanced_audio = AudioSegment(
            reduced_noise.tobytes(),
            frame_rate=audio.frame_rate,
            sample_width=audio.sample_width,
            channels=1
        )

        output_filename = f"enhanced_{os.path.splitext(file.filename)[0]}.wav"
        output_path = os.path.join(UPLOAD_FOLDER, output_filename)
        enhanced_audio.export(output_path, format="wav")

        return jsonify({
            "message": "Audio enhanced successfully!",
            "file": output_filename
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/uploads/<filename>")
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)


