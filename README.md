# vlc-switch-config
Switch between VLC configurations

## About
This is a small Python CLI utility used to switch between configuration files on VLC. This is helpful for if you have one for production and one for testing to show more information. I've
only tested this on Windows currently, but Linux support will be tested soon. Please note that custom installations of VLC may not work correctly.

## Installation
### Requirements
* [Python 3](https://www.python.org/)
* [VLC](https://www.videolan.org/)
* [Git (optional)](https://git-scm.com/)
### Setting up
1. Clone the repository via Git (``git clone https://github.com/davidcralph/vlc-switch-config``) or download it via "Code" -> "Download ZIP" on the GitHub UI
2. ``cd`` into the directory in a terminal
3. Install dependencies with ``pip install -r requirements.txt``
4. Run ``python switchconfig.py to <configname>`` to switch to a config, and ``python switchconfig.py revert`` to revert to your previous one
### Building (Windows)
*Note: this is optional, but it makes it easier to run on new Windows devices*
1. Run ``build_win.bat``
### Building (Linux)
*Note: you probably don't need this, but it might make it easier for you*
1. Run ``build_linux.sh``

## License
[MIT](LICENSE)
