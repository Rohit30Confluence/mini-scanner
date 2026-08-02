# Hosting the Mini Scanner demo on GitHub Pages

This is a **static, simulated** demo — pure HTML/CSS/JS, no backend, no real
scanning. It's meant to show off the UI and result format. (GitHub Pages
can't run Python or open real network sockets, so this is the version that
fits it. If you later want a *real* scanner online, that needs a small
backend host like Render/Railway — happy to set that up whenever you want.)

## Files
```
index.html
style.css
app.js
```

## Steps

1. **Add the files to your repo.**
   Simplest option: put `index.html`, `style.css`, and `app.js` in a `docs/`
   folder at the root of `mini-scanner` (or in the root itself — either
   works, you'll pick which in step 3).

   ```bash
   git checkout main
   mkdir -p docs
   cp index.html style.css app.js docs/
   git add docs
   git commit -m "Add static UI demo for GitHub Pages"
   git push
   ```

2. **Go to your repo's Settings.**
   `github.com/Rohit30Confluence/mini-scanner` → **Settings** tab.

3. **Open Pages.**
   Left sidebar → **Pages**.

4. **Set the source.**
   Under "Build and deployment" → **Source**: choose **Deploy from a branch**.
   Under **Branch**: choose `main`, and the folder — `/docs` (or `/root` if
   you put the files at the repo root). Click **Save**.

5. **Wait ~1 minute, then get your link.**
   GitHub will show a banner: *"Your site is live at
   `https://rohit30confluence.github.io/mini-scanner/`"*. That's your
   shareable link — open it in any browser.

That's it — no build step, no server to keep running. Any time you push a
change to `index.html`/`style.css`/`app.js` on that branch, the Pages site
updates automatically in a minute or two.
