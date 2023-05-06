def gitUserConfig():

    import configparser
    import os
    import sys

    name = input("Enter Username: ")
    email = input("Enter Useremail: ")
    section_name = 'user'

    cwd = os.getcwd()

    config = configparser.ConfigParser()

    path = os.path.join(cwd, '.git', 'config')

    try:

        if not os.path.exists(os.path.join(cwd, '.git')):
            os.system("git init")

        config.read(path)

        if not config.has_section(section_name):
            config.add_section(section_name)

        config.set(section_name, 'name', name)
        config.set(section_name, 'email', email)

        with open(path, 'w') as configfile:
            config.write(configfile)
    except Exception as e:
        print(e)
        sys.exit()

if __name__ == "__main__":
    gitUserConfig()

