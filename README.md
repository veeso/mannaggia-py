# Mannaggia-py

Remember [Mannaggia](https://github.com/LegolasTheElf/mannaggia)? This is the Python remake, with new features.

## Features 👼

- Support for different dictionary of "santi"
  - local storage file (see [factory.py](mannaggia/santi/factory.py))
  - <http://www.beatiesanti.it>
- Support for different text-to-speech engines
  - google translator
  - mozilla tts
- Automatically plays the sound using pydub. You can check here the requirements to play audio: <https://github.com/jiaaro/pydub#playback>.

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

### Mozilla tts 🦊

To beging, you need to install mozilla tts on your machine with `pip3 install tts`.

In order to use mozilla TTS as text to speech engine for mannaggia, you need to provide the following options when running mannaggia:

```sh
mannaggia --model_name $MODEL_NAME -t mozilla
```

where model name is something like `tts_models/de/thorsten/tacotron2-DCA` in addition to this you need also to provide the `--config_path` argument, which must be the file containing the models list.

The default configuration file, can be found at <https://raw.githubusercontent.com/mozilla/TTS/master/TTS/.models.json>.

## License 📜

Licensed under the **DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE**, you can find [HERE](LICENSE) the entire license
