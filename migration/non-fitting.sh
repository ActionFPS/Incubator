#!/bin/bash
# Determine stuff that doesn't fit in our format
grep -v -E '^.+'$'\t''.+('$'\t''.+|)$' *.tsv
