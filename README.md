# PSX Trading Calculator Pro v1.0.0

## 🎯 Professional Desktop Application for Pakistan Stock Exchange Trading

A complete, portable desktop application for trading calculations with NO system folder dependencies. All files are saved directly in the program directory.

### ✨ Key Features

✅ **Fully Portable** - Works on any Windows computer
✅ **No System Folders** - All data saved in program directory
✅ **No Installation Required** - Just Python + requirements.txt
✅ **Complete Trading Toolkit** - 5 major calculators
✅ **Trade Tracking** - Full journal with statistics
✅ **Multiple Export Formats** - CSV, Excel, PDF
✅ **Professional GUI** - Easy to use interface
✅ **100% Offline** - No internet required
✅ **PSX-Optimized** - Pre-configured for Pakistan Stock Exchange

---

## 📋 Features Overview

### 1. Position Size Calculator
Calculate exact number of shares to buy based on risk management:
- Input: Capital, Risk %, Entry Price, Stop Loss
- Output: Risk Amount, Risk Per Share, Shares to Buy
- Formula: `Shares = Risk Amount ÷ (Entry - Stop Loss)`
- **Precision**: Uses Decimal for accurate calculations

### 2. Stop Loss Manager
Three different methods for stop loss calculation:
- **Manual**: Enter stop loss price directly
- **Percentage**: `SL = Entry - (Entry × %)`
- **ATR-Based**: `SL = Entry - (ATR × Multiplier)`
- Shows risk per share for each method

### 3. Risk/Reward Calculator
Calculate target prices for multiple risk/reward ratios:
- **1:1 Ratio** (Conservative)
- **1:2 Ratio** (Standard)
- **1:3 Ratio** (Aggressive)
- Formula: `Target = Entry + (Risk/Share × Ratio)`
- Shows profit percentage for each target

### 4. Brokerage Calculator
Complete PSX charges calculation:
- **Broker Commission**: 0.10% (customizable)
- **CDC Charge**: 0.04% (customizable)
- **Exchange Fee**: Included
- **Capital Gains Tax**: 12.5% on profit (customizable)
- Detailed breakdown of all charges
- Shows net P&L and ROI %

### 5. Trade Journal
Complete trade tracking and analytics:
- Record all trade details
- Automatic P&L calculation
- Trade status (Won/Lost/Even)
- Trade history display
- Performance statistics:
  - Total trades, wins, losses
  - Win rate percentage
  - Average win/loss
  - Profit factor
  - Total P&L

### 6. Export Options
- **CSV Export**: Open in Excel or any spreadsheet
- **Excel Export**: Professional format with formatting
- **PDF Export**: Print-ready reports

---

## 🚀 Quick Start

### 1. Install Python
- Download: https://www.python.org/downloads/
- **IMPORTANT**: Check "Add Python to PATH"

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python psx_calculator.py
```

**Done!** Application opens immediately.

---

## 📁 File Structure

```
PSX_Trading_Calculator_Complete/
│
├── psx_calculator.py           ← Main application (run this)
├── requirements.txt             ← Dependencies (pip install -r requirements.txt)
├── SETUP_INSTRUCTIONS.md        ← Detailed setup guide
└── README.md                    ← This file

When you run the app, it creates:
├── psx_data/                   ← Auto-created data folder
│   ├── trades.json             ← Your trades (backup this!)
│   ├── settings.json           ← Application settings
│   ├── trades_YYYYMMDD_HHMMSS.csv    ← Exports
│   ├── trades_YYYYMMDD_HHMMSS.xlsx   ← Exports
│   └── trades_YYYYMMDD_HHMMSS.pdf    ← Exports
```

**All data is saved in the program directory - No system folders used!**

---

## 💻 System Requirements

| Requirement | Minimum | Recommended |
|------------|---------|-------------|
| OS | Windows 7 | Windows 10/11 |
| Python | 3.7 | 3.9+ |
| RAM | 512 MB | 2 GB |
| Disk | 50 MB | 100 MB |
| Internet | Not needed | Not needed |

---

## 🔧 Installation Details

### Requirements.txt Contents
```
openpyxl==3.10.10       # For Excel export
reportlab==4.0.7        # For PDF export
```

### Dependencies
- **openpyxl**: Excel file creation and manipulation
- **reportlab**: PDF document generation
- **Tkinter**: GUI (built-in with Python)
- **json**: Data storage (built-in with Python)
- **csv**: CSV export (built-in with Python)
- **decimal**: Precision calculations (built-in with Python)
- **datetime**: Date/time handling (built-in with Python)

---

## 📊 Usage Examples

### Example 1: Calculate Position Size
```
Inputs:
  Capital: 500,000 PKR
  Risk %: 2%
  Entry: 1000 PKR
  Stop Loss: 950 PKR

Results:
  Risk Amount: 10,000 PKR (2% of capital)
  Risk Per Share: 50 PKR (1000 - 950)
  Shares to Buy: 200 shares (10,000 ÷ 50)
```

### Example 2: Risk/Reward Targets
```
Inputs:
  Entry: 1000 PKR
  Stop Loss: 950 PKR
  Risk Per Share: 50 PKR

