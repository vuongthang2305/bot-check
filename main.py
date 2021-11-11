import discord, json
from discord.ext.commands import Bot
from discord import Member, Client, ClientUser, File
from easy_pil import Font,Editor, Canvas
import requestt

TOKEN = ''
bot = Bot('!')

@bot.command(pass_context=True, name='check')
async def check(ctx, *args):
    summoner_name = ' '.join(args)

    
    class user():
        name = 0
        score = 1
        def __init__(self,name , score = 1):
            self.name = name
            self.score = score
    data = requestt.cralw(summoner_name)
    json.dumps(data)
    print(type(data), data)
    if data['code'] == 200:
        db = [user(data['champ_top']['champ_name'], data['champ_top']['score']),user(data['champ_mid']['champ_name'], data['champ_mid']['champ_name']),user(data['champ_jungle']['champ_name'], data['champ_jungle']['champ_name'])]
        db.sort(key = lambda x: x.score, reverse = True)
        for i in db:
            print(i.name, i.score)
        
        his = data['history']
        if len(his) < 1:
            await ctx.send('Không tìm thấy lịch sử đấu vui lòng thử lại')
            win_rate = 0
        else:
            win_rate = round(int(his.count('Thắng')) / len(his) * 100, 2)

        rank = str(data['rank']).split(' ')[0]
        background = Editor(f"./champion/{str(data['champ_mid']['champ_name']).lower()}.jpg")
        profile = Editor("./img/avt.jpg").resize((80, 80)).circle_image()
        profile_image = Editor("./img/os.png")
        icon_rank = Editor(f"./rank/{rank}.png").resize((130, 130))
        square = Canvas((1920,1080), (255,255,255,90))
        background.paste(square, (0,0))

        x = 680
        y = 125

        for i in range(len(his)):
            if i == 10:
                x = 680
                y = y + 30
            x = x + 30
            if his[i] == 'Thất Bại':
                background.rectangle((x,y), 20,20, "red","red",1)
            else:
                background.rectangle((x,y), 20,20, "blue","blue",1)


        champ = Editor("./avatar_champion/" + db[0].name.lower() + ".jpg").resize((100,100)).circle_image()
        background.text((520 + 20, 320), db[0].name, font = Font("./font1.ttf", 20))
        background.paste(champ.image, (520  ,190))
        db.remove(db[0])
        x_champ = 370
        for i in range(len(db)):

            if "'" in  db[i].name:
                name = db[i].name.lower().split("'")[0] + "" + db[i].name.lower().split("'")[1]
            else:
                name = db[i].name.lower()
                
            champ = Editor("./avatar_champion/" + name + ".jpg").resize((100,100)).circle_image()
            background.paste(champ.image, (x_champ,218))
            background.text((x_champ + 20, 340), db[i].name, font = Font("./font1.ttf", 20))
            x_champ = x_champ + 300
            
        
        background.rectangle((680,100), 350,100, None,"black",2)
        background.paste(profile_image.image, (0,0))
        background.paste(profile.image, (27,74))
        background.paste(icon_rank.image, (25,213))
        background.text((140,80), f'{data["summoner_name"]}', font=Font("./font1.ttf", 20), color="white")
        background.text((140,110), f'{data["level"]}', font=Font("./font1.ttf", 15), color="white")
        background.text((165,240), f"{data['rank']}", font=Font("./font1.ttf", 20), color="white")
        background.text((165,270), f"Win Rate: {win_rate}%", font=Font("./font1.ttf", 15), color="white")
        file = File(fp=background.image_bytes, filename='card.png')
        await ctx.send(file = file)
    else:
        await ctx.send(f'{data["message"]}')
bot.run(TOKEN)