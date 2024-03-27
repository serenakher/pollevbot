from pollevbot import PollBot


def main():
    user = 'sk10780@nyu.edu'
    password = 'Gintro1123!'
    host = 'kw3341'

    # If you're using a non-uw PollEv account,
    # add the argument "login_type='pollev'"
    with PollBot(user, password, host) as bot:
        bot.run()


if __name__ == '__main__':
    main()
