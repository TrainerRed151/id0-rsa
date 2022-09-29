#!/bin/bash

printf `printf id0-rsa.pub | shasum -a 256 | cut -d' ' -f1` | md5
