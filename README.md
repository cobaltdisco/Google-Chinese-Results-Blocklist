## 中文搜索结果黑名单

垃圾站点出现在 Google、百度的中文搜索结果中，实在是恶心——于是这个黑名单就这么出来了。

黑名单主要由我自己使用 Google 搜索时收集（ 当然，也有来自网友的热心提交 ），所以更新频率无法保证。然而已经断断续续更新了 4 年，就职的公司都被收购了，部门也换了 4 次。

## 如何使用

你可以安装以下插件导入黑名单，插件选其中之一即可。

强烈建议使用 **uBlacklist**，因为这个插件可以对搜索结果标题进行匹配。例如，Google 搜索结果中可能有成百上千的“小X百科网”、“小X知识网”，手动屏蔽域名是不可能的。这时候用正则匹配标题，将会非常简单。

同理，由于 **Google Hit Hider by Domain** 和 **AC-baidu** 没有这样的功能，屏蔽效果会比 **uBlacklist** 差。

### 屏蔽 Google 中文搜索结果

**1. uBlacklist**（ 下载地址：[Chrome Web Store](https://chrome.google.com/webstore/detail/ublacklist/pncfbmialoiaghdehhbnbhkkgmjanfhe)、[Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/ublacklist/)、[Mac App Store](https://apps.apple.com/app/ublacklist-for-safari/id1547912640) ）
- 将[该列表中的内容](https://raw.githubusercontent.com/cobaltdisco/Google-Chinese-Results-Blocklist/master/uBlacklist_subscription.txt)地址，添加到 Subscription 订阅中。
- 将[该列表的链接](https://raw.githubusercontent.com/cobaltdisco/Google-Chinese-Results-Blocklist/master/uBlacklist_match_patterns.txt)添加到 Sites blocked from appearing in Google search results 输入框下。

**2. Google Hit Hider by Domain**（ 下载地址：[GreasyFork](https://greasyfork.org/zh-CN/scripts/1682-google-hit-hider-by-domain-search-filter-block-sites) ） 
- 将[该列表](https://raw.githubusercontent.com/cobaltdisco/Google-Chinese-Results-Blocklist/master/GHHbD_perma_ban_list.txt)中的网址，通过 List Until -> Import 进行导入。


### 屏蔽百度中文搜索结果

**1. Google Hit Hider by Domain**（ 下载地址：[GreasyFork](https://greasyfork.org/zh-CN/scripts/1682-google-hit-hider-by-domain-search-filter-block-sites) ） 

- 同 Google 方案操作。

**2. AC-baidu**（ 下载地址：[GreasyFork](https://greasyfork.org/zh-CN/scripts/14178-ac-baidu-%E9%87%8D%E5%AE%9A%E5%90%91%E4%BC%98%E5%8C%96%E7%99%BE%E5%BA%A6%E6%90%9C%E7%8B%97%E8%B0%B7%E6%AD%8C%E5%BF%85%E5%BA%94%E6%90%9C%E7%B4%A2-favicon-%E5%8F%8C%E5%88%97) ）
- 开启“附加2-自主拦截域名”，点击 DIY，将[该列表](https://raw.githubusercontent.com/cobaltdisco/Google-Chinese-Results-Blocklist/master/GHHbD_perma_ban_list.txt)中的网址导入。
> 注：这个脚本似乎也会同时对搜狗、谷歌、必应搜索结果同时产生影响。
