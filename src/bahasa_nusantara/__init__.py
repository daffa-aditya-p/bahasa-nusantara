"""
BahasaNusantara - Python Interpreter dengan Sintaks Bahasa Indonesia

BahasaNusantara adalah interpreter Python yang memungkinkan pemrogram Indonesia
untuk menulis kode Python menggunakan kata kunci dalam Bahasa Indonesia.
Dibuat khusus untuk membantu pemula Indonesia belajar pemrograman tanpa
hambatan bahasa.

Contoh penggunaan:
    fungsi halo(nama):
        tulis("Halo", nama)
        kembali benar
    
    jika __name__ == "__main__":
        halo("Dunia")

Author: Daffa Aditya
Version: 2.0.0
License: MIT
"""

__version__ = "2.0.0"
__author__ = "Daffa Aditya Pratama"
__email__ = "daffaadityp@proton.me"
__description__ = "Python Interpreter dengan Sintaks Bahasa Indonesia"

# Import main function dari indo.py agar bisa diakses sebagai API
try:
    from .indo import main, BahasaNusantaraInterpreter
    __all__ = ['main', 'BahasaNusantaraInterpreter', '__version__']
except ImportError:
    # Fallback jika indo.py belum ada
    __all__ = ['__version__']

# Metadata untuk package
KEYWORDS = [
    "indonesian", "bahasa", "indonesia", "python", "interpreter", 
    "programming", "education", "beginner", "nusantara"
]

CLASSIFIERS = [
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
]
