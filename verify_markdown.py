import os
import re
import sys

def verify_markdown():
    file_path = "Centro_comercial_ER.md"
    print(f"Verificando {file_path}...")
    
    if not os.path.exists(file_path):
        print("ERROR: El archivo no existe.")
        sys.exit(1)
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Verificar secciones requeridas
    required_sections = [
        "Modelo Conceptual (Notación de Chen)",
        "Modelo Lógico Relacional (Notación de Patas de Gallo)",
        "Diccionario de Datos Interactivo",
        "Estructura Física y Esquemas de Tablas SQL"
    ]
    
    for section in required_sections:
        if section not in content:
            print(f"ERROR: Falta la sección '{section}' en el documento.")
            sys.exit(1)
            
    # Verificar presencia de diagramas Mermaid
    mermaids = re.findall(r"```mermaid\s+(.*?)\s+```", content, re.DOTALL)
    if len(mermaids) < 2:
        print(f"ERROR: Se esperaban al menos 2 diagramas Mermaid, se encontraron {len(mermaids)}.")
        sys.exit(1)
        
    # Verificar la presencia de entidades clave en el texto
    entities = ["Empresa", "Local", "Empleado", "servicio", "vendedor", "jefe de local", "Local Comercial", "Local de Esparcimiento", "Local de Comidas"]
    for ent in entities:
        if ent.lower() not in content.lower():
            print(f"ERROR: La entidad o elemento '{ent}' no se encuentra en el documento.")
            sys.exit(1)
            
    print("¡Verificación exitosa! El archivo cumple con todos los requerimientos.")

if __name__ == "__main__":
    verify_markdown()
