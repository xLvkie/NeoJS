# main.py
import sys
from antlr4 import CommonTokenStream, FileStream
from gen.NeoJSLexer import NeoJSLexer
from gen.NeoJSParser import NeoJSParser
from semantic.semantic_visitor import SemanticVisitor
from codegen.code_gen_visitor import CodeGenVisitor

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <archivo_entrada.txt> [carpeta_salida]")
        sys.exit(1)

    carpeta_destino = sys.argv[2] if len(sys.argv) >= 3 else "salida_java"

    # 1. Leer el archivo fuente
    entrada = FileStream(sys.argv[1], encoding="utf-8")

    # 2. Lexer y Parser (ANTLR4)
    lexer  = NeoJSLexer(entrada)
    tokens = CommonTokenStream(lexer)
    parser = NeoJSParser(tokens)
    arbol  = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("\n[!] Se encontraron errores sintácticos. Compilación abortada.")
        sys.exit(1)

    # 3. Análisis semántico
    semantico = SemanticVisitor()
    semantico.visit(arbol)

    if semantico.errores:
        for e in semantico.errores:
            print("Error:", e)
        sys.exit(1)

    # 4. Generación de código (Backend Java)
    codegen = CodeGenVisitor()
    codegen.visit(arbol)
    codegen.finalizar()

    # 5. Guardar y emitir el código Java generado
    codigo_generado = codegen.emitir(carpeta_destino)
    print(codigo_generado)

if __name__ == "__main__":
    main()