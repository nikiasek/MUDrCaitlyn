from os import path

def credential():
    if path.exists("Scripts\Credentials\Credentials.json"):
        import Scripts.Application.window
    else:
        import Scripts.Credentials.window



if __name__ == "Scripts.checker":
    credential()