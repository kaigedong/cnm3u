#!/bin/bash

wget https://iptv-org.github.io/iptv/countries/cn.m3u 2>/dev/null -O cn.m3u
echo "#EXTM3U" > cn_1080/cn1080.m3u
grep -A 1 "\(1080p\)" cn.m3u | grep -v '^--' >> cn_1080/cn1080.m3u

