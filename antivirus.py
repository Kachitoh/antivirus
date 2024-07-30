import os
import argparse
import logging

# Crear directorio de logs si no existe
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configuración del registro de logs
logging.basicConfig(filename='logs/antivirus_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Lista de firmas de virus (simuladas)
VIRUS_SIGNATURES = [
    b"VIRUS123",
    b"MALWARE456",
    b"TROJAN789"
]

def scan_file(file_path):
    try:
        with open(file_path, 'rb') as file:  # Abre en modo binario
            content = file.read()
            for signature in VIRUS_SIGNATURES:
                if signature in content:
                    return True
    except Exception as e:
        logging.error(f"Error al leer el archivo {file_path}: {e}")
    return False

def scan_directory(directory):
    infected_files = []
    total_files = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            total_files += 1
            file_path = os.path.join(root, file)
            if scan_file(file_path):
                infected_files.append(file_path)
    return infected_files, total_files

def main():
    parser = argparse.ArgumentParser(description="Antivirus básico")
    parser.add_argument("directory", help="Directorio a escanear")
    args = parser.parse_args()

    directory = args.directory

    if not os.path.isdir(directory):
        print("El directorio ingresado no existe.")
        logging.error(f"El directorio ingresado no existe: {directory}")
        return
    
    print(f"Escaneando el directorio: {directory}...")
    logging.info(f"Comenzando el escaneo del directorio: {directory}")

    infected_files, total_files = scan_directory(directory)

    print(f"Archivos escaneados: {total_files}")
    print(f"Archivos infectados encontrados: {len(infected_files)}")
    logging.info(f"Archivos escaneados: {total_files}")
    logging.info(f"Archivos infectados encontrados: {len(infected_files)}")

    if infected_files:
        print("Lista de archivos infectados:")
        logging.info("Lista de archivos infectados:")
        for file in infected_files:
            print(f"- {file}")
            logging.info(f"Archivo infectado: {file}")
    else:
        print("No se encontraron archivos infectados.")
        logging.info("No se encontraron archivos infectados.")

if __name__ == "__main__":
    main()
