# PSX Trading Calculator Pro - Complete Setup Guide

## ⚡ Quick Start (5 Minutes)

### Step 1: Install Python
- Download from: https://www.python.org/downloads/
- **IMPORTANT**: Check "Add Python to PATH"
- Click "Install"

### Step 2: Open Command Prompt
- Press: `Windows + R`
- Type: `cmd`
- Press: `Enter`

### Step 3: Navigate to Program Folder
```bash
cd C:\path\to\PSX_Trading_Calculator_Complete
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Run the Program
```bash
python psx_calculator.py
```

**✓ Application should open immediately!**

---

## 📋 Detailed Step-by-Step Guide

### STEP 1: Verify Python Installation

1. Open Command Prompt (Windows + R → cmd)
2. Type: `python --version`
3. You should see: `Python 3.9.x` or higher
4. If you see an error, install Python from https://www.python.org/downloads/

### STEP 2: Download the Program Files

1. Download the **PSX_Trading_Calculator_Complete** folder
2. Save to: `C:\Users\YourName\Downloads\` OR any location
3. Remember the location!

### STEP 3: Open Command Prompt in Program Folder

**Method A: Using Windows Explorer**
1. Open Windows Explorer
2. Navigate to PSX_Trading_Calculator_Complete folder
3. Hold: Shift
4. Right-click in empty space
5. Click: "Open PowerShell window here" OR "Open Command Prompt here"

**Method B: Manual Navigation**
1. Open Command Prompt (Windows + R → cmd)
2. Type: `cd C:\Users\YourName\Downloads\PSX_Trading_Calculator_Complete`
3. Press Enter

### STEP 4: Install Required Packages

In the Command Prompt, type:

```bash
pip install -r requirements.txt
```

**Wait for it to complete** (about 1-2 minutes)

You should see:
```
Successfully installed openpyxl-3.10.10 reportlab-4.0.7
```

### STEP 5: Run the Application

Type:
```bash
python psx_calculator.py
```

**The application window should open!**

---

## ✅ Verification Checklist

After installation, verify everything works:

- [ ] Command Prompt opened successfully
- [ ] Navigated to program folder
- [ ] `pip install -r requirements.txt` completed without errors
- [ ] Application window opened
- [ ] Can see all 5 tabs:
  - [ ] Position Sizer
  - [ ] Stop Loss Manager
  - [ ] Risk/Reward
  - [ ] Brokerage
  - [ ] Trade Journal
- [ ] Can enter numbers and calculate
- [ ] Can add trades to journal

---

## 🚀 How to Run the Program Later

After first-time setup, you only need to do:

```bash
# Navigate to folder
cd C:\path\to\PSX_Trading_Calculator_Complete

# Run the program
python psx_calculator.py
```

Or create a shortcut:
1. Right-click: `psx_calculator.py`
2. Click: "Send to" → "Desktop (create shortcut)"
3. Double-click the shortcut on desktop to run

---

## 📁 File Locations

### Program Files Location
```
PSX_Trading_Calculator_Complete/
├── psx_calculator.py          ← Main program (double-click to run)
├── requirements.txt            ← Dependencies list
└── README.md                   ← This guide
```

### Data Storage Location
When you run the program, it creates:
```
PSX_Trading_Calculator_Complete/
└── psx_data/                   ← Created automatically
    ├── trades.json             ← Your trades
    ├── settings.json           ← Your settings
    ├── trades_20240101_120000.csv   ← Exports
    ├── trades_20240101_120000.xlsx  ← Exports
    └── trades_20240101_120000.pdf   ← Exports
