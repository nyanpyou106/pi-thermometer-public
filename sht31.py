import time
import smbus
import json

"""
ピン接続
V 1番 SDA 3番 SCL 5番 GND 6番 
"""

def tempChanger(msb, lsb):
    """温度変換"""
    mlsb = ((msb << 8) | lsb)
    return (-45 + 175 * int(str(mlsb), 10) / (pow(2, 16) - 1))

def humidChanger(msb, lsb):
    """湿度変換"""
    mlsb = ((msb << 8) | lsb)
    return (100 * int(str(mlsb), 10) / (pow(2, 16) - 1))

def get_temperature_data():
    """SHT31から温度データを取得し、温度をJSONで返す"""
    i2c = smbus.SMBus(1)
    i2c_addr = 0x45

    i2c.write_byte_data(i2c_addr, 0x24, 0x00)
    # 測定終了まで待つ
    time.sleep(1)
    data = i2c.read_i2c_block_data(i2c_addr, 0x00, 6)
    temperature = tempChanger(data[0], data[1])
    return {"room": str(temperature)[0:4]}

if __name__ == "__main__":
    print(get_temperature_data())