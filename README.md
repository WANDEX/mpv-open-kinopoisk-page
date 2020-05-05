# mpv-open-kinopoisk-page
Script for mpv that opens the kinopoisk page for the currently playing media file.

It does this by extracting/guessing the relevant metadata from the file name (using [guessit](https://github.com/guessit-io/guessit)), finding it on kinopoisk, and then opening the page in a new tab on your default browser.

## Requirements
You need Python 3 installed and in path, as well as the modules ```guessit``` and ```kinopoiskpy```:

```bash
pip install guessit kinopoiskpy
```

## Install
Copy or symlink the ```.lua``` and ```.py``` files to your mpv scripts folder.\
(if you're unfamiliar with its location, check the mpv documentation)

On linux your order of actions could look like this:
```bash
mkdir -p ~/Downloads/git/ ~/.config/mpv/scripts/
git clone https://github.com/WANDEX/mpv-open-kinopoisk-page.git ~/Downloads/git/
cd ~/Downloads/git/mpv-open-kinopoisk-page/
ln -rs open-kinopoisk-page.* ~/.config/mpv/scripts/
```

## Usage
By default, the script binds itself to ```Ctrl+Shift+K```.\
To change default binding simply add following line into your **input.conf** file inside your mpv config dir.
```bash
K script-binding launch_kinopoisk       # for mpv-open-kinopoisk-page
```

You can change the binding by editing the last line in the ```.lua``` script file.

## Troubleshooting
In case you didn't know why it does nothing or throw error, try to update rebulk to 2.0.1 or later.\
Useful info link: [first solved issue](https://github.com/Toilal/rebulk/issues/20)

Or edit this file manually like in commit (depends on your python3 version)\
~/.local/lib/python3.8/site-packages/rebulk/loose.py
[rebulk commit with fix](https://github.com/Toilal/rebulk/commit/65e9ddfb9d1a56c168bdc13defe1fe74333f482f)

## Credits
**mpv-open-kinopoisk-page** is inspired/based on [mpv-open-imdb-page](https://github.com/ctlaltdefeat/mpv-open-imdb-page) written by ctlaltdefeat.

And of course thanks to the creators and maintainers of guessit and kinopoiskpy.

Many thanks to all of them. :heart:

## License
[MIT](https://choosealicense.com/licenses/mit/)

