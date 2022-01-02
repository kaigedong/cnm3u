#!/bin/bash

wget https://raw.githubusercontent.com/iptv-org/iptv/master/channels/cn.m3u 2>/dev/null
echo "#EXTM3U" > source_cn_1080/cn_1080.m3u
grep -A 1 "\(1080p\)" cn.m3u | grep -v '^--' >> source_cn_1080/cn_1080.m3u

