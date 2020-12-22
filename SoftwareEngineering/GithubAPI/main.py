from github import Github


def main():
    g = Github()
    user = g.get_user("Conall-Tuohy")
    for repo in user.get_repos():
        if repo.description != None:
            print(repo.name + ": " + repo.description)
        else:
            print(repo.name + ": No Desciption")


if __name__ == '__main__':
    main()
