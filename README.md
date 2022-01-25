# Mannaggia-py 👼

<p align="center">
  <img src="/assets/logo.png" width="128" height="128" />
</p>

Remember [Mannaggia](https://github.com/LegolasTheElf/mannaggia)? This is a Python remake of it, with new features.

mannaggia is a python application to praise or more likely to **curse** the saints.

When mannaggia is started, it will start naming all the known saints (and more!), preeceding their name with a curse (such as `mannaggia a xxxxx`) or with a praise (such as `lode a xxxxx`).

 This tool is extremely suggested to be used during an intense debugging session or when implementing those kinds of tasks that makes you want to resign from your job.

## Features 🐷

- Support for different dictionary of saints
  - local storage file (see [factory.py](mannaggia/santi/factory.py))
  - <http://www.beatiesanti.it>
  - local file (read line by line)
- Support for different text-to-speech engines
  - google translator
  - mozilla tts
- Automatically plays the sound using **pydub**. You can check here the requirements to play audio: <https://github.com/jiaaro/pydub#playback>.

## Get started 🚀

1. Install requirements

    ```sh
    pip3 install -r requirements.txt
    ```

2. Install mannaggia

    ```sh
    pip3 install mannaggia
    ```

3. Run mannaggia

    ```sh
    mannaggia --help
    ```

---

### Mozilla tts 🦊

To beging, you need to install mozilla tts on your machine with `pip3 install tts`.

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