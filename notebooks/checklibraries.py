import subprocess
import sys

# List of required libraries and versions
required_libraries = {
    "numpy": "2.2.6",
    "pandas": None,
    "scikit-learn": None,
    "matplotlib": None,
    "seaborn": None,
    "xgboost": None,
    "shap": None,
    "joblib": None,
    "tqdm": None,
    "numba": None,
    "llvmlite": None,
    "slicer": None
}

for lib, version in required_libraries.items():
    try:
        __import__(lib)
        if version:
            import pkg_resources
            installed_version = pkg_resources.get_distribution(lib).version
            if installed_version != version:
                print(f"{lib} version mismatch: {installed_version} → installing {version}")
                subprocess.check_call([sys.executable, "-m", "pip", "install", f"{lib}=={version}"])
            else:
                print(f"{lib} ✅ version {installed_version} is correct")
        else:
            print(f"{lib} ✅ installed")
    except ImportError:
        print(f"{lib} not found → installing...")
        if version:
            subprocess.check_call([sys.executable, "-m", "pip", "install", f"{lib}=={version}"])
        else:
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

print("\nAll required libraries are checked and installed ✅")

