# This script is designed to download YouTube videos to watch offline.
# In order to use this script, you have to install the pytube module from here:
#
#    https://github.com/NFicano/pytube
#
# Note: This script is a variation of the sample script on the github site.
# I've customized it to get more options out of the user.
#
# Because the script is similar to the author of the module, it's going to use
# that license.
#
# Copyright (c) 2012 Nick Ficano (http://nickficano.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sub-license, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice, and every other copyright notice found in this
# software, and all the attributions in every file, and this permission notice
# shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# By: Tom Yarrish
# Version 1.0
#
from pytube import YouTube
from pprint import pprint

yt = YouTube()

# Copy and paste the YouTube URL into the next line
yt_url = raw_input("Enter the URL to download: ")

yt.url = yt_url

# This confirms the video is what you want
print "The video name is {}".format(yt.filename)

# Just where you want to save it
yt_save = raw_input("Enter the location to save the file: ")

# So here we list the various formats to save the file as
print "Here are the codec and quality options:\n"
pprint(yt.videos)

# The next two lines allow you to set the codec and quality you want
yt_codec = raw_input("Enter the codec you want(ex. mp4): ")
yt_quality = raw_input("Enter the quality(ex. 720p): ")

yt_video = yt.get(yt_codec, yt_quality)

print "Downloading {} from YouTube...please wait".format(yt.filename)
# And here we finally save the file
yt_video.download(yt_save)
