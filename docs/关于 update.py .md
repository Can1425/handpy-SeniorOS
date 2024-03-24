# 关于 update.py .md

是FlagOS用于自更新的模块.

# 核心原理

借鉴了Git的思想.

在云端存储着若干以其自身文件内容为md5的文件, 还有各个版本的升级清单

本地拿到升级清单后 根据MD5等字段从云端下载文件并写入

# 清单样式

```json
{
    "version": "1.0.0",         // 系统当前版本
    "updVersion": "1.0.1",      // 更新后的版本
    // 更新清单
    "updateList": {
        "update.py": "698d51a1wdnmd21ce581499d7b701668f",
        "/dir/update.md":"698d51191981021ce58149cjbgj01668f"
        // 剩下的同理.
    },
    // 配置文件更新策略MD5
    "updCfgST":"698d51a19d8a12111451499d7b701668f" //也是MD5
}
```

此为单次升级的升级清单

一般情况下 清单的URL为`{IP}/GetUpdList/{currentVer}/{updateVer}`
