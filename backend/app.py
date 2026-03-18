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






# from flask import Flask, request, jsonify, send_from_directory
# from flask_cors import CORS
# from pydub import AudioSegment
# from pydub.effects import normalize
# from pydub.utils import which
# import os
# import numpy as np
# import noisereduce as nr

# AudioSegment.converter = which("ffmpeg")
# AudioSegment.ffprobe = which("ffprobe")

# app = Flask(__name__)
# CORS(app)

# UPLOAD_FOLDER = "uploads"
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# @app.route("/")
# def home():
#     return "Backend Running Successfully!"

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
#         audio = AudioSegment.from_file(input_path)
#         audio = normalize(audio)

#         samples = np.array(audio.get_array_of_samples())

#         if audio.channels == 2:
#             samples = samples.reshape((-1, 2))
#             mono = samples.mean(axis=1)
#         else:
#             mono = samples

#         mono = mono.astype(np.float32)

#         noise_sample = mono[:int(0.5 * audio.frame_rate)]

#         reduced_noise = nr.reduce_noise(
#             y=mono,
#             y_noise=noise_sample,
#             sr=audio.frame_rate,
#             prop_decrease=0.9
#         )

#         reduced_noise = np.clip(reduced_noise, -32768, 32767).astype(np.int16)

#         enhanced_audio = AudioSegment(
#             reduced_noise.tobytes(),
#             frame_rate=audio.frame_rate,
#             sample_width=audio.sample_width,
#             channels=1
#         )

#         output_filename = f"enhanced_{os.path.splitext(file.filename)[0]}.wav"
#         output_path = os.path.join(UPLOAD_FOLDER, output_filename)
#         enhanced_audio.export(output_path, format="wav")

#         return jsonify({
#             "message": "Audio enhanced successfully!",
#             "file": output_filename
#         })

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route("/uploads/<filename>")
# def download_file(filename):
#     return send_from_directory(UPLOAD_FOLDER, filename)

# if __name__ == "__main__":
#     app.run(debug=True)








# from flask import Flask, request, jsonify, send_from_directory
# from flask_cors import CORS
# from pydub import AudioSegment
# from pydub.effects import normalize
# from pydub.utils import which
# import os
# import numpy as np
# import noisereduce as nr
# import uuid

# # Configure ffmpeg
# AudioSegment.converter = which("ffmpeg")
# AudioSegment.ffprobe = which("ffprobe")

# app = Flask(__name__)
# CORS(app)

# UPLOAD_FOLDER = "uploads"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# @app.route("/")
# def home():
#     return "Backend Running Successfully!"


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

#         # Normalize volume first
#         audio = normalize(audio)

#         # Convert to mono
#         audio = audio.set_channels(1)

#         sample_rate = audio.frame_rate

#         # Convert to numpy array
#         samples = np.array(audio.get_array_of_samples()).astype(np.float32)
#         samples /= 32768  # normalize to -1.0 to 1.0

#         # Automatically detect quiet parts as noise
#         threshold = 0.02  # adjust if needed
#         noise_sample = samples[np.abs(samples) < threshold]
#         if len(noise_sample) == 0:
#             noise_sample = samples[:sample_rate]  # fallback to first second

#         # Apply noise reduction
#         reduced_noise = nr.reduce_noise(
#             y=samples,
#             y_noise=noise_sample,
#             sr=sample_rate,
#             prop_decrease=0.8,
#             stationary=True
#         )

#         # Convert back to int16
#         reduced_noise = (reduced_noise * 32767).astype(np.int16)

#         # Convert to AudioSegment
#         enhanced_audio = AudioSegment(
#             reduced_noise.tobytes(),
#             frame_rate=sample_rate,
#             sample_width=2,
#             channels=1
#         )

#         # Remove hum/hiss
#         enhanced_audio = enhanced_audio.high_pass_filter(120).low_pass_filter(8000)

#         # Boost voice safely
#         peak = max(enhanced_audio.max, 1)
#         gain = min(5, 32767 / peak)  # avoid clipping
#         enhanced_audio += gain

#         # Save enhanced audio with unique filename
#         output_filename = f"enhanced_{uuid.uuid4().hex}.wav"
#         output_path = os.path.join(UPLOAD_FOLDER, output_filename)
#         enhanced_audio.export(output_path, format="wav")

#         return jsonify({
#             "message": "Audio enhanced successfully!",
#             "file": output_filename
#         })

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# @app.route("/uploads/<filename>")
# def download_file(filename):
#     return send_from_directory(UPLOAD_FOLDER, filename)


# if __name__ == "__main__":
#     app.run(debug=True)







# from flask import Flask, request, jsonify, send_from_directory
# from flask_cors import CORS
# from pydub import AudioSegment
# from pydub.effects import normalize
# from pydub.utils import which
# import os
# import numpy as np
# import noisereduce as nr
# import uuid

