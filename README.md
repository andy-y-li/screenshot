# screenshot
Make a simple screenshot on window via python

- **Usage:**
```
Usage: python3 screenshot.py target_title images_filepath
```

- **Install python module:**
```
pyhton3 -m pip install pyautogui pygetwindow pywinauto
```
- **Load DLL error:**
```
import win32api
ImportError: DLL Load failed
```
 Found the DLL files(pythoncom37.dll, pywintypes37.dll) in the path, it may  in other path:
 ```
 C: \Users|xxx\AppData\Local|Packages\PythonSoftwareFoundation.Python.3.7_qbz5n2kfra8p0\LocalCache\local-packages
 ```
Copy to "C:IWindows\System32"

