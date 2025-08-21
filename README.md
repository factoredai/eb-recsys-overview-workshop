![Factored Banner](images/Factored_Logo_Profile_Asset_Cover-.png)

# 🚀 **Beyond Matrix Factorization: Deep RecSys Architectures in Action**

Recommender systems have become one of the most impactful business applications of machine learning, helping users navigate and interact with the vast variety of products and services companies offer. From personalized playlists on Spotify to movie suggestions on Netflix, recommender systems are already a part of our daily lives, and leveraging them effectively is key to driving user engagement and business growth.

In this hands-on workshop, we’re ready to take your understanding of recommender systems to the next level. We’ll move beyond traditional approaches like collaborative filtering and explore modern deep learning architectures that power today’s most sophisticated platforms. You’ll gain a practical introduction to cutting-edge algorithms while building an intuitive understanding of how recommendation models are evolving worldwide.

Whether you’re building your one recommender or enhancing an existing one, this session will help you grasp key architectural trade-offs, explore real-world use cases, and walk away with insights and code to keep learning and iterating with modern RecSys techniques.

## 🛠️ Environment Setup Instructions

We’ll use [`uv`](https://github.com/astral-sh/uv), a superfast Python package manager that also handles virtual environments. This will ensure all participants use the same environment for consistent results.

---

### ✅ 1. Install `uv` (only once)

#### 💻 macOS / Linux / WSL
```bash
curl -Ls https://astral.sh/uv/install.sh | bash
```

#### 🪟 Windows (PowerShell)
```powershell
iwr -useb https://astral.sh/uv/install.ps1 | iex
```

After installation, check that it works:
```bash
uv --version
```

---

### ✅ 2. Clone this repository
```bash
git clone https://github.com/your-org/recsys-workshop-homework.git
cd recsys-workshop-homework
```

Replace the link above with the actual repository link if different.

---

### ✅ 3. Create the environment and install dependencies
```bash
uv venv
uv pip install -r requirements.txt
```

This will:
- Create a `.venv` folder with a virtual environment
- Install all dependencies listed in `requirements.txt` using `uv`'s fast backend

---

### ✅ 4. Activate the environment

#### 💻 macOS / Linux / WSL
```bash
source .venv/bin/activate
```

#### 🪟 Windows
```powershell
.venv\Scripts\Activate.ps1
```

You should now see your prompt change to something like:
```bash
(.venv) $
```

---

## 📝 Alternative: Conda (optional)

If you prefer using `conda` or `mamba`, we recommend sticking with `uv` for consistency in this workshop. However, feel free to create your own environment manually using the `requirements.txt` file.