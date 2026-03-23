const simForm = document.getElementById("sim-form");
const clearBtn = document.getElementById("clearBtn");
const exitBtn = document.getElementById("exitBtn");
const errorEl = document.getElementById("error");
const stepsBody = document.getElementById("stepsBody");
const referenceStringInput = document.getElementById("referenceString");

const faultsEl = document.getElementById("faults");
const hitsEl = document.getElementById("hits");
const failureRateEl = document.getElementById("failureRate");
const successRateEl = document.getElementById("successRate");

// Auto-format reference string with spaces
referenceStringInput.addEventListener("input", (e) => {
  const value = e.target.value;
  const cleaned = value.replace(/\s+/g, "").replace(/[^\d]/g, "");
  const formatted = cleaned.split("").join(" ");
  e.target.value = formatted;
});

simForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  errorEl.textContent = "";

  const algorithm = document.getElementById("algorithm").value;
  const frames = parseInt(document.getElementById("frameCount").value, 10);
  const referenceInput = document.getElementById("referenceString").value.trim();

  if (!frames || frames < 1) {
    errorEl.textContent = "Please enter a valid number of frames.";
    return;
  }

  if (!referenceInput) {
    errorEl.textContent = "Please enter a reference string.";
    return;
  }

  const referenceString = referenceInput
    .split(/\s+/)
    .map((item) => Number(item))
    .filter((num) => !Number.isNaN(num));

  if (referenceString.length === 0) {
    errorEl.textContent = "Reference string must contain valid numbers.";
    return;
  }

  try {
    const response = await fetch("/simulate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        algorithm,
        frames,
        referenceString,
      }),
    });

    const data = await response.json();

    if (!response.ok || data.error) {
      errorEl.textContent = data.error || "Simulation failed.";
      return;
    }

    renderResults(data);
  } catch (err) {
    errorEl.textContent = "Unable to connect to the backend.";
  }
});

function renderResults(data) {
  stepsBody.innerHTML = "";

  if (!data.steps || data.steps.length === 0) {
    stepsBody.innerHTML = `
      <tr>
        <td colspan="3" class="placeholder">No steps returned.</td>
      </tr>
    `;
  } else {
    data.steps.forEach((step) => {
      const row = document.createElement("tr");
      const resultClass = step.result === "FAULT" ? "result-fault" : "result-hit";

      row.innerHTML = `
        <td>${step.page}</td>
        <td>${step.frames}</td>
        <td class="${resultClass}">${step.result}</td>
      `;

      stepsBody.appendChild(row);
    });
  }

  faultsEl.textContent = data.pageFaults;
  hitsEl.textContent = data.pageHits;
  failureRateEl.textContent = `${Number(data.failureRate).toFixed(2)}%`;
  successRateEl.textContent = `${Number(data.successRate).toFixed(2)}%`;
}

clearBtn.addEventListener("click", () => {
  document.getElementById("frameCount").value = "";
  document.getElementById("referenceString").value = "";
  document.getElementById("algorithm").value = "FIFO";
  errorEl.textContent = "";

  stepsBody.innerHTML = `
    <tr>
      <td colspan="3" class="placeholder">No simulation yet.</td>
    </tr>
  `;

  faultsEl.textContent = "-";
  hitsEl.textContent = "-";
  failureRateEl.textContent = "-";
  successRateEl.textContent = "-";
});

exitBtn.addEventListener("click", () => {
  window.close();

  setTimeout(() => {
    errorEl.textContent = "You can close this tab manually.";
  }, 200);
});