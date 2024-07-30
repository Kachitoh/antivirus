# Antivirus Básico

## Descripción

Este es un programa básico de antivirus casero escrito en Python. Escanea los archivos en un directorio dado en busca de firmas de virus predefinidas y reporta los archivos infectados.

## Características

- Escaneo de directorios para detectar archivos infectados.
- Registro detallado de la actividad del escaneo.
- Detección de firmas de virus en archivos binarios.
- Interfaz de línea de comandos para especificar el directorio a escanear.

## Instalación

1. Clona el repositorio o descarga el código fuente.
    ```sh
    git clone https://github.com/tu_usuario/antivirus_basico.git
    ```

2. Navega al directorio del proyecto.
    ```sh
    cd antivirus_basico
    ```

3. (Opcional) Crea un entorno virtual y actívalo.
    ```sh
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

4. Instala las dependencias.
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta el programa desde la terminal, especificando el directorio que deseas escanear.
    ```sh
    python antivirus.py <directorio>
    ```

    Reemplaza `<directorio>` con la ruta del directorio que deseas escanear. Por ejemplo:
    ```sh
    python antivirus.py /home/usuario/documentos
    ```

2. Los resultados del escaneo se mostrarán en la terminal y se registrarán en el archivo `logs/antivirus_log.txt`.

## Ejemplo de Ejecución

```sh
python antivirus.py /path/to/directory
