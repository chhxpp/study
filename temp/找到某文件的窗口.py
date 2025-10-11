import ctypes
from ctypes import wintypes
import time
from pathlib import Path
import xlwings as xw
from pprint import pprint

# 目标文件（按需修改）
target = r'd:\mydoc\projs\py\res\doc\股票.txt'
target_basename = Path(target).name

# Windows API 准备
user32 = ctypes.windll.user32
EnumWindows = user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
GetWindowTextW = user32.GetWindowTextW
GetWindowTextLengthW = user32.GetWindowTextLengthW
GetWindowThreadProcessId = user32.GetWindowThreadProcessId
ShowWindow = user32.ShowWindow
SetForegroundWindow = user32.SetForegroundWindow
MoveWindow = user32.MoveWindow

SW_SHOWNORMAL = 1
SW_RESTORE = 9

def list_all_windows():
    windows = []
    @EnumWindowsProc
    def _cb(hwnd, lParam):
        # 读取顶层窗口标题（不过滤可见性）
        length = GetWindowTextLengthW(hwnd)
        if length > 0:
            buf = ctypes.create_unicode_buffer(length + 1)
            GetWindowTextW(hwnd, buf, length + 1)
            windows.append((hwnd, buf.value))
        return True
    EnumWindows(_cb, 0)
    return windows

def find_window_by_title_contains(sub):
    sub = (sub or "").lower()
    for hwnd, title in list_all_windows():
        if sub in (title or "").lower():
            return hwnd, title
    return None, None

def hwnd_get_pid(hwnd):
    pid = wintypes.DWORD()
    GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
    return pid.value

def ensure_window_and_move(hwnd, x, y, w, h):
    try:
        # 若被最小化或隐藏，先恢复
        try:
            ShowWindow(hwnd, SW_RESTORE)
        except Exception:
            ShowWindow(hwnd, SW_SHOWNORMAL)
        # 置前
        try:
            SetForegroundWindow(hwnd)
        except Exception:
            pass
        # 移动/调整大小
        MoveWindow(hwnd, x, y, w, h, True)
        return True
    except Exception:
        return False

def open_with_xlwings(path, visible=False):
    """尝试用 xlwings 打开文件，返回 (app, wb) 或 (None, None)"""
    try:
        app = xw.App(visible=visible, add_book=False)
        wb = app.books.open(path)
        return app, wb
    except Exception:
        try:
            # 如果上面失败，确保清理
            app.kill()
        except Exception:
            pass
        return None, None

def find_xlwings_app_for_book(path):
    """在 xw.apps 中查找打开了指定文件的 Excel 实例（若存在）"""
    p = Path(path).resolve()
    for a in xw.apps:
        for b in a.books:
            try:
                if Path(b.fullname).resolve() == p or b.name == p.name:
                    return a, b
            except Exception:
                # 兼容某些非标准 Office 实现（如 WPS）可能抛出
                try:
                    if b.name == p.name:
                        return a, b
                except Exception:
                    pass
    return None, None

def main():
    # 先尝试用 xlwings 后台打开（不会显示窗口）
    app, wb = open_with_xlwings(target, visible=False)
    if wb:
        # 读取示例区域并打印（后台也能读）
        try:
            pprint(wb.sheets[0].range('A1:B5').value)
        except Exception:
            pass

    # 如果 xlwings 能找到对应的 App（适用于 Microsoft Excel），优先从其获取 Hwnd
    a, b = find_xlwings_app_for_book(target)
    hwnd = None
    if a:
        try:
            hwnd = int(a.api.Hwnd)
            if hwnd == 0:
                # 有时后台实例无窗口句柄，尝试把 app 可见后再取
                try:
                    a.visible = True
                    time.sleep(0.3)
                    hwnd = int(a.api.Hwnd)
                except Exception:
                    pass
        except Exception:
            hwnd = None

    # 如果没有通过 xlwings 找到 hwnd 或使用 WPS（xw.apps 为空），通过枚举窗口查找包含文件名的顶层窗口
    if not hwnd:
        # 等待窗口出现并尝试匹配（最多等待 10 秒）
        x, y, w, h = 100, 100, 800, 600
        for _ in range(50):
            hwnd, title = find_window_by_title_contains(target_basename)
            if hwnd:
                ok = ensure_window_and_move(hwnd, x, y, w, h)
                pid = hwnd_get_pid(hwnd)
                print("找到窗口:", title, "HWND=", hwnd, "PID=", pid, "move_ok=", ok)
                break
            time.sleep(0.2)
        else:
            print(f"未找到包含 '{target_basename}' 的顶层窗口，或窗口标题不包含文件名片段。")
    else:
        # 已有 hwnd：直接恢复并移动
        x, y, w, h = 100, 100, 1200, 800
        ok = ensure_window_and_move(hwnd, x, y, w, h)
        pid = hwnd_get_pid(hwnd) if hwnd else None
        print("通过 xlwings 找到 Excel 实例，HWND=", hwnd, "PID=", pid, "move_ok=", ok)

    # 清理：如果我们通过 xlwings 打开了文件并希望关闭，可在此处理（示例不自动关闭）
    # if wb:
    #     wb.close()
    # if app:
    #     app.quit()

if __name__ == "__main__":
    main()