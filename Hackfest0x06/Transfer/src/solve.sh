for i in {1..3}
do
	cat index$i.txt | base64 -d > image$i.png
done
