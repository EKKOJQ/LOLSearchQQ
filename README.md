
# 接口已经失效!!!
试用链接：https://ekkojq.github.io/LOLSearchQQ/
# LOL信息查询程序  Py

这个简单的Python程序使用了Tkinter库和Requests库，用于查询LOL玩家的相关信息，包括QQ号码和绑定手机号等信息。

## 如何使用

1. 首先确保已经安装了Python，并安装了Tkinter和Requests库。
   
2. 运行 `main.py` 文件，启动程序。

3. 在程序界面输入要查询的LOL昵称，点击“查询”按钮。

4. 程序将会显示查询结果，包括QQ号、游戏名、游戏大区、绑定号码和号码地区。

5. 点击“复制QQ号”按钮可以复制查询到的QQ号到剪贴板，点击“复制手机号”按钮可以复制绑定手机号到剪贴板。
![image](https://github.com/EKKOJQ/LOLSearchQQ/assets/97377143/2712036d-746a-40dc-b1ad-288cb6eae885)

## 注意事项

- 确保网络连接正常，否则无法查询到相关信息。

- 若查询出错，可能是服务器异常或输入信息有误，请检查输入的LOL昵称是否正确。

- 本接口查询信息所用LOL昵称需为该账号注册时的昵称,建议配合WeGame荣誉截图查找最早的昵称
  
- 请勿滥用查询功能，遵守相关法律法规。



# LOL信息查询应用 Web端

这是一个简单的网页应用，用于查询LOL游戏玩家的相关信息，包括QQ号和绑定的电话号码。用户可以输入LOL昵称或QQ号来查询相关信息。

## 如何使用

1. 打开 `index.html` 文件。
2. 在输入框中输入LOL昵称或QQ号。
3. 点击“查询”按钮。
4. 查询结果将显示LOL账号的QQ号，游戏名和游戏大区。
5. 用户可以点击“复制QQ号”按钮将QQ号复制到剪贴板。
6. 如果查询成功，还会显示QQ绑定的电话号码以及号码所属地区。
7. 用户可以点击“复制手机号”按钮将电话号码复制到剪贴板。
![image](https://github.com/EKKOJQ/LOLSearchQQ/assets/97377143/914a5a2e-e3de-496b-9c3f-dbae6ef40e19)

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
- 如果明确说拉取不到信息，那就是接口被ban了。

## 作者

本程序由EKKOJQ开发，欢迎访问我的GitHub主页：[EKKOJQ](https://github.com/EKKOJQ)

如果有任何建议或问题，请在GitHub上提Issue。


