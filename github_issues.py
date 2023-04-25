from github import Github


#TOK = "your token"
g = Github(TOK)


Repo_name = "kaihsin/Cytnx"
repo = g.get_repo(Repo_name)

## get issues:
open_issues = repo.get_issues(state='open')
for issue in open_issues:
    title = "[#%d] %s"%(issue.number,issue.title)
    print(issue.body)
    comments = issue.get_comments()

    print("=======")


    for i,comment in enumerate(comments):
        print("[comment %d]"%(i))
        print(comment.body)








