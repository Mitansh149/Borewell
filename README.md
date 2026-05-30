# 💧 Borewell Farm Water — Business Manager

A free, mobile-friendly web app to manage a borewell water supply business.  
Track sessions, farmers, payments, ledgers, and print receipts — all from your phone or PC.

**Live Demo →** `https://YOUR-USERNAME.github.io/borewell`

---

## 📱 Screenshots

| Dashboard | Sessions | Ledger |
|-----------|----------|--------|
| Live totals, pending dues, recent sessions | Add pump sessions with auto bill calculator | Full per-farmer account history |

---

## ✨ Features

- **Dashboard** — Total billed, collected, pending dues, hours pumped
- **Sessions** — Add pump sessions (date, farmer, start/end time, rate, payment)
- **Farmers** — View all farmers, record payments, track balances
- **Ledger** — Full account history per farmer with totals
- **Receipts** — Generate and print professional receipts
- **Mobile-first** — Works great on Android and iPhone
- **Offline** — All data saved locally in the browser (no internet needed after loading)
- **PWA ready** — Install on phone home screen like a real app

---

## 🚀 How to Use

### Option 1 — Open directly (no setup needed)
Just open `index.html` in any browser on your PC or phone.

### Option 2 — Host on GitHub Pages (share with anyone)
1. Fork or upload this repo to your GitHub account
2. Go to **Settings → Pages**
3. Set source to **main branch / root**
4. Your site is live at `https://YOUR-USERNAME.github.io/borewell`

### Option 3 — Install as mobile app (PWA)
1. Open the GitHub Pages link on your phone
2. **Android (Chrome):** tap ⋮ menu → "Add to Home Screen"
3. **iPhone (Safari):** tap Share → "Add to Home Screen"

---

## 🗂️ Files

```
borewell/
├── index.html       ← The entire app (single file)
├── build_site.py    ← Python script to regenerate index.html
└── README.md        ← This file
```

---

## 🛠️ Built With

- Pure HTML, CSS, JavaScript — no frameworks, no dependencies
- localStorage for data persistence
- Python script to generate the HTML

---

## 📋 How Data is Stored

All your data (sessions, payments, farmer records) is saved in your browser's **localStorage**.  
This means:
- ✅ Works completely offline
- ✅ Data persists after closing the browser
- ⚠️ Data is per-device (phone and PC won't sync automatically)

> Want real-time sync across devices? Firebase integration can be added — open an issue!

---

## 👨‍💻 Contributing

Pull requests welcome! Feel free to open issues for bugs or feature requests.

---

## 📄 License

MIT License — free to use, modify, and share.

---

*Made for a family borewell water business 💧*
