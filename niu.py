import frida, sys
import json
def on_message(message, data):
    if message['type'] == 'send':
        print("[============] {0}".format(message['payload']), message)
    else:
        print(message)

# def get_headers(url, headers):
#     process = frida.get_usb_device().attach('com.ss.android.ugc.aweme')
#     jscode = open('./js/code.js', 'r', encoding='utf8').read()
#     script = process.create_script(jscode)
#     script.on('message', on_message)
#     print('开始 Running CTF')
#     script.load()
#     res = script.exports.xgorgon(url, headers)
#     jso = json.loads(res)
#     headers['X-Khronos'] = jso['X-Khronos']
#     headers['X-Gorgon'] = jso['X-Gorgon']
#
#     return headers
# # sys.stdin.read()
device = frida.get_device_manager().add_remote_device("129.211.37.203:5888")
print(device)
pid = device.spawn(['com.ss.android.ugc.aweme'])
print(pid)
device.resume(pid)
process = device.attach(pid)
print(process)
