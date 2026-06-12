match:
	python main.py macro match --log --input gamepad

chronicle-match:
	python main.py macro match --file chronicle_match --log

free-match:
	python main.py macro match --file free_match --log

pack-gui:
	auto-py-to-exe
