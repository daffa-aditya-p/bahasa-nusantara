#!/usr/bin/env python3
import sys
import os
import re
import ast
import traceback
from typing import Dict, List, Any

# Import termcolor jika tersedia, jika tidak gunakan fallback
try:
    from termcolor import colored
    HAS_TERMCOLOR = True
except ImportError:
    HAS_TERMCOLOR = False
    def colored(text, color=None, on_color=None, attrs=None):
        return text

class BahasaNusantaraInterpreter:
    def __init__(self):
        self.keyword_mapping = {
            # Struktur kontrol
            'fungsi': 'def',
            'kembali': 'return',
            'jika': 'if',
            'jika_lainnya': 'elif',
            'lainnya': 'else',
            'untuk': 'for',
            'dalam': 'in',
            'selama': 'while',
            'selesai': 'break',
            'teruskan': 'continue',
            'lewati': 'pass',
            
            # Input/Output
            'tulis': 'print',
            'tanya': 'input',
            
            # Import
            'gunakan': 'import',
            'dari': 'from',
            'sebagai': 'as',
            
            # Class dan exception
            'kelas': 'class',
            'coba': 'try',
            'kecuali': 'except',
            'akhirnya': 'finally',
            'naikkan': 'raise',
            'tegas': 'assert',
            
            # Konteks dan async
            'dengan': 'with',
            'async': 'async',
            'tunggu': 'await',
            
            # Operator logika
            'adalah': 'is',
            'bukan': 'not',
            'dan': 'and',
            'atau': 'or',
            'dalam_list': 'in',
            'bukan_dalam': 'not in',
            'adalah_bukan': 'is not',
            
            # Nilai boolean dan None
            'benar': 'True',
            'salah': 'False',
            'kosong': 'None',
            
            # Lainnya
            'global': 'global',
            'nonlokal': 'nonlocal',
            'lambda': 'lambda',
            'hapus': 'del',
            'hasil': 'yield',
            'dari_hasil': 'yield from',
        }
        
        self.builtin_functions = {
            'panjang': 'len',
            'tipe': 'type',
            'str': 'str',
            'int': 'int',
            'float': 'float',
            'bool': 'bool',
            'list': 'list',
            'dict': 'dict',
            'set': 'set',
            'tuple': 'tuple',
            'range': 'range',
            'enumerate': 'enumerate',
            'zip': 'zip',
            'map': 'map',
            'filter': 'filter',
            'sorted': 'sorted',
            'reversed': 'reversed',
            'sum': 'sum',
            'min': 'min',
            'max': 'max',
            'abs': 'abs',
            'round': 'round',
            'pow': 'pow',
            'divmod': 'divmod',
            'hex': 'hex',
            'oct': 'oct',
            'bin': 'bin',
            'ord': 'ord',
            'chr': 'chr',
            'all': 'all',
            'any': 'any',
            'iter': 'iter',
            'next': 'next',
            'open': 'open',
            'format': 'format',
            'vars': 'vars',
            'dir': 'dir',
            'help': 'help',
            'id': 'id',
            'hash': 'hash',
            'callable': 'callable',
            'isinstance': 'isinstance',
            'issubclass': 'issubclass',
            'hasattr': 'hasattr',
            'getattr': 'getattr',
            'setattr': 'setattr',
            'delattr': 'delattr',
        }

    def print_colored(self, text: str, color: str = None, style: str = None):
        """Print text dengan warna jika termcolor tersedia"""
        attrs = []
        if style == 'bold':
            attrs.append('bold')
        elif style == 'underline':
            attrs.append('underline')
        
        print(colored(text, color, attrs=attrs if attrs else None))

    def show_error(self, message: str, line_number: int = None, filename: str = None):
        """Tampilkan pesan error dalam Bahasa Indonesia dengan warna"""
        if line_number and filename:
            error_msg = f"❌ Kesalahan pada {filename}, baris {line_number}: {message}"
        elif line_number:
            error_msg = f"❌ Kesalahan pada baris {line_number}: {message}"
        else:
            error_msg = f"❌ Kesalahan: {message}"
        
        self.print_colored(error_msg, 'red', 'bold')

    def show_success(self, message: str):
        """Tampilkan pesan sukses dengan warna hijau"""
        self.print_colored(f"✅ {message}", 'green')

    def show_info(self, message: str):
        """Tampilkan pesan info dengan warna biru"""
        self.print_colored(f"ℹ️  {message}", 'blue')

    def extract_string_literals(self, code: str) -> tuple:
        """Ekstrak string literals dari kode untuk menghindari translasi di dalamnya"""
        string_parts = []
        temp_code = code
        string_counter = 0
        
        # Pola untuk menangkap string literals
        string_patterns = [
            r'""".*?"""',  # Triple double quotes
            r"'''.*?'''",  # Triple single quotes
            r'"[^"\\]*(?:\\.[^"\\]*)*"',  # Double quotes
            r"'[^'\\]*(?:\\.[^'\\]*)*'"   # Single quotes
        ]
        
        for pattern in string_patterns:
            matches = list(re.finditer(pattern, temp_code, re.DOTALL))
            for match in reversed(matches):  # Reverse untuk menghindari perubahan indeks
                string_content = match.group(0)
                placeholder = f"__STRING_{string_counter}__"
                string_parts.append((placeholder, string_content))
                temp_code = temp_code[:match.start()] + placeholder + temp_code[match.end():]
                string_counter += 1
        
        return temp_code, string_parts

    def extract_comments(self, code: str) -> tuple:
        """Ekstrak komentar dari kode"""
        comment_parts = []
        lines = code.split('\n')
        temp_lines = []
        comment_counter = 0
        
        for line in lines:
            # Cari komentar yang tidak dalam string
            comment_match = re.search(r'#.*$', line)
            if comment_match and not self.is_in_string(line, comment_match.start()):
                comment_content = comment_match.group(0)
                placeholder = f"__COMMENT_{comment_counter}__"
                comment_parts.append((placeholder, comment_content))
                temp_line = line[:comment_match.start()] + placeholder
                temp_lines.append(temp_line)
                comment_counter += 1
            else:
                temp_lines.append(line)
        
        return '\n'.join(temp_lines), comment_parts

    def is_in_string(self, line: str, position: int) -> bool:
        """Periksa apakah posisi berada dalam string literal"""
        in_single_quote = False
        in_double_quote = False
        i = 0
        
        while i < position:
            char = line[i]
            if char == "'" and not in_double_quote:
                if i == 0 or line[i-1] != '\\':
                    in_single_quote = not in_single_quote
            elif char == '"' and not in_single_quote:
                if i == 0 or line[i-1] != '\\':
                    in_double_quote = not in_double_quote
            i += 1
        
        return in_single_quote or in_double_quote

    def translate_keywords(self, code: str) -> str:
        """Terjemahkan kata kunci BahasaNusantara ke Python"""
        # Ekstrak string literals dan komentar
        temp_code, string_parts = self.extract_string_literals(code)
        temp_code, comment_parts = self.extract_comments(temp_code)
        
        # Translate keywords
        for indo_keyword, python_keyword in self.keyword_mapping.items():
            pattern = r'\b' + re.escape(indo_keyword) + r'\b'
            temp_code = re.sub(pattern, python_keyword, temp_code)
        
        # Translate built-in functions
        for indo_func, python_func in self.builtin_functions.items():
            pattern = r'\b' + re.escape(indo_func) + r'\b(?=\s*\()'
            temp_code = re.sub(pattern, python_func, temp_code)
        
        # Kembalikan string literals dan komentar
        for placeholder, original_content in comment_parts:
            temp_code = temp_code.replace(placeholder, original_content)
        
        for placeholder, original_content in string_parts:
            temp_code = temp_code.replace(placeholder, original_content)
        
        return temp_code

    def add_custom_functions(self, globals_dict: dict):
        """Tambahkan fungsi custom ke namespace"""
        def acak(sequence):
            """Fungsi acak untuk memilih elemen random dari sequence"""
            import random
            if hasattr(sequence, '__iter__') and len(sequence) > 0:
                return random.choice(sequence)
            else:
                raise ValueError("Sequence harus berisi minimal satu elemen")
        
        globals_dict['acak'] = acak

    def execute_nus_code(self, code: str, filename: str = "<string>", args: List[str] = None):
        """Eksekusi kode BahasaNusantara"""
        if args is None:
            args = []
        
        try:
            # Translate code
            python_code = self.translate_keywords(code)
            
            # Setup environment
            original_argv = sys.argv[:]
            if filename != "<string>":
                sys.argv = [filename] + args
            
            # Setup globals
            script_globals = {
                '__file__': os.path.abspath(filename) if filename != "<string>" else filename,
                '__name__': '__main__',
                '__builtins__': __builtins__,
            }
            
            # Tambahkan fungsi custom
            self.add_custom_functions(script_globals)
            
            # Compile dan eksekusi
            try:
                compiled_code = compile(python_code, filename, 'exec')
                exec(compiled_code, script_globals)
            except SyntaxError as e:
                self.show_error(f"Kesalahan sintaks: {e.msg}", e.lineno, filename)
                return 1
            except Exception as e:
                # Tampilkan traceback yang sudah di-translate
                self.show_error(f"Kesalahan runtime: {str(e)}")
                if hasattr(e, '__traceback__'):
                    tb_lines = traceback.format_exception(type(e), e, e.__traceback__)
                    for line in tb_lines[1:-1]:  # Skip first and last line
                        print(line.rstrip(), file=sys.stderr)
                return 1
            
            # Restore sys.argv
            sys.argv = original_argv
            return 0
            
        except Exception as e:
            self.show_error(f"Kesalahan tidak terduga: {str(e)}")
            return 1

    def execute_file(self, filepath: str, args: List[str] = None) -> int:
        """Eksekusi file .nus"""
        if args is None:
            args = []
        
        # Periksa file
        if not os.path.exists(filepath):
            self.show_error(f"File '{filepath}' tidak ditemukan.")
            return 1
        
        if not filepath.endswith('.nus'):
            self.show_error(f"File harus berekstensi .nus, ditemukan: {filepath}")
            return 1
        
        try:
            # Baca file
            with open(filepath, 'r', encoding='utf-8') as f:
                code = f.read()
            
            # Eksekusi
            return self.execute_nus_code(code, filepath, args)
            
        except FileNotFoundError:
            self.show_error(f"File '{filepath}' tidak dapat dibuka.")
            return 1
        except UnicodeDecodeError:
            self.show_error(f"File '{filepath}' tidak dapat dibaca (encoding error).")
            return 1

    def start_repl(self):
        """Mulai REPL interaktif"""
        self.print_colored("🇮🇩 BahasaNusantara REPL v2.0", 'cyan', 'bold')
        self.print_colored("Ketik 'keluar()' atau Ctrl+C untuk keluar", 'yellow')
        print()
        
        while True:
            try:
                # Input dari user
                user_input = input(colored(">>> ", 'green'))
                
                if user_input.strip() in ['keluar()', 'keluar', 'exit()', 'exit', 'quit()', 'quit']:
                    self.print_colored("Selamat tinggal! 👋", 'cyan')
                    break
                
                if user_input.strip() == '':
                    continue
                
                # Eksekusi kode
                self.execute_nus_code(user_input, "<repl>")
                
            except KeyboardInterrupt:
                print()
                self.print_colored("Selamat tinggal! 👋", 'cyan')
                break
            except EOFError:
                print()
                self.print_colored("Selamat tinggal! 👋", 'cyan')
                break
            except Exception as e:
                self.show_error(f"Kesalahan REPL: {str(e)}")

    def show_help(self):
        """Tampilkan bantuan penggunaan"""
        help_text = """
🇮🇩 BahasaNusantara Interpreter v2.0
Interpreter Python dengan sintaks Bahasa Indonesia

Penggunaan:
  python indo.py <file.nus> [argumen...]
  python indo.py                          # Mulai REPL interaktif
  
Contoh:
  python indo.py program.nus
  python indo.py program.nus arg1 arg2
  
Kata kunci yang didukung:
  fungsi → def          kembali → return      jika → if
  untuk → for           dalam → in            selama → while
  tulis → print         tanya → input         gunakan → import
  benar → True          salah → False         kosong → None
  dan → and             atau → or             bukan → not
  panjang() → len()     acak() → random.choice()  tipe() → type()
  
Contoh kode .nus:
  fungsi halo(nama):
      tulis("Halo", nama)
      angka = acak([1, 2, 3, 4, 5])
      tulis("Panjang nama:", panjang(nama))
      kembali benar
  
  jika __name__ == "__main__":
      halo("Dunia")
"""
        self.print_colored(help_text, 'cyan')

def main():
    """Fungsi utama interpreter"""
    interpreter = BahasaNusantaraInterpreter()
    
    # Parse arguments
    if len(sys.argv) < 2:
        # Tidak ada argumen, mulai REPL
        interpreter.start_repl()
        return 0
    
    if sys.argv[1] in ['-h', '--help', 'bantuan', 'help']:
        interpreter.show_help()
        return 0
    
    # Ada file .nus yang akan dieksekusi
    nus_file = sys.argv[1]
    script_args = sys.argv[2:] if len(sys.argv) > 2 else []
    
    return interpreter.execute_file(nus_file, script_args)

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)