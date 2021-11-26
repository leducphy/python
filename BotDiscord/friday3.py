from time import sleep
import discord
from discord.ext import commands
import random
import sys
import requests 
from friday_image import friday_image

response = requests.get('https://api.apify.com/v2/key-value-stores/ZsOpZgeg7dFS1rgfM/records/LATEST?utm_source=j2team&utm_medium=url_shortener')
data = response.json()
friday = commands.Bot(command_prefix='.')
friday.add_cog(friday_image(friday))

@friday.event
async def on_ready():
    print('We have logged in as {0.user}'.format(friday))

@friday.command()
async def ping(ctx):
    await ctx.send(f'```Ping: {round(friday.latency * 1000)}ms```')

@friday.command()
async def rd(ctx):
    rand = ['A', 'B', 'C', 'D']
    await ctx.send(f'```The correct answer is: {random.choice(rand)} ```')

@friday.command()
async def ext(ctx):
    await ctx.send("```Goodbye!\nBot is offline```")
    sys.exit()

@friday.command()
async def fe(ctx):
    fe = f'```PRF192      06/11/2021      12h50-14h20      PE      \nCSI104      17/11/2021      07h30-09h00      FE      \nPRF192      18/11/2021      16h10-17h40      FE      \nMAE101      19/11/2021      07h30-09h00      FE      \nCEA201      20/11/2021      09h10-10h40      FE      ```'
    await ctx.send(fe)

@friday.command()
async def list(ctx):
    listThanhPho = f'```0.TP. Hồ Chí Minh \n1.Bình Dương \n2.Đồng Nai \n3.Long An \n4.Tiền Giang \n5.Tây Ninh \n6.An Giang \n7.Đồng Tháp \n8.Khánh Hòa \n9.Kiên Giang \n10.Cần Thơ \n11.Bắc Giang \n12.Đà Nẵng \n13.Bình Thuận\n14.Bà Rịa – Vũng Tàu \n15.Hà Nội \n16.Sóc Trăng \n17.Đắk Lắk \n18.Phú Yên \n19.Trà Vinh \n20.Vĩnh Long \n21.Nghệ An \n22.Bến Tre \n23.Bắc Ninh \n24.Bạc Liêu \n25.Quảng Bình \n26.Cà Mau \n27.Bình Phước \n28.Bình Định \n29.Gia Lai \n30.Quảng Nam \n31.Ninh Thuận \n32.Hậu Giang \n33.Thừa Thiên Huế \n34.Thanh Hóa \n35.Hải Dương \n36.Hà Nam \n37.Đắk Nông \n38.Hà Giang \n39.Phú Thọ \n40.Hà Tĩnh \n41.Quảng Ngãi \n42.Lâm Đồng \n43.Quảng Trị \n44.Hưng Yên \n45.Sơn La \n46.Nam Định \n47.Vĩnh Phúc \n48.Lạng Sơn \n49.Kon Tum \n50.Ninh Bình \n54.Hải Phòng \n55.Điện Biên \n56.Hòa Bình \n57.Thái Nguyên \n58.Tuyên Quang \n59.Yên Bái \n60.Lai Châu \n61.Bắc Kạn \n62.Cao Bằng```'
    await ctx.send(listThanhPho)

@friday.command()
async def cov(ctx, *num):
    num =int(" ".join(num))
    detail = f'```Detail: {data["detail"][num]["name"]} \nDeath: {data["detail"][num]["death"]} \nCases: {data["detail"][num]["cases"]} \nCases Today: {data["detail"][num]["casesToday"]}```'
    print(detail)
    await ctx.send(detail)

# @friday.command(aliases = ['q', 'r'])
# async def ques(ctx, *, ques):
#     response = ['Quân', 'Thái', 'Nhân', 'Hân']
#     await ctx.send(f'Question: {ques}\nAnswer: {random.choice(response)} là người ngu nhất. =))))')










#token   
token = "OTAwNDI0MDk0NjUzMjMxMTU0.YXBHSQ.qX7hWhsggpxSN671etVdjU2nVMM"
friday.run(token)
