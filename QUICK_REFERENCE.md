# PSX Trading Calculator - Quick Reference

## ⚡ 1-Minute Setup

```bash
# 1. Install Python from python.org
# 2. Open Command Prompt in program folder
# 3. Run this:
pip install -r requirements.txt

# 4. Run the app:
python psx_calculator.py

# Done! App opens.
```

---

## 📊 5 Calculators at a Glance

### 1️⃣ Position Sizer
| Input | Value |
|-------|-------|
| Capital | 500,000 |
| Risk % | 2 |
| Entry | 1,000 |
| Stop Loss | 950 |

**Output:**
- Risk Amount: 10,000
- Risk/Share: 50
- **Shares: 200** ✅

---

### 2️⃣ Stop Loss Manager
**Three Methods:**

| Method | Formula | Example |
|--------|---------|---------|
| Manual | Enter directly | 950 |
| % Based | Entry - (Entry × %) | 1000 - 50 = 950 |
| ATR | Entry - (ATR × Mult) | 1000 - 22.5 = 977.5 |

**All show Risk/Share automatically**

---

### 3️⃣ Risk/Reward Calculator
**Auto-calculate Targets:**

| Ratio | Formula | Example | Profit |
|-------|---------|---------|--------|
| 1:1 | Entry + Risk | 1050 | +50 PKR |
| 1:2 | Entry + (Risk×2) | 1100 | +100 PKR |
| 1:3 | Entry + (Risk×3) | 1150 | +150 PKR |

**Choose before entering trade!**

---

### 4️⃣ Brokerage Calculator

**Default PSX Charges:**
- Broker: 0.10%
- CDC: 0.04%
- Tax: 12.5% (on profit only)

**Shows:**
- Entry charges
- Exit charges
- Capital gains tax
- **NET PROFIT** ✅

---

### 5️⃣ Trade Journal

**Add Trade:**
- Stock name
- Entry, Exit prices
- Quantity
- SL, Target

**Get:**
- P&L automatically
- Win/Loss status
- Full history
- **Statistics** ✅

---

## 📁 File Locations

```
Program Folder/
├── psx_calculator.py   ← RUN THIS
├── requirements.txt    ← pip install this
├── README.md          ← Read this
├── SETUP_INSTRUCTIONS.md ← Instructions
└── psx_data/          ← Your data (auto-created)
    ├── trades.json
    ├── settings.json
    └── exports/
```

**All saved in program folder - ZERO system dependencies!**

---

## 🎯 Common Workflows

### Workflow 1: Simple Trade
```
1. Position Sizer
   → Entry: 1000, SL: 950
   → Get: 200 shares

2. Risk/Reward
   → Entry: 1000, SL: 950
   → Get: Targets 1050/1100/1150

3. Buy 200 shares at 1000

4. Sell at 1100 (1:2 target)

5. Trade Journal
   → Add trade: Entry 1000, Exit 1100, Qty 200
   → Get: P&L +20,000

6. Review Statistics
   → Win rate, profit factor, etc.
```

### Workflow 2: Check Before Trading
```
Position Sizer
↓
Stop Loss Manager
↓
Risk/Reward Calculator
↓
Brokerage Calculator (to see charges)
↓
THEN trade!
```

---

## 💻 Keyboard Shortcuts

| Action | How |
|--------|-----|
| Run App | `python psx_calculator.py` |
| Next Tab | `Ctrl + Tab` |
| Previous Tab | `Ctrl + Shift + Tab` |
| Calculate | Button click or Enter |
| Export | Button click |

---

## 🔢 Formulas Used

### Position Sizing
```
Risk Amount = Capital × (Risk % ÷ 100)
Risk/Share = Entry - Stop Loss
Shares = Risk Amount ÷ Risk/Share
```

### Stop Loss Percentage
```
SL = Entry - (Entry × Percentage ÷ 100)
```

### Target Price
```
Target = Entry + (Risk/Share × Ratio)
```

### Brokerage
```
Commission = Entry/Exit Value × %
Total Charges = Entry Commission + Exit Commission + Tax
Net P&L = Gross P&L - Total Charges
```

---

## 📊 Trade Journal Statistics

**What it calculates:**
- Total trades
- Winning trades
- Losing trades
- Win rate %
- Average win
- Average loss
- Profit factor (total profit ÷ total loss)
- Total P&L

**How to interpret:**
- Win Rate > 50% = More wins than losses ✅
- Profit Factor > 1 = Profits > Losses ✅
- Profit Factor > 2 = Excellent system ✅

---

## 📤 Export Options

### CSV (Excel)
- Click "Export to CSV"
- Opens in Excel
- Can edit and analyze
- File saved in `psx_data/`

### Excel (Professional)
- Click "Export to Excel"
- Formatted spreadsheet
- Professional appearance
- File saved in `psx_data/`

### PDF (Print)
- Click "Export to PDF"
- Print-ready format
- Professional report
- File saved in `psx_data/`

---

## ✅ Pre-trade Checklist

Before you trade, use the app:

- [ ] Position Sizer: Calculate exact shares
- [ ] Risk/Reward: Determine exit targets
- [ ] Stop Loss Manager: Set stop loss
- [ ] Brokerage: See net profit potential
- [ ] Then execute trade

---

## 🐛 Quick Fixes

| Problem | Fix |
|---------|-----|
| App won't start | `python --version` check 3.7+ |
| Import error | `pip install -r requirements.txt` |
| No data folder | Quit app and restart (auto-creates) |
| Can't export | Check dependencies installed |
| Trades disappear | Check `psx_data/trades.json` exists |

---

## 💾 Backup Your Data

```bash
# Copy this folder to backup trades:
psx_data/

# Keep backups in:
- Cloud (OneDrive, Google Drive)
- USB drive
- External hard drive
- Email to yourself
```

---

## 🎯 Trading Tips

1. **Never risk > 2%** - Use position sizer
2. **Always use SL** - Use stop loss calculator
3. **Plan exits** - Use risk/reward calculator
4. **Check charges** - Use brokerage calculator
5. **Record trades** - Use trade journal
6. **Review stats** - Click Statistics button
7. **Backup data** - Copy psx_data/ folder regularly

---

## 📱 Data Files

### trades.json
- Your complete trade history
- Edit-able (but use app instead)
- Format: JSON array
- Backup this file!

### settings.json
- Your preferred charges
- PSX defaults pre-configured
- Change in Brokerage tab

---

## 🌟 Features Summary

✅ Position Sizer - Find exact shares
✅ Stop Loss Manager - 3 different methods
✅ Risk/Reward - Auto-calculate targets
✅ Brokerage - See net profit
✅ Trade Journal - Track everything
✅ CSV Export - Analyze in Excel
✅ Excel Export - Professional format
✅ PDF Export - Print-ready
✅ Statistics - Win rate, profit factor
✅ No system folders - 100% portable

---

## 🚀 Next Steps

1. Install Python
2. `pip install -r requirements.txt`
3. `python psx_calculator.py`
4. Start with Position Sizer
5. Use Risk/Reward to plan exits
6. Execute your trade
7. Record in Trade Journal
8. Review statistics

---

## 💡 Pro Tips

- **Bookmark targets**: Use Risk/Reward BEFORE trading
- **Follow the math**: Don't deviate from calculated sizes
- **Review monthly**: Look at statistics to improve
- **Backup weekly**: Copy psx_data/ folder
- **Export quarterly**: Save trades to Excel

---

## 📞 Resources

- **Python**: https://www.python.org/
- **PSX**: https://www.psx.com.pk/
- **Trading**: Educate yourself on PSX stocks
- **Help**: Read SETUP_INSTRUCTIONS.md

---

## ⏱️ Time Estimate

| Task | Time |
|------|------|
| Install Python | 5 min |
| Install requirements | 2 min |
| First run | <1 min |
| Position calculation | <1 min |
| Add trade | <1 min |
| Review statistics | <1 min |
| **Total Setup** | **~10 min** |

---

## 🎉 You're Ready!

Everything is set up and ready.

**Start trading with confidence using your own professional calculator!**

---

**PSX Trading Calculator Pro**
*Quick • Accurate • Professional*
