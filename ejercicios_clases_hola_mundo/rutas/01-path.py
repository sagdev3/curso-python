from pathlib import Path

# Path(r"C:\Archiovode de Programas\Minecraft") Rutas para Windows
# Path("/usr/bin") Ruta Linux Absoluta
# Path()
# Path.home()
# Path("one/__init__.py") #Ruta relativa

path = Path("hola-mundo/mi-archivo.py")
path.is_file
path.is_dir
path.exists

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

p = path.with_name('chanchito.py')
print(p)
p = path.with_suffix('.bat')
print(p)
p = path.with_stem('feliz')
print(p)
