from pynput import keyboard
from pynput.keyboard import Key, Controller,KeyCode
key_map = {
    'alt':Key.alt,
    'alt_l':Key.alt_l,
    'alt_r':Key.alt_r,
    'alt_gr':Key.alt_gr,
    'backspace':Key.backspace,
    'caps_lock':Key.caps_lock,
    'cmd':Key.cmd,
    'cmd_l':Key.cmd_l,
    'ctrl':Key.ctrl,
    'ctrl_l':Key.ctrl_l ,
    'delete':Key.delete,
    'down':Key.down,
    'end':Key.end,
    'enter':Key.enter,
    'esc':Key.esc,
    'f1':Key.f1,
    'f2':Key.f2,
    'f3':Key.f3,
    'f4':Key.f4,
    'f5':Key.f5,
    'f6':Key.f6,
    'f7':Key.f7,
    'f8':Key.f8,
    'f9':Key.f9,
    'f10':Key.f10,
    'f11':Key.f11,
    'f12':Key.f12,
    'f13':Key.f13,
    'f14':Key.f14,
    'f15':Key.f15,
    'f16':Key.f16,
    'f17':Key.f17,
    'f18':Key.f18,
    'f19':Key.f19,
    'f20':Key.f20,
    'home':Key.home,
    'left':Key.left,
    'page_down':Key.page_down,
    'page_up':Key.page_up,
    'right':Key.right,
    'shift':Key.shift,
    'shift_l':Key.shift_l,
    'shift_r':Key.shift_r,
    'space':Key.space,
    'tab':Key.tab,
    'up':Key.up,
    'media_play_pause':Key.media_play_pause,
    'media_volume_mute':Key.media_volume_mute,
    'media_volume_down':Key.media_volume_down,
    'media_volume_up':Key.media_volume_up,
    'media_previous':Key.media_previous,
    'media_next':Key.media_next,
    'insert':Key.insert,
    'menu':Key.menu,
    'num_lock':Key.num_lock,
    'pause':Key.pause,
    'print_screen':Key.print_screen,
    'scroll_lock':Key.scroll_lock
}

def on_press(key):
    print("-----{0}".format(key))
    # try:
    #     print('alphanumeric key  {0} pressed'.format(key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(key))

def on_release(key):
    pass
    # print('{0} released'.format(key))
    # print('{0}'.format(key))
    # if key == keyboard.Key.esc:
    #     return False

while True:
    with keyboard.Listener(
        on_press = on_press,
        on_release = on_release) as listener:
        listener.join()

