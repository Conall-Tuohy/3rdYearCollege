import requests
from github import Github
import networkx as nx
import matplotlib.pyplot as plt

accessTokenFile = open('token.txt', 'r')
token = accessTokenFile.readline()
accessTokenFile.close()
g = Github(token)
relationGraph = nx.Graph()


def main():
    loopProgram = 1
    exitCondition = 1
    while loopProgram:
        while exitCondition:
            print("Enter the username of the user you would like to look at:")
            user = input()
            r = requests.get('https://api.github.com/users/' + user)
            if '404' in r:
                print("That didn't seem to be a valid user, please try again")
            else:
                exitCondition = 0
                print("User found!")

        exitCondition = 0
        user = g.get_user(user)
        relationGraph.add_node(user.name, repos= user.get_repos().totalCount ,followers= user.get_followers().totalCount, following= user.get_following().totalCount)
        print("Would you like to see this users Repositories ('Y' for Yes, anything else for No)")
        if input() == 'Y':
            for repo in user.get_repos():
                if repo.description != None:
                    print(repo.name + ": " + repo.description)
                else:
                    print(repo.name + ": No Desciption")
        else:
            print("'Y' Not detected.")
        if user.get_repos().totalCount == 0:
            print("The user had no repositories.")
        if user.get_projects().totalCount == 0:
            print("The user had no projects.")
        print("The user had", user.get_followers().totalCount, "followers and followed", user.get_following().totalCount, "people.")
        print("Would you like to see the Users followers and their relevant statistics? ('Y' for Yes, anything else for No)")
        print("This step may take a while no matter the choice.")
        if input() == 'Y':
            if user.get_followers().totalCount == 0:
                print("The user had no followers and followed ", user.get_following().totalCount, " people.")
            else:
                print("Their followers were:")
                for follower in user.get_followers():
                    print(follower.name, "who has", follower.get_followers().totalCount, "followers and", follower.get_repos().totalCount, "repos")
                    relationGraph.add_node(follower.name, repos= follower.get_repos().totalCount ,followers= follower.get_followers().totalCount, following= follower.get_following().totalCount)
                    relationGraph.add_edge(user.name, follower.name, relationship="Follower")
        else:
            for follower in user.get_followers():
                relationGraph.add_node(follower.name,
                                       repos=follower.get_repos().totalCount,
                                       followers=follower.get_followers().totalCount,
                                       following=follower.get_following().totalCount)
                relationGraph.add_edge(user.name, follower.name, relationship="Follower")
        plt.plot
        pos = nx.spring_layout(relationGraph)
        color = range(20)
        print("Would you like to see the graph comparison based followers, following, or repos?('repo' for repository data, 'followers' for followers and 'following' for following)")
        graphChoice = input()
        if graphChoice == 'repo' or graphChoice == 'followers' or graphChoice == 'following':
            d = nx.get_node_attributes(relationGraph, graphChoice)
        else:
            print("Choice didn't match any options. Default option of repositories chosen")
            d = nx.get_node_attributes(relationGraph, 'repos')
        options = {
            "node_color": "#A0CBE2",
            "edge_color": "gray",
            "width": 2,
            "edge_cmap": plt.cm.Blues_r,
            "with_labels": True,
            "node_size": [v*100 for v in d.values()],
        }
        nx.draw(relationGraph, pos, **options)
        plt.show()
    else:
        print("'Y' not detected.")
    print("Program complete!")
    exit()

if __name__ == '__main__':
    main()
