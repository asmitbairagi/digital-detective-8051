# Mission 6 — Git and GitHub

## 1. Objective
To understand version control using Git and learn how GitHub supports collaboration through branches and Pull Requests.

## 2. Git Commands Practised

| Command       | Purpose                                 |

| `git status`  | Checks the current working tree status  |

| `git add`     | Stages changes                          |

| `git commit`  | Saves staged changes in Git history     |

| `git log`     | Displays commit history                 |

| `git branch`  | Lists or creates branches               |

| `git switch`  | Switches between branches               |

| `git push`    | Uploads commits to a remote repository  |

## 3. Branching

I created a separate branch named `update-about` using:

- `git branch update-about`
- `git switch update-about`

A branch allows developers to work on changes independently without directly modifying the main branch.

## 4. Changes Made

I updated the root `README.md` by adding a **My Learning** section summarising the concepts covered in the assignment.

I staged and committed the change using:

- `git add README.md`
- `git commit -m "Update README with learning summary"`

## 5. Pushing the Branch

I pushed the branch to GitHub using:

`git push -u origin update-about`

The branch was successfully uploaded and linked to its remote counterpart.

## 6. Pull Request

I created a Pull Request to propose merging `update-about` into `main`.

- Source branch: `update-about`
- Target branch: `main`
- Commit: `81ff0de`
- PR status: Open

The Pull Request allows changes to be reviewed before merging. I left it open as instructed.

## 7. What I Learned

I learned how Git tracks changes, how branches isolate development work, and how Pull Requests support code review and collaboration.

I also understood the difference between committing changes locally and pushing them to a remote GitHub repository.

## 8. Evidence and Files

- Root `README.md` — Updated learning summary.
- Git commit: `81ff0de`
- GitHub branch: `update-about`
- Pull Request: [View Pull Request](https://github.com/asmitbairagi/digital-detective-8051/pull/1)

## 9. Commit Details

- Branch: `update-about`
- Commit message: `Update README with learning summary`