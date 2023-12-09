# mpv-open-kinopoisk-page
Script for mpv that opens the kinopoisk page for the currently playing media file.

It does this by extracting/guessing the relevant metadata from the file name (using [guessit](https://github.com/guessit-io/guessit)), and opening a web page in a new tab of your default browser.

## Requirements
[mpv](https://github.com/mpv-player/mpv)\
[guessit](https://github.com/guessit-io/guessit)\
python 3

## Install
Copy or symlink the ```.lua``` and ```.py``` files to your mpv scripts folder.\
`$ ln -rs open-kinopoisk-page.* ~/.config/mpv/scripts/`

## Usage
By default, the script binds itself to ```alt+ctrl+shift+K```.\
To change default binding simply add following line into **input.conf**
```
K script-binding mpv_open_kinopoisk_page
```

## Credits
**mpv-open-kinopoisk-page** is inspired / based on
[mpv-open-imdb-page](https://github.com/ctlaltdefeat/mpv-open-imdb-page)
written by **ctlaltdefeat**

Thanks to the creators, maintainers and contributors
[mpv](https://github.com/mpv-player/mpv),
[guessit](https://github.com/guessit-io/guessit)

## License
[MIT](https://choosealicense.com/licenses/mit/)

