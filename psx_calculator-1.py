#!/usr/bin/env python3
"""
PSX Trading Calculator Pro
Complete desktop application for PSX trading calculations
All files saved in program directory - No hardcoded paths
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
import csv

# Try to import openpyxl and reportlab, but make them optional
try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    EXCEL_AVAILABLE = True
except ImportError:
    EXCEL_AVAILABLE = False

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib import colors
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False


class PSXTradingCalculator:
    """Main application class"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("PSX Trading Calculator Pro v1.0.0")
        self.root.geometry("1000x700")
        
        # Get program directory (where script is running)
        self.program_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Create data directory in program folder
        self.data_dir = os.path.join(self.program_dir, "psx_data")
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        
        self.trades_file = os.path.join(self.data_dir, "trades.json")
        self.settings_file = os.path.join(self.data_dir, "settings.json")
        
        # Load settings
        self.settings = self.load_settings()
        
        # Setup GUI
        self.setup_ui()
        
        print(f"✓ Program Directory: {self.program_dir}")
        print(f"✓ Data Directory: {self.data_dir}")
    
    def setup_ui(self):
        """Setup user interface"""
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Create tabs
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)
        self.tab4 = ttk.Frame(self.notebook)
        self.tab5 = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab1, text="Position Sizer")
        self.notebook.add(self.tab2, text="Stop Loss Manager")
        self.notebook.add(self.tab3, text="Risk/Reward")
        self.notebook.add(self.tab4, text="Brokerage")
        self.notebook.add(self.tab5, text="Trade Journal")
        
        self.setup_position_sizer()
        self.setup_stop_loss()
        self.setup_risk_reward()
        self.setup_brokerage()
        self.setup_trade_journal()
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief='sunken')
        status_bar.pack(side='bottom', fill='x')
    
    def setup_position_sizer(self):
        """Position Sizer Tab"""
        frame = ttk.LabelFrame(self.tab1, text="Position Size Calculator", padding=10)
        frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Inputs
        ttk.Label(frame, text="Total Capital (PKR):").grid(row=0, column=0, sticky='w', pady=5)
        self.capital_var = tk.StringVar(value="500000")
        ttk.Entry(frame, textvariable=self.capital_var, width=20).grid(row=0, column=1, sticky='w', pady=5)
        
        ttk.Label(frame, text="Risk % per Trade:").grid(row=1, column=0, sticky='w', pady=5)
        self.risk_pct_var = tk.StringVar(value="2")
        ttk.Entry(frame, textvariable=self.risk_pct_var, width=20).grid(row=1, column=1, sticky='w', pady=5)
        
        ttk.Label(frame, text="Entry Price (PKR):").grid(row=2, column=0, sticky='w', pady=5)
        self.entry_price_var = tk.StringVar(value="1000")
        ttk.Entry(frame, textvariable=self.entry_price_var, width=20).grid(row=2, column=1, sticky='w', pady=5)
        
        ttk.Label(frame, text="Stop Loss Price (PKR):").grid(row=3, column=0, sticky='w', pady=5)
        self.stop_loss_var = tk.StringVar(value="950")
        ttk.Entry(frame, textvariable=self.stop_loss_var, width=20).grid(row=3, column=1, sticky='w', pady=5)
        
        # Calculate button
        ttk.Button(frame, text="Calculate", command=self.calculate_position).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Results
        result_frame = ttk.LabelFrame(frame, text="Results", padding=10)
        result_frame.grid(row=5, column=0, columnspan=2, sticky='ew', pady=10)
        
        ttk.Label(result_frame, text="Risk Amount (PKR):").grid(row=0, column=0, sticky='w')
        self.risk_amount_label = ttk.Label(result_frame, text="0.00", font=('Arial', 11, 'bold'), foreground='green')
        self.risk_amount_label.grid(row=0, column=1, sticky='w')
        
        ttk.Label(result_frame, text="Risk Per Share (PKR):").grid(row=1, column=0, sticky='w')
        self.risk_share_label = ttk.Label(result_frame, text="0.00", font=('Arial', 11, 'bold'), foreground='green')
        self.risk_share_label.grid(row=1, column=1, sticky='w')
        
        ttk.Label(result_frame, text="Shares to Buy:").grid(row=2, column=0, sticky='w')
        self.shares_label = ttk.Label(result_frame, text="0", font=('Arial', 12, 'bold'), foreground='green')
        self.shares_label.grid(row=2, column=1, sticky='w')
    
    def setup_stop_loss(self):
        """Stop Loss Manager Tab"""
        frame = ttk.LabelFrame(self.tab2, text="Stop Loss Manager", padding=10)
        frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        ttk.Label(frame, text="Entry Price (PKR):").grid(row=0, column=0, sticky='w', pady=5)
        self.sl_entry_var = tk.StringVar(value="1000")
        ttk.Entry(frame, textvariable=self.sl_entry_var, width=20).grid(row=0, column=1, sticky='w', pady=5)
        
        ttk.Label(frame, text="Method:").grid(row=1, column=0, sticky='w', pady=5)
        self.sl_method = tk.StringVar(value="manual")
        ttk.Radiobutton(frame, text="Manual", variable=self.sl_method, value="manual").grid(row=1, column=1, sticky='w')
        ttk.Radiobutton(frame, text="Percentage", variable=self.sl_method, value="percentage").grid(row=2, column=1, sticky='w')
        ttk.Radiobutton(frame, text="ATR Based", variable=self.sl_method, value="atr").grid(row=3, column=1, sticky='w')
        
        ttk.Label(frame, text="Stop Loss / Percentage / ATR:").grid(row=4, column=0, sticky='w', pady=5)
        self.sl_value_var = tk.StringVar(value="950")
        ttk.Entry(frame, textvariable=self.sl_value_var, width=20).grid(row=4, column=1, sticky='w', pady=5)
        
        ttk.Label(frame, text="Multiplier (for ATR):").grid(row=5, column=0, sticky='w', pady=5)
        self.sl_multiplier_var = tk.StringVar(value="1.5")
        ttk.Entry(frame, textvariable=self.sl_multiplier_var, width=20).grid(row=5, column=1, sticky='w', pady=5)
        
        ttk.Button(frame, text="Calculate", command=self.calculate_stop_loss).grid(row=6, column=0, columnspan=2, pady=10)
        
        # Results
        result_frame = ttk.LabelFrame(frame, text="Stop Loss Result", padding=10)
        result_frame.grid(row=7, column=0, columnspan=2, sticky='ew', pady=10)
        
        ttk.Label(result_frame, text="Stop Loss Price:").grid(row=0, column=0, sticky='w')
        self.sl_result_label = ttk.Label(result_frame, text="0.00", font=('Arial', 11, 'bold'), foreground='blue')
        self.sl_result_label.grid(row=0, column=1, sticky='w')
        
        ttk.Label(result_frame, text="Risk Per Share:").grid(row=1, column=0, sticky='w')
        self.sl_risk_label = ttk.Label(result_frame, text="0.00", font=('Arial', 11, 'bold'), foreground='blue')
        self.sl_risk_label.grid(row=1, column=1, sticky='w')
    
    def setup_risk_reward(self):
        """Risk/Reward Calculator Tab"""
        frame = ttk.LabelFrame(self.tab3, text="Risk/Reward Calculator", padding=10)
        frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        ttk.Label(frame, text="Entry Price (PKR):").grid(row=0, column=0, sticky='w', pady=5)
        self.rr_entry_var = tk.StringVar(value="1000")
        ttk.Entry(frame, textvariable=self.rr_entry_var, width=20).grid(row=0, column=1, sticky='w', pady=5)
        
        ttk.Label(frame, text="Stop Loss (PKR):").grid(row=1, column=0, sticky='w', pady=5)
        self.rr_sl_var = tk.StringVar(value="950")
        ttk.Entry(frame, textvariable=self.rr_sl_var, width=20).grid(row=1, column=1, sticky='w', pady=5)
        
        ttk.Button(frame, text="Calculate Targets", command=self.calculate_risk_reward).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Results
        result_frame = ttk.LabelFrame(frame, text="Target Prices", padding=10)
        result_frame.grid(row=3, column=0, columnspan=2, sticky='ew', pady=10)
        
        ratios = ["1:1", "1:2", "1:3"]
        for i, ratio in enumerate(ratios):
            ttk.Label(result_frame, text=f"{ratio} Ratio:").grid(row=i, column=0, sticky='w', pady=5)
            label = ttk.Label(result_frame, text="0.00", font=('Arial', 10, 'bold'), foreground='purple')
            label.grid(row=i, column=1, sticky='w')
            setattr(self, f"target_{ratio.replace(':', '')}_label", label)
    
    def setup_brokerage(self):
        """Brokerage Calculator Tab"""
        frame = ttk.LabelFrame(self.tab4, text="PSX Brokerage Calculator", padding=10)
        frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        ttk.Label(frame, text="Entry Price (PKR):").grid(row=0, column=0, sticky='w', pady=5)
        self.br_entry_var = tk.StringVar(value="1000")
        ttk.Entry(frame, textvariable=self.br_entry_var, width=20).grid(row=0, column=1, sticky='w', pady=5)
        
        ttk.Label(frame, text="Exit Price (PKR):").grid(row=1, column=0, sticky='w', pady=5)
        self.br_exit_var = tk.StringVar(value="1100")
        ttk.Entry(frame, textvariable=self.br_exit_var, width=20).grid(row=1, column=1, sticky='w', pady=5)
        
        ttk.Label(frame, text="Quantity (Shares):").grid(row=2, column=0, sticky='w', pady=5)
        self.br_qty_var = tk.StringVar(value="500")
        ttk.Entry(frame, textvariable=self.br_qty_var, width=20).grid(row=2, column=1, sticky='w', pady=5)
        
        ttk.Label(frame, text="Broker Commission (%):").grid(row=3, column=0, sticky='w', pady=5)
        self.br_commission_var = tk.StringVar(value="0.10")
        ttk.Entry(frame, textvariable=self.br_commission_var, width=20).grid(row=3, column=1, sticky='w', pady=5)
        
        ttk.Label(frame, text="CDC Charge (%):").grid(row=4, column=0, sticky='w', pady=5)
        self.br_cdc_var = tk.StringVar(value="0.04")
        ttk.Entry(frame, textvariable=self.br_cdc_var, width=20).grid(row=4, column=1, sticky='w', pady=5)
        
        ttk.Label(frame, text="Capital Gains Tax (%):").grid(row=5, column=0, sticky='w', pady=5)
        self.br_tax_var = tk.StringVar(value="12.5")
        ttk.Entry(frame, textvariable=self.br_tax_var, width=20).grid(row=5, column=1, sticky='w', pady=5)
        
        ttk.Button(frame, text="Calculate Charges", command=self.calculate_brokerage).grid(row=6, column=0, columnspan=2, pady=10)
        
        # Results
        result_frame = ttk.LabelFrame(frame, text="Results", padding=10)
        result_frame.grid(row=7, column=0, columnspan=2, sticky='ew', pady=10)
        
        self.br_results_text = tk.Text(result_frame, height=10, width=50)
        self.br_results_text.pack(fill='both', expand=True)
    
    def setup_trade_journal(self):
        """Trade Journal Tab"""
        frame = ttk.Frame(self.tab5, padding=10)
        frame.pack(fill='both', expand=True)
        
        # Input frame
        input_frame = ttk.LabelFrame(frame, text="Add Trade", padding=10)
        input_frame.pack(fill='x', pady=5)
        
        ttk.Label(input_frame, text="Stock:").grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.tj_stock_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.tj_stock_var, width=15).grid(row=0, column=1, sticky='w', padx=5, pady=5)
        
        ttk.Label(input_frame, text="Entry:").grid(row=0, column=2, sticky='w', padx=5, pady=5)
        self.tj_entry_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.tj_entry_var, width=15).grid(row=0, column=3, sticky='w', padx=5, pady=5)
        
        ttk.Label(input_frame, text="Exit:").grid(row=0, column=4, sticky='w', padx=5, pady=5)
        self.tj_exit_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.tj_exit_var, width=15).grid(row=0, column=5, sticky='w', padx=5, pady=5)
        
        ttk.Label(input_frame, text="Qty:").grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.tj_qty_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.tj_qty_var, width=15).grid(row=1, column=1, sticky='w', padx=5, pady=5)
        
        ttk.Label(input_frame, text="SL:").grid(row=1, column=2, sticky='w', padx=5, pady=5)
        self.tj_sl_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.tj_sl_var, width=15).grid(row=1, column=3, sticky='w', padx=5, pady=5)
        
        ttk.Label(input_frame, text="Target:").grid(row=1, column=4, sticky='w', padx=5, pady=5)
        self.tj_target_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.tj_target_var, width=15).grid(row=1, column=5, sticky='w', padx=5, pady=5)
        
        ttk.Button(input_frame, text="Add Trade", command=self.add_trade).grid(row=2, column=0, columnspan=6, pady=10)
        
        # Display frame
        display_frame = ttk.LabelFrame(frame, text="Trade History", padding=10)
        display_frame.pack(fill='both', expand=True, pady=5)
        
        # Treeview for trades
        columns = ("Date", "Stock", "Entry", "Exit", "Qty", "SL", "Target", "P&L", "Status")
        self.trades_tree = ttk.Treeview(display_frame, columns=columns, height=12)
        self.trades_tree.column("#0", width=0, stretch=tk.NO)
        for col in columns:
            self.trades_tree.column(col, anchor=tk.CENTER, width=80)
            self.trades_tree.heading(col, text=col)
        
        scrollbar = ttk.Scrollbar(display_frame, orient='vertical', command=self.trades_tree.yview)
        self.trades_tree.configure(yscroll=scrollbar.set)
        
        self.trades_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Export buttons
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill='x', pady=5)
        
        ttk.Button(button_frame, text="Export to CSV", command=self.export_csv).pack(side='left', padx=5)
        if EXCEL_AVAILABLE:
            ttk.Button(button_frame, text="Export to Excel", command=self.export_excel).pack(side='left', padx=5)
        if PDF_AVAILABLE:
            ttk.Button(button_frame, text="Export to PDF", command=self.export_pdf).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Refresh", command=self.load_trades).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Statistics", command=self.show_statistics).pack(side='left', padx=5)
        
        # Load trades
        self.load_trades()
    
    def calculate_position(self):
        """Calculate position size"""
        try:
            capital = float(self.capital_var.get())
            risk_pct = float(self.risk_pct_var.get())
            entry = float(self.entry_price_var.get())
            sl = float(self.stop_loss_var.get())
            
            if sl >= entry:
                messagebox.showerror("Error", "Stop Loss must be less than Entry Price")
                return
            
            risk_amount = capital * (risk_pct / 100)
            risk_per_share = entry - sl
            shares = Decimal(str(risk_amount)) / Decimal(str(risk_per_share))
            shares = int(shares.quantize(Decimal('1'), rounding=ROUND_HALF_UP))
            
            self.risk_amount_label.config(text=f"{risk_amount:,.2f}")
            self.risk_share_label.config(text=f"{risk_per_share:.2f}")
            self.shares_label.config(text=f"{shares:,}")
            
            self.status_var.set(f"✓ Position Size: {shares:,} shares")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def calculate_stop_loss(self):
        """Calculate stop loss"""
        try:
            entry = float(self.sl_entry_var.get())
            method = self.sl_method.get()
            
            if method == "manual":
                sl = float(self.sl_value_var.get())
            elif method == "percentage":
                pct = float(self.sl_value_var.get())
                sl = entry - (entry * pct / 100)
            else:  # atr
                atr = float(self.sl_value_var.get())
                multiplier = float(self.sl_multiplier_var.get())
                sl = entry - (atr * multiplier)
            
            risk_per_share = entry - sl
            
            self.sl_result_label.config(text=f"{sl:.2f}")
            self.sl_risk_label.config(text=f"{risk_per_share:.2f}")
            
            self.status_var.set(f"✓ Stop Loss: {sl:.2f} (Risk: {risk_per_share:.2f})")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def calculate_risk_reward(self):
        """Calculate risk/reward targets"""
        try:
            entry = float(self.rr_entry_var.get())
            sl = float(self.rr_sl_var.get())
            
            if sl >= entry:
                messagebox.showerror("Error", "Stop Loss must be less than Entry Price")
                return
            
            risk = entry - sl
            
            targets = {
                "1:1": entry + risk,
                "1:2": entry + (risk * 2),
                "1:3": entry + (risk * 3)
            }
            
            for ratio, price in targets.items():
                label_name = f"target_{ratio.replace(':', '')}_label"
                getattr(self, label_name).config(text=f"{price:.2f}")
            
            self.status_var.set("✓ Risk/Reward targets calculated")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def calculate_brokerage(self):
        """Calculate brokerage and charges"""
        try:
            entry = float(self.br_entry_var.get())
            exit_price = float(self.br_exit_var.get())
            qty = int(self.br_qty_var.get())
            comm_pct = float(self.br_commission_var.get()) / 100
            cdc_pct = float(self.br_cdc_var.get()) / 100
            tax_pct = float(self.br_tax_var.get()) / 100
            
            entry_value = entry * qty
            exit_value = exit_price * qty
            
            # Entry charges
            entry_comm = entry_value * comm_pct
            entry_cdc = entry_value * cdc_pct
            total_entry_cost = entry_value + entry_comm + entry_cdc
            
            # Exit charges
            exit_comm = exit_value * comm_pct
            exit_cdc = exit_value * cdc_pct
            gross_pnl = exit_value - entry_value
            tax = max(0, gross_pnl * tax_pct)
            total_exit_cost = exit_comm + exit_cdc + tax
            
            net_pnl = gross_pnl - (entry_comm + entry_cdc) - total_exit_cost
            roi = (net_pnl / entry_value * 100) if entry_value > 0 else 0
            
            result_text = f"""
Entry Value:           PKR {entry_value:,.2f}
Entry Charges:
  - Broker Commission: PKR {entry_comm:,.2f}
  - CDC Charge:        PKR {entry_cdc:,.2f}
Total Entry Cost:      PKR {total_entry_cost:,.2f}

Exit Value:            PKR {exit_value:,.2f}
Exit Charges:
  - Broker Commission: PKR {exit_comm:,.2f}
  - CDC Charge:        PKR {exit_cdc:,.2f}
  - Capital Gains Tax: PKR {tax:,.2f}

Gross Profit:          PKR {gross_pnl:,.2f}
Total Charges:         PKR {entry_comm + entry_cdc + exit_comm + exit_cdc + tax:,.2f}
NET PROFIT/LOSS:       PKR {net_pnl:,.2f}
ROI %:                 {roi:.2f}%
            """
            
            self.br_results_text.delete('1.0', tk.END)
            self.br_results_text.insert('1.0', result_text.strip())
            
            self.status_var.set(f"✓ Net P&L: PKR {net_pnl:,.2f}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def add_trade(self):
        """Add trade to journal"""
        try:
            stock = self.tj_stock_var.get().strip()
            entry = float(self.tj_entry_var.get())
            exit_price = float(self.tj_exit_var.get())
            qty = int(self.tj_qty_var.get())
            sl = float(self.tj_sl_var.get())
            target = float(self.tj_target_var.get())
            
            if not stock:
                messagebox.showerror("Error", "Please enter stock name")
                return
            
            pnl = (exit_price - entry) * qty
            pnl_pct = ((exit_price - entry) / entry * 100) if entry > 0 else 0
            
            status = "✓ Won" if pnl > 0 else "✗ Lost" if pnl < 0 else "= Even"
            
            trades = self.load_trades_data()
            trade = {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "stock": stock,
                "entry": entry,
                "exit": exit_price,
                "qty": qty,
                "sl": sl,
                "target": target,
                "pnl": pnl,
                "pnl_pct": pnl_pct,
                "status": status
            }
            trades.append(trade)
            
            with open(self.trades_file, 'w') as f:
                json.dump(trades, f, indent=2)
            
            self.load_trades()
            
            # Clear inputs
            self.tj_stock_var.set("")
            self.tj_entry_var.set("")
            self.tj_exit_var.set("")
            self.tj_qty_var.set("")
            self.tj_sl_var.set("")
            self.tj_target_var.set("")
            
            self.status_var.set(f"✓ Trade added: {stock} - P&L: PKR {pnl:,.0f}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid trade data")
    
    def load_trades_data(self):
        """Load trades from JSON"""
        if os.path.exists(self.trades_file):
            with open(self.trades_file, 'r') as f:
                return json.load(f)
        return []
    
    def load_trades(self):
        """Load and display trades"""
        # Clear tree
        for item in self.trades_tree.get_children():
            self.trades_tree.delete(item)
        
        trades = self.load_trades_data()
        
        for i, trade in enumerate(trades):
            values = (
                trade['date'][:10],
                trade['stock'],
                f"{trade['entry']:.2f}",
                f"{trade['exit']:.2f}",
                str(trade['qty']),
                f"{trade['sl']:.2f}",
                f"{trade['target']:.2f}",
                f"{trade['pnl']:,.0f}",
                trade['status']
            )
            self.trades_tree.insert('', 'end', values=values)
    
    def load_settings(self):
        """Load settings from JSON"""
        if os.path.exists(self.settings_file):
            with open(self.settings_file, 'r') as f:
                return json.load(f)
        
        default_settings = {
            "broker_commission": 0.10,
            "cdc_charge": 0.04,
            "capital_gains_tax": 12.5
        }
        
        with open(self.settings_file, 'w') as f:
            json.dump(default_settings, f, indent=2)
        
        return default_settings
    
    def export_csv(self):
        """Export trades to CSV"""
        try:
            trades = self.load_trades_data()
            if not trades:
                messagebox.showwarning("Warning", "No trades to export")
                return
            
            filename = os.path.join(self.data_dir, f"trades_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
            
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Date', 'Stock', 'Entry', 'Exit', 'Qty', 'SL', 'Target', 'P&L', 'Status'])
                
                for trade in trades:
                    writer.writerow([
                        trade['date'],
                        trade['stock'],
                        trade['entry'],
                        trade['exit'],
                        trade['qty'],
                        trade['sl'],
                        trade['target'],
                        trade['pnl'],
                        trade['status']
                    ])
            
            messagebox.showinfo("Success", f"Exported to:\n{filename}")
            self.status_var.set(f"✓ Exported CSV: {os.path.basename(filename)}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Export failed: {str(e)}")
    
    def export_excel(self):
        """Export trades to Excel"""
        if not EXCEL_AVAILABLE:
            messagebox.showerror("Error", "openpyxl not installed. Run: pip install openpyxl")
            return
        
        try:
            trades = self.load_trades_data()
            if not trades:
                messagebox.showwarning("Warning", "No trades to export")
                return
            
            filename = os.path.join(self.data_dir, f"trades_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx")
            
            wb = Workbook()
            ws = wb.active
            ws.title = "Trades"
            
            # Headers
            headers = ['Date', 'Stock', 'Entry', 'Exit', 'Qty', 'SL', 'Target', 'P&L', 'Status']
            ws.append(headers)
            
            # Data
            for trade in trades:
                ws.append([
                    trade['date'],
                    trade['stock'],
                    trade['entry'],
                    trade['exit'],
                    trade['qty'],
                    trade['sl'],
                    trade['target'],
                    trade['pnl'],
                    trade['status']
                ])
            
            wb.save(filename)
            messagebox.showinfo("Success", f"Exported to:\n{filename}")
            self.status_var.set(f"✓ Exported Excel: {os.path.basename(filename)}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Export failed: {str(e)}")
    
    def export_pdf(self):
        """Export trades to PDF"""
        if not PDF_AVAILABLE:
            messagebox.showerror("Error", "reportlab not installed. Run: pip install reportlab")
            return
        
        try:
            trades = self.load_trades_data()
            if not trades:
                messagebox.showwarning("Warning", "No trades to export")
                return
            
            filename = os.path.join(self.data_dir, f"trades_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf")
            
            doc = SimpleDocTemplate(filename, pagesize=letter)
            styles = getSampleStyleSheet()
            
            # Title
            elements = [Paragraph("Trade Journal Report", styles['Title'])]
            elements.append(Spacer(1, 12))
            
            # Table data
            table_data = [['Date', 'Stock', 'Entry', 'Exit', 'Qty', 'SL', 'Target', 'P&L', 'Status']]
            for trade in trades:
                table_data.append([
                    trade['date'][:10],
                    trade['stock'],
                    f"{trade['entry']:.2f}",
                    f"{trade['exit']:.2f}",
                    str(trade['qty']),
                    f"{trade['sl']:.2f}",
                    f"{trade['target']:.2f}",
                    f"{trade['pnl']:,.0f}",
                    trade['status']
                ])
            
            # Create table
            table = Table(table_data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 8),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            
            elements.append(table)
            doc.build(elements)
            
            messagebox.showinfo("Success", f"Exported to:\n{filename}")
            self.status_var.set(f"✓ Exported PDF: {os.path.basename(filename)}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Export failed: {str(e)}")
    
    def show_statistics(self):
        """Show trade statistics"""
        trades = self.load_trades_data()
        
        if not trades:
            messagebox.showinfo("Statistics", "No trades recorded yet")
            return
        
        total_trades = len(trades)
        winning = [t for t in trades if t['pnl'] > 0]
        losing = [t for t in trades if t['pnl'] < 0]
        even = [t for t in trades if t['pnl'] == 0]
        
        win_count = len(winning)
        loss_count = len(losing)
        win_rate = (win_count / total_trades * 100) if total_trades > 0 else 0
        
        total_pnl = sum(t['pnl'] for t in trades)
        total_profit = sum(t['pnl'] for t in winning)
        total_loss = sum(t['pnl'] for t in losing)
        
        avg_win = (total_profit / win_count) if win_count > 0 else 0
        avg_loss = (total_loss / loss_count) if loss_count > 0 else 0
        profit_factor = (total_profit / abs(total_loss)) if total_loss != 0 else 0
        
        stats = f"""
TRADE JOURNAL STATISTICS

Total Trades:          {total_trades}
Winning Trades:        {win_count}
Losing Trades:         {loss_count}
Even Trades:           {len(even)}

Win Rate:              {win_rate:.1f}%
Average Win:           PKR {avg_win:,.0f}
Average Loss:          PKR {avg_loss:,.0f}
Profit Factor:         {profit_factor:.2f}

Total Profit:          PKR {total_profit:,.0f}
Total Loss:            PKR {total_loss:,.0f}
NET P&L:               PKR {total_pnl:,.0f}
        """
        
        messagebox.showinfo("Statistics", stats.strip())


def main():
    """Main entry point"""
    root = tk.Tk()
    app = PSXTradingCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
