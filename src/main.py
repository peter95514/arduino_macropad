import serial
import subprocess

# import pyautogui

# 請根據你的 Arduino 實際連接的埠號進行修改
# Windows 通常是 COM3, COM4 等
SERIAL_PORT = "/dev/ttyACM0"
BAUD_RATE = 9600


def open_work_env():
    print("啟動工作所需程序...")


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
        # 如果序列埠有資料進來
        if ser.in_waiting > 0:
            # 讀取資料、解碼並去除頭尾空白與換行符號
            command = ser.readline().decode("utf-8").strip()
            print(f"收到指令: {command}")

            # 根據收到的字串執行對應功能
            if command == "BTN_WORK":
                open_work_env()


if __name__ == "__main__":
    main()
