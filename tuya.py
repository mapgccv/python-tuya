import argparse
import pytuya



parser = argparse.ArgumentParser(description='Interact with tuya devices')
parser.add_argument("-id", "--id", type=str, help="uuid")
parser.add_argument("-key", "--key", type=str, help="local key")
parser.add_argument("-ip", "--ipaddress", type=str,
                    help="ip address")

args = parser.parse_args()
if args.ipaddress is not None:
    print(args.ipaddress)
else:
    args.ipaddress = "192.168.1.39"

if args.id is not None:
    print(args.id)
else:
    args.id = "18810700840d8e857a15"

if args.key is not None:
    print(args.key)
else:
    args.key = "a8941a193b0b9142"


d = pytuya.CombinedDevice(args.id, args.ipaddress, args.key)
data = d.status()  # NOTE this does NOT require a valid key
print('Dictionary %r' % data)
print('state (bool, true is ON) %r' % data['dps']['1'])  # Show status of first controlled switch on device

# Toggle switch state
switch_state = data['dps']['1']
data = d.set_status(not switch_state)  # This requires a valid key
if data:
    print('set_status() result %r' % data)

#d.set_white(255, 255)
d.set_colour(33,33,0)
d.turn_off_led()
#d.set_brightness(25)
# on a switch that has 4 controllable ports, turn the fourth OFF (1 is the first)
#data = d.set_status(False, 4)
#if data:
#    print('set_status() result %r' % data)
#    print('set_status() extrat %r' % data[20:-8])



