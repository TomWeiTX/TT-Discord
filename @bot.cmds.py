
# проста команда:

@bot.command()
async def команда(ctx):
    await ctx.send(f' відповідь бота')

# слеш команда:

@bot.slash_command(name="команда", description="опис команди")
async def команда(ctx: discord.ApplicationContext):
    await ctx.respond(f' відповідь бота')
  
