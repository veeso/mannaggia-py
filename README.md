# Mannaggia-py 👼

<p align="center">
  <img src="/assets/logo.png" width="128" height="128" />
</p>

<p align="center">~ mannaggia is a python application to praise or more likely to curse the saints. ~</p>
<p align="center">
  <a href="https://ko-fi.com/veeso" target="_blank">Ko-fi</a>
  ·
  <a href="#get-started-">Installation</a>
  ·
  <a href="CHANGELOG.md" target="_blank">Changelog</a>
</p>

<p align="center">Developed by <a href="https://veeso.github.io/" target="_blank">@veeso</a></p>
<p align="center">Current version: 0.1.3 (25/01/2022)</p>

<p align="center">
  <a href="https://opensource.org/licenses/MIT"
    ><img
      src="https://img.shields.io/badge/License-MIT-teal.svg"
      alt="License-MIT"
  /></a>
  <a href="https://github.com/veeso/mannaggia-py/stargazers"
    ><img
      src="https://img.shields.io/github/stars/veeso/mannaggia-py.svg"
      alt="Repo stars"
  /></a>
  <a href="https://pepy.tech/project/mannaggia"
    ><img
      src="https://pepy.tech/badge/mannaggia"
      alt="Downloads counter"
  /></a>
  <a href="https://pypi.org/project/mannaggia/"
    ><img
      src="https://badge.fury.io/py/mannaggia.svg"
      alt="Latest version"
  /></a>
  <a href="https://ko-fi.com/veeso">
    <img
      src="https://img.shields.io/badge/donate-ko--fi-red"
      alt="Ko-fi"
  /></a>
</p>

---

Remember [Mannaggia](https://github.com/LegolasTheElf/mannaggia)? This is a Python remake of it, with new features.

mannaggia is a python application to praise or more likely to **curse** the saints.

When mannaggia is started, it will start naming all the known saints (and more!), preeceding their name with a curse (such as `mannaggia a xxxxx`) or with a praise (such as `lode a xxxxx`).

 This tool is extremely suggested to be used during an intense debugging session or when implementing those kinds of tasks that makes you want to resign from your job.

## Features 🐷

- Support for different **dictionaries of saints**
  - local storage file (see [factory.py](mannaggia/santi/factory.py))
  - <http://www.beatiesanti.it>
  - local file (read line by line)
- Support for different **text-to-speech** engines:
  - [espeak](http://espeak.sourceforge.net/)
  - [Google Translator](https://translate.google.it)
  - [iSpeech](http://www.ispeech.org)
  - **MacOs voice-over**
  - [Mozilla TTS](https://github.com/mozilla/TTS)
- Automatically plays the sound using **pydub**. You can check here the requirements to play audio: <https://github.com/jiaaro/pydub#playback>.

## Get started 🚀

1. Install mannaggia with pip

    ```sh
    pip3 install mannaggia
    ```

2. Run mannaggia

    ```sh
    mannaggia --help
    ```

    or in case it's still not available in your path

    ```sh
    python3 -m mannaggia
    ```

In case you're missing some dependencies after installation, run:

```sh
pip3 install -r requirements.txt
```

---

### Mozilla tts 🦊

To get started with mozilla tts, you need to install mozilla tts on your machine with `pip3 install tts`.

In order to use mozilla TTS as text to speech engine for mannaggia, you need to provide the following options when running mannaggia:

```sh
mannaggia --model_name $MODEL_NAME -t mozilla
```

where model name is something like `tts_models/de/thorsten/tacotron2-DCA` in addition to this you need also to provide the `--config_file` argument, which must be the file containing the models list.

The default configuration file, can be found at <https://raw.githubusercontent.com/mozilla/TTS/master/TTS/.models.json> or in this repository at [config/models.json](config/models.json).

example:

```sh
mannaggia --model_name tts_models/fr/mai/tacotron2-DDC --config_file config/models.json -t mozilla --prefix "Va te faire enculer"
```

### File as a dictionary

You can opt to use a text file as a dictionary. To do so, it'll be enough to write line by line the name of the "characters" to invoke in mannaggia.

example:

```sh
mannaggia -d file -D ./config/dictionary.txt
```

---

## License 📜

Licensed under the **DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE**, you can find [HERE](LICENSE) the entire license
