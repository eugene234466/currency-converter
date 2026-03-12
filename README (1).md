# 💱 Currency Converter

A real-time currency converter built with Python Flask. Fetches live exchange rates from the [Open Exchange Rates API](https://open.er-api.com) — no API key required.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?style=flat-square&logo=flask)
![Railway](https://img.shields.io/badge/Deployed_on-Railway-blueviolet?style=flat-square)

---

## Features

- 🔄 Live exchange rates (160+ currencies)
- ⇄ Swap currencies with one click
- ⚡ Server-side rate caching (1-hour TTL) to avoid redundant API calls
- 🛡️ Input validation on both client and server
- 🌐 Deployed and accessible via public URL

---

## Tech Stack

| Layer    | Technology                                      |
|----------|-------------------------------------------------|
| Backend  | Python, Flask, Gunicorn                         |
| Frontend | HTML, CSS, Vanilla JS                           |
| API      | [open.er-api.com](https://open.er-api.com) (free, no key) |
| Hosting  | Railway                                         |

---

## Project Structure

```
currency-converter/
├── app.py               # Flask backend — routes, caching, conversion logic
├── requirements.txt     # Python dependencies
├── Procfile             # Railway/Gunicorn entry point
└── templates/
    └── index.html       # Frontend UI
```

---

## Getting Started (Local)

**1. Clone the repo**

```bash
git clone https://github.com/eugene234466/currency-converter.git
cd currency-converter
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Run the app**

```bash
python app.py
```

**4. Open in browser**

```
http://127.0.0.1:5000
```

> ⚠️ Do not open `index.html` directly — it must be served by Flask for the API routes to work.

---

## API Endpoints

| Method | Endpoint      | Description                          |
|--------|---------------|--------------------------------------|
| GET    | `/`           | Serves the main UI                   |
| GET    | `/currencies` | Returns a sorted list of all currency codes |
| POST   | `/convert`    | Converts an amount between two currencies |

### POST `/convert` — Request body

```json
{
  "amount": 100,
  "from_cur": "USD",
  "to_cur": "EUR"
}
```

### POST `/convert` — Response

```json
{
  "amount": 100,
  "from": "USD",
  "to": "EUR",
  "result": 91.25,
  "rate": 0.9125,
  "last_updated": "2026-03-12 10:00 UTC"
}
```

---

## Deployment (Railway)

This app is configured for one-click deployment on [Railway](https://railway.app).

1. Push this repo to GitHub
2. Go to [railway.app](https://railway.app) → **New Project** → **Deploy from GitHub repo**
3. Select this repo — Railway auto-detects Python and uses the `Procfile`
4. Click **Generate Domain** to get a public URL

Railway will auto-redeploy on every push to `main`.

---

## Environment Variables

No environment variables are required. Railway injects `PORT` automatically and the app reads it at startup.

---

## License

Copyright (c) 2026 Eugene Yarney. All rights reserved.

This software and its source code are proprietary and confidential.
Unauthorized copying, distribution, modification, public display,
or public performance of this software, in whole or in part, is
strictly prohibited without the prior written permission of the
copyright owner.

RESTRICTIONS

1. You may not copy, reproduce, or duplicate this software or any
   portion of it.

2. You may not modify, adapt, translate, or create derivative works
   based on this software.

3. You may not distribute, sublicense, sell, rent, lease, transfer,
   or otherwise make this software available to any third party.

4. You may not reverse engineer, disassemble, decompile, or attempt
   to derive the source code of any compiled or obfuscated components
   of this software.

5. You may not use this software or any portion of it for any
   commercial purpose without the express written consent of the
   copyright owner.

DISCLAIMER

THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND
NONINFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT OWNER BE LIABLE
FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

CONTACT

For licensing inquiries or permission requests, contact the
copyright owner directly via the repository contact information.

