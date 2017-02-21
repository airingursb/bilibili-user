# bilibili-user

Bilibili用户爬虫

知乎专栏地址：[https://zhuanlan.zhihu.com/p/24434456](https://zhuanlan.zhihu.com/p/24434456)

本文所使用的数据可视化为 [infogr.am](infogr.am)

**该爬虫仅供学习使用**

## 文件介绍

* `bilibili_user.py`：爬虫文件
* `bilibili_user_info.sql`：数据库文件
* `get_face.py`：用户头像下载器

## Bilibili用户报告（Web App）

演示地址：[http://ursb.me/bilibili-report](http://ursb.me/bilibili-report)
GitHub：[https://github.com/airingursb/bilibili-report](https://github.com/airingursb/bilibili-report)

**跪求Star Orz...**

## 用户数据初步分析

> 转自我的博客 [B站2000万用户分析](http://ursb.me/2016/02/23/B%E7%AB%992000%E4%B8%87%E7%94%A8%E6%88%B7%E5%88%86%E6%9E%90/)

### 基本概况

- 总数据数：20119918
- 抓取用户的顺序为其注册时间顺序：2009-06-24 14:06:54 至 2016-02-18 21:04:52
- 预估遗漏数据：不超过2%
- 抓取字段：用户id，昵称，性别，头像，等级，经验值，粉丝数，生日，地址，注册时间，签名，等级与经验值等。

### 性别

- 有效数据：14643019
- 保密：11621898
- 男：1674196
- 女：1346925

![性别统计](http://7xkcl8.com1.z0.glb.clouddn.com/ursbbilibili-sex1.png-600.jpg)

这个男女比例是有点出乎个人预料的，接近1：1。其实之前初步抓了2013年暑假之前的数据，男女比例当时还在3：1这样。

![性别统计](http://7xkcl8.com1.z0.glb.clouddn.com/ursbbilibili-sex2.png-600.jpg)

![性别统计](http://7xkcl8.com1.z0.glb.clouddn.com/ursbbilibili-sex3.png-600.jpg)

可见明确性别的群体还是比较少的，只占了总数据的 15% 左右。

更多的分析日后再做。

### 年龄

- 统计范围：1970-2010（1980年除外）
- 总数据：3800767

具体数据不放了，简单看一下统计结果吧。

![年龄统计](http://7xkcl8.com1.z0.glb.clouddn.com/ursbbilibili-age3.png-600.jpg)

主要用户分布在93-00年的用户（大概16-23周岁），其中97年（19岁）用户占了绝对的主导地位。

事实证明，B站小学生并不多，而是高中生、大学生比较多。

![年龄统计](http://7xkcl8.com1.z0.glb.clouddn.com/ursbbilibili-age1.png-600.jpg)

![年龄统计](http://7xkcl8.com1.z0.glb.clouddn.com/ursbbilibili-age2.png-600.jpg)

90后用户占主体，但是用户年龄段正在不断后移。毕竟，是一个年轻人的网站。

### 地区

- 分析范围：国内34个省市及地区。
- 有效数据：863541

![地区统计](http://7xkcl8.com1.z0.glb.clouddn.com/ursbbilibili-place1.png-600.jpg)

主要用户分布在：广东、江苏、北京、上海、浙江等地区。都是一些经济很发达的沿海地区。

![地区统计](http://7xkcl8.com1.z0.glb.clouddn.com/ursbbilibili-place3.png-600.jpg)

![地区统计](http://7xkcl8.com1.z0.glb.clouddn.com/ursbbilibili-place2.png-600.jpg)

### 注册时间

- 统计时间：2009-06-24 14:06:54 至 2016-02-18 21:04:52
- 总数据：20119823

![注册时间统计](http://7xkcl8.com1.z0.glb.clouddn.com/ursbbilibili-reg1.png-600.jpg)

由于16年才过去2个多月，所以少一点，不过可以预见其发展必将远超2015年。自2009年开站以来，每年用户几乎都是以指数级增长。

![注册时间统计](http://7xkcl8.com1.z0.glb.clouddn.com/ursbbilibili-reg2.png-600.jpg)

![注册时间统计](http://7xkcl8.com1.z0.glb.clouddn.com/ursbbilibili-reg3.png-600.jpg)

### 活跃度统计

- 等级范围：0 - 6
- 总数据：20119918
- 截止时间：2016-02-18

由于B站有经验等级规则，用户的活跃度可以依据等级判断。

等级为0，就是只注册未登陆过的用户。等级为1或2，为非活跃用户。等级为3以上，就是活跃用户。其中等级为5或6的，为投稿数特别特别多、视频特别火爆的用户，为B站的主干用户（约5000人）。

![等级统计](http://7xkcl8.com1.z0.glb.clouddn.com/ursbbilibili-level1.png-600.jpg)

![等级统计](http://7xkcl8.com1.z0.glb.clouddn.com/ursbbilibili-level2.png-600.jpg)

关于留存率等数据，日后再统计分析。

### 粉丝统计

- 有效数据：2011918
- 范围：0 - 988323
- 截止时间：2016-02-18 21:04:52

![粉丝统计](http://7xkcl8.com1.z0.glb.clouddn.com/ursbbilibili-fans1.png-600.jpg)

哎- -，我也是有2个粉丝的人！

![粉丝统计](http://7xkcl8.com1.z0.glb.clouddn.com/ursbbilibili-fans4.png-600.jpg)

以下是B站TOP20用户。很多人都非常的眼熟哈。

![粉丝统计](http://7xkcl8.com1.z0.glb.clouddn.com/ursbbilibili-fans3.png-600.jpg)

