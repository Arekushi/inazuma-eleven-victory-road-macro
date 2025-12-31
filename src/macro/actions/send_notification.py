import asyncio
from desktop_notifier import DEFAULT_SOUND, DesktopNotifier, Urgency


notifier = DesktopNotifier(
    app_name='IE: Victory Road Macro'
)

def send_notification(
    title: str,
    message: str
):
    async def send_coro():
        await notifier.send(
            title=title,
            message=message,
            urgency=Urgency.Normal,
            on_clicked=None,
            on_dismissed=None,
            timeout=30,
            sound=None
        )
    
    try:
        loop = asyncio.get_running_loop()
        _ = asyncio.create_task(send_coro())
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(send_coro())
        loop.close()
