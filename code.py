'''Image Captcha'''

# Importing Necessary module
from captcha.image import ImageCaptcha

# set image dimension
Captcha_image = ImageCaptcha(width = 280, height = 90)

# random genrate image having alphabet and number
values = Captcha_image.generate("Hello2001Akash")

# genrate and create the new captcha image file
Captcha_image.write("Hello2001Akash","captcha.png")