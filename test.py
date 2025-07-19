from brotab.api import MultipleMediatorsAPI
from brotab.main import create_clients
import webbrowser
import subprocess


def focus_window_by_title(title_keyword):
    try:
        # List all windows
        output = subprocess.check_output(['wmctrl', '-l']).decode('utf-8')

        # Search for the window by title keyword
        for line in output.splitlines():
            if title_keyword.lower() in line.lower():
                window_id = line.split()[0]
                subprocess.run(['wmctrl', '-ia', window_id])
                print(f"Brought window to front: {line}")
                return

        print(f"No window found with title containing: '{title_keyword}'")

    except Exception as e:
        print(f"Error: {e}")

api = MultipleMediatorsAPI(create_clients())
result = api.list_tabs([])


# Activate the Anchor Watch Tab
urlAW = "http://tatooinepi:3333/d/ednkv6r5ez0n4c/anchor-watch?orgId=1&var-myTime=3h&from=now-1h&to=now&timezone=browser&refresh=1m"
tabAW = "Anchor Watch"
tabAWcnt = 0
wndAWtitle = "Anchor Watch"

for line in result:
    print(line)

    # Check for "Anchor Watch" and extract the string before the first space
    if tabAW in line:
        tabID = line.split()[0]
        tabAWcnt = tabAWcnt + 1
        print("Anchor Watch found.")
        # Close if multible Anchor Watch tabs were found
        if tabAWcnt > 1:
            result = api.close_tabs([tabID])
            print("One Tab closed")
        else:
            result = api.activate_tab([tabID],True)

#If ther is no Open Anchow Watch tab
if tabAWcnt == 0:
    webbrowser.open_new_tab(urlAW)

focus_window_by_title("Anchor Watch")