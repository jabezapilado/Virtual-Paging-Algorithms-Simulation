const express = require("express");
const path = require("path");
const { spawnSync } = require("child_process");

const app = express();
const PORT = 3000;
const PYTHON_BRIDGE_PATH = path.join(__dirname, "python_bridge.py");

app.use(express.json());
app.use(express.static(path.join(__dirname, "public")));

function runPythonSimulation(payload) {
  const processResult = spawnSync("python3", [PYTHON_BRIDGE_PATH], {
    input: JSON.stringify(payload),
    encoding: "utf8",
  });

  if (processResult.error) {
    return { status: 500, body: { error: "Failed to start Python backend." } };
  }

  const output = (processResult.stdout || "").trim();
  let parsedOutput = null;

  if (output) {
    try {
      parsedOutput = JSON.parse(output);
    } catch {
      parsedOutput = null;
    }
  }

  if (processResult.status !== 0) {
    const defaultMessage =
      processResult.status === 2
        ? "Selected algorithm is not implemented yet."
        : "Python simulation failed.";

    return {
      status: processResult.status === 2 ? 400 : 500,
      body: {
        error: parsedOutput?.error || defaultMessage,
      },
    };
  }

  if (!parsedOutput) {
    return { status: 500, body: { error: "Invalid response from Python backend." } };
  }

  return { status: 200, body: parsedOutput };
}

function handleSimulate(req, res) {
  const { algorithm, frames, referenceString } = req.body || {};

  const normalizedAlgorithm = typeof algorithm === "string" ? algorithm.trim() : "";
  const parsedFrames = Number(frames);
  const hasReferenceString = Array.isArray(referenceString) && referenceString.length > 0;

  if (!normalizedAlgorithm || !Number.isInteger(parsedFrames) || parsedFrames <= 0 || !hasReferenceString) {
    return res.status(400).json({ error: "Missing required fields." });
  }

  const result = runPythonSimulation({
    algorithm: normalizedAlgorithm,
    frames: parsedFrames,
    referenceString,
  });
  return res.status(result.status).json(result.body);
}

app.post("/simulate", handleSimulate);
app.post("/api/simulate", handleSimulate);

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});