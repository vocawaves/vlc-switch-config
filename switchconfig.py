import shutil
import getpass
import os
import platform
import click
import subprocess

def vlc_running(userSystem):
    """
    Checks if VLC is running
    """
    if userSystem == "Windows":
        return subprocess.call("tasklist | find /I /C \"vlc.exe\"", shell=True) == 0
    else:
        return subprocess.call("ps -A | grep vlc", shell=True) == 0

@click.group()
def main():
    """
    Switch VLC config files
    """
    pass

@main.command('to')
@click.argument('config')
def to(config):
    """
    Switch to specified configuration file
    """
    userSystem = platform.system()

    if vlc_running(userSystem):
      click.echo('VLC is running, stopping it')
      if userSystem == 'Windows':
        subprocess.call('taskkill /F /IM vlc.exe', shell=True)
      elif userSystem == 'Linux':
        subprocess.call('killall vlc', shell=True)
    click.echo('VLC stopped')

    if config == 'vlcrc-backup':
      click.echo('Invalid config name')
      return

    if userSystem == 'Linux':
      shutil.copyfile(os.path.expanduser('~')+'\\.config\\vlc\\vlcrc', './vlcrc-backup')
    elif userSystem == 'Windows':
      shutil.copyfile('C:\\Users\\'+getpass.getuser()+'\\Application Data\\vlc\\vlcrc', './vlcrc-backup')
    click.echo('Backed up old config to ./vlcrc-backup')

    if userSystem == 'Linux':
      shutil.copyfile(config, os.path.expanduser('~')+'\\.config\\vlc')
    elif userSystem == 'Windows':
      shutil.copyfile(config, 'C:\\Users\\'+getpass.getuser()+'\\Application Data\\vlc\\vlcrc')
    click.echo('Switched to '+config)

@main.command('revert')
def revert():
    """
    Revert to old config
    """
    userSystem = platform.system()

    if vlc_running(userSystem):
      click.echo('VLC is running, stopping it')
      if userSystem == 'Windows':
        subprocess.call('taskkill /F /IM vlc.exe', shell=True)
      elif userSystem == 'Linux':
        subprocess.call('killall vlc', shell=True)
    click.echo('VLC stopped')

    if userSystem == 'Linux':
      shutil.copyfile('./vlcrc-backup', os.path.expanduser('~')+'\\.config\\vlc\\vlcrc')
    elif userSystem == 'Windows':
      shutil.copyfile('./vlcrc-backup', 'C:\\Users\\'+getpass.getuser()+'\\Application Data\\vlc\\vlcrc')
    click.echo('Reverted to old config')
    
    os.remove('./vlcrc-backup')
    click.echo('Removed backup')

if __name__ == '__main__':
    main()
