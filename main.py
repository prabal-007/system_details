import platform

def system_details():
    print('='*20, 'Ststem Information', "="*20)
    uname = platform.uname()
    print(f'System : {uname.system}\nNode name : {uname.node}\nRelease : {uname.release}\n'
    f'Version : {uname.version}\nMachine : {uname.machine}\nProcessor : {uname.processor}')


if __name__ == "__main__":
    system_details()
    
