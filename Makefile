match:
	python -m src.commands macro match --log --input gamepad

chronicle-match:
	python -m src.commands macro match --file chronicle_match --log

free-match:
	python -m src.commands macro match --file free_match --log

pack-gui:
	auto-py-to-exe
