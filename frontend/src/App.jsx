import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {

  const [file, setFile] = useState(null);

  const [query, setQuery] = useState("");

  const [response, setResponse] = useState("");

  const [graphData, setGraphData] = useState([]);

  const [loading, setLoading] = useState(false);

  const [uploadedFile, setUploadedFile] = useState("");

  const uploadFile = async (type) => {

    if (!file) {

      alert("Select a file");

      return;
    }

    setLoading(true);

    const formData = new FormData();

    formData.append("file", file);

    try {

      const res = await axios.post(
        `http://127.0.0.1:8000/upload/${type}`,
        formData
      );

      setUploadedFile(file.name);

      alert(res.data.status);

      if (res.data.graph) {

        setGraphData(res.data.graph);
      }

    } catch (err) {

      console.log(err);

      alert("Upload failed");
    }

    setLoading(false);
  };

  const askQuestion = async () => {

    if (!query) {
      return;
    }

    setLoading(true);

    try {

      const res = await axios.post(
        "http://127.0.0.1:8000/query/",
        {
          query: query
        }
      );

      setResponse(res.data.answer);

    } catch (err) {

      console.log(err);

      alert("Query failed");
    }

    setLoading(false);
  };

  return (

    <div className="app">

      <div className="overlay"></div>

      <div className="container">

        <h1>
          NeuroLens AI
        </h1>

        <p className="subtitle">
          AI-powered retrieval and summarization across PDFs, images, and audio
        </p>

        <div className="upload-card">

          <input
            type="file"
            onChange={(e) => setFile(e.target.files[0])}
          />

          {uploadedFile && (

            <p className="file-name">
              Uploaded: {uploadedFile}
            </p>
          )}

          <div className="buttons">

            <button onClick={() => uploadFile("pdf")}>
              Upload PDF
            </button>

            <button onClick={() => uploadFile("image")}>
              Upload Image
            </button>

            <button onClick={() => uploadFile("audio")}>
              Upload Audio
            </button>

          </div>

        </div>

        <div className="query-card">

          <textarea
            placeholder="Ask something about the uploaded content..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />

          <button
            className="ask-btn"
            onClick={askQuestion}
          >
            Ask AI
          </button>

        </div>

        {loading && (

          <div className="loading">
            Processing...
          </div>
        )}

        {graphData.length > 0 && (

          <div className="response-card">

            <h2>
              Knowledge Graph
            </h2>

            <div className="graph-container">

              {graphData.map((edge, index) => (

                <div
                  key={index}
                  className="graph-edge"
                >

                  <span className="node">
                    {edge[0]}
                  </span>

                  <span className="arrow">
                    →
                  </span>

                  <span className="node">
                    {edge[1]}
                  </span>

                </div>
              ))}

            </div>

          </div>
        )}

        {response && (

          <div className="response-card">

            <h2>
              AI Response
            </h2>

            <p>
              {response}
            </p>

          </div>
        )}

      </div>

    </div>
  );
}

export default App;