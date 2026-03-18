// import { useState } from "react";
// import axios from "axios";
// import "./App.css";

// function App() {
//   const [file, setFile] = useState(null);
//   const [message, setMessage] = useState("");

//   const handleFileChange = (e) => {
//     setFile(e.target.files[0]);
//   };

//   const handleUpload = async () => {
//     if (!file) {
//       alert("Please select a file first!");
//       return;
//     }

//     const formData = new FormData();
//     formData.append("audio", file);

//     try {
//       const response = await axios.post(
//         "http://127.0.0.1:5000/upload",
//         formData,
//         {
//           headers: {
//             "Content-Type": "multipart/form-data",
//           },
//         }
//       );

//       setMessage(response.data.message);
//     } catch (error) {
//       console.error("Upload error:", error);
//       setMessage("Upload failed!");
//     }
//   };

//   return (
//     <div className="container">
//       <h1 className="title">Audio Enhancer</h1>

//       <input
//         type="file"
//         accept="audio/*"
//         onChange={handleFileChange}
//         className="file-input"
//       />

//       <br />

//       <button
//         onClick={handleUpload}
//         className="upload-btn"
//       >
//         Upload
//       </button>

//       <div className="message">{message}</div>
//     </div>
//   );
// }

// export default App;




// import { useState } from "react";
// import axios from "axios";
// import "./App.css";

// function App() {
//   const [file, setFile] = useState(null);
//   const [message, setMessage] = useState("");
//   const [downloadUrl, setDownloadUrl] = useState("");

//   const handleFileChange = (e) => {
//     setFile(e.target.files[0]);
//   };

//   const handleUpload = async () => {
//     if (!file) {
//       alert("Please select a file first!");
//       return;
//     }

//     const formData = new FormData();
//     formData.append("audio", file);

//     try {
//       const response = await axios.post(
//         "http://127.0.0.1:5000/upload",
//         formData,
//         {
//           headers: {
//             "Content-Type": "multipart/form-data",
//           },
//         }
//       );

//       setMessage(response.data.message);

//       // Create download link
//       setDownloadUrl(
//         `http://127.0.0.1:5000/uploads/${response.data.file}`
//       );

//     } catch (error) {
//       console.error("Upload error:", error);
//       setMessage("Upload failed!");
//     }
//   };

//   return (
//     <div className="container">
//       <h1 className="title">Audio Enhancer</h1>

//       <input
//         type="file"
//         accept="audio/*"
//         onChange={handleFileChange}
//         className="file-input"
//       />

//       <br />

//       <button onClick={handleUpload} className="upload-btn">
//         Upload
//       </button>

//       <div className="message">{message}</div>

//       {downloadUrl && (
//         <div>
//           <a href={downloadUrl} download>
//             Download Enhanced Audio
//           </a>
//         </div>
//       )}
//     </div>
//   );
// }

// export default App;



// import { useState } from "react";
// import axios from "axios";
// import "./App.css";

// function App() {
//   const [file, setFile] = useState(null);
//   const [message, setMessage] = useState("");
//   const [downloadUrl, setDownloadUrl] = useState("");

//   const handleFileChange = (e) => {
//     setFile(e.target.files[0]);
//   };

//   const handleUpload = async () => {
//     if (!file) {
//       alert("Please select a file first!");
//       return;
//     }

//     const formData = new FormData();
//     formData.append("audio", file);

//     try {
//       const response = await axios.post(
//         "http://127.0.0.1:5000/upload",
//         formData,
//         {
//           headers: { "Content-Type": "multipart/form-data" },
//         }
//       );

//       setMessage(response.data.message);
//       setDownloadUrl(`http://127.0.0.1:5000/uploads/${response.data.file}`);
//     } catch (error) {
//       console.error("Upload error:", error);
//       setMessage("Upload failed!");
//     }
//   };

//   return (
//     <div className="app-container">
//       <h1 className="title">Audio Enhancer</h1>

