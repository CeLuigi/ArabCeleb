# ArabCeleb

ArabCeleb is an audio dataset collected in the wild that specifically focuses on arabic language. The proposed dataset contains utterances from 100 celebrities taken from video on YouTube.com. The dataset might be used for several speaker recognition tasks: identification, verification, gender recognition as well as multimodal recognition tasks thus integrating audio and video tracks.

![](https://github.com/CeLuigi/ArabCeleb/blob/main/assets/teaser.png)

## Dependencies
* Python 3.8
* [pytube](https://pytube.io/en/latest/) 11.0.1
* ffmpeg 4.2.4

In order to successfully run the code, install the packages listed in `requirements.txt` as follows:
```
pip install -r requirements.txt
```

## Download
The dataset can be downloaded using the information provided into the file `info.json` running the script `prepare_dataset.py` as follows:
```
python prepare_dataset.py
```
The script:
<ol>
 <li>Download the video at the given Youtube URL</li>
 <li>Cut the entire video into video sequences</li>
 <li>Extract and save the audio signal into wav a file</li>
</ol>

## License
The ArabCeleb dataset is available to download for commercial/research purposes under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). The copyright remains with the original owners of the video. A complete version of the license can be found [here](https://github.com/CeLuigi/ArabCeleb/blob/main/LICENSE).

**Caution:** We note that the distribution of identities in the ArabCeleb datasets may not be representative of the global human population. Please be careful of unintended societal, gender, racial and other biases when training or deploying models trained on this data.

Please contact the authors below if you have any queries regarding the dataset.

## Citation
Please cite the following if you make use of the dataset:
* Simone Bianco, Luigi Celona, Intissar Khalifa, Paolo Napoletano, Alexey Petrovsky, Flavio Piccoli, Raimondo Schettini, and Ivan Shanin. ArabCeleb: Speaker Recognition in Arabic. In _International Conference of the Italian Association for Artificial Intelligence (AIxIA)_, 2021.
```
@inproceedings{bianco2021arabceleb,
 author = {Bianco, Simone and Celona, Luigi and Khalifa, Intissar and Napoletano, Paolo and Petrovsky, Alexey and Piccoli, Flavio and Schettini, Raimondo and Shanin, Ivan},
 year = {2021},
 title = {ArabCeleb: Speaker Recognition in Arabic},
 booktitle = {International Conference of the Italian Association for Artificial Intelligence (AIxIA)},
}
```
