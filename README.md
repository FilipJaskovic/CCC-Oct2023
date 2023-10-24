<div align="center">
<h1 align="center">
<!-- <img src="CCC-Logo.png" height="150" /> -->
<img src="header-icon-big-dd51142e51225a243f87602c26ce87ab -  - 2023-10-24 09-29-01.svg" height="150" />
<br>CCC-OCT2023</h1>
<h3>◦ CCC-Oct2023: CCC October 2023 Solution Repository</h3>


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
- [⚙️ Solutions Explained](#%EF%B8%8F-solutions-explained)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running CCC-Oct2023](#-running-CCC-Oct2023)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

Welcome to the CCC October 2023 Solution Repository! This repository contains my code solutions for the [Cloudflight Coding Contest October 2023](https://register.codingcontest.org/). Feel free to explore, learn and contribute.

The CCC (short for Cloudflight Coding Contest) is one of the biggest competitions of its kind. Each Spring and Autumn over 4,000 coders from all around the world simultaneously compete against each other in level-based coding games. With each level the difficulty increases and the candidate (or team) reaching the highest level within the shortest time wins.

The contest's structure was delineated into multiple levels, each presenting a unique set of algorithmic challenges that demanded not only an understanding of computer science principles but also the ability to apply logical deductions and data manipulation techniques effectively.

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


## ⚙️ Solutions Explained

<details closed><summary>Level 1 Solution Explanation</summary>
Level 1 involved a frequency analysis task where we were given a collection of puzzle pieces, each described using a string of characters representing its shape. Our solution involved creating a dictionary-based counter in Python, specifically using the 'collections.Counter' class, to track the occurrences of each unique piece. We optimized string handling and file I/O operations for efficiency, ensuring minimal computational delay.
</details>
<details closed><summary>Level 2 Solution Explanation</summary>
Level 2 elevated the complexity by introducing the concept of rotational invariance among puzzle pieces. Here, we implemented a normalization function to account for the orientation aspect. By generating all possible rotations of a piece and using string manipulation, we could identify pieces of the same type. We stored these representations in a normalized form, ensuring that comparisons were consistent and computationally economical.
</details>
<details closed><summary>Level 3 Solution Explanation</summary>
Level 3 presented an error correction problem within an assembled puzzle matrix. Our solution strategy involved devising a custom function to scan the puzzle's adjacency relationships, identifying 'mistake' conditions based on the knobs and holes pattern. We used multidimensional list indexing to simulate the puzzle grid, enabling direct access to 'neighboring' pieces. When inconsistencies were detected, we programmatically altered the relevant piece's string descriptor to correct the puzzle's integrity while maintaining the state of correct connections. This level necessitated careful control flow to ensure that only genuine mistakes were adjusted without disrupting the surrounding, correct alignments.
</details>
<details closed><summary>Level 4 Solution Explanation</summary>

</details>
Each level required us to produce output files that reflected our solutions. We incorporated systematic file handling to read inputs and write outputs, employing context management protocols in Python to interact with the file system efficiently. Additionally, the code was structured for reusability and scalability, evidenced by the modular approach in the main executable section, allowing for convenient iteration through multiple input files.





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

