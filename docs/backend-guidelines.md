# Backend Development Guidelines

To maintain a clean, readable, and consistent codebase, all backend developers for Afrimarket must adhere to the following guidelines.

## 1. Branch Strategy

We use a feature-branch workflow based on Git Flow.

- **`main`:** The production-ready branch. Code here should always be deployable. Do not push directly to `main`.
- **`dev`:** The active development branch. All feature branches merge into this branch before going to `main`.
- **Feature Branches:** Created from `dev` for specific tasks.
  - Naming convention: `feature/<short-description>` (e.g., `feature/user-auth`)
- **Bugfix Branches:** Created from `dev` (or `main` if it's a hotfix).
  - Naming convention: `bugfix/<short-description>` (e.g., `bugfix/login-crash`)

## 2. Commit Message Style

Commit messages should be clear and descriptive. We follow a standard format:

`[Type]: Short description of changes`

**Types:**
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, etc.)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools

**Examples:**
- `feat: add user registration endpoint`
- `fix: resolve issue with product image upload`
- `docs: update database design markdown`

## 3. Code Formatting

We follow the standard Python formatting guidelines (PEP 8).

- Use **4 spaces** for indentation.
- Maximum line length is **79 characters** (or 88 if using `black`).
- Use tools like `flake8` or `black` to format and lint your code before committing.
- Ensure imports are grouped: Standard library, third-party libraries, local application imports.

## 4. Naming Conventions

- **Variables and Functions:** `snake_case` (e.g., `user_profile`, `get_active_products()`)
- **Classes (Models, Serializers, Views):** `PascalCase` (e.g., `UserProfile`, `ProductSerializer`)
- **Constants:** `UPPER_SNAKE_CASE` (e.g., `MAX_LOGIN_ATTEMPTS`)
- **File Names:** `snake_case.py` (e.g., `models.py`, `custom_permissions.py`)

## 5. Pull Request (PR) Process

1. **Push:** Push your feature branch to GitHub.
2. **Open PR:** Create a Pull Request targeting the `dev` branch.
3. **Description:** Clearly describe what the PR does, what issue it solves, and any testing steps required.
4. **Review:** Request a review from at least one other team member (e.g., Simret).
5. **Address Feedback:** Make any requested changes and push them to the same branch.
6. **Merge:** Once approved and all tests pass, the PR can be merged into `dev`. Use "Squash and merge" to keep the history clean.