Results:
  1:1 Target: 1050 PKR (profit: 50, +5%)
  1:2 Target: 1100 PKR (profit: 100, +10%)
  1:3 Target: 1150 PKR (profit: 150, +15%)
```

### Example 3: Brokerage Calculation
```
Inputs:
  Entry: 1000 PKR × 500 shares = 500,000 PKR
  Exit: 1100 PKR × 500 shares = 550,000 PKR
  Charges: 0.10% + 0.04% + 12.5% tax on profit

Results:
  Gross Profit: 50,000 PKR
  Charges: 7,730.50 PKR
  NET PROFIT: 42,269.50 PKR
  ROI: 8.45%
```

---

## 🎯 How to Use Each Tab

### Position Sizer Tab
1. Enter your total capital
2. Enter risk percentage (typically 2%)
3. Enter entry and stop loss prices
4. Click "Calculate"
5. See exact shares to buy

### Stop Loss Manager Tab
1. Choose method: Manual, Percentage, or ATR-Based
2. Enter relevant values
3. Click "Calculate"
4. See stop loss price and risk per share

### Risk/Reward Tab
1. Enter entry and stop loss prices
2. Click "Calculate Targets"
3. See target prices for all 3 ratios
4. Choose which ratio to aim for

### Brokerage Tab
1. Enter entry price, exit price, quantity
2. Adjust charges if needed
3. Click "Calculate Charges"
4. See detailed breakdown and net profit

### Trade Journal Tab
1. Enter trade details (stock, entry, exit, qty, SL, target)
2. Click "Add Trade"
3. Trade appears in history table
4. Click "Statistics" to see performance
5. Export to CSV, Excel, or PDF

---

## 💾 Data Storage

### Trade Data Location
All trades are saved in: `psx_data/trades.json`
- Located in the program directory
- Automatically created on first use
- Can be backed up easily

### Backup Your Data
1. Go to program folder
2. Copy `psx_data/` folder
3. Store in safe location
4. Can restore anytime

### Restore Data
1. If you delete a trade, it's gone (no undo)
2. Always have backups!
3. Restore by replacing `psx_data/trades.json`

---

## 🖥️ GUI Features

### Professional Tkinter Interface
- Tabbed interface for each calculator
- Clean, organized layout
- Real-time status bar
- Color-coded results
- Input validation
- Error messages for invalid data

### Treeview Display
- Trade history in table format
- Sortable columns
- Scrollable interface
- Easy to read and review

### Export Formats
- **CSV**: Open in Excel, Google Sheets, or any tool
- **Excel**: Professional format with formatting
- **PDF**: Print-ready reports with tables

---

## 🚨 Troubleshooting

### "Python is not recognized"
- Reinstall Python with "Add Python to PATH" checked
- Restart Command Prompt after installation

### "ModuleNotFoundError: No module named 'openpyxl'"
- Run: `pip install -r requirements.txt`
- Make sure you're in the program directory

### "Permission denied" on data folder
- Right-click program folder → Properties
- Check "Read & Write" permissions
- Or run Command Prompt as Administrator

### Application won't start
- Make sure `psx_calculator.py` exists
- Check Python version: `python --version` (should be 3.7+)
- Try: `python psx_calculator.py` in Command Prompt

### Trades not saving
- Check `psx_data/` folder exists
- Verify write permissions to folder
- Make sure JSON file isn't corrupted

---

## 🔐 Data Safety

### How Data is Stored
- Plain JSON format (easy to backup and restore)
- Human-readable (can edit manually if needed)
- No encryption (suitable for personal use)

### Backup Strategy
1. Regularly backup `psx_data/trades.json`
2. Export trades to Excel monthly
3. Keep multiple backups in different locations

### Data Privacy
- No cloud upload (100% local)
- No telemetry or tracking
- No registration required
- Your data stays on your computer

---

## 📈 Best Practices

### Risk Management
1. Never risk more than 2% per trade
2. Always use stop losses
3. Follow calculated position sizes
4. Don't override your calculations

### Trade Journal
1. Record EVERY trade
2. Include entry, exit, SL, target
3. Note trade conditions/reasons
4. Review monthly for patterns

### Exit Strategy
1. Always plan exits before entering
2. Use Risk/Reward to set targets
3. Consider taking profits at 1:1 ratio
4. Use trailing stops once profitable

---

## 🔄 Workflow Example

```
1. PLAN
   ├─ Use Position Sizer → Determine shares
   ├─ Use Risk/Reward → Determine targets
   └─ Use Stop Loss Manager → Set stop loss

2. EXECUTE
   ├─ Buy shares at calculated entry
   ├─ Set stop loss (hard stop)
   └─ Set targets (partial or full exit)

3. TRACK
   ├─ Monitor in real-time
   ├─ Record in Trade Journal
   └─ Review brokerage costs

4. ANALYZE
   ├─ Click "Statistics" in Trade Journal
   ├─ View win rate, P&L, profit factor
   └─ Identify patterns and improvements

