<p align="center">
    <img src="public/assets/images/CommentSense.png" width="200" style="border-radius: 20px;" />
</p>
<p align="center">
    <h1 align="center">CommentSense</h1>
</p>

<p align="center">
  <img src="https://img.shields.io/github/license/Eemayas/CommentSense?style=flat&color=0080ff" alt="license">
  <img src="https://img.shields.io/github/last-commit/Eemayas/CommentSense?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
  <img src="https://img.shields.io/github/languages/top/Eemayas/CommentSense?style=flat&color=0080ff" alt="repo-top-language">
  <img src="https://img.shields.io/github/languages/count/Eemayas/CommentSense?style=flat&color=0080ff" alt="repo-language-count">
  <img src="https://img.shields.io/github/issues/Eemayas/CommentSense?style=flat&color=0080ff" alt="open-issues">
  <img src="https://img.shields.io/github/forks/Eemayas/CommentSense?style=flat&color=0080ff" alt="forks">
  <img src="https://img.shields.io/github/stars/Eemayas/CommentSense?style=flat&color=0080ff" alt="stars">
  <img src="https://img.shields.io/github/issues-pr/Eemayas/CommentSense?style=flat&color=0080ff" alt="pull-requests">
  <img src="https://img.shields.io/github/contributors/Eemayas/CommentSense?style=flat&color=0080ff" alt="contributors">
  <img src="https://img.shields.io/github/commit-activity/m/Eemayas/CommentSense?style=flat&color=0080ff" alt="commit-activity">
  <img src="https://img.shields.io/github/languages/code-size/Eemayas/CommentSense?style=flat&color=0080ff" alt="code-size">
  <img src="https://img.shields.io/github/repo-size/Eemayas/CommentSense?style=flat&color=0080ff" alt="repo-size">
  <img src="https://img.shields.io/github/v/release/Eemayas/CommentSense?style=flat&color=0080ff" alt="release-version">
  <img src="https://img.shields.io/codecov/c/github/Eemayas/CommentSense?style=flat&color=0080ff" alt="coverage">
  <img src="https://img.shields.io/snyk/vulnerabilities/github/Eemayas/CommentSense?style=flat&color=0080ff" alt="security">
  <img src="https://img.shields.io/website?style=flat&color=0080ff&url=https%3A%2F%2Fexample.com" alt="performance">
  <img src="https://img.shields.io/github/commit-activity/y/Eemayas/CommentSense?style=flat&color=0080ff" alt="activity">
</p>

<p align="center">
    <em>Constructed using the following tools and technologies:</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=for-the-badge&logo=TypeScript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/CSS3-1572B6.svg?style=for-the-badge&logo=CSS3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white" alt="HTML">
  <img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6.svg?style=for-the-badge&logo=CSS3&logoColor=white" alt="CSS">
  <img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Next.js-000000.svg?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js">
  <img src="https://img.shields.io/badge/Electron-47848F.svg?style=for-the-badge&logo=Electron&logoColor=white" alt="Electron">
  <img src="https://img.shields.io/badge/Prettier-F7B93E.svg?style=for-the-badge&logo=Prettier&logoColor=black" alt="Prettier">
</p>
    
# Project Overview
**CommentSense** is a web application that enhances user interaction on websites by providing a smart and efficient sentiment analysis of the YouTube comments. It leverages libraries like React, Redux, and MongoDB for state management and database interaction, ensuring seamless user experiences. Additionally, the project incorporates Next-Auth for authentication, Tailwind CSS and Headless UI for UI components, and Framer Motion for animation, making it a robust and visually appealing application. The key features of the project include support for Next.js 14.0.0, React 17.7.2, Redux, MongoDB, Next-Auth, Tailwind CSS, and Framer Motion, with scripts for development, building, starting, and linting.

