## Google、百度搜索结果黑名单

垃圾站点出现在 Google、百度的搜索结果中，实在是恶心——于是这个黑名单就这么出来了。

黑名单主要由我自己使用 Google 搜索时收集和网友的提交，所以更新频率无法保证——而我，现在使用 Kagi 了，所以更加没法保证更新时间了……

## 如何使用

### 屏蔽 Google 或非百度类搜索结果

下载 uBlacklist (下载地址：[Chrome Web Store](https://chrome.google.com/webstore/detail/ublacklist/pncfbmialoiaghdehhbnbhkkgmjanfhe)、[Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/ublacklist/)、[Mac App Store](https://apps.apple.com/app/ublacklist-for-safari/id1547912640))，将以下 3 个链接，通过点击 Add a subscription 添加到 Subscription 分类下：

- [精确匹配](https://raw.githubusercontent.com/cobaltdisco/Google-Chinese-Results-Blocklist/master/uBlacklist_subscription.txt)、[百家号、腾讯云、华为云等精确匹配](https://raw.githubusercontent.com/cobaltdisco/Google-Chinese-Results-Blocklist/refs/heads/master/uBlacklist_subscription_extra.txt)：该匹配方式主要是通过 `*://*.xyz.com/*` 的方式来匹配搜索结果，进行过滤。基本不会有误杀。

- [模糊匹配](https://raw.githubusercontent.com/cobaltdisco/Google-Chinese-Results-Blocklist/master/uBlacklist_match_patterns.txt)：该匹配方式主要是通过如 `*://*/list.php?s=*`、`title/小.(百科|知识)网/` 的方式来匹配搜索结果，进行过滤。存在小范围的误杀。若会击中自己经常使用的网站，请自行修改规则配置到插件中，防止被误杀。

### 屏蔽百度搜索结果

下载  AC-baidu (下载地址：[GreasyFork](https://greasyfork.org/zh-CN/scripts/14178-ac-baidu-%E9%87%8D%E5%AE%9A%E5%90%91%E4%BC%98%E5%8C%96%E7%99%BE%E5%BA%A6%E6%90%9C%E7%8B%97%E8%B0%B7%E6%AD%8C%E5%BF%85%E5%BA%94%E6%90%9C%E7%B4%A2-favicon-%E5%8F%8C%E5%88%97))，在屏蔽功能中，将[该列表](https://raw.githubusercontent.com/cobaltdisco/Google-Chinese-Results-Blocklist/master/GHHbD_perma_ban_list.txt)中的网址导入。
