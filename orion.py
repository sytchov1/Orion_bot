import random
import os
import discord
from discord.ext import commands

# 2-200, 201-500, 501-800, 801-1200, 1201-1999
listOfReactions = [["Ты вообще бил? <:Wazowski:735071616278462515>", "Как тебя вообще взяли в гильдию? <:angryFace:734840585839706202>", "Наверное, простоял весь бой в стане <:peepoRot:735068283325251594>", "Вероятно, у него 0% хита <:cringeCoin:735442078502223902>", "Другу дал на персонаже поиграть? <:pepeYEP:736132332674744431>", "Нужно было бить, а не кусать Иринчика! <:yaramazAngry:736237341940908042>", "Это провал! <:sadCat:734828578692268061>"],
                   ["Неплохо, если ты СОВА :owl:", "Не размялся перед боем? <:Thonk:736132222498897950>", "Шо такое? Слетели хоткеи? <:HEH:735079233759608932>", "Опять пол боя переписывался с Фочерепом? <:pepeEZ:735054691792060506>", "Поднажми, а то кикнут из статика! <:monkaGun:734827149470597212>", "Молодец - обогнал мили-ханта на 1 ДПС! <:Kappa:734842134817144942>", "Ты в пвп-спеке, гиена? <:pigFace:736131906827190357>"],
                   ["ДПС среднестатистического орионца <:peepoPet:735074292848525392>", "Не стоило пропускать субботний забафф <:wowRetroPal:735833161585393748>", "Еще чуть-чуть поднажать, и девочки будут от тебя в восторге! <:AYAYA:734831458203598872>", "Иди почитай еще гайды <:peepoDumb:735051861358280714>", "Впрочем, никто не удивлён <:peepoSmoke:735054922520854578>", "Гордиться еще рано <:peepoToilet:734849389692059688>"],
                   ["Ух, почему ты еще не КЛ? <:pepeEvilLook:735075521334870068>", "Вот это достойная цифра! <:wolf_woah:734847495858946078>", "...А вот если бы взял все ворлд-баффы... <:RoflanEbalo:735052900195237968>", "Хмм, наверное ты рога или вар... или смайт-прист <:monkaHmm:734830012649177311>", "Вот кто тащит Орион на своих плечах! <:PogU:734853384573550612>", "Это у тебя прозвище \"Большая пушка?\" <:oFROGo:734851248108601504>"],
                   ["Ну ты зверюга! <:dinoEZ:734853153907933305>", "Звезда Азерота в деле! <:catShy:734854369874542752>", "Это твой памятник стоит на входе в Штормград? <:peepoHappy:734860687360262171>", "Да тебе пора писать гайды на WoWHead <:pepeG:734842056962211993>", "Винтер Чилл уже положил на тебя глаз <:peepoDetective:734832063521357894>", "Ну как тебя похвалить? Ну за#бись ДПС. П#здатый ДПС. Ещё пару красивых слов? Невъ#бенный ДПС! <:pepeClown:734832082660098148>"]]

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    game = discord.Game(name='!help')
    await bot.change_presence(activity=game)


@bot.command(name='sendAll', help='Рассылает введённое сообщение всем членам гильдии')
@commands.has_role('Админ')
async def sendAll(ctx, *, message):
    guild = bot.get_guild(701839838160355348)
    role = guild.get_role(701928368865804318)
    getters = role.members
    for member in getters:
        await member.send(message)


@sendAll.error
async def sendAll_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send('Где сообщение, Митруд?')
    elif isinstance(error, commands.MissingRole):
        await ctx.channel.send('Недостаточно прав, Перчик')


@bot.command(name='roll', help='Аналог /roll из игры с диапазоном значений от 1 до 100')
@commands.has_role('Участник гильдии')
async def roll(ctx):
    embed = discord.Embed(
        color=discord.Color.teal(),
        description=f":game_die: {ctx.message.author.display_name} выбрасывает {random.randint(1, 100)} :game_die:"
    )
    await ctx.channel.send(embed=embed)


@bot.command(name='dps', help='/roll на ДПС от 1 до 2000')
@commands.has_role('Участник гильдии')
async def dps(ctx):
    dps = random.randint(1, 2000)
    reaction = ''
    if dps == 1:
        reaction = "Ты не в ту сторону воюешь, Сынок <:KEKW:734849495912939561>"
    elif dps == 666:
        reaction = "Ну ты ЧОРТ :imp:"
    elif dps == 777:
        reaction = "Ёб#нный рот этого казино! :slot_machine:"
    elif dps == 1488:
        reaction = "А вот это уже статья... <:pepeSSS:735063236558192721>"
    elif dps == 2000:
        reaction = "Адский разгон! Нам п#зда! <:Jerry:734847322810220664>"
    elif dps < 351:
        reaction = listOfReactions[0][random.randint(0, 6)]
    elif dps < 701:
        reaction = listOfReactions[1][random.randint(0, 6)]
    elif dps < 1101:
        reaction = listOfReactions[2][random.randint(0, 5)]
    elif dps < 1601:
        reaction = listOfReactions[3][random.randint(0, 5)]
    elif dps < 2000:
        reaction = listOfReactions[4][random.randint(0, 5)]
    embed = discord.Embed(
        color=discord.Color.teal(),
        description=f"{ctx.message.author.display_name} разогнался до {dps} ДПС! {reaction}"
    )
    await ctx.channel.send(embed=embed)


@bot.command(name='clear', help='удаляет все сообщения до стоп-символа (включительно). За раз можно удалить не более 50 сообщений')
@commands.has_role('Админ')
async def clear(ctx):
    stopReaction = '🛑'
    deletingMessages = []
    async for message in ctx.channel.history(limit=50):
        for reaction in message.reactions:
            if reaction.emoji == stopReaction:
                async for user in reaction.users():
                    if user.top_role.name == 'Админ':
                        deletingMessages.append(message)
                        await ctx.channel.delete_messages(deletingMessages)
                        return
        deletingMessages.append(message)


@bot.command(name='help', help='Выводит список доступных команд с пояснениями')
@commands.has_role('Участник гильдии')
async def help(ctx):
    embed = discord.Embed(
        color=discord.Color.blue(),
        description=":regional_indicator_h: :regional_indicator_e: :regional_indicator_l: :regional_indicator_p: "
    )
    for command in bot.commands:
        embed.add_field(name=bot.command_prefix+command.name, value=command.help, inline=False)
    await ctx.channel.send(embed=embed)

bot.run(os.environ['token'])
