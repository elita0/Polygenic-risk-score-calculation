Thfis will set up enviroment for PRS salcualtions using PRSice and PLINK2

# 1. Build the Docker image

Make sure you are in the same directory as the `Dockerfile`, then run:

```bash
docker build -t prs-env .
```

# 2. Run an interactive session
 ```
docker run --rm -it -v "$PWD":/work prs-env bash
```

Alternatively: you can build it directly from GitHub without downloading the repo:

docker build -t prs-env https://github.com/elita0/PRS.git


