# Day 4 - Git and Professional Engineering History

## What I Learned

Git records the history of changes made to a project. It allows engineers to review previous versions, work safely on branches and return to known versions when problems occur.

## Working Directory, Staging and Commits

My working directory contains the files I am currently editing.

`git add` places selected changes into the staging area.

`git commit` records the staged changes as a checkpoint in the local repository.

`git push` sends local commits to a remote repository such as GitHub.

## Branches

A branch provides an isolated place to make changes without directly changing the main branch.

I created the `day-04-git-practice` branch for today's work.

## Pull Requests

A pull request proposes merging changes from one branch into another.

Pull requests make it possible to review the files and commits before changing the main branch.

## Commit Messages

I used small commits with clear messages so that the repository history explains what changed.

Examples include:

- `chore: add repository ignore rules`
- `docs: add project run instructions`
- `docs: add Day 4 Git workflow notes`

## Security

I created a `.gitignore` file so that common environment files, private keys, Terraform state and generated files are not accidentally committed.

Secrets should never be committed to Git.