# # Configure ffmpeg
# AudioSegment.converter = which("ffmpeg")
# AudioSegment.ffprobe = which("ffprobe")

# app = Flask(__name__)
# CORS(app)

# UPLOAD_FOLDER = "uploads"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# @app.route("/")
# def home():
#     return "Backend Running Successfully!"


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

#         # Normalize volume first
#         audio = normalize(audio)

#         # Convert to mono
#         audio = audio.set_channels(1)

#         sample_rate = audio.frame_rate

#         # Convert to numpy array (-1 to 1)
#         samples = np.array(audio.get_array_of_samples()).astype(np.float32)
#         samples /= 32768

#         # --- Step 1: Detect quiet parts automatically as noise ---
#         threshold = 0.02
#         noise_sample = samples[np.abs(samples) < threshold]
#         if len(noise_sample) == 0:
#             noise_sample = samples[:sample_rate]  # fallback

#         # --- Step 2: Apply stronger noise reduction ---
#         reduced_noise = nr.reduce_noise(
#             y=samples,
#             y_noise=noise_sample,
#             sr=sample_rate,
#             prop_decrease=0.9,   # stronger effect
#             stationary=True
#         )

#         # --- Step 3: Convert back to AudioSegment ---
#         reduced_noise = (reduced_noise * 32767).astype(np.int16)
#         enhanced_audio = AudioSegment(
#             reduced_noise.tobytes(),
#             frame_rate=sample_rate,
#             sample_width=2,
#             channels=1
#         )

#         # --- Step 4: Multi-stage filtering ---
#         enhanced_audio = enhanced_audio.high_pass_filter(120).low_pass_filter(8000)

#         # --- Step 5: Optional volume boost safely ---
#         peak = max(enhanced_audio.max, 1)
#         gain = min(3, 32767 / peak)  # avoid clipping
#         enhanced_audio += gain

#         # --- Step 6: Save enhanced audio ---
#         output_filename = f"enhanced_{uuid.uuid4().hex}.wav"
#         output_path = os.path.join(UPLOAD_FOLDER, output_filename)
#         enhanced_audio.export(output_path, format="wav")

#         return jsonify({
#             "message": "Audio enhanced successfully!",
#             "file": output_filename
#         })

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# @app.route("/uploads/<filename>")
# def download_file(filename):
#     return send_from_directory(UPLOAD_FOLDER, filename)


# if __name__ == "__main__":
#     app.run(debug=True)





# from flask import Flask, request, jsonify, send_from_directory
# from flask_cors import CORS
# from pydub import AudioSegment
# from pydub.effects import normalize, compress_dynamic_range
# from pydub.utils import which
# import os
# import numpy as np
# import noisereduce as nr
# import uuid

# AudioSegment.converter = which("ffmpeg")
# AudioSegment.ffprobe = which("ffprobe")

# app = Flask(__name__)
# CORS(app)

# UPLOAD_FOLDER = "uploads"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route("/")
# def home():
#     return "Backend Running Successfully!"

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

#         # Convert to mono for easier processing
#         audio = audio.set_channels(1)

#         # Normalize volume first
#         audio = normalize(audio)

#         sample_rate = audio.frame_rate

#         # Convert to numpy array
#         samples = np.array(audio.get_array_of_samples()).astype(np.float32)
#         samples /= 32768

#         # --- Adaptive noise reduction ---
#         reduced_noise = nr.reduce_noise(
#             y=samples,
#             sr=sample_rate,
#             stationary=False,  # adaptive, handles changing noise
#             prop_decrease=0.9
#         )

#         # Convert back to AudioSegment
#         reduced_noise = (reduced_noise * 32767).astype(np.int16)
#         enhanced_audio = AudioSegment(
#             reduced_noise.tobytes(),
#             frame_rate=sample_rate,
#             sample_width=2,
#             channels=1
#         )

#         # --- Apply filters (voice clarity) ---
#         enhanced_audio = enhanced_audio.high_pass_filter(300).low_pass_filter(4000)

#         # --- Compress to make speech prominent ---
#         enhanced_audio = compress_dynamic_range(enhanced_audio, threshold=-20.0, ratio=2.0)

#         # --- Final normalization ---
#         enhanced_audio = normalize(enhanced_audio)

#         # Save enhanced audio
#         output_filename = f"enhanced_{uuid.uuid4().hex}.wav"
#         output_path = os.path.join(UPLOAD_FOLDER, output_filename)
#         enhanced_audio.export(output_path, format="wav")

#         return jsonify({
#             "message": "Audio enhanced successfully!",
#             "file": output_filename
#         })

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route("/uploads/<filename>")
# def download_file(filename):
#     return send_from_directory(UPLOAD_FOLDER, filename)

# if __name__ == "__main__":
#     app.run(debug=True)







