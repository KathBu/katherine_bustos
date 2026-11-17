import os

ruta_carpeta = r"C:\Users\Ponyo\Documents\iacc\15procesos-informáticos\Tarea3" 

nombre = "Katherine"
apellido = "Bustos"

def renombrar_archivos_log(ruta):
    archivos = os.listdir(ruta)

    archivos_log = [archivo for archivo in archivos if archivo.endswith(".log")]
    
    contador = 1
    
    for archivo in archivos_log:
        ruta_original = os.path.join(ruta, archivo)
        
        nuevo_nombre = f"{nombre}_{apellido}_{contador}.log"
        ruta_nueva = os.path.join(ruta, nuevo_nombre)
        
        os.rename(ruta_original, ruta_nueva)
        print(f"Archivo renombrado: {archivo} -> {nuevo_nombre}")
        
        contador += 1

if __name__ == "__main__":
    print(f"Iniciando el proceso de renombrado en: {ruta_carpeta}")
    renombrar_archivos_log(ruta_carpeta)
    print("Proceso completado exitosamente.")