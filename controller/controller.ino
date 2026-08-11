#include <Arduino.h>
#include <IRremote.h>

// 定義接收器接在 Pin 2
const int IR_RECEIVE_PIN = 7;

void setup() {
    Serial.begin(9600);

    // 啟動紅外線接收器，並開啟內建 LED (Pin 13) 作為接收指示燈
    IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK);

    Serial.println("IR Decoder is Ready!");
    Serial.println("Please press a button on your remote...");
}

void loop() {
    // 如果成功接收到紅外線訊號，且解碼完成
    if (IrReceiver.decode()) {
        int command = IrReceiver.decodedIRData.command;

        /*Serial.print("Protocol: ");
        Serial.print(getProtocolString(IrReceiver.decodedIRData.protocol));
        Serial.print(" | Command Code: 0x");
        Serial.println(IrReceiver.decodedIRData.command, HEX);*/

        if (command == 0x45) {
            Serial.println("BTN_WORK");
        }

        IrReceiver.resume();
    }
}
