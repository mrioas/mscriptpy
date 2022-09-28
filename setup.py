# from pathlib import Path
# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# with open('requirements.txt', 'r') as f:
#    requirements = f.read().splitlines()


with open("README.md", "r") as readme:
    long_description = readme.read()


# root = Path(__file__).parent.resolv()
# root = os.path.dirname(os.path.abspath(__file__))
# long_description = (root / "README.md").read_text(encoding="utf-8")

setup(
    name='mscriptpy',
    version=1.0,
    author="mas",
    author_email="marioaas@proton.me",
    description='My personal python script',
    # url="https://github.com/pypa/sampleproject",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="src", exclude=['tests']),
    package_dir={"": "src"},
    py_modules=['pv'],
    entry_points='''
        [console_scripts]
        pv=pv:cli"
    ''',
    install_requires=[
           "Click",
        ],
)
