# main.py
import sys
from antlr4 import *
from gen.NeoJSLexer import NeoJSLexer
from gen.NeoJSParser import NeoJSParser
from semantic.semantic_visitor import SemanticVisitor
from codegen.code_gen_visitor import CodeGenVisitor


def compilar_archivo(ruta_archivo):
    print(f"==================================================")
    print(f"Analizando archivo: {ruta_archivo}")
    print(f"==================================================")

    # Análisis Léxico y Sintáctico
    input_stream = FileStream(ruta_archivo, encoding='utf-8')
    lexer = NeoJSLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = NeoJSParser(stream)

    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print(f"\n[FALLO] Se encontraron errores sintácticos en '{ruta_archivo}'.")
        return

    print("[OK] Análisis Léxico y Sintáctico completado sin errores.")

    # Análisis Semántico
    semantico = SemanticVisitor()
    semantico.visit(tree)

    if len(semantico.errores) > 0:
        print(f"\n[FALLO] Se detectaron {len(semantico.errores)} errores semánticos:")
        for idx, err in enumerate(semantico.errores, 1):
            print(f"  {idx}. {err}")
        return

    print("[OK] Análisis Semántico completado exitosamente.")
    print(f"  - Ítems registrados ({len(semantico.items_declarados)}): {list(semantico.items_declarados.keys())}")
    print(f"  - Armas registradas ({len(semantico.weapons_declaradas)}): {list(semantico.weapons_declaradas.keys())}")
    print(f"  - Recetas registradas ({len(semantico.recipes_declaradas)}): {list(semantico.recipes_declaradas.keys())}")
    print(f"  - Mobs registrados ({len(semantico.mobs_declarados)}): {list(semantico.mobs_declarados.keys())}")
    print(f"  - Modificaciones vanilla ({len(semantico.modificaciones)}): {[m['target'] for m in semantico.modificaciones]}")

    # Generación de Código Java y Recursos JSON
    print("\n--- Iniciando Generación de Código Java (Minecraft NeoForge) ---")
    codegen = CodeGenVisitor()
    codegen.visit(tree)
    codegen.finalizar()
    codigo_java = codegen.emitir("salida_neoforge")
    print(codigo_java)
    print("\n[ÉXITO] Código Java y recursos JSON para NeoForge generados en './salida_neoforge/'")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        compilar_archivo(sys.argv[1])
    else:
        print("Uso: python main.py <ruta_del_archivo.txt>")