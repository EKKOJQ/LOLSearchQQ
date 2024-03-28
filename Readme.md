# LOL信息查询应用

这是一个简单的网页应用，用于查询LOL游戏玩家的相关信息，包括QQ号和绑定的电话号码。用户可以输入LOL昵称或QQ号来查询相关信息。

## 如何使用

1. 打开 `index.html` 文件。
2. 在输入框中输入LOL昵称或QQ号。
3. 点击“查询”按钮。
4. 查询结果将显示LOL账号的QQ号，游戏名和游戏大区。
5. 用户可以点击“复制QQ号”按钮将QQ号复制到剪贴板。
6. 如果查询成功，还会显示QQ绑定的电话号码以及号码所属地区。
7. 用户可以点击“复制手机号”按钮将电话号码复制到剪贴板。

## 技术实现

- 该应用使用HTML、CSS和JavaScript编写。
- 通过Fetch API与后端API进行交互，获取LOL账号和QQ号相关信息。
- 使用`copyToClipboard`函数将文本复制到剪贴板。

## 相关API

- LOL信息查询API: `https://zy.xywlapi.cc/lolname`
  - 参数: `name` (LOL昵称或QQ号)
- QQ信息查询API: `https://zy.xywlapi.cc/qqapi`
  - 参数: `qq` (QQ号)

## 注意事项

- 请确保网络连接正常，否则无法查询信息。
- 本应用仅用于查询LOL游戏相关信息，不涉及其他用途。

希望您能通过这个readme了解并使用这个LOL信息查询应用！
