import discord
from discord.ext import commands, tasks
from datetime import datetime
import pyautogui
import os
import json
import tkinter as tk
from tkinter import messagebox
import threading
import asyncio

CONFIG_FILE = "config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {
        "TOKEN": "",
        "CHANNEL_ID": "",
        "COMMAND_PREFIX": "!",
        "INTERVAL": 30,
        "CAPTURE_COMMAND": "c"
    }

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

class SettingsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Discord Cap Settings")
        self.root.geometry("400x450")
        self.bot_thread = None
        self.bot_instance = None
        
        config = load_config()

        # Status
        self.status_label = tk.Label(root, text="Status: Offline", fg="red", font=("Arial", 10, "bold"))
        self.status_label.pack(pady=10)

        # Token
        tk.Label(root, text="Bot Token:").pack()
        self.token_entry = tk.Entry(root, width=40, show="*")
        self.token_entry.insert(0, config.get("TOKEN", ""))
        self.token_entry.pack(pady=5)

        # Channel ID
        tk.Label(root, text="Channel ID:").pack()
        self.channel_entry = tk.Entry(root, width=40)
        self.channel_entry.insert(0, str(config.get("CHANNEL_ID", "")))
        self.channel_entry.pack(pady=5)

        # Prefix
        tk.Label(root, text="Command Prefix:").pack()
        self.prefix_entry = tk.Entry(root, width=10)
        self.prefix_entry.insert(0, config.get("COMMAND_PREFIX", "!"))
        self.prefix_entry.pack(pady=5)

        # Interval
        tk.Label(root, text="Auto Report Interval (minutes):").pack()
        self.interval_entry = tk.Entry(root, width=10)
        self.interval_entry.insert(0, str(config.get("INTERVAL", 30)))
        self.interval_entry.pack(pady=5)

        # Command Name
        tk.Label(root, text="Capture Command Name:").pack()
        self.command_entry = tk.Entry(root, width=10)
        self.command_entry.insert(0, config.get("CAPTURE_COMMAND", "c"))
        self.command_entry.pack(pady=5)

        # Buttons
        self.start_button = tk.Button(root, text="Start Bot", command=self.toggle_bot, bg="#4CAF50", fg="white", width=15)
        self.start_button.pack(pady=20)

    def toggle_bot(self):
        if self.bot_instance and not self.bot_instance.is_closed():
            self.stop_bot()
        else:
            self.start_bot()

    def start_bot(self):
        token = self.token_entry.get().strip()
        channel_id = self.channel_entry.get().strip()
        prefix = self.prefix_entry.get().strip()
        interval = self.interval_entry.get().strip()
        cmd_name = self.command_entry.get().strip()

        if not token or not channel_id:
            messagebox.showerror("Error", "Please enter Token and Channel ID")
            return

        try:
            channel_id = int(channel_id)
            interval = int(interval)
        except ValueError:
            messagebox.showerror("Error", "Channel ID and Interval must be numbers")
            return

        config = {
            "TOKEN": token,
            "CHANNEL_ID": channel_id,
            "COMMAND_PREFIX": prefix,
            "INTERVAL": interval,
            "CAPTURE_COMMAND": cmd_name
        }
        save_config(config)

        self.status_label.config(text="Status: Starting...", fg="orange")
        self.start_button.config(text="Stop Bot", bg="#f44336")
        
        self.bot_thread = threading.Thread(target=self.run_bot_logic, args=(config,), daemon=True)
        self.bot_thread.start()

    def run_bot_logic(self, config):
        try:
            import asyncio
            # Create a new loop for the thread
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            intents = discord.Intents.default()
            intents.message_content = True
            self.bot_instance = commands.Bot(command_prefix=config["COMMAND_PREFIX"], intents=intents)

            @tasks.loop(minutes=config["INTERVAL"])
            async def auto_report():
                channel = self.bot_instance.get_channel(config["CHANNEL_ID"])
                if channel:
                    path = f"auto_{config['CHANNEL_ID']}.png"
                    try:
                        pyautogui.screenshot(path)
                        await channel.send(f"🕒 **Auto Report**:", file=discord.File(path))
                        os.remove(path)
                    except: pass

            @self.bot_instance.event
            async def on_ready():
                self.root.after(0, lambda: self.status_label.config(text=f"Status: Online ({self.bot_instance.user.name})", fg="green"))
                if not auto_report.is_running():
                    auto_report.start()

            @self.bot_instance.command(name=config["CAPTURE_COMMAND"])
            async def capture(ctx):
                path = "manual_ss.png"
                try:
                    pyautogui.screenshot(path)
                    await ctx.send(file=discord.File(path))
                    os.remove(path)
                except Exception as e:
                    await ctx.send(f"Error: {e}")

            loop.run_until_complete(self.bot_instance.start(config["TOKEN"]))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Bot Error", str(e)))
            self.root.after(0, self.stop_bot)

    def stop_bot(self):
        if self.bot_instance:
            # We need to close the bot from the correct loop
            future = asyncio.run_coroutine_threadsafe(self.bot_instance.close(), self.bot_instance.loop)
            try:
                future.result(timeout=5)
            except:
                pass
        
        self.status_label.config(text="Status: Offline", fg="red")
        self.start_button.config(text="Start Bot", bg="#4CAF50")


if __name__ == "__main__":
    root = tk.Tk()
    gui = SettingsGUI(root)
    root.mainloop()
