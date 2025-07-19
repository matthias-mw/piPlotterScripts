from brotab.api import MultipleMediatorsAPI
from brotab.main import create_clients
api = MultipleMediatorsAPI(create_clients())
result = api.list_tabs([])
for line in result:
    print(line)

    # Check for "Anchor Watch" and extract the string before the first space
    if "Anchor Watch" in line:
        tabID = line.split()[0]
        print("Anchor Watch found.")
        print("First word:", tabID)
        result = api.close_tabs([tabID])
    


#