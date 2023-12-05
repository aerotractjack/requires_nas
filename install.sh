#!/bin/bash

mkdir -p /home/aerotract/software/requires_nas/requires_nas
pushd /home/aerotract/software/requires_nas/
rm -rf *.egg-info/ dist/ build/
/usr/bin/python3 setup.py sdist bdist_wheel
/usr/bin/python3 -m pip install --upgrade --force-reinstall dist/requires_nas-0.1-py3-none-any.whl
popd