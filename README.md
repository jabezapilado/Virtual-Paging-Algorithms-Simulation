# Virtual Paging Algorithms Simulation

The **Virtual Paging Algorithms Simulation** project is a learning-focused toolkit for page replacement in Operating Systems. It provides a Python CLI simulation flow and a lightweight web UI, both connected to the same algorithm modules.

## Overview

- Dual experience: terminal-based simulation and browser-based simulation.
- Supports step-by-step frame state tracking per page request.
- Reports faults, hits, failure rate, and success rate.
- Modular architecture separates algorithms, metrics, and UI layers.

## Tech Stack

- **Python 3.10+** for the simulation core and CLI.
- **Node.js 18+ + Express** for the web UI server.
- **Vanilla HTML/CSS/JS** frontend for browser interaction.

## Implemented Algorithms

- FIFO
- LRU
- MRU
- OPTIMAL
- SECOND CHANCE

## Prerequisites

1. Python 3.10 or newer.
2. Node.js 18 or newer (for web UI only).
3. Git (optional, for collaboration workflow).

## CLI Workflow (Python)

From `Virtual Paging Algorithms Simulation/`:

```bash
python3 main.py
```

Then:
1. Choose an algorithm from the menu.
2. Enter number of frames.
3. Enter a reference string.
4. Review the step-by-step output plus summary metrics.

### Sample Input

- Frames: `3`
- Reference string: `7 0 1 2 0 3 0 4 2 3 0 3 2`

## Web UI Workflow

From `Virtual Paging Algorithms Simulation/`:

```bash
cd src/ui/page-replacement-ui
npm install
npm start
```

Open http://localhost:3000

The UI supports:
- Algorithm selection
- Frame count input
- Reference string input
- Results table (Page, Frames, Result)
- Metrics summary (faults, hits, failure/success rates)

## Project Structure

```text
Virtual Paging Algorithms Simulation/
├── main.py
├── requirements.txt
├── README.md
└── src/
   ├── algorithms.py
   ├── contracts.py
   ├── fifo.py
   ├── lru.py
   ├── metrics.py
   ├── mru.py
   ├── optimal.py
   ├── runner.py
   ├── second_chance.py
   └── ui/
      ├── cli.py
      └── page-replacement-ui/
         ├── server.js
         ├── python_bridge.py
         └── public/
```

## Contributors

- Apilado, Jabez Timothy E. — Backend lead, integration, contracts, metrics, CLI orchestration
- Maninang, Allein Dane G. — OPTIMAL and SECOND CHANCE algorithms
- Parungao, Nikko S. — FIFO and MRU algorithms
- Gurango, Christine Francoise O. — Frontend/input UX support
- Quilantang, Grant Mihkael D. — Frontend/output UX and documentation support

## Team Grouping and Roles

- **Backend (3):** Jabez, Nikko, Dane
- **Frontend (2):** Francoise, Grant

Detailed task delegation is documented in the workspace root at `TEAM_TASK_DELEGATION.md`.

## Notes

- All required algorithms run in one integrated program.
- Output includes both step-by-step traces and summary metrics.
- For sample test sets, see `examples/sample_inputs.md` in the workspace root.

## References

- **Backend (Algorithms / OS Concepts)**
   - GeeksforGeeks. (n.d.). *Page Replacement Algorithms in Operating Systems*. https://www.geeksforgeeks.org/operating-systems/page-replacement-algorithms-in-operating-systems/
   - GeeksforGeeks. (n.d.). *FIFO Page Replacement Algorithm*. https://www.geeksforgeeks.org/program-page-replacement-algorithms-set-2-fifo/
   - GeeksforGeeks. (n.d.). *Least Recently Used (LRU) Page Replacement Algorithm*. https://www.geeksforgeeks.org/program-for-least-recently-used-lru-page-replacement-algorithm/
   - GeeksforGeeks. (n.d.). *Optimal Page Replacement Algorithm*. https://www.geeksforgeeks.org/page-replacement-algorithms-in-operating-systems/#:~:text=Optimal%20Page%20replacement
   - GeeksforGeeks. (n.d.). *Second Chance (Clock) Page Replacement Policy*. https://www.geeksforgeeks.org/operating-systems/second-chance-or-clock-page-replacement-policy/
   - Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.
   - Tanenbaum, A. S., & Bos, H. (2014). *Modern Operating Systems* (4th ed.). Pearson.

- **Frontend / Tooling**
   - Express.js. (n.d.). *Express - Node.js web application framework*. https://expressjs.com/
   - Node.js. (n.d.). *Node.js Documentation*. https://nodejs.org/en/docs
   - MDN Web Docs. (n.d.). *Fetch API*. https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
   - MDN Web Docs. (n.d.). *Using the Fetch API*. https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
   - MDN Web Docs. (n.d.). *HTML tables*. https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table

## License

This project is released for educational use. Apply additional licensing as needed before redistribution.
