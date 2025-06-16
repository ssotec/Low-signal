import unittest

# Helper functions replicating Arduino command parsing logic

def parse_i2cdetect(cmd):
    prefix_index = cmd.find("-y ")
    if prefix_index != -1:
        bus_string = cmd[prefix_index + 3:]
        return int(bus_string)
    raise ValueError("Invalid command")


def parse_i2cset(cmd):
    prefix_index = cmd.find("-y ")
    if prefix_index == -1:
        raise ValueError("Invalid command")
    addr_index = cmd.find("0x", prefix_index + 3)
    reg_index = cmd.find("0x", addr_index + 2)
    value_index = cmd.find("0x", reg_index + 2)
    bus = int(cmd[prefix_index + 3:addr_index].strip())
    address = int(cmd[addr_index:reg_index], 16)
    reg = int(cmd[reg_index:value_index], 16)
    value = int(cmd[value_index:], 16)
    return bus, address, reg, value


def parse_i2cget(cmd):
    prefix_index = cmd.find("-y ")
    if prefix_index == -1:
        raise ValueError("Invalid command")
    addr_index = cmd.find("0x", prefix_index + 3)
    reg_index = cmd.find("0x", addr_index + 2)
    bus = int(cmd[prefix_index + 3:addr_index].strip())
    address = int(cmd[addr_index:reg_index], 16)
    reg = int(cmd[reg_index:], 16)
    return bus, address, reg


class TestParsing(unittest.TestCase):
    def test_i2cdetect(self):
        self.assertEqual(parse_i2cdetect("i2cdetect -y 1"), 1)

    def test_i2cset(self):
        cmd = "i2cset -y 1 0x50 0x10 0xff"
        self.assertEqual(parse_i2cset(cmd), (1, 0x50, 0x10, 0xff))

    def test_i2cget(self):
        cmd = "i2cget -y 2 0x50 0x01"
        self.assertEqual(parse_i2cget(cmd), (2, 0x50, 0x01))


if __name__ == '__main__':
    unittest.main()
