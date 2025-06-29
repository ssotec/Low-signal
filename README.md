# Low-signal

Experimental Arduino sketch for basic EEPROM testing and I2C bus commands.

## Usage

1. Open `sketch_apr21e.ino` in the Arduino IDE or build with [`arduino-cli`](https://arduino.github.io/arduino-cli/):

   ```sh
   arduino-cli compile --fqbn <board> .
   arduino-cli upload --port <port> --fqbn <board> .
   ```

2. Connect to the board's serial port at `9600` baud.
3. Send one of the commands below, ending with a newline:
   - `i2cdetect -y <bus>` – scan the specified I2C bus.
   - `i2cdump -y <bus> 0x<addr>` – dump 256 bytes starting at `addr`.
   - `i2cset -y <bus> 0x<addr> 0x<reg> 0x<value>` – write a byte.
   - `i2cget -y <bus> 0x<addr> 0x<reg>` – read a byte.

During `setup()` the sketch clears three EEPROM devices. It then writes a sample
string to `0x0010` on the first EEPROM; uncomment the other calls in the source
if you need to write to additional devices.

## Project status

This repository is a personal experiment. It is a work in progress and not
officially supported. Use it at your own risk.
