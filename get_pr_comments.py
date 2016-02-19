import sys
import requests


# on command line, run this file:
# > get_pr_comments.pr <PR_NUMBER> <GITHUB_ACCESS_TOKEN>

pr_num = sys.argv[1]
api_token = sys.argv[2]
r = requests.get("https://api.github.com/repos/AltSchool/vishnu-frontend/pulls/%s/comments?access_token=%s" % (pr_num, api_token))

files = {}

for comment in r.json():
  file = comment['path']
  author = comment['user']['login']
  text = comment['body']

  if file in files:
    files[file].append({
      'author': author,
      'text': text
    })
  else:
    files[file] = [{
      'author': author,
      'text': text
    }]

for file, comments in files.items():
  print file
  for comment in comments:
    print "    %s:" % comment['author']
    print "        --%s" % comment['text']