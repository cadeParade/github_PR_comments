# github_PR_comments
gitcher comments

Export comments in markdown todo-list format from your Altschool/vishnu-frontend github pr!

```
app/templates/components/card-actions-toolbar/share-button.hbs
- [ ]    Samantha:
        --What are you doing with your code
- [ ]    Belinda:
        --This is so great
- [ ]    Samantha:
        --I can't believe you've done this

```

### REQUIREMENTS

1. [Github api token](https://github.com/blog/1509-personal-api-tokens)
2. Install python requests library: `pip install requests`
3. PR number

To use:
On command line:
`> python get_pr_comments.py <PR_NUMBER> <GITHUB_ACCESS_TOKEN>`
