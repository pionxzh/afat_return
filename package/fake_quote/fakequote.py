# -*- coding: utf-8 -*-

import imgkit
from PIL import Image
from os import path, chdir
p = path.abspath(__file__)
dir_path = path.dirname(p)

# .js檔案內容，{{}}可跳脫
js = """
    {{
    document.getElementById("avatar").style.backgroundImage='url({0})';
    document.getElementById("username").innerHTML='{1}';
    document.getElementById("username").style.color='{2}';
    document.getElementById("timestamp").innerHTML='{3}';
    document.getElementById("ctx").innerHTML='{4}';
    }}
    
    var len = document.getElementById("ctx").scrollWidth;
    var max_len = {5}
    console.log(len);
    if (len > max_len) {{
        document.getElementById("ctx").style.whiteSpace = 'pre-wrap';
        document.getElementById("ctx").style.width = max_len + 'px';
    }}
"""


def fq(avatar_url, username, timestamp, ctx, max_width=600, scale=1.2, color='#dcddde'):

    # 設定wkhtmltoimage程式位置
    chdir(dir_path)
    config = imgkit.config(wkhtmltoimage=dir_path+'\\wkhtmltoimage.exe')
    script = js.format(avatar_url, username, color, timestamp, ctx, str(max_width))
    with open('temp.js', 'w', encoding='UTF-8') as f:
        f.write(script)
    options = {
        'format': 'png',
        'encoding': "UTF-8",
        'quality': "100",
        'transparent': '',
        'zoom': str(scale),
        'quiet': '',
        'crop-y': '0',
    }
    output = 'out.png'
    imgkit.from_file(filename='sample.html', output_path=output, config=config, options=options)
    # 調用47行會在終端出現一行字，目前找不到解法
    # 已經試過調用stdout跟print('\r')等
    im = Image.open(output)
    size = (0, 3, im.size[0], im.size[1]-3)
    im = im.crop(size)
    im2 = im.crop(im.getbbox())  # 去除透明部分
    im2.save(output)
    result = open(output, 'rb')  # 返回byte形式檔案，方便傳送至Discord
    return result


if __name__ == '__main__':
    url = "https://cdn.discordapp.com/avatars/196536997039308800/a_67866b1edef6d67840a1e6b43c01e06b.png"
    fq(url, ':))', 'today', '內容'*50, 700, 1.3)

