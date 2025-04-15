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

[Issue #5: Handling of HTTP errors](https://github.com/l3vzNJIT/homework10/issues/9)



## Things I Learned


This assignment deepened my understanding of how FastAPI uses Pydantic schemas to generate OpenAPI documentation, and how seemingly small mismatches in example data can create real usability issues in developer tooling like Swagger UI. By aligning the example data between registration and login endpoints, I gained practical insight into how schema consistency enhances both API clarity and developer experience. I also learned how to cleanly extract shared example values for reuse across multiple schema classes, balancing the need for testable consistency with runtime flexibility like dynamic nickname generation.

On the collaboration and workflow side, I ran into a common but important issue: making significant changes before branching. I learned how to properly migrate staged changes onto a new branch after the fact, as well as how Git handles staged and unstaged changes during a branch switch — especially when files have diverged. This helped me better understand Git’s concept of conflicts and how it determines when user intervention is necessary. Lastly, by containerizing and testing with Docker Compose and using targeted `pytest` commands, I reinforced good habits for maintaining consistent, reproducible test environments. These insights made the assignment more than a technical task — it became a full-stack workflow lesson.
