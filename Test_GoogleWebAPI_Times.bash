#!/bin/bash

for number in {1..60}
do
	echo "----------------------------------"
	sleep 0.5
	python gTTS.py 這是數字"$number" number
	python ./SpeechRecongnitionTest.py number
	echo -e "This number: \t $number"
done
exit 0
