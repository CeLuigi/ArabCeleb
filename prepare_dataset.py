import os
import json
import datetime
import pytube
from pytube import YouTube


if __name__ == '__main__':
	dest_dir = 'full_videos'
	if not os.path.exists(dest_dir):
		os.makedirs(dest_dir)

	with open("utterance_info.json") as f:
		data = json.load(f)

	not_available = []

	for key,value in data.items():
		celeb_datadir = os.path.join(dest_dir, key)
		if not os.path.exists(celeb_datadir):
			os.makedirs(celeb_datadir)

		for id_video, (url, value) in enumerate(value['utterances'].items()):
			yt = YouTube(url)
			try:
				s = yt.streams.filter(only_audio=True)[0]
			except pytube.exceptions.VideoPrivate as e:
				not_available.append(url)
				continue
			filename = str(id_video) + '.mp4'
			s.download('.', filename=filename)

			for utterance in value:
				utterance_fn = utterance['name']
				utterance_from = utterance['from']
				utterance_to = utterance['to']
				wav_filename = os.path.join(celeb_datadir, utterance_fn)
				os.system('ffmpeg -y -i {} -acodec pcm_s16le '
				 '-ss {} -to {} {}'.format(filename,
				 	str(datetime.timedelta(seconds=utterance_from)),
				 	str(datetime.timedelta(seconds=utterance_to)),
				 	wav_filename))
			os.remove(filename)
			
	print('---------------------------------------------')
	print('The following videos are no longer available:')
	for na in not_available: print(na)
	print('---------------------------------------------')
