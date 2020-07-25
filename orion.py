import random
import os
import discord
from discord.ext import commands

# 2-200, 201-500, 501-800, 801-1200, 1201-1999
listOfReactions = [["Ты вообще бил? :Wazowski:", "Как тебя вообще взяли в гильдию? :angryFace:", "Наверное, простоял весь бой в стане :peepoRot:", "Вероятно, у него 0% хита :cringeCoin:", "Другу дал на персонаже поиграть? :pepeYEP:", "Нужно было бить, а не кусать Иринчика! :yaramazAngry:", "Это провал! :sadCat:"],
                   ["Неплохо, если ты СОВА :owl:", "Не размялся перед боем? :Thonk:", "Шо такое? Слетели хоткеи? :HEH:", "Опять пол боя переписывался с Фочерепом? :pepeEZ:", "Поднажми, а то кикнут из статика! :monkaGun:", "Молодец - обогнал мили-ханта на 1 ДПС! :Kappa:", "Ты в пвп-спеке, гиена? :pigFace:"],
                   ["ДПС среднестатистического орионца :peepoPet:", "Не стоило пропускать субботний забафф :wowRetroPal:", "Еще чуть-чуть поднажать, и девочки будут от тебя в восторге! :AYAYA:", "Иди почитай еще гайды :peepoDumb:", "Впрочем, никто не удивлён :peepoSmoke:", "Гордиться еще рано :peepoToilet:"],
                   ["Ух, почему ты еще не КЛ? :pepeEvilLook:", "Вот это достойная цифра! :wolf~1:", "...А вот если бы взял все ворлд-баффы... :RoflanEbalo:", "Хмм, наверное ты рога или вар... или смайт-прист :monkaHmm:", "Вот кто тащит Орион на своих плечах! :PogU:", "Это у тебя прозвище \"Большая пушка?\" :oFROGo:"],
                   ["Ну ты зверюга! :dinoEZ:", "Звезда Азерота в деле! :bearHappy:", "Это твой памятник стоит на входе в Штормград? :peepoHappy:", "Да тебе пора писать гайды на WoWHead :pepeG:", "Винтер Чилл уже положил на тебя глаз :peepoDetective:", "Ну как тебя похвалить? Ну за#бись ДПС. П#здатый ДПС. Ещё пару красивых слов? Невъ#бенный ДПС!"]]

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    game = discord.Game(name='!help')
    await bot.change_presence(activity=game)


@bot.command(name='sendAll', help='Рассылает введённое сообщение всем членам гильдии')
@commands.has_role('Администратор')
async def sendAll(ctx, *, message):
    guild = bot.get_guild(733311628208242858)
    role = guild.get_role(733320565879996467)
    getters = role.members
    for member in getters:
        await member.send(message)


@sendAll.error
async def sendAll_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send('Где сообщение, Тварына?')
    elif isinstance(error, commands.MissingRole):
        await ctx.channel.send('Недостаточно прав, Перчик')


@bot.command(name='roll', help='Аналог /roll из игры с диапазоном значений от 1 до 100')
@commands.has_role('орионовец')
async def roll(ctx):
    embed = discord.Embed(
        color=discord.Color.teal(),
        description=f":game_die: {ctx.message.author.display_name} выбрасывает {random.randint(1, 100)} :game_die:"
    )
    await ctx.channel.send(embed=embed)


@bot.command(name='dps', help='/roll на ДПС от 1 до 2000')
@commands.has_role('орионовец')
async def dps(ctx):
    dps = random.randint(1, 2000)
    reaction = ''
    if dps == 1:
        reaction = "Ты не в ту сторону воюешь, Сынок :KEKW:"
    elif dps == 666:
        reaction = "Ну ты ЧОРТ :imp:"
    elif dps == 777:
        reaction = "Ёб#нный рот этого казино! :slot_machine:"
    elif dps == 1488:
        reaction = "А вот это уже статья... :pepeSSS:"
    elif dps == 2000:
        reaction = "Адский разгон! Нам п#зда! :Jerry:"
    elif dps < 201:
        reaction = listOfReactions[0][random.randint(0, 6)]
    elif dps < 501:
        reaction = listOfReactions[1][random.randint(0, 6)]
    elif dps < 801:
        reaction = listOfReactions[2][random.randint(0, 5)]
    elif dps < 1201:
        reaction = listOfReactions[3][random.randint(0, 5)]
    elif dps < 2000:
        reaction = listOfReactions[4][random.randint(0, 5)]
    embed = discord.Embed(
        color=discord.Color.teal(),
        description=f"{ctx.message.author.display_name} разогнался до {dps} ДПС! {reaction}"
    )
    await ctx.channel.send(embed=embed)


@bot.command(name='help', help='Выводит список доступных команд с пояснениями')
@commands.has_role('орионовец')
async def help(ctx):
    embed = discord.Embed(
        color=discord.Color.blue(),
        description=":regional_indicator_h: :regional_indicator_e: :regional_indicator_l: :regional_indicator_p: "
    )
    for command in bot.commands:
        embed.add_field(name=bot.command_prefix+command.name, value=command.help, inline=False)
    await ctx.channel.send(embed=embed)

bot.run(os.environ['token'])
