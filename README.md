# Wework-Auto-Register

selenium 练习产物，自动化浏览器以达成自动预约 Wework 办公桌操作。

原理简单，就是用 selenium 登录，点击各个按钮预约。

预约时指定文本为 **Book for 0 credit** 的按钮，因此不需要担忧 credit 被无意花费。

## 使用

1. 进入 config.py 填写账户邮箱、密码

2. 填写要预约的地点（如： `450 Lexington Ave` ），与网页内的要一致

3. 如果想要运行时看到浏览器运行，保持 `is_headless = False`；否则改为 `True` 。

4. 运行 main.py ，根据指示走即可
   - 如果是批量预约，用法为`日期&日期&日期`
