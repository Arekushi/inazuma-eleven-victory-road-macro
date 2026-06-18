"6.match:
	python main.py macro match

pack-gui:
	auto-py-to-exe

add-target:
	tufup targets add 6.0.0 output/ie-vr-macro repo/keys

remove-latest:
	tufup targets remove-latest repo/keys

release:
	gh release create v6.0.0 \
		./repo/metadata/root.json \
		./repo/metadata/targets.json \
		./repo/metadata/snapshot.json \
		./repo/metadata/timestamp.json \
		./repo/targets/inazuma-eleven-victory-road-macro-6.0.0.tar.gz\
		--title "v6.0.0" \
		--notes "Teste release TUFUP"
