<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>CCC-OCT2023</h1>
<h3>◦ CCC-Oct2023: CCC October 2023 Solution Repository</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat&logo=HTML5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python" />
</p>
<img src="https://img.shields.io/github/license/FilipJaskovic/CCC-Oct2023?style=flat&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/FilipJaskovic/CCC-Oct2023?style=flat&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/FilipJaskovic/CCC-Oct2023?style=flat&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/FilipJaskovic/CCC-Oct2023?style=flat&color=5D6D7E" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 repository Structure](#-repository-structure)
- [⚙️ Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running CCC-Oct2023](#-running-CCC-Oct2023)
    - [🧪 Tests](#-tests)
- [🛣 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

Welcome to the CCC October 2023 Solution Repository! This repository contains my code solutions for the [Cloudflight Coding Contest October 2023](https://register.codingcontest.org/). Feel free to explore, learn and contribute.

The CCC (short for Cloudflight Coding Contest) is one of the biggest competitions of its kind. Each Spring and Autumn over 4,000 coders from all around the world simultaneously compete against each other in level-based coding games. With each level the difficulty increases and the candidate (or team) reaching the highest level within the shortest time wins.

---

## 📦 Features

|    | Feature            | Description |
|----|--------------------|--------------------------------------------------------------|
| ⚙️ | **Architecture** | The architecture is straightforward with clear separation of inputs, outputs and level descriptions. |
| 📄 | **Documentation** | There's a README file to provide a overview or to describe how to run and interact with the repository. |
| 🔗 | **Dependencies** | The repository does not have any external library dependencies. |


---


## 📂 Repository Structure

```sh
└── CCC-Oct2023/
    ├── Inputs/
    │   ├── level1_1.in
    │   ├── level1_2.in
    │   ├── level1_3.in
    │   ├── level1_4.in
    │   ├── level1_5.in
    │   ├── level1_example.in
    │   ├── level2_1.in
    │   ├── level2_2.in
    │   ├── level2_3.in
    │   ├── level2_4.in
    │   ├── level2_5.in
    │   ├── level2_example.in
    │   ├── level3_1.in
    │   ├── level3_2.in
    │   ├── level3_3.in
    │   ├── level3_4.in
    │   ├── level3_5.in
    │   └── level3_example.in
    ├── LevelDescriptions/
    ├── Outputs/
    │   ├── level1_1-output.txt
    │   ├── level1_2-output.txt
    │   ├── level1_3-output.txt
    │   ├── level1_4-output.txt
    │   ├── level1_5-output.txt
    │   ├── level1_example.out
    │   ├── level2_1-output.txt
    │   ├── level2_2-output.txt
    │   ├── level2_3-output.txt
    │   ├── level2_4-output.txt
    │   ├── level2_5-output.txt
    │   ├── level2_example.out
    │   ├── level3_1-output.txt
    │   ├── level3_2-output.txt
    │   ├── level3_3-output.txt
    │   ├── level3_4-output.txt
    │   ├── level3_5-output.txt
    │   └── level3_example.out
    ├── level1.py
    ├── level2.py
    ├── level3.py
    └── visualizer.html

```

---


## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [level1.py](https://github.com/FilipJaskovic/CCC-Oct2023/blob/main/level1.py)             | The provided Python script reads from files named'level1_#.in' where # ranges from 1 to 5 in the'Inputs' directory. The script counts occurrences of specific lines (puzzle pieces) in each file. The counts are then written into corresponding files named'level1_#-output.txt' in the'Outputs' directory.                                                                                                        |
| [visualizer.html](https://github.com/FilipJaskovic/CCC-Oct2023/blob/main/visualizer.html) | The given HTML and JavaScript code creates a web-based "Puzzle Visualizer". A user inputs a puzzle string into a text field, formatted such that each 2x2 block represents pieces and joins. As the puzzle string is modified, an SVG graphical representation of it dynamically updates, visually displaying the user's puzzle configuration in real time with different types of links between pieces.            |
| [level2.py](https://github.com/FilipJaskovic/CCC-Oct2023/blob/main/level2.py)             | The "level2.py" script counts puzzle pieces. It reads from.in files from disk, normalizes each piece by rotating it, sorts rotations, and counts repeated piece patterns using a dictionary. It then writes the total piece counts, along with corresponding puzzle piece, into a new.txt output file. The process then repeats for five.in files, named'level2_1' through'level2_5'.                               |
| [level3.py](https://github.com/FilipJaskovic/CCC-Oct2023/blob/main/level3.py)             | This'level3.py' script processes puzzles, correcting mistakes within each puzzle matrix. Each puzzle matrix is read from a specified file ('*.in') and processed to identify and correct matching pairs of'K' and'H' pieces adjacent in specific directions. The script checks all the puzzles (from'level3_1.in' to'level3_5.in'), and writes the corrected puzzles into respective output files ('*-output.txt'). |

</details>



---

## 🚀 Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ️ Dependency 1`

`- ℹ️ Dependency 2`

`- ℹ️ ...`

### 🔧 Installation

1. Clone the CCC-Oct2023 repository:
```sh
git clone https://github.com/FilipJaskovic/CCC-Oct2023
```

2. Change to the project directory:
```sh
cd CCC-Oct2023
```

3. Install the dependencies:
```sh
► INSERT-TEXT
```

### 🤖 Running CCC-Oct2023

```sh
► INSERT-TEXT
```

<!-- ### 🧪 Tests
```sh
► INSERT-TEXT
``` -->

---


<!-- ## 🛣 Project Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Implement Y`
> - [ ] `ℹ️ ...` -->


---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/FilipJaskovic/CCC-Oct2023/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/FilipJaskovic/CCC-Oct2023/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/FilipJaskovic/CCC-Oct2023/issues)**: Submit bugs found or log feature requests for FILIPJASKOVIC.

#### *Contributing Guidelines*

<details closed>
<summary>Click to expand</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone <your-forked-repo-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

## 📄 License


This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#Top)

---

