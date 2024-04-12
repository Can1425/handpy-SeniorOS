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
        "/dir/update.md":"698d51191981021ce58149cjbgj01668f",
        // 剩下的同理.

        "dir":[
            "dir1",
            "dir2",
            "dir1/dir3"
            // 剩下的同理.
        ]
    },
    // 配置文件更新策略MD5
    "updCfgST":"698d51a19d8a12111451499d7b701668f" //也是MD5
}
```

此为单次升级的升级清单

一般情况下 清单的URL为`{IP}/GetUpdList/{currentVer}/{updateVer}`

# 关于各类对象

| 函数名 | 类型 | 功能 | 参数 | 返回值 | 备注 |
|-|-|-|-|-|-|
|FastHash|func|快速/低ram的hash文件|文件路径,\[可选\]哈希类型|哈希值|/|
|GetFileList|func|获取本地文件清单|/|本地文件清单数据|/|
| GetUpdList | func | 获取升级清单 | / | 升级清单 | 返回升级清单 | / |
| GetLatestVer | func | 获取最新版本的版本号 | / | 版本号 | / | / |
| GetUpdFile | func | 获取升级文件 | 文件MD5 | 文件内容 | / | /|
| UpdFile | func | 覆写需要更新的文件 | 预处理好的更新清单 | / | /|/|
| UpdCfg | func | 下载并运行配置升级程序 | 配置升级程序Hash值 | /| /|
| Update| func | 一键式更新系统| / | / | /|

# 注意

- 升级清单的URL为`{IP}/GetUpdList/{currentVer}/{updateVer}`
- 升级清单的URL为`{IP}/GetUpdFile/{fileMD5}`

# 关于自定义化更新

我们将各类更新步骤拆分开来 便于各位开发者自定义化
## 步骤
- **获取** 本地文件清单 与 更新清单
- **对比** 更新清单
- **写入** 需要更新的文件/文件夹
- **删除** 不需要的文件/文件夹
- **运行** 配置升级程序
- **重启** 重启SeniorOS

>我们编写了一个示例 位于`core/update.py func(UpdateST)`
>
>各位开发者可以参照此示例进行编写 插入所需的UI/交互等
# 注意

- 升级清单的URL为`{IP}/GetUpdList/{currentVer}/{updateVer}`
- 升级清单的URL为`{IP}/GetUpdFile/{fileMD5}`
