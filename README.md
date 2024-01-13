# 使用说明:

每天自动获取上游仓库[iptv-org/iptv](https://github.com/iptv-org/iptv)的[中国源](https://iptv-org.github.io/iptv/countries/cn.m3u)，并生成自己的 m3u 列表:

```
# m3u链接
https://kaigedong.github.io/cnm3u/cn1080.m3u
```

## 生成规则：

- 首先删除掉黑名单[blacklist.txt](./blacklist.txt)

- 然后导出白名单里的列表[whitelist.txt](./whitelist.txt)

- 然后使用 IPTV Checker 对源的有效性进行筛选

- 自动提交到[gh](https://github.com/kaigedong/cnm3u/tree/gh)分支，并使用 GithubPage 进行托管

## TODO:

- [ ] 处理上游源更新导致的重复频道问题

## 特点：

- [x] 每天定时根据最新上游源进行更新

- [x] 列表顺序按照白名单顺序

- [x] 添加[IPTV Checker](https://github.com/freearhey/iptv-checker)进行筛选

## 如何生成自己的个性化列表

- [ ] Fork 本仓库 并 到仓库的 settings/pages 设置 Source 为 gh 分支

- [ ] 添加其他上游源

- [ ] 按需要修改黑/白名单

- [ ] 最后生成的自己的链接为 https://{你的 github 用户名}.github.io/cnm3u/cn1080.m3u

## 相关Repo

+ https://github.com/fanmingming/live
+ https://github.com/drangjchen/IPTV （一个IPV6源）
