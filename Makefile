.PHONY: all

dist-clean:
	rm -rf gimei.egg-info/* dist/*

build-package:
	python setup.py sdist bdist_wheel

upload-testpypi:
	twine upload -r testpypi dist/*

upload-pypi:
	twine upload -r pypi dist/*

test-deploy: dist-clean build-package upload-testpypi

build-docs:
	pandoc --from=markdown --to=rst --output=README.rst README.md
	pandoc --from=markdown --to=rst --output=CHANGES.rst CHANGES

deploy: build-docs dist-clean build-package upload-pypi
