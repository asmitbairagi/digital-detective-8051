# Mission 2 — Terminal and File Management

## 1. Task / Objective

Learn how to navigate the macOS Terminal, manage files and directories, understand command flags, use pipes, and explore Homebrew.

## 2. Commands Practised

| Command    | Purpose                                |

| `pwd`      | Displays the current working directory |

| `ls`       | Lists files and directories            |

| `ls -la`   | Displays hidden files and detailed information |

| `ls -lh`   | Displays file sizes in human-readable format |

| `cd`       | Changes the current directory |

| `cd ..`    | Moves to the parent directory |

| `mkdir`    | Creates directories |

| `mkdir -p` | Creates nested directories |

| `touch`    | Creates empty files |

| `cp`       | Copies files |

| `mv`       | Moves or renames files |

| `cat`      | Displays file contents |

| `echo`     | Prints text |

| `>`        | Redirects output and overwrites existing contents |

| `>>`       | Appends output to existing contents |

| `grep`     | Searches for matching text |

| `ls -R`    | Lists directory contents recursively |

## 3. Practical Work

Created a `terminal-practice` directory containing:

- `notes.txt`
- `notes_backup.txt`
- `commands.txt`
- `practice/level1/level2/`

Practised moving files using `mv`, copying files using `cp`, and creating nested directories using `mkdir -p`.

Also practised output redirection using `>` and `>>`, and displaying file contents using `cat`.

## 4. Flags and Pipes

Flags modify the behaviour of commands.

Examples:
- `-l`: Long listing format.
- `-a`: Includes hidden files.
- `-h`: Human-readable file sizes.
- `-p`: Creates parent directories when used with `mkdir`.
- `-R`: Recursive listing.

A pipe (`|`) passes the output of one command to another.

Example:

`ls -l | grep ".txt"`

This filters the command output to show lines containing `.txt`.

## 5. Homebrew

Checked Homebrew installation and existing packages.

- Homebrew version: 7.0.13
- Checked installed formulae and casks using `brew list`.

Homebrew is a package manager for macOS that helps install and manage software and developer tools.

## 6. What I Learned

I learned how to navigate directories, create and manage files, copy and move files, inspect file contents, use command flags, redirect output, and connect commands using pipes.

I also understood the difference between moving a file and creating a separate copy.

## 7. Difficulties and Resolutions

Initially, I created the practice files in the mission directory instead of the `terminal-practice` directory. I corrected this by using the `mv` command.

I also learned how `>` overwrites existing file contents, whereas `>>` appends new content.

## 8. Evidence and Files

- `terminal-practice/notes.txt`
- `terminal-practice/notes_backup.txt`
- `terminal-practice/commands.txt`
- `terminal-practice/practice/level1/level2/`

## 9. Commit Details

To be updated after committing and pushing Mission 2 to GitHub.