//       <div className="upload-container">
//         <input
//           type="file"
//           accept="audio/*"
//           onChange={handleFileChange}
//           className="file-input"
//         />
       
//         <button onClick={handleUpload} className="upload-btn">
//           Upload
//         </button>

//         {message && <div className="message">{message}</div>}

//         {downloadUrl && (
//           <a href={downloadUrl} download className="download-link">
//             Download Enhanced Audio
//           </a>
//         )}
//       </div>
//     </div>
//   );
// }

// export default App;









// import { useState } from "react";
// import axios from "axios";
// import "./App.css";

// function App() {
//   const [file, setFile] = useState(null);
//   const [message, setMessage] = useState("");
//   const [downloadUrl, setDownloadUrl] = useState("");

//   const handleFileChange = (e) => {
//     setFile(e.target.files[0]);
//   };

//   const handleUpload = async () => {
//     if (!file) {
//       alert("Please select a file first!");
//       return;
//     }

//     const formData = new FormData();
//     formData.append("audio", file);

//     try {
//       const response = await axios.post(
//         "http://127.0.0.1:5000/upload",
//         formData,
//         {
//           headers: { "Content-Type": "multipart/form-data" },
//         }
//       );

//       setMessage(response.data.message);
//       setDownloadUrl(`http://127.0.0.1:5000/uploads/${response.data.file}`);
//     } catch (error) {
//       setMessage("Upload failed!");
//     }
//   };

//   return (
//     <div className="app-container">
//       <h1 className="title">Audio Enhancer</h1>

//       <div className="content">
//         <div className="upload-container">
//           <input
//             type="file"
//             accept="audio/*"
//             onChange={handleFileChange}
//             className="file-input"
//           />

//           <button onClick={handleUpload} className="upload- btn">
//             Upload
//           </button>

//           {message && <div className="message">{message}</div>}

//           {downloadUrl && (
//             <a href={downloadUrl} download className="download-link">
//               Download Enhanced Audio
//             </a>
//           )}
//         </div>
//       </div>
//     </div>
//   );
// }

// export default App;

import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {

  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [downloadUrl, setDownloadUrl] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {

    if (!file) {
      alert("Please select an audio file first!");
      return;
    }

    const formData = new FormData();
    formData.append("audio", file);

    try {

      const response = await axios.post(
        "http://127.0.0.1:5000/upload",
        formData,
        { headers: { "Content-Type": "multipart/form-data" } }
      );

      setMessage(response.data.message);
      setDownloadUrl(`http://127.0.0.1:5000/uploads/${response.data.file}`);

    } catch (error) {

      if (error.response) {
        setMessage(error.response.data.error);
        console.log(error.response.data.trace);
      } else {
        setMessage("Server error");
      }

    }

  };

  return (
    <div className="app-container">

      <h1 className="title">Audio Enhancer</h1>

      <p className="subtitle">
        Clean background noise and improve recording clarity
      </p>

      <div className="upload-container">

        <label className="file-box">

          <input
            type="file"
            accept="audio/*"
            onChange={handleFileChange}
          />

          <div className="upload-text">

            <span className="upload-icon">🎧</span>

            <p className="upload-main">
              Select an audio file
            </p>

            <p className="upload-sub">
              Supported formats: WAV • MP3 • M4A
            </p>

          </div>

        </label>

        {file && (
          <p className="selected-file">
            Selected file: <span>{file.name}</span>
          </p>
        )}

        <button
          className="upload-btn"
          onClick={handleUpload}
        >
          Enhance Audio
        </button>

        {message && <p className="message">{message}</p>}

        {downloadUrl && (
          <div className="result">

            <audio controls src={downloadUrl}></audio>

            <a
              href={downloadUrl}
              download
              className="download-link"
            >
              Download Enhanced Audio
            </a>

          </div>
        )}

      </div>

    </div>
  );
}

export default App;