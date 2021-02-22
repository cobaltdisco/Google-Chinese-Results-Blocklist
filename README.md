### Google 中文搜索结果屏蔽黑名单

各种垃圾 SEO 站点出现在谷歌中文搜索结果中，实在是恶心——于是这个黑名单就这么出来了。黑名单纯靠我自己使用谷歌搜索时收集，所以更新频率无法保证（然而已经断断续续更新了 4 年，就职的公司都被收购了）。

你可以安装以下插件导入黑名单，插件选其中之一即可：

**1. uBlacklist**（下载地址：[Chrome Web Store](https://chrome.google.com/webstore/detail/ublacklist/pncfbmialoiaghdehhbnbhkkgmjanfhe)、[Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/ublacklist/)）
- 将[该列表](https://raw.githubusercontent.com/cobaltdisco/Google-Chinese-Results-Blocklist/master/uBlacklist_match_patterns.txt)中的通配符添加到 Sites blocked from appearing in Google search results 的输入框下。
- 将[该列表](https://raw.githubusercontent.com/cobaltdisco/Google-Chinese-Results-Blocklist/master/uBlacklist_subscription.txt)地址，添加到 Subscription 订阅中。

**2. Google Hit Hider by Domain**（下载地址：[GreasyFork](https://greasyfork.org/zh-CN/scripts/1682-google-hit-hider-by-domain-search-filter-block-sites)） 
- 将[该列表](https://raw.githubusercontent.com/cobaltdisco/Google-Chinese-Results-Blocklist/master/GHHbD_perma_ban_list.txt)中的网址，通过 List Until -> Import 进行导入。
- 注：Google Hit Hider by Domain 与 uBlacklist 的不同，在于 uBlock 是直接隐藏搜索结果，Google Hit Hider by Domain 则有两种方式，一种是直接隐藏，一种是降低搜索结果展示的权重。

----

### 当然，你也可以用这个名单来屏蔽百度搜索结果

**AC-baidu**（下载地址：[GreasyFork](https://greasyfork.org/zh-CN/scripts/14178-ac-baidu-%E9%87%8D%E5%AE%9A%E5%90%91%E4%BC%98%E5%8C%96%E7%99%BE%E5%BA%A6%E6%90%9C%E7%8B%97%E8%B0%B7%E6%AD%8C%E5%BF%85%E5%BA%94%E6%90%9C%E7%B4%A2-favicon-%E5%8F%8C%E5%88%97)）
- 开启“附加2-自主拦截域名”，点击 DIY，将[该列表](https://raw.githubusercontent.com/cobaltdisco/Google-Chinese-Results-Blocklist/master/GHHbD_perma_ban_list.txt)中的网址导入。
- 注：这个脚本似乎也会同时对搜狗、谷歌、必应搜索结果同时产生影响。
