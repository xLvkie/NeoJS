# semantic_visitor.py
from gen.NeoJSVisitor import NeoJSVisitor
from gen.NeoJSParser import NeoJSParser

class SemanticVisitor(NeoJSVisitor):

    def __init__(self):
        # Tablas de Símbolos separadas por categoría
        self.items_declarados = {}
        self.bosses_declarados = {}
        self.loots_declarados = {}
        self.modificaciones = []
        self.errores = []

        # Sistema de Tipos (Type System) para todos los bloques
        self.reglas_tipos = {
            # Atributos de Ítems y Jefes
            "damage": "NUMBER",
            "durability": "NUMBER",
            "attack_speed": "NUMBER",
            "hp": "NUMBER",
            "armor": "NUMBER",
            "name": "STRING",
            "rarity": "STRING",
            "effect": "STRING",
            "ability": "STRING",
            "crit_chance": "PERCENTAGE",
            "lifesteal": "PERCENTAGE",
            "fire_immune": "BOOLEAN",
            "glowing": "BOOLEAN",
            "enrage_time": "TIME_LITERAL",
            # Atributos exclusivos de Drops en Loot
            "chance": "PERCENTAGE",
            "min": "NUMBER",
            "max": "NUMBER"
        }

    # 1. Validación de Ítems
    def visitItemDecl(self, ctx: NeoJSParser.ItemDeclContext):
        nombre = ctx.ID().getText()
        linea = ctx.start.line

        if nombre in self.items_declarados:
            self.errores.append(f"[Línea {linea}] Error Semántico: El ítem '{nombre}' ya fue declarado.")
        
        atributos = self.visit(ctx.attrList())
        self.items_declarados[nombre] = atributos

    # 2. Validación de Jefes y Fases
    def visitBossDecl(self, ctx: NeoJSParser.BossDeclContext):
        nombre = ctx.ID().getText()
        linea = ctx.start.line
        es_fase = ctx.TK_PHASE() is not None

        if nombre in self.bosses_declarados:
            self.errores.append(f"[Línea {linea}] Error Semántico: El jefe/fase '{nombre}' ya fue declarado.")

        atributos = self.visit(ctx.attrList())
        self.bosses_declarados[nombre] = {"is_phase": es_fase, "attrs": atributos}

    # 3. Validación de Loot y Suma de Probabilidades <= 100%
    def visitLootDecl(self, ctx: NeoJSParser.LootDeclContext):
        nombre_loot = ctx.ID().getText()
        linea = ctx.start.line

        if nombre_loot in self.loots_declarados:
            self.errores.append(f"[Línea {linea}] Error Semántico: La tabla de loot '{nombre_loot}' ya fue declarada.")

        drops = self.visit(ctx.dropList())
        suma_probabilidades = 0.0

        for d in drops:
            attrs = d["attrs"]
            if "chance" in attrs:
                tipo, valor = attrs["chance"]
                if tipo == "PERCENTAGE":
                    suma_probabilidades += valor

        # ERROR SEMÁNTICO DE LÓGICA DE DOMINIO: Probabilidad > 100%
        if suma_probabilidades > 100.0:
            self.errores.append(
                f"[Línea {linea}] Error Semántico: El loot '{nombre_loot}' tiene probabilidades que suman {suma_probabilidades}% (máximo permitido: 100%)."
            )

        self.loots_declarados[nombre_loot] = drops

    def visitDropList(self, ctx: NeoJSParser.DropListContext):
        lista_drops = []
        for drop_ctx in ctx.dropDecl():
            lista_drops.append(self.visit(drop_ctx))
        return lista_drops

    def visitDropDecl(self, ctx: NeoJSParser.DropDeclContext):
        item_id = ctx.ID().getText()
        atributos = self.visit(ctx.attrList())
        return {"item": item_id, "attrs": atributos}

    # 4. Validación de Modificaciones
    def visitModifyDecl(self, ctx: NeoJSParser.ModifyDeclContext):
        target_id = ctx.ID().getText()
        linea = ctx.start.line

        if ":" not in target_id:
            self.errores.append(
                f"[Línea {linea}] Error Semántico: Para modificar '{target_id}' debes incluir su namespace (ej. 'minecraft:{target_id}')."
            )

        atributos = self.visit(ctx.attrList())
        self.modificaciones.append({"target": target_id, "attributes": atributos})

    # Recorrido de atributos y condiciones
    def visitAttrList(self, ctx: NeoJSParser.AttrListContext):
        atributos_recolectados = {}
        for attr_ctx in ctx.attr():
            clave, valor_info = self.visit(attr_ctx)
            atributos_recolectados[clave] = valor_info
        return atributos_recolectados

    def visitAttr(self, ctx: NeoJSParser.AttrContext):
        linea = ctx.start.line

        # Si es una regla 'condition : ID OP_REL value'
        if ctx.TK_CONDITION():
            cond_info = self.visit(ctx.condition())
            return "condition", ("CONDITION", cond_info)

        # Si es un atributo normal 'ID : value'
        nombre_attr = ctx.ID().getText()
        tipo_actual, valor_limpio = self.visit(ctx.value())

        if nombre_attr in self.reglas_tipos:
            tipo_esperado = self.reglas_tipos[nombre_attr]
            if tipo_actual != tipo_esperado:
                self.errores.append(
                    f"[Línea {linea}] Error Semántico: '{nombre_attr}' requiere tipo {tipo_esperado}, pero recibió {tipo_actual} ({valor_limpio})."
                )
        else:
            self.errores.append(
                f"[Línea {linea}] Error Semántico: El atributo '{nombre_attr}' no es reconocido por NeoJS."
            )

        return nombre_attr, (tipo_actual, valor_limpio)

    def visitCondition(self, ctx: NeoJSParser.ConditionContext):
        var_name = ctx.ID().getText()
        op = ctx.OP_REL().getText()
        _, val = self.visit(ctx.value())
        return f"{var_name} {op} {val}"

    def visitValue(self, ctx: NeoJSParser.ValueContext):
        if ctx.NUMBER():
            return ("NUMBER", float(ctx.NUMBER().getText()))
        elif ctx.STRING():
            return ("STRING", ctx.STRING().getText()[1:-1])
        elif ctx.PERCENTAGE():
            return ("PERCENTAGE", float(ctx.PERCENTAGE().getText().replace("%", "")))
        elif ctx.TIME_LITERAL():
            return ("TIME_LITERAL", ctx.TIME_LITERAL().getText())
        elif ctx.TRUE() or ctx.FALSE():
            return ("BOOLEAN", ctx.getText() == "true")
        elif ctx.ID():
            return ("ID", ctx.ID().getText())
        return ("UNKNOWN", ctx.getText())