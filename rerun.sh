#!/usr/bin/env bash

set -e

rm -f .duecredit.p
DUECREDIT_ENABLE=yes python myscript.py
duecredit summary --format bibtex
