import plyer


def notify_message(message):
    plyer.notification.notify(
        title="Silent Print Application",
        message=message,
        app_icon="temp/print.ico",
        timeout=1,
    )