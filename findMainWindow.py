
import win32gui
import win32con
import win32com.client
import win32process as wproc
import win32api as wapi


def get_all_windows():
    windows = []
    
    def callback(hwnd, extra):
        if win32gui.IsWindowVisible(hwnd):
            window_title = win32gui.GetWindowText(hwnd)
            print(window_title);
            windows.append((hwnd, window_title))
    
    win32gui.EnumWindows(callback, None)
    return windows

# Search for windows by title
def find_windows_by_title(title="DeadByDaylight"):
    windows = get_all_windows()
    return [(hwnd, window_title) for hwnd, window_title in windows if title in window_title]

#wird nicht benötigt alternative lösung gefunden
def ThreadUnion(handle):
    remote_thread, _ = wproc.GetWindowThreadProcessId(handle)
    wproc.AttachThreadInput(wapi.GetCurrentThreadId(), remote_thread, True)
    prev_handle = win32gui.SetFocus(handle)
    return prev_handle


def GetDBDWindow():
    target_title = "Dead"
    found_windows = find_windows_by_title(target_title)

    if found_windows:
        for hwnd, window_title in found_windows:
            print(f"Window Title: {window_title}, Handle: {hwnd}")
            #handle = ThreadUnion(hwnd)
            win32gui.ShowWindow(hwnd, win32con.SW_NORMAL) # Restore if minimized
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('%')
            win32gui.SetForegroundWindow(hwnd)
            print("Succesful")
        
    else:
        print(f"No windows found with the title: {target_title}")
