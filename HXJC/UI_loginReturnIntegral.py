# -----------------------------------------------本用例用于海西建材的人员登录获取积分测试
import pymssql,time
from selenium import webdriver
import tesserocr
from PIL import Image
#数据库类
class ConnectDataBase:
    def __init__(self,server,user,password,database):
        self.server=server
        self.user=user
        self.password=password
        self.database=database
    def get_connection(self):
        self.conn=pymssql.connect(self.server,self.user,self.password,self.database)
        self.conn.autocommit(True)
        cursor=self.conn.cursor()
        if not cursor:
            raise (NameError,'连接数据库失败')
        else:
            return cursor
    def execute_sql(self,sql,valueList=None):
        cursor=self.get_connection()
        if valueList:#插入数据
            cursor.executemany(sql, valueList)
            self.conn.close()
        else:#查询数据
            cursor.execute(sql)
            results = cursor.fetchall()
            self.conn.close()
            return results
#图片处理类
class ImageProcessing:
    def image_grayscale_deal(self,image):
        """
        图片转灰度处理
        :param image:图片文件
        :return: 转灰度处理后的图片文件
        """
        image = image.convert('L')
        # 取消注释后可以看到处理后的图片效果
        # image.show()
        return image

    def image_thresholding_method(self,image):
        """
        图片二值化处理
        :param image:转灰度处理后的图片文件
        :return: 二值化处理后的图片文件
        """
        # 阈值，控制二值化程度，自行调整（不能超过256）
        threshold = 200
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        # 图片二值化，此处第二个参数为数字一
        image = image.point(table, '1')

        # 取消注释后可以看到处理后的图片效果
        # image.show()
        return image

    # 去噪点处理
    def image_interference_point(self,image):
        data = image.getdata()
        w, h = image.size
        black_point = 0
        for x in range(1, w - 1):
            for y in range(1, h - 1):
                mid_pixel = data[w * y + x]  # 中央像素点像素值
                if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
                    top_pixel = data[w * (y - 1) + x]
                    left_pixel = data[w * y + (x - 1)]
                    down_pixel = data[w * (y + 1) + x]
                    right_pixel = data[w * y + (x + 1)]
                    # 判断上下左右的黑色像素点总个数
                    if top_pixel < 10:
                        black_point += 1
                    if left_pixel < 10:
                        black_point += 1
                    if down_pixel < 10:
                        black_point += 1
                    if right_pixel < 10:
                        black_point += 1
                    if black_point < 1:
                        image.putpixel((x, y), 255)
                    # print(black_point)
                    black_point = 0

        image.save('VerifyCodeImg1.png')
        return image
#获取返回积分
def getIntegral(username):
    time.sleep(1)
    responseText=driver.find_element_by_css_selector('.l-dialog-content.l-dialog-content-noimage.l-dialog-content-nopadding').text
    print(username,'    ',responseText)
    if responseText=='登录失败':
        driver.find_element_by_css_selector('.l-dialog-btn-inner').click()
        time.sleep(1)
        driver.find_element_by_css_selector('#Verifycode').clear()
        driver.find_element_by_css_selector('#VerifyCodeImg').click()
        time.sleep(1)
        verifyCodeImgText = getVerifyCode()
        driver.find_element_by_css_selector('#Verifycode').send_keys(verifyCodeImgText)
        time.sleep(1)
        getIntegral(username)
    elif responseText=='登录成功':
        driver.execute_script("$.post('/HXHome/Logout',null,function(){location.reload();})")
    elif '每日首次登录' in responseText:
        driver.execute_script("$.post('/HXHome/Logout',null,function(){location.reload();})")

#获取验证码
def getVerifyCode():
    driver.find_element_by_css_selector('#VerifyCodeImg').screenshot('VerifyCodeImg.png')
    image = Image.open('VerifyCodeImg.png')
    # 将图像进行转灰度、二值化处理，便于tesserocr识别
    imageObj = ImageProcessing()
    image = imageObj.image_grayscale_deal(image)
    image = imageObj.image_thresholding_method(image)
    image = imageObj.image_interference_point(image)
    verifyCodeImgText = tesserocr.image_to_text(image)
    return verifyCodeImgText

#----------------------------------------配置信息
dbServer='192.168.0.108'
url='localhost:38850'
user='devuser'
password='devuser'
database='HXJC'
#----------------------------------------
conn_object=ConnectDataBase(dbServer,user,password,database)
sql="SELECT* from tbSysUser where Password LIKE '%E10ADC3949BA59ABBE56E057F20F883E%'"
results=conn_object.execute_sql(sql)

try:
    driver=webdriver.Chrome()
    driver.get(f'http://{url}/HXHome/Login?returnUrl=http://{url}//')
    driver.implicitly_wait(10)
    driver.maximize_window()
    time.sleep(1)
    for result in results:
        verifyCodeImgText=getVerifyCode()
        driver.find_element_by_css_selector('#UserName').send_keys(result[1])
        driver.find_element_by_css_selector('#Password').send_keys('123456')
        driver.find_element_by_css_selector('#Verifycode').send_keys(verifyCodeImgText)
        # driver.find_element_by_css_selector('.dl_nav').click()
        time.sleep(1)
        getIntegral(result[1])
except Exception as e:
    print('--------------出错了----------------')
    # driver.quit()
    raise e
driver.quit()


