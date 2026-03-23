# Page Replacement UI (Node.js)

A web UI for FIFO, LRU, MRU, Optimal, and Second Chance page replacement algorithms.

This UI is wired to the Python backend through `python_bridge.py`.

## Requirements

- Node.js 18+
- Python 3 (available as `python3` in your terminal)

## Run

```bash
cd src/ui/page-replacement-ui
npm install
npm start
```

Open http://localhost:3000

## API

- `POST /simulate`
- `POST /api/simulate`

### Request Body

```json
{
	"algorithm": "LRU",
	"frames": 3,
	"referenceString": [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
}
```


