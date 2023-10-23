
import subprocess

# List of packages to install
packages_to_install = [
    'pyautogui',
    'keyboard',
    'pywin32'
]

def install_packages(packages):
    for package in packages:
        try:
            subprocess.check_call(['pip', 'install', package])
            print(f'Successfully installed {package}')
        except subprocess.CalledProcessError as e:
            print(f'Error installing {package}: {e}')
            continue

if __name__ == '__main__':
    install_packages(packages_to_install)
