import discord
from discord.ext import commands

from calcs.combat import Combat
from calcs.experience import next_level_string
from helpers.hiscore import Hiscore
from helpers.tracker import Tracker
from helpers.urls import get_icon_url, hiscore_url


class Levels(commands.Cog, command_attrs=dict(hidden=True)):
    """ Level commands used to pull stats from hiscore page.\n(Logout or hop to update hiscore page) """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='stats',
                      description='Show all stats for a user',
                      aliases=['stat', 'hiscore', 'hiscores'],
                      hidden=False,
                      case_insensitive=True)
    async def stats_command(self, ctx, *username):
        """ Shows all stats for a user """
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title=safe_name,
                              description=f'**{user.overall_xp:,}** XP\n'
                                          f'**{user.overall_level:,}** Total\n'
                                          f'**{user.overall_rank:,}** Rank',
                              url=f'{hiscore_url}{url_safe_name}')
        embed.add_field(name='Details', value=f'```{user.generate_hiscore_table()}```')
        embed.set_footer(text=f'Closest level up: {user.closest_level_up()}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='lvl',
                      description='Use to list all available level commands',
                      aliases=['levels', 'level', 'lvls'],
                      hidden=False,
                      case_insensitive=True)
    async def levels_command(self, ctx):
        """ Shows a list of available level commands """
        bot = ctx.bot
        embed = discord.Embed(title="Levels", description="Here is a list of available level lookup commands")
        temp = ""
        for command in bot.get_cog("Levels").get_commands():
            temp += f'`{command}`\n'
        embed.add_field(name="Commands", value=temp, inline=True)
        example = f'```!b [command|alias] <username>```Common nicknames are possible to use\n' \
                  f'For example:```!b att bluetrane```To see list of aliases type ```!b help [command]```'
        embed.add_field(name="Usage", value=example)
        embed.set_footer(text=f'Level commands used to pull stats from hiscore page.\n'
                              f'(Logout or hop to update hiscore page)')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)

    @commands.command(name='combat',
                      description='Calculate combat level',
                      aliases=['cmb'],
                      hidden=False,
                      case_insensitive=True)
    async def combat_command(self, ctx, *username):
        """ Calculates combat level for a user """
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Combat(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        levels = f'{safe_name}\n' \
                 f'**{user.calculate_combat():.1f}**\n' \
                 f'{user.discipline}'
        details = user.generate_combat_table()
        embed = discord.Embed(title="Combat", description=levels)
        embed.add_field(name="Details", value=f'```{details}```', inline=False)
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='overall',
                      description='Pulls the overall level for a specific username',
                      aliases=['total'],
                      case_insensitive=True)
    async def overall_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Overall", description=f'{safe_name}')
        embed.add_field(name="Level", value=f'**{user.overall_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.overall_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.overall_rank:,}', inline=True)
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='attack',
                      description='Pulls the attack level for a specific username',
                      aliases=['att'],
                      case_insensitive=True)
    async def attack_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Attack", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("attack")}')
        embed.add_field(name="Level", value=f'**{user.attack_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.attack_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.attack_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.attack_xp, "attack")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='defence',
                      description='Pulls the defence level for a specific username',
                      aliases=['defense', 'def'],
                      case_insensitive=True)
    async def defence_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Defence", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("defence")}')
        embed.add_field(name="Level", value=f'**{user.defence_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.defence_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.defence_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.defence_xp, "defence")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='strength',
                      description='Pulls the strength level for a specific username',
                      aliases=['str'],
                      case_insensitive=True)
    async def strength_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Strength", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("strength")}')
        embed.add_field(name="Level", value=f'**{user.strength_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.strength_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.strength_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.strength_xp, "strength")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='hitpoints',
                      description='Pulls the hitpoints level for a specific username',
                      aliases=['hp', 'health'],
                      case_insensitive=True)
    async def hitpoints_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Hitpoints", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("hitpoints")}')
        embed.add_field(name="Level", value=f'**{user.hitpoints_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.hitpoints_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.hitpoints_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.hitpoints_xp, "hitpoints")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='ranged',
                      description='Pulls the ranged level for a specific username',
                      aliases=['range', 'rng'],
                      case_insensitive=True)
    async def ranged_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Ranged", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("ranged")}')
        embed.add_field(name="Level", value=f'**{user.ranged_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.ranged_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.ranged_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.ranged_xp, "ranged")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='prayer',
                      description='Pulls the prayer level for a specific username',
                      aliases=['pray'],
                      case_insensitive=True)
    async def prayer_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Prayer", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("prayer")}')
        embed.add_field(name="Level", value=f'**{user.prayer_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.prayer_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.prayer_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.prayer_xp, "prayer")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='magic',
                      description='Pulls the magic level for a specific username',
                      aliases=['mage'],
                      case_insensitive=True)
    async def magic_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Magic", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("magic")}')
        embed.add_field(name="Level", value=f'**{user.magic_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.magic_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.magic_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.magic_xp, "magic")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='cooking',
                      description='Pulls the cooking level for a specific username',
                      aliases=['cook'],
                      case_insensitive=True)
    async def cooking_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Cooking", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("cooking")}')
        embed.add_field(name="Level", value=f'**{user.cooking_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.cooking_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.cooking_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.cooking_xp, "cooking")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='woodcutting',
                      description='Pulls the woodcutting level for a specific username',
                      aliases=['wc'],
                      case_insensitive=True)
    async def woodcutting_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Woodcutting", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("woodcutting")}')
        embed.add_field(name="Level", value=f'**{user.woodcutting_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.woodcutting_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.woodcutting_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.woodcutting_xp, "woodcutting")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='fletching',
                      description='Pulls the fletching level for a specific username',
                      aliases=['fletch'],
                      case_insensitive=True)
    async def fletching_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Fletching", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("fletching")}')
        embed.add_field(name="Level", value=f'**{user.fletching_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.fletching_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.fletching_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.fletching_xp, "fletching")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='fishing',
                      description='Pulls the fishing level for a specific username',
                      aliases=['fish'],
                      case_insensitive=True)
    async def fishing_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Fishing", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("fishing")}')
        embed.add_field(name="Level", value=f'**{user.fishing_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.fishing_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.fishing_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.fishing_xp, "fishing")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='firemaking',
                      description='Pulls the firemaking level for a specific username',
                      aliases=['fm'],
                      case_insensitive=True)
    async def firemaking_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Firemaking", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("firemaking")}')
        embed.add_field(name="Level", value=f'**{user.firemaking_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.firemaking_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.firemaking_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.firemaking_xp, "firemaking")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='crafting',
                      description='Pulls the crafting level for a specific username',
                      aliases=['craft'],
                      case_insensitive=True)
    async def crafting_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Crafting", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("crafting")}')
        embed.add_field(name="Level", value=f'**{user.crafting_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.crafting_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.crafting_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.crafting_xp, "crafting")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='smithing',
                      description='Pulls the smithing level for a specific username',
                      aliases=['smith'],
                      case_insensitive=True)
    async def smithing_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Smithing", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("smithing")}')
        embed.add_field(name="Level", value=f'**{user.smithing_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.smithing_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.smithing_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.smithing_xp, "smithing")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='mining',
                      description='Pulls the mining level for a specific username',
                      aliases=['mine'],
                      case_insensitive=True)
    async def mining_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Mining", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("mining")}')
        embed.add_field(name="Level", value=f'**{user.mining_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.mining_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.mining_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.mining_xp, "mining")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='herblore',
                      description='Pulls the herblore level for a specific username',
                      aliases=['herb'],
                      case_insensitive=True)
    async def herblore_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Herblore", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("herblore")}')
        embed.add_field(name="Level", value=f'**{user.herblore_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.herblore_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.herblore_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.herblore_xp, "herblore")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='agility',
                      description='Pulls the agility level for a specific username',
                      aliases=['agil'],
                      case_insensitive=True)
    async def agility_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Agility", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("agility")}')
        embed.add_field(name="Level", value=f'**{user.agility_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.agility_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.agility_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.agility_xp, "agility")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='thieving',
                      description='Pulls the thieving level for a specific username',
                      aliases=['thiev', 'thief'],
                      case_insensitive=True)
    async def thieving_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Thieving", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("thieving")}')
        embed.add_field(name="Level", value=f'**{user.thieving_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.thieving_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.thieving_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.thieving_xp, "thieving")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='slayer',
                      description='Pulls the slayer level for a specific username',
                      aliases=['slay'],
                      case_insensitive=True)
    async def slayer_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Slayer", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("slayer")}')
        embed.add_field(name="Level", value=f'**{user.slayer_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.slayer_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.slayer_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.slayer_xp, "slayer")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='farming',
                      description='Pulls the farming level for a specific username',
                      aliases=['farm'],
                      case_insensitive=True)
    async def farming_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Farming", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("farming")}')
        embed.add_field(name="Level", value=f'**{user.farming_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.farming_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.farming_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.farming_xp, "farming")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='runecraft',
                      description='Pulls the runecraft level for a specific username',
                      aliases=['rc'],
                      case_insensitive=True)
    async def runecraft_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Runecraft", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("runecraft")}')
        embed.add_field(name="Level", value=f'**{user.runecraft_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.runecraft_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.runecraft_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.runecraft_xp, "runecraft")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='hunter',
                      description='Pulls the hunter level for a specific username',
                      aliases=['hunt'],
                      case_insensitive=True)
    async def hunter_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Hunter", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("hunter")}')
        embed.add_field(name="Level", value=f'**{user.hunter_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.hunter_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.hunter_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.hunter_xp, "hunter")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='construction',
                      description='Pulls the construction level for a specific username',
                      aliases=['con'],
                      case_insensitive=True)
    async def construction_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="Construction", description=f'{safe_name}')
        embed.set_thumbnail(url=f'{get_icon_url("construction")}')
        embed.add_field(name="Level", value=f'**{user.construction_level:,}**', inline=True)
        embed.add_field(name="XP", value=f'{user.construction_xp:,}', inline=True)
        embed.add_field(name="Rank", value=f'{user.construction_rank:,}')
        embed.set_footer(text=f'{next_level_string(user.construction_xp, "construction")}')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='kc',
                      description='Pulls kill counts for a specific username',
                      aliases=['killcount', 'boss'],
                      hidden=False,
                      case_insensitive=True)
    async def kc_lookup(self, ctx, *username):
        """ Lookup a user's boss kill counts """
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        field_count = 0
        await ctx.send(f'{ctx.message.author.mention}')
        embed = discord.Embed(title="Boss kill counts", description=f'{safe_name}')
        if user.generate_kc_table():
            embed.add_field(name='Details', value=f'```{user.generate_kc_table()}```')
        else:
            embed.add_field(name='Nothing found', value='No kill counts on the hiscore page.')
        await ctx.send(embed=embed)
        return

    @commands.command(name="99s",
                      description='Shows all level 99s for a user',
                      aliases=['99', 'max'],
                      hidden=False,
                      case_insensitive=True)
    async def max_lvl_lookup(self, ctx, *username):
        """ Shows user's level 99s """
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        async with ctx.typing():
            await user.fetch()
        embed = discord.Embed(title="99s", description=f'{safe_name}\n{user.overall_level} total')
        count, table = user.generate_99_table()
        if table:
            embed.add_field(name=f'**{count} / 23**', value=f'```{table}```')
        else:
            embed.add_field(name=f'**0 / 23**', value='User doesn\'t have any 99s')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return

    @commands.command(name='xp',
                      description='XP tracker using Crystal Math Labs\n'
                                  'This command can be really slow because it needs to update your XP\n'
                                  'Use `mxp` alias to see monthly activity.\n'
                                  'Use `yxp` alias to see yearly activity.\n'
                                  'XP is only updated when checking weekly activity.',
                      aliases=['mxp', 'yxp'],
                      hidden=False,
                      case_insensitive=True)
    async def tracker_command(self, ctx, *username):
        """ Shows weekly activity for a user """
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        tracker = Tracker(url_safe_name)
        # Determine duration to show, defaulting to weekly (7d)
        time = '7d'
        skills = 5
        title = 'Weekly activity'
        update = True
        if ctx.invoked_with == 'xp':
            await ctx.send(f'Updating XP for **{safe_name}**...')
        if ctx.invoked_with == 'mxp':
            time = '30d'
            title = 'Monthly activity'
            skills = 10
            update = False
        elif ctx.invoked_with == 'yxp':
            time = '365d'
            title = 'Yearly activity'
            skills = 15
            update = False
        async with ctx.typing():
            await tracker.fetch(time=time, update=update)
        embed = discord.Embed(title=title, url=tracker.url)
        embed.set_thumbnail(url=tracker.logo)
        # Overall stats
        (overall_name, overall_xp, overall_rank, overall_lvl) = tracker.stats[0]
        embed.add_field(name=f'{safe_name}',
                        value=f'**{int(overall_xp):,}** XP\n'
                              f'**{int(tracker.get_non_virtual_lvl("Overall")):,}** Total\n'
                              f'**{int(overall_rank):,}** Rank')
        # Overall gains
        (overall_name, overall_xp, overall_rank, overall_levels, overall_ehp) = tracker.top_gains[0]
        embed.add_field(name='Overall gains', value=f'+{overall_xp:,} XP\n'
                                                    f'{overall_levels} levels\n'
                                                    f'{overall_rank} overall rank')
        # Top 5 gains
        embed.add_field(name=f'Top {skills} gains', value=f'```{tracker.generate_table(skills=skills)}```', inline=False)
        # Boss kills
        if tracker.generate_recent_kills_table():
            embed.add_field(name='Boss kills', value=f'```{tracker.generate_recent_kills_table()}```', inline=False)
        embed.set_footer(text=f'Checked: {tracker.last_checked} ago\n'
                              f'Changed: {tracker.last_changed} ago\n'
                              f'Oldest data point: {tracker.oldest_data} ago')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        return


# Cog setup
def setup(bot):
    bot.add_cog(Levels(bot))
