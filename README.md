# DiscordCap (Screen Capture Discord Bot)

[ไทย] | [English]

---

## 🇹🇭 ภาษาไทย

### รายละเอียดโครงการ
**DiscordCap** เป็นแอปพลิเคชันบอทสำหรับ Discord ที่พัฒนาด้วยภาษา Python มีวัตถุประสงค์เพื่ออำนวยความสะดวกในการบันทึกภาพหน้าจอ (Screenshot) และส่งข้อมูลภาพไปยังช่องทางการสื่อสาร (Channel) ใน Discord ที่กำหนดไว้โดยอัตโนมัติ เหมาะสำหรับการตรวจสอบสถานะการทำงานของคอมพิวเตอร์ผ่านทางไกล

### คุณสมบัติหลัก
- **การบันทึกภาพตามคำสั่ง (Manual Capture):** สามารถสั่งการให้บอทบันทึกภาพหน้าจอได้ทันทีผ่านคำสั่งใน Discord
- **การรายงานผลอัตโนมัติ (Auto Report):** ระบบจะดำเนินการบันทึกและส่งภาพหน้าจอตามช่วงเวลาที่ผู้ใช้กำหนด (Scheduled Interval)
- **ส่วนขยายการตั้งค่า (Graphical User Interface):** รองรับการตั้งค่าผ่านหน้าจอ GUI เพื่อความสะดวกในการระบุ Bot Token และ Channel ID โดยไม่จำเป็นต้องปรับแก้รหัสต้นฉบับ (Source Code)

### ขั้นตอนการติดตั้ง
1. ดำเนินการดาวน์โหลดรหัสต้นฉบับจาก Repository
2. ติดตั้งไลบรารีที่จำเป็นผ่าน Command Prompt หรือ Terminal:
   ```bash
   pip install -r requirements.txt
   ```
3. เริ่มการทำงานของแอปพลิเคชัน:
   ```bash
   python Discord_Cap.py
   ```
4. ระบุข้อมูล **Bot Token** และ **Channel ID** ในหน้าต่างการตั้งค่า
5. เลือก **Start Bot** เพื่อเริ่มต้นการทำงาน

### คำสั่งการใช้งาน
- `!c` (ค่าเริ่มต้น): คำสั่งสำหรับบันทึกภาพหน้าจอและส่งไปยัง Discord ทันที

### วิธีการตั้งค่า Discord Bot
1. **สร้าง Application:** ไปที่ [Discord Developer Portal](https://discord.com/developers/applications)
2. **สร้าง Bot:** กดที่เมนู "Bot" จากนั้นกด "Reset Token" (หรือ "Copy Token") เพื่อรับ **Bot Token**
3. **เปิดสิทธิ์ Intent:** เลื่อนลงมาที่หัวข้อ **Privileged Gateway Intents** แล้วเปิด **Message Content Intent** (จำเป็นอย่างยิ่ง)
4. **เชิญบอทเข้า Server:**
   - ไปที่เมนู "OAuth2" -> "URL Generator"
   - ติ๊กเลือก `bot`
   - ใน Bot Permissions ติ๊กเลือก `Send Messages`, `Attach Files`, and `Read Message History`
   - คัดลอก URL ไปวางในเบราว์เซอร์แล้วเลือก Server ที่ต้องการ
5. **หา Channel ID:** 
   - เปิด Discord Settings -> Advanced -> เปิด **Developer Mode**
   - คลิกขวาที่ห้อง (Channel) ที่ต้องการ แล้วเลือก **Copy Channel ID**

---

## 🇺🇸 English

### Project Description
**DiscordCap** is a Python-based Discord bot designed to facilitate remote screen monitoring. It allows users to capture screenshots and automatically transmit them to a designated Discord channel, making it an efficient tool for remote system status checks.

### Key Features
- **Manual Capture:** Instantly trigger a screen capture via a specific Discord command.
- **Auto Report:** Periodically captures and sends screenshots at user-defined intervals.
- **Configuration GUI:** User-friendly interface for managing Bot Token and Channel ID without modifying the source code.

### Installation Guide
1. Download the source code from this repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the application:
   ```bash
   python Discord_Cap.py
   ```
4. Enter your **Bot Token** and **Channel ID** in the configuration window.
5. Click **Start Bot** to initiate the service.

### Commands
- `!c` (default): Manual trigger for instant screen capture and delivery.

### Discord Bot Setup
1. **Create Application:** Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. **Create Bot:** Navigate to the "Bot" tab and click "Reset Token" (or "Copy Token") to get your **Bot Token**.
3. **Enable Intents:** Scroll down to **Privileged Gateway Intents** and enable **Message Content Intent** (Crucial).
4. **Invite Bot:**
   - Go to "OAuth2" -> "URL Generator".
   - Select `bot` scope.
   - In Bot Permissions, select `Send Messages`, `Attach Files`, and `Read Message History`.
   - Copy the generated URL into your browser to invite the bot to your server.
5. **Get Channel ID:** 
   - Open Discord Settings -> Advanced -> Enable **Developer Mode**.
   - Right-click the desired channel and select **Copy Channel ID**.

---

## ⚠️ ข้อควรระวัง / Disclaimer
แอปพลิเคชันนี้พัฒนาขึ้นเพื่อวัตถุประสงค์ในการใช้งานส่วนบุคคลเท่านั้น ผู้ใช้งานควรศึกษาและปฏิบัติตามข้อตกลงการใช้งานของ Discord (ToS) และเคารพในสิทธิความเป็นส่วนตัวของผู้อื่นขณะใช้งานระบบบันทึกภาพหน้าจอ

This application is intended for personal use only. Users are responsible for complying with Discord's Terms of Service and respecting the privacy of others while using screen capture features.
