#!/bin/bash

if [[ $(python3 -m radon cc --min D src/ test/) ]]; then
  exit 1
fi