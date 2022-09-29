#!/bin/bash

gpg --import gpg-key.txt
gpg --decrypt message.txt
