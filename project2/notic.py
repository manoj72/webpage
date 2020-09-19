from plyer import notification
def notification1(title,massage):
    notification.notify(
    title=title,
    massage=massage,
    app_icon=None,
    timeout=10
    )
if __name__ == '__main__':
    notification1('hello', 'i am manoj bhatt')
