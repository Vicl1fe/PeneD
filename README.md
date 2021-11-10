# PeneD

用于从网络上获取的字典或本地字典进行分类去重。

例子：

添加配置到配置文件中。支持本地绝对路径。

```
python3 PeneD.py add php:http://xxx.com/php.txt
```

工具会将每个分类下的url或者本地路径进行读取，并且去重放到`result`目录下

更新字典库

```
python3 PeneD.py update
```

更新某个分类的字典库

```
python3 PeneD.py update php
```



一些细节还没有完善。等有时间再完善。



**注意：请勿用于非法用途 后果作者概不负责**