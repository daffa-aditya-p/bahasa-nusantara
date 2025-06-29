#!/usr/bin/env python3
"""
Setup script untuk BahasaNusantara
Python Interpreter dengan Sintaks Bahasa Indonesia
"""

from setuptools import setup, find_packages
import os

# Baca README.md untuk long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Baca requirements dari file jika ada
def read_requirements():
    requirements = ["termcolor>=1.1.0"]
    requirements_file = "requirements.txt"
    if os.path.exists(requirements_file):
        with open(requirements_file, "r", encoding="utf-8") as f:
            requirements.extend([line.strip() for line in f if line.strip() and not line.startswith("#")])
    return requirements

setup(
    # Informasi Dasar Package
    name="bahasa-nusantara",
    version="2.0.0",
    author="Daffa Aditya Pratama",
    author_email="daffaadityp@proton.me",
    description="Python Interpreter dengan Sintaks Bahasa Indonesia untuk Pemula",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    
    # URLs
    url="https://github.com/daffa-aditya-p/bahasa-nusantara",
    project_urls={
        "Bug Reports": "https://github.com/daffa-aditya-p/bahasa-nusantara/issues",
        "Source": "https://github.com/daffa-aditya-p/bahasa-nusantara",
        "Documentation": "https://github.com/daffa-aditya-p/bahasa-nusantara#readme",
    },
    
    # Package Configuration
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    
    # Dependencies
    install_requires=read_requirements(),
    python_requires=">=3.7",
    
    # Entry Points - CLI Commands
    entry_points={
        "console_scripts": [
            "jalankan=bahasa_nusantara.indo:main",
            "run=bahasa_nusantara.indo:main",
            "bahasa-nusantara=bahasa_nusantara.indo:main",
            "nus=bahasa_nusantara.indo:main",
        ],
    },
    
    # Metadata
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Education",
        "Topic :: Software Development :: Interpreters",
        "Natural Language :: Indonesian",
        "Operating System :: OS Independent",
    ],
    
    keywords="indonesian bahasa indonesia python interpreter programming education beginner nusantara",
    
    # Extra metadata
    license="MIT",
    zip_safe=False,
    
    # Optional dependencies
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
        "test": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
        ],
    },
)
