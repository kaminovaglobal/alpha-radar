import asyncio

from telegram import Bot

from config import (
    BOT_TOKEN,
    CHAT_ID
)

bot = Bot(BOT_TOKEN)


class Item:
    def init(self, category, title):
        self.category = category
        self.title = title


async def send_report(all_items):
    report = "🚀 Alpha Radar Daily Intel\n\n"

    for item in all_items[:10]:
        report += (
            f"{item.category}:\n"
            f"{item.title}\n\n"
        )

    await bot.send_message(
        chat_id=CHAT_ID,
        text=report
    )


test_items = [
    Item("Funding", "Monad raises funding"),
    Item("Security", "Bridge exploit detected")
]

asyncio.run(send_report(test_items))