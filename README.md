# ArabCeleb

ArabCeleb, a dataset collected in the wild that specifically focuses on arabic language. The proposed dataset contains utterances from 100 celebrities taken from video on YouTube.com. The dataset might be used for several speaker recognition tasks: identification, verification, gender recognition as well as multimodal recognition tasks thus integrating audio and video tracks.

![](https://github.com/CeLuigi/ArabCeleb/blob/main/assets/teaser.png)

## Dependencies
* Python 3.8
* [pytube](https://pytube.io/en/latest/) 11.0.1
* ffmpeg 4.2.4

In order to successfully run the code, install the packages listed in `requirements.txt` as follows:
```
pip install -r requirements.txt
```

## Citation
If you use our dataset, please consider cite the following:
* Simone Bianco, Luigi Celona, Intissar Khalifa, Paolo Napoletano, Alexey Petrovsky, Flavio Piccoli, Raimondo Schettini, and Ivan Shanin. ArabCeleb: Speaker Recognition in Arabic. In _International Conference of the Italian Association for Artificial Intelligence (AIxIA)_, 2021.
```
@inproceedings{bianco2021arabceleb,
 author = {Bianco, Simone and Celona, Luigi and Khalifa, Intissar and Napoletano, Paolo and Petrovsky, Alexey and Piccoli, Flavio and Schettini, Raimondo and Shanin, Ivan},
 year = {2021},
 title = {ArabCeleb: Speaker Recognition in Arabic},
 booktitle = {International Conference of the Italian Association for Artificial Intelligence (AIxIA)},
}
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

## Contacts
* Celona Luigi (luigi \<dot\> celona \<at\> unimib \<dot\> it)
* Flavio Piccoli (flavio \<dot\> piccoli \<at\> unimib \<dot\> it)