5. EXPORT
   ├─ Export to CSV for analysis
   ├─ Export to Excel for record-keeping
   └─ Export to PDF for sharing/printing
```

---

## 📊 Performance Metrics

The application tracks:
- **Total Trades**: Number of completed trades
- **Win Rate %**: Percentage of profitable trades
- **Average Win**: Average profit on winning trades
- **Average Loss**: Average loss on losing trades
- **Profit Factor**: Total Profit ÷ Total Loss
- **Total P&L**: Overall profit or loss

### Interpreting Results
- **Win Rate > 50%**: More winners than losers
- **Profit Factor > 1.0**: Total profits exceed losses
- **Profit Factor > 2.0**: Excellent trading system

---

## 🎓 PSX-Specific Information

### Pre-configured Charges
- **Broker Commission**: 0.10% (typical for PSX)
- **CDC Charge**: 0.04% (PSX standard)
- **Capital Gains Tax**: 12.5% (Pakistan federal tax)

### Can Be Customized
All charges can be adjusted in the Brokerage tab:
1. Click "Brokerage" tab
2. Modify percentage values
3. Click "Calculate Charges"

### PSX Trading Hours
- **Opening**: 10:00 AM (Monday-Friday)
- **Closing**: 3:00 PM (Monday-Friday)
- **Settlement**: T+2 (trades settle 2 days later)

---

## 📝 File Descriptions

### psx_calculator.py
- **Size**: ~15 KB
- **Lines**: ~600+
- **Purpose**: Complete application with all features
- **Run With**: `python psx_calculator.py`

### requirements.txt
- **Size**: <1 KB
- **Purpose**: List of Python dependencies
- **Install With**: `pip install -r requirements.txt`

### SETUP_INSTRUCTIONS.md
- **Size**: ~20 KB
- **Purpose**: Detailed installation and usage guide
- **Read**: Before first use

### README.md (this file)
- **Size**: ~30 KB
- **Purpose**: Complete feature overview and documentation
- **Reference**: Anytime you need information

---

## 🌟 Advantages Over Alternatives

| Feature | This App | Excel | Spreadsheet | Other Tools |
|---------|----------|-------|------------|------------|
| Portable | ✅ | ❌ | ❌ | ❌ |
| No Installation | ✅ | ❌ | ❌ | ❌ |
| Local Storage | ✅ | ✅ | ✅ | ❌ |
| Easy Export | ✅ | ✅ | ✅ | ❌ |
| Built-in Calc | ✅ | ❌ | ❌ | ✅ |
| Trade Journal | ✅ | ❌ | ❌ | ✅ |
| Statistics | ✅ | ❌ | ❌ | ✅ |
| PSX Charges | ✅ | ❌ | ❌ | ❌ |
| Free | ✅ | ❌ | ✅ | ❌ |

---

## 🎯 What's Included

✅ Complete source code (600+ lines)
✅ Professional GUI application
✅ 5 major calculators
✅ Trade journal with analytics
✅ 3 export formats (CSV, Excel, PDF)
✅ Full setup instructions
✅ Complete documentation
✅ No dependencies on system folders
✅ 100% offline operation
✅ PSX-optimized settings

---

## 🚀 Getting Started Now

1. **Download** the folder
2. **Install Python** from https://www.python.org/downloads/
3. **Run**: `pip install -r requirements.txt`
4. **Start**: `python psx_calculator.py`

**That's it! Start trading!**

---

## 📞 Support & Help

### Common Issues
- See SETUP_INSTRUCTIONS.md → Troubleshooting section
- Check Python version: `python --version`
- Reinstall dependencies: `pip install -r requirements.txt`

### Learning Resources
- Python: https://www.python.org/
- PSX: https://www.psx.com.pk/
- Trading: Various trading education platforms

---

## 📄 License & Terms

- **License**: MIT (Free to use and modify)
- **Cost**: Completely free
- **Support**: Self-help via documentation
- **Warranty**: Provided as-is

---

## ✨ Version History

### v1.0.0 (Current)
✅ Complete trading calculator
✅ 5 major calculators
✅ Trade journal with statistics
✅ Multiple export formats
✅ No system folder dependencies
✅ Full offline operation

---

## 🎉 Ready to Start Trading?

Everything is set up and ready to use!

### Next Steps:
1. ✅ Install Python
2. ✅ Run `pip install -r requirements.txt`
3. ✅ Run `python psx_calculator.py`
4. ✅ Start using the calculators
5. ✅ Record your trades
6. ✅ Review your statistics
7. ✅ Export reports

---

## 💡 Pro Tips

1. **Bookmark targets** - Use Risk/Reward calculator before every trade
2. **Follow position sizer** - Never deviate from calculated sizes
3. **Track everything** - Record all trades in the journal
4. **Review monthly** - Check statistics and identify patterns
5. **Backup regularly** - Copy psx_data/ folder to safe location
6. **Use exports** - Excel is great for analysis and record-keeping

---

**Happy Trading!** 📈🎯

For detailed instructions, see **SETUP_INSTRUCTIONS.md**

---

**PSX Trading Calculator Pro v1.0.0**
*Professional Trading Tools | Local | Secure | Complete*
