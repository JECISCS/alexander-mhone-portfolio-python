# Alexander Mhone — Engineering Portfolio

A mobile-first Flask portfolio for Alexander Gabriel Mhone.

## Run locally

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python build.py
python app.py
```

Open http://127.0.0.1:5000

The build command copies the single PDF in `data/mycv/` to the ignored deployment
asset `public/cv.pdf`. Local and Vercel deployments use the same `/cv.pdf` link.

## Deploy to Vercel

1. Push this repository to GitHub and import it into Vercel.
2. Keep the Vercel project root set to this repository's root. Vercel detects the
   Flask `app` in `app.py` and installs dependencies from `requirements.txt`.
3. Vercel uses `.python-version` and the `build` script in `pyproject.toml`.
   The build publishes the CV to `public/cv.pdf`; Vercel serves `public/` assets
   from its CDN.
4. Enable Git deployments in Vercel. Each push to the connected production branch
   triggers a deployment.

The site assets live in `public/static/`. Flask's built-in static handler is
disabled; a local-only-compatible Flask route serves the same files during
`python app.py`, while Vercel serves them directly from `public/`.

## Updating the CV

Replace the existing PDF in `data/mycv/` with the new CV and commit the change.
The folder must contain exactly one `.pdf` file. If you give the replacement a
different filename, remove the old PDF as well. On the next Git deployment,
`python build.py` publishes the new file as `/cv.pdf`, so the website links stay
the same. Do not edit or commit `public/cv.pdf`; it is generated and ignored.

The CV source is not placed in the public asset folder; only the generated
`public/cv.pdf` is publicly served.