# from flask import Flask, request, jsonify, send_from_directory
# from flask_cors import CORS
# from pydub import AudioSegment
# from pydub.effects import normalize, compress_dynamic_range
# from pydub.utils import which
# import os
# import numpy as np
# import noisereduce as nr
# import uuid

# AudioSegment.converter = which("ffmpeg")
# AudioSegment.ffprobe = which("ffprobe")

# app = Flask(__name__)
# CORS(app)

# UPLOAD_FOLDER = "uploads"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route("/")
# def home():
#     return "Backend Running Successfully!"

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
#         audio = audio.set_channels(1)  # mono
#         audio = normalize(audio)

#         sample_rate = audio.frame_rate
#         samples = np.array(audio.get_array_of_samples()).astype(np.float32) / 32768

#         # --- Multi-pass adaptive noise reduction ---
        
#         reduced_noise = nr.reduce_noise(
#     y=samples,
#     sr=sample_rate,
#     stationary=False,
#     prop_decrease=0.6
# )
#         # --- Noise gate (remove very quiet hiss) ---
#         threshold = 0.01
#         reduced_noise_2[np.abs(reduced_noise_2) < threshold] = 0

#         # Convert back to AudioSegment
#         reduced_noise_2 = (reduced_noise_2 * 32767).astype(np.int16)
#         enhanced_audio = AudioSegment(
#             reduced_noise_2.tobytes(),
#             frame_rate=sample_rate,
#             sample_width=2,
#             channels=1
#         )

#         # --- Filter for human speech clarity ---
#         enhanced_audio = enhanced_audio.high_pass_filter(300).low_pass_filter(4000)

#         # --- Compress and normalize ---
#         enhanced_audio = compress_dynamic_range(enhanced_audio, threshold=-20.0, ratio=2.0)
#         enhanced_audio = normalize(enhanced_audio)

#         # Save enhanced audio
#         output_filename = f"enhanced_{uuid.uuid4().hex}.wav"
#         output_path = os.path.join(UPLOAD_FOLDER, output_filename)
#         enhanced_audio.export(output_path, format="wav")

#         return jsonify({
#             "message": "Audio enhanced successfully!",
#             "file": output_filename
#         })

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route("/uploads/<filename>")
# def download_file(filename):
#     return send_from_directory(UPLOAD_FOLDER, filename)

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from pydub import AudioSegment
from pydub.effects import normalize
from pydub.utils import which
import noisereduce as nr
import numpy as np
import soundfile as sf
import os
import uuid
import traceback

# configure ffmpeg for pydub
AudioSegment.converter = which("ffmpeg")
AudioSegment.ffprobe = which("ffprobe")

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


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

    try:
        # save uploaded file
        raw_filename = f"{uuid.uuid4().hex}_{file.filename}"
        raw_path = os.path.join(UPLOAD_FOLDER, raw_filename)

        file.save(raw_path)
        print("Uploaded:", raw_path)

        # load audio
        audio = AudioSegment.from_file(raw_path)

        # convert to mono + correct sample rate
        audio = audio.set_channels(1)
        audio = audio.set_frame_rate(48000)

        # normalize volume
        audio = normalize(audio)

        # temporary wav file
        temp_input = os.path.join(UPLOAD_FOLDER, f"in_{uuid.uuid4().hex}.wav")

        audio.export(
            temp_input,
            format="wav",
            parameters=["-acodec", "pcm_s16le"]
        )

        # read waveform
        data, rate = sf.read(temp_input)

        # stronger noise reduction
        reduced_noise = nr.reduce_noise(
            y=data,
            sr=rate,
            prop_decrease=1.0
        )

        temp_output = os.path.join(UPLOAD_FOLDER, f"clean_{uuid.uuid4().hex}.wav")

        sf.write(temp_output, reduced_noise, rate)

        # load cleaned audio
        enhanced_audio = AudioSegment.from_wav(temp_output)

        # speech frequency filters
        enhanced_audio = enhanced_audio.high_pass_filter(100)
        enhanced_audio = enhanced_audio.low_pass_filter(7500)

        # dynamic compression
        enhanced_audio = enhanced_audio.compress_dynamic_range(
            threshold=-20.0,
            ratio=4.0
        )

        # normalize loudness
        enhanced_audio = normalize(enhanced_audio)

        # save final output
        output_filename = f"enhanced_{uuid.uuid4().hex}.wav"
        output_path = os.path.join(UPLOAD_FOLDER, output_filename)

        enhanced_audio.export(output_path, format="wav")

        # cleanup
        if os.path.exists(temp_input):
            os.remove(temp_input)

        if os.path.exists(temp_output):
            os.remove(temp_output)

        return jsonify({
            "message": "Audio enhanced successfully!",
            "file": output_filename
        })

    except Exception as e:

        error = traceback.format_exc()
        print(error)

        return jsonify({
            "error": str(e),
            "trace": error
        }), 500


@app.route("/uploads/<filename>")
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)