```

**All files are saved in the program directory - NO system folders used!**

---

## 🎯 How to Use Each Feature

### 1. Position Sizer
1. Click "Position Sizer" tab
2. Enter:
   - Total Capital: 500000
   - Risk %: 2
   - Entry Price: 1000
   - Stop Loss: 950
3. Click "Calculate"
4. See result: Shares to Buy = 200

### 2. Stop Loss Manager
1. Click "Stop Loss Manager" tab
2. Enter Entry Price: 1000
3. Select Method: Manual / Percentage / ATR Based
4. Enter Stop Loss value
5. Click "Calculate"
6. See Stop Loss Price and Risk Per Share

### 3. Risk/Reward Calculator
1. Click "Risk/Reward" tab
2. Enter Entry Price: 1000
3. Enter Stop Loss: 950
4. Click "Calculate Targets"
5. See target prices for 1:1, 1:2, 1:3 ratios

### 4. Brokerage Calculator
1. Click "Brokerage" tab
2. Enter:
   - Entry Price: 1000
   - Exit Price: 1100
   - Quantity: 500
   - Charges (defaults are PSX rates)
3. Click "Calculate Charges"
4. See all charges and NET P&L

### 5. Trade Journal
1. Click "Trade Journal" tab
2. Enter trade details:
   - Stock name
   - Entry, Exit, Quantity
   - SL, Target
3. Click "Add Trade"
4. Trade appears in history
5. Export to CSV, Excel, or PDF
6. Click "Statistics" to see performance

---

## 🐛 Troubleshooting

### Problem: "Python is not recognized"
**Solution:**
1. Uninstall Python completely
2. Download from https://www.python.org/downloads/
3. **IMPORTANT**: Check "Add Python to PATH"
4. Install
5. Restart Command Prompt
6. Try again

### Problem: "ModuleNotFoundError: No module named 'openpyxl'"
**Solution:**
```bash
pip install -r requirements.txt
```

### Problem: Application won't start
**Solution:**
1. Make sure you're in the correct folder
2. Verify `psx_calculator.py` exists there
3. Try: `python psx_calculator.py` again
4. Check for error messages in Command Prompt

### Problem: Export buttons don't work
**Solution:**
Make sure dependencies are installed:
```bash
pip install -r requirements.txt
```

### Problem: Can't save trades
**Solution:**
1. Make sure you have write permission to the folder
2. Check that `psx_data/` folder exists
3. Create it manually if needed

---

## 💡 Tips & Tricks

### Create a Shortcut on Desktop
1. Right-click: `psx_calculator.py`
2. "Send to" → "Desktop (create shortcut)"
3. Double-click shortcut to run

### Change Default Values
Edit the application:
1. Right-click: `psx_calculator.py`
2. "Open with" → "Notepad"
3. Find the default values (e.g., "500000", "2", "1000")
4. Change them
5. Save the file

### Backup Your Data
Your trades are saved in: `psx_data/trades.json`
- Copy this file to backup your data
- Can restore by pasting back in `psx_data/` folder

### Share Your Data
All your data is in `psx_data/` folder
- Share the entire folder to move to another computer
- Or export to Excel/CSV to share with others

---

## 🎯 Key Features

✅ **No Installation Required** - Just Python + pip install
✅ **Portable** - Works on any Windows computer
✅ **Local Data Storage** - All files saved in program folder
✅ **No Internet Needed** - Works offline completely
✅ **Easy to Share** - Just copy the folder
✅ **Multiple Export Formats** - CSV, Excel, PDF
✅ **Trade Tracking** - Record and analyze your trades
✅ **PSX-Specific** - Pre-configured for Pakistan Stock Exchange

---

## 📊 Calculator Features

### Position Sizer
- Calculate exact shares based on risk management
- Uses Decimal precision for accuracy
- Formula: Shares = Risk Amount ÷ Risk Per Share

### Stop Loss Manager
- **Manual**: Enter stop loss price directly
- **Percentage**: Calculate as % of entry price
- **ATR-Based**: Use ATR and multiplier

### Risk/Reward Calculator
- Calculate target prices for 1:1, 1:2, 1:3 ratios
- Shows profit percentage for each target
- Helps plan exits before entering

### Brokerage Calculator
- **PSX Default Charges**:
  - Broker Commission: 0.10%
  - CDC Charge: 0.04%
  - Capital Gains Tax: 12.5%
- Customizable charge rates
- Shows net profit/loss after all charges

### Trade Journal
- Record every trade
- Track entry, exit, SL, target
- Automatic P&L calculation
- Performance statistics:
  - Win rate %
  - Average win/loss
  - Profit factor
  - Total P&L

---

## 📈 Sample Workflow

### Example Trade Calculation

1. **Position Sizer**
   - Capital: 500,000 PKR
   - Risk: 2%
   - Entry: 1000, SL: 950
   - Result: Buy 200 shares

2. **Risk/Reward**
   - Entry: 1000, SL: 950
   - Results: 1:1 at 1050, 1:2 at 1100, 1:3 at 1150

3. **Execute Trade**
   - Buy 200 shares at 1000

4. **Close Trade**
   - Sell at 1050 (1:1 profit)
   - Open Trade Journal and add the trade

5. **Brokerage Calc**
   - Entry: 1000, Exit: 1050, Qty: 200
   - See net profit after charges

6. **Review Stats**
   - Click "Statistics" to see overall performance

---

## ⚙️ System Requirements

- **OS**: Windows 7 or higher
- **Python**: 3.7 or higher
- **RAM**: 512 MB minimum
- **Disk**: 50 MB free space
- **Internet**: Not required (except for pip install)

---

## 🔄 Updating the Program

To get updates:
1. Download the latest version
2. Copy `psx_calculator.py` to your current folder
3. Replace the old file
4. Your `psx_data/` folder stays (all your trades safe)

---

## 📞 Support

If you encounter any issues:

1. **Check the error message** - It usually tells you what's wrong
2. **Check Python version**: `python --version` (should be 3.7+)
3. **Reinstall dependencies**: `pip install -r requirements.txt`
4. **Check folder permissions** - Ensure you can write to the folder

---

## 🎓 Learning Resources

- Python: https://www.python.org/
- Tkinter: https://docs.python.org/3/library/tkinter.html
- PSX: https://www.psx.com.pk/

---

## 📝 Version Information

- **Version**: 1.0.0
- **Release Date**: 2024
- **License**: MIT (Free to use)
- **Language**: Python 3.7+

---

## ✨ Enjoy Trading!

This complete trading calculator is ready to use. No complicated setup, no system folders, just download and run!

**Happy Trading!** 📈🎯

For any questions, refer back to this guide.
