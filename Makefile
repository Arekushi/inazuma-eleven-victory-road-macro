match:
	python main.py macro match

pack-gui:
	auto-py-to-exe

add-target:
	tufup targets add $(app_version) output/ie-vr-macro repo/keys

remove-latest:
	tufup targets remove-latest repo/keys
