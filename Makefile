draw:
	python3 draw_rothe.py ${w}

tree:
	python3 driver.py ${code}

clean:
	rm main.aux
	rm main.log
	rm main.out
	rm main.tex