# Table of Content

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Folder Structure](#folder-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
    - [Step 1: Clone the Repository](#step-1-clone-the-repository)
    - [Step 2: Install Dependencies](#step-2-install-dependencies)
    - [Step 3: Set Environment Variables](#step-3-set-environment-variables)
    - [Step 4: Configure Environment Variables](#step-4-configure-environment-variables)
  - [Running the Project](#running-the-project)
    - [Step 1: Build and Compile](#step-1-build-and-compile)
    - [Step 2: Start Development Server](#step-2-start-development-server)
  - [Tests](#tests)
  - [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
    - [Contributing Guidelines](#contributing-guidelines)
- [Contributors](#contributors)
- [License](#license)

# Features
- Real-time sentiment analyis of comment posting and updates.
- Utilization of Deep Learning model like LSTM, RNN, GRU and transformer like RoBerta
- Optimized for performance with **Next.js**.
- Deployable on **Vercel**.

# Folder Structure
```sh
CommentSense/
├── .prettierrc
├── tsconfig.json
├── README.md
├── st.css
├── tailwind.config.ts
├── .gitignore
├── components/
│   ├── HeroCarousel.tsx
│   ├── SentimentAnalysisSectionWrapper.tsx
│   ├── AuthFormBox.tsx
│   ├── EndpointSetup.tsx
│   ├── CommentSection.tsx
│   ├── InputField.tsx
│   ├── ForgotPassword.tsx
│   ├── TextField.tsx
│   ├── Navbar.tsx
│   ├── Modals.tsx
│   ├── Searchbar.tsx
│   ├── YoutubeVideoSection.tsx
│   ├── CommentsCards.tsx
│   ├── ModelDetailSection.tsx
│   ├── DropDown.tsx
│   ├── UserCard.tsx
│   ├── ProfileDropDown.tsx
│   ├── Sidebar.tsx
│   └── Icons.tsx
├── public/
│   ├── vercel.svg
│   ├── assets/
│   │   ├── images/
│   │   │   ├── CommentSense-removebg-preview.png
│   │   │   ├── hero-1.jpg
│   │   │   ├── hero-5.svg
│   │   │   ├── CommentSense.png
│   │   │   ├── hero-3.svg
│   │   │   ├── trending.svg
│   │   │   ├── hero-4.jpg
│   │   │   ├── hero-1.svg
│   │   │   ├── CommentSense.webp
│   │   │   ├── hero-4.svg
│   │   │   ├── hero-2.jpg
│   │   │   ├── hero-3.jpg
│   │   │   ├── hero-2.svg
│   │   │   └── details.svg
│   │   └── icons/
│   │       ├── bag.svg
│   │       ├── logo copy.svg
│   │       ├── x-close.svg
│   │       ├── bookmark.svg
│   │       ├── star.svg
│   │       ├── check.svg
│   │       ├── square.svg
│   │       ├── chart.svg
│   │       ├── mail.svg
│   │       ├── chevron-down.svg
│   │       ├── price-tag.svg
│   │       ├── arrow-down.svg
│   │       ├── sun.svg
│   │       ├── comment.svg
│   │       ├── logo.svg
│   │       ├── red-heart.svg
│   │       ├── user.svg
│   │       ├── share.svg
│   │       ├── hand-drawn-arrow.svg
│   │       ├── search.svg
│   │       ├── black-heart.svg
│   │       ├── arrow-up.svg
│   │       ├── arrow-right.svg
│   │       └── frame.svg
│   └── next.svg
├── package-lock.json
├── lib/
│   ├── context/
│   │   ├── AuthProvider.tsx
│   │   └── ReduxProvider.tsx
│   ├── model/
│   │   ├── userDetail.model.ts
│   │   └── userLogin.model.ts
│   ├── store/
│   │   └── Reducer/
│   │       ├── commentDataReducer.ts
│   │       ├── commentDataPaginationReducer.ts
│   │       ├── constant.ts
│   │       ├── modalReducer.ts
│   │       ├── searchPromptReducer.ts
│   │       ├── textReducer.ts
│   │       ├── store.ts
│   │       ├── index.ts
│   │       ├── BaseUrlReducer.ts
│   │       └── youtubeLinkReducer.ts
│   ├── action/
│   │   ├── LoginFunctionalities.tsx
│   │   ├── YoutubeCommentFetch.tsx
│   │   └── ScrollFunctionalities.tsx
│   ├── CommentsData.ts
│   ├── mongoose.ts
│   └── utils/
│       └── motion.js
├── app/
│   ├── resetpassword/
│   │   └── page.tsx
│   ├── forgotpassword/
│   │   └── page.tsx
│   ├── globals.css
│   ├── style.css
│   ├── (home)/
│   │   └── components/
│   │       ├── YouTubeCommentAnalysisTablarView.tsx
│   │       └── ExportCSVButton.tsx
│   ├── api/
│   │   ├── login/
│   │   │   └── route.ts
│   │   ├── user/
│   │   │   └── route.ts
│   │   ├── flask/
│   │   │   ├── Model/
│   │   │   │   ├── RNN_sentimentmodel.h5
│   │   │   │   ├── GRU_sentimentmodel.h5
│   │   │   │   └── rnnmodel.h5
│   │   │   ├── README.md
│   │   │   ├── global_variables.py
│   │   │   ├── Tokenizer/
│   │   │   │   ├── LSTMtokenizer.pkl
│   │   │   │   └── RNNtokenizer.pkl
│   │   │   ├── preprocessing.py
│   │   │   ├── apis copy.py
│   │   │   ├── constants.py
│   │   │   ├── app.py
│   │   │   ├── test.py
│   │   │   ├── Analysis/
│   │   │   │   ├── singleComment.py
│   │   │   │   ├── LSTM.py
│   │   │   │   ├── GRU.py
│   │   │   │   ├── RNN.py
│   │   │   │   └── roberta.py
│   │   │   ├── requirements.txt
│   │   │   └── utils/
│   │   │       ├── prediction_utils.py
│   │   │       ├── load_roberta_model.py
│   │   │       ├── preprocessing.py
│   │   │       ├── model_downloader.py
│   │   │       ├── comment_scrapping.py
│   │   │       └── utils.py
│   │   ├── register/
│   │   │   └── route.ts
│   │   └── auth/
│   │       └── [...nextauth]/
│   │           ├── options.ts
│   │           └── route.ts
│   ├── login/
│   │   └── page.tsx
│   ├── predict/
│   │   ├── components/
│   │   │   ├── TabularView.tsx
│   │   │   └── TextbarEntry.tsx
│   │   └── page.tsx
│   ├── layout.tsx
│   ├── constants/
│   │   └── apiEndpints.ts
│   ├── page.tsx
│   ├── favicon.ico
│   ├── personaldetail/
│   │   ├── style.css
│   │   ├── components/
│   │   │   ├── ProfileImageUploader.tsx
│   │   │   └── ProfileForm.tsx
│   │   ├── page.tsx
│   │   └── types/
│   │       └── index.ts
│   └── register/
│       └── page.tsx
├── package copy.json
├── next.config.js
├── postcss.config.js
├── check-env.js
├── requirements.txt
├── types.ts
├── tries.html
└── package.json

36 directories, 143 files
```
# Getting Started
Welcome to CommentSense! This is a comprehensive installation guide that will walk you through setting up the project on your local machine.

## Prerequisites
Before installing CommentSense, ensure you have the following software and tools installed:

* Node.js (14.17 or higher) - [Download](https://nodejs.org/en/download/)
* npm (6.14 or higher) - included with Node.js installation
* yarn (1.22 or higher) - [Install](https://yarnpkg.com/getting-started)
* Git (2.29 or higher) - [Download](https://git-scm.com/downloads)
* Python (3.11 or higher) -[Download](https://www.python.org/downloads/)


## Installation

### Step 1: Clone the Repository
Clone the CommentSense repository from GitHub using:

```bash
git clone https://github.com/Eemayas/CommentSense.git
```

Navigate into the cloned directory:
```bash
cd CommentSense
```

### Step 2: Install Dependencies

Install all dependencies required by the project using:

```bash
python3 -m venv venv && venv/bin/activate && pip install -r requirements.txt && yarn install
```

or with npm:

```bash
python3 -m venv venv && venv/bin/activate && pip install -r requirements.txt && npm install
```

This may take a few minutes to complete, as it downloads and installs numerous packages.

### Step 3: Set Environment Variables

Create a `.env` file in the root directory and set environment variables as needed. The following example sets API keys for authentication:

```makefile
GOOGLE_CLIENT_ID=<GOOGLE_CLIENT_ID_KEY>
GOOGLE_CLIENT_SECRET=<GOOGLE_CLIENT_SECRET_KEY>
GITHUB_ID=<GITHUB_ID_KEY>
GITHUB_SECRET=<GITHUB_SECRET_KEY>
NEXTAUTH_SECRET=<NEXTAUTH_SECRET_KEY>
MONGODB_URI=<MONGODB_URI_KEY>
YOUTUBEAPI=<YOUTUBEAPI_KEY>
```

Replace `<GOOGLE_CLIENT_ID_KEY>`, `<GOOGLE_CLIENT_SECRET_KEY>`, `<GITHUB_ID_KEY>`, `<GITHUB_SECRET_KEY>`, `<NEXTAUTH_SECRET_KEY>`, `<MONGODB_URI_KEY>`, and `<YOUTUBEAPI_KEY>` with your actual API key and auth domain values.

### Step 4: Configure Environment Variables

Configure environment variables using the following command:

```bash
yarn env
```

or with npm:

```bash
npm run env
```

This will create a `.env` file in the root directory, populated with default values for environment variables.

## Running the Project
### Step 1: Build and Compile

Build and compile the project using:

```bash
yarn build
```

or with npm:

```bash
npm run build
```

This step compiles all TypeScript code into JavaScript, making it ready to be executed by a web browser.

### Step 2: Start Development Server

Start the development server using:

```bash
yarn dev
```

or with npm:

```bash
npm run dev
```

This will launch the application on `http://localhost:3000` or another specified port, depending on your configuration. You can now access and interact with CommentSense in your web browser.

### For Hosted website
1. Open the [collab](https://colab.research.google.com/drive/15P4siaaG-bKo0mJxJzguwemtNYRBLSWE#scrollTo=1VDezgRvbDGR) file.
2. Click **Run all** option in the section **Runtime**

## Troubleshooting

Common issues that may arise during installation and how to resolve them:

* **Error: Cannot find module '...'**: Ensure you have installed all dependencies by running `yarn install` or `npm install`.
* **Error: Invalid configuration**: Review your environment variables in `.env` file and update as necessary.
* **Error: Docker container not found**: Restart the Docker daemon using `systemctl restart docker` (on Linux) or `sudo kill -9 $(ps aux | grep "docker" | awk '{print $2}')`.
* **Error: TypeScript compilation issues**: Review your TypeScript code for errors and fix as necessary.

By following this installation guide, you should now have a working version of CommentSense running on your local machine. If you encounter any difficulties or issues during the process, refer to the troubleshooting section above for assistance.
# Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/Eemayas/CommentSense/pulls)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/Eemayas/CommentSense/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/Eemayas/CommentSense/issues)**: Submit bugs found or log feature requests for CommentSense.

### Contributing Guidelines

1. **Fork the Repository**:
    - Start by forking the project repository to your GitHub account.
2. **Clone the Repository**:
    - Clone your forked repository to your local machine using the command:
    ```sh
    git clone https://github.com/your-username/CommentSense.git
    ```
    - Replace ``your-username`` with your GitHub username.
3. **Create a New Branch**:
    - Create a new branch for your changes using the command:
    ```sh
    git checkout -b your-branch-name
    ```
4. **Make Your Changes**:
    - Edit, add, or delete files as needed. Ensure your changes align with the project's contribution guidelines.
5. **Commit Your Changes**:
    - Stage your changes and commit them with a descriptive message:
      ```bash
      git add .
      git commit -m "Your descriptive message"
      ```
6. **Push Your Changes:**
    - Push your branch to your forked repository:
      ```bash
      git push origin your-branch-name
      ```
7. **Create a Pull Request (PR):**
    - Go to the original repository on GitHub and click “Compare & pull request.” Provide a clear description of the changes and submit the PR.

Once your PR is reviewed and approved, it will be merged into the main branch.

# Contributors

| Avatar | Contributor | GitHub Profile | No of Contributions |
|:--------:|:--------------:|:----------------:|:-------------------:|
| <img src='https://avatars.githubusercontent.com/u/100434825?v=4' width='40' height='40' style='border-radius:50%;'/> | Eemayas | [@Eemayas](https://github.com/Eemayas) | 56 |

# License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---