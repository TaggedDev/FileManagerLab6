File manager project. 
---
<sub>Laboratory work No. 6 on the discipline "Programming Workshop". The second year of study at the Financial University</sub>

File manager is a command line that uses `os` module and `shutil`. File manager specifies environment folder and works only inside of it. Will create config folder on the first launch. Available commands:
* `mkdir foldername` - create folder in current directory called `foldername` (supports creating inner folders)
* `rm folderpath` - removes folder located on the `path` (folder path must end with `\`)
* `go path` - moves in folder
* `go ..` - goes back
* `cat path` - displays folder content or file content
* `touch filename` - creates new file called `filename`
* `write filename` - writes text (using `input()` function) in file called `filename`
* `rename filename, new_filename` - changes name from `filename` to `new_filename`
* `move filename, new_path` - removes file called `filename` from it's current path and creates it in `new_path` (file content saved)
* `copy filename, new_path` - moves file called `filename` but doesn't remove it
