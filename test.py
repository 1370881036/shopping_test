from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
print("当前页面标题:", driver.title)

# 添加 input() 阻塞程序，按回车后才会关闭浏览器
input("按 Enter 键关闭浏览器...")  # 程序会停在这里等待用户操作

driver.quit()