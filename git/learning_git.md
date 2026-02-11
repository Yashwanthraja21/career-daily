"Git" is an version control sytem

"Version control" is a tool that tracks, manages, and records different versions of files in a special database called a repository.
 
"Repository" stores the file. It act like an database. 


Ex: "Rough_draft.pdf" --> "Rough_draft_v2.pdf"('Some_changes' are made at Rough_draft and save) --> "Rough_draftv3.pdf"('some changes' are made at "Rough_draft_v2" and save)

So if need to use "Rough_draft_v2.pdf" i can use it with the help of version control system because the version control system hold's 
the change's made. So when ever it's required we can "Rollback" to the orginal or previous version.

The repository one in the github is remote repository and the one in machine is local repository.


![Git commands workflow](image.png)

The above diagram showing the workflow of Git commands between the working directory, staging area, local repository, and remote repository.

//Commands//

1."git clone" is used to create a local copy of an existing remote repository, including its complete commit history, branches, and files.
2."git init" Create an empty Git repository or reinitialize an existing one.
3."git add ." Stages new, modified, and deleted files (in the current directory and subdirectories).
4."git add file_name" Adds the "specified file" from the working directory to the staging area.
5."git status" is used to display the current state of files in the working directory and staging area, showing which files are untracked, modified, staged, or ready to be committed.
6."git commit -m "Message"" -creates a commit (save point) by recording the changes that are currently in the staging area into the local repository.
7."git commit -a -m "Message"" - automatically stages and commits all modified tracked files, skipping the manual "git add" step.
8."git log" - see commit history.
9."git remote add origin "repo_link"" - This command links a local Git repository to a remote repository by adding a remote reference named origin.
10."git push -u origin main" - pushing the files from local repo to remote repo. By using this command next time we can use "git push" "git pull".
11."git push origin main" - This command uploads local commits from the main branch to the main branch of the remote repository named origin.
