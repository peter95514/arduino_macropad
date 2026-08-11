import serial
import subprocess
import webbrowser
import time
import os

# import pyautogui

# 請根據你的 Arduino 實際連接的埠號進行修改
# Windows 通常是 COM3, COM4 等
SERIAL_PORT = "COM3"
BAUD_RATE = 9600


def open_work_env():
    print("啟動工作所需程序...")
    subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe"])

def open_yt():
    print("啟動YT...")
    url = "https://www.youtube.com"
    edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
    edge_browser = webbrowser.get(edge_path)
    edge_browser.open(url)

def init():
    print("INIT...")
    dc_path = r"C:\Users\kuany\AppData\Local\Discord\app-1.0.9251\Discord.exe"
    subprocess.Popen(
    [dc_path],
    stdout=subprocess.DEVNULL,  # 隱藏一般輸出
    stderr=subprocess.DEVNULL,  # 隱藏錯誤輸出
    creationflags=subprocess.CREATE_NO_WINDOW  # (選用) Windows 專屬：避免彈出黑框
    )
    subprocess.Popen([r"C:\Users\kuany\AppData\Local\NGENUITY\current\NGENUITY.exe"])


def main():
    print(f"嘗試連接至 {SERIAL_PORT}...")
    try:
        # 建立與 Arduino 的連線
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
        print("連線成功！等待硬體指令中...")
    except Exception as e:
        print(f"連線失敗，請檢查 COM 埠: {e}")
        return

    while True:
        command = ser.readline().decode('utf-8').strip()
        
        # 只要走到下一行，代表一定有收到完整指令了
        if command:  # 確保收到的不是空字串
            print(f"收到指令: {command}")

            if command == "BTN_WORK":
                open_work_env()
            elif command == "OPEN_YT":
                open_yt()
            elif command == "INIT":
                init()


if __name__ == "__main__":
    main()
