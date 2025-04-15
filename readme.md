# Homework 10
### Lev Zelenin
Spring 2025

## Docker Hub

[Dockerhub repo](https://hub.docker.com/r/l3vz/homework10)


## Issues Fixed


[Issue #1: dockerhub](https://github.com/l3vzNJIT/homework10/issues/1)

[Issue #2: vulnerabilities](https://github.com/l3vzNJIT/homework10/issues/3)

[Issue #3: Login and register example data mismatch](https://github.com/l3vzNJIT/homework10/issues/5)

[Issue #4: Cryptographic hashing improvement](https://github.com/l3vzNJIT/homework10/issues/7)



## Things I Learned


This assignment deepened my understanding of how FastAPI uses Pydantic schemas to generate OpenAPI documentation, and how seemingly small mismatches in example data can create real usability issues in developer tooling like Swagger UI. By aligning the example data between registration and login endpoints, I gained practical insight into how schema consistency enhances both API clarity and developer experience. I also learned how to cleanly extract shared example values for reuse across multiple schema classes, balancing the need for testable consistency with runtime flexibility like dynamic nickname generation.

On the collaboration and workflow side, I ran into a common but important issue: making significant changes before branching. I learned how to properly migrate staged changes onto a new branch after the fact, as well as how Git handles staged and unstaged changes during a branch switch — especially when files have diverged. This helped me better understand Git’s concept of conflicts and how it determines when user intervention is necessary. Lastly, by containerizing and testing with Docker Compose and using targeted `pytest` commands, I reinforced good habits for maintaining consistent, reproducible test environments. These insights made the assignment more than a technical task — it became a full-stack workflow lesson.


## Submission Requirements

To complete this assignment, submit the following:

1. **GitHub Repository Link**: Ensure that your repository is well-organized and includes:
  - Links to five closed issues, each with accompanying test code and necessary application code modifications.
  - Each issue should be well-documented, explaining the problem, the steps taken to resolve it, and the outcome. Proper documentation helps others understand your work and facilitates future maintenance.
  - All issues should be merged into the main branch, following the Git workflow and best practices.

2. **Updated README**: Replace the existing README with:
  - Links to the closed issues, providing easy access to your work.
  - Link to project image deployed to Dockerhub.
  - A 2-3 paragraph reflection on what you learned from this assignment, focusing on both technical skills and collaborative processes. Reflect on the challenges you faced, the solutions you implemented, and the insights you gained. This reflection helps solidify your learning and provides valuable feedback for improving the assignment in the future.

## Grading Rubric

| Criteria                                                                                                                | Points |
|-------------------------------------------------------------------------------------------------------------------------|--------|
| Resolved 5 issues related to username validation, password validation, and profile field edge cases                      | 30     |
| Resolved the issue demonstrated in the instructor video                                                                 | 20     |
| Increased test coverage to 90% by writing comprehensive test cases                                                      | 20     |
| Followed collaborative development practices using Git and GitHub (branching, pull requests, code reviews)              | 15     |
| Submitted a well-organized GitHub repository with clear documentation, links to closed issues, and a reflective summary | 15     |
| **Total**                                                                                                               | **100**|
