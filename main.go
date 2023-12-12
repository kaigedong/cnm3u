package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var highPriority = []string{"CCTV", "卫视", "斗鱼", "douyu", "(1080p)"}
var highPriorityMap = map[string][]*M3u{}
var extraChannel = map[string][]*M3u{}

func init() {
	for _, v := range highPriority {
		highPriorityMap[v] = []*M3u{}
	}
}

func main() {
	parseM3u()
}

func parseM3u() error {
	file, err := os.Open("cn.m3u.tmp")
	if err != nil {
		return err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var m3u *M3u
	for scanner.Scan() {
		line := scanner.Text()
		switch {
		case strings.HasPrefix(line, "#EXTM3U"):
			continue
		case strings.HasPrefix(line, "#EXTINF"):
			items := strings.Split(line, ",")
			m3u = &M3u{
				ExtinfLine: items[0],
				TVName:     strings.ReplaceAll(items[1], " ", ""),
			}
		case strings.HasPrefix(line, "#"):
			m3u.ExtraLine = append(m3u.ExtraLine, line)
		default:
			m3u.Url = line
			for k, v := range highPriorityMap {
				if strings.Contains(m3u.TVName, k) {
					v = append(v, m3u)
				}
			}
			m3u.ToString()
		}
	}
	return nil
}

type M3u struct {
	ExtinfLine string
	TVName     string
	ExtraLine  []string
	Url        string
}

func (m3u *M3u) ToString() {
	fmt.Println(m3u.ExtinfLine + "," + m3u.TVName)
	for _, line := range m3u.ExtraLine {
		fmt.Println(line)
	}
	fmt.Println(m3u.Url)
}

func output() {
	for _, v := range highPriorityMap {
		for _, m3u := range v {
			m3u.ToString()
		}
	}
}
