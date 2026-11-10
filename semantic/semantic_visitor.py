# semantic/semantic_visitor.py
from gen.NeoJSVisitor import NeoJSVisitor
from gen.NeoJSParser import NeoJSParser


class SemanticVisitor(NeoJSVisitor):

    def __init__(self):
        self.items_declarados = {}
        self.weapons_declaradas = {}
        self.recipes_declaradas = {}
        self.mobs_declarados = {}
        self.modificaciones = []
        self.errores = []

        # Tipos esperados por atributo
        self.reglas_tipos = {
            "name": "STRING",
            "base_item": "ID",
            "asset_path": "STRING",
            "rarity": "STRING",
            "stack_size": "NUMBER",
            "fire_immune": "BOOLEAN",
            "damage": "NUMBER",
            "durability": "NUMBER",
            "attack_speed": "NUMBER",
            "effect": "STRING",
            "crit_chance": "PERCENTAGE",
            "result": "ID",
            "amount": "NUMBER",
            "ingredients": "STRING",
            "base_model": "ID",
            "behavior": "STRING",
            "hp": "NUMBER",
            "defense": "NUMBER",
            "armor": "NUMBER",
            "hitbox_w": "NUMBER",
            "hitbox_h": "NUMBER",
            "scale": "NUMBER",
        }

        # Atributos permitidos según el contexto de la declaración (Error #3)
        self.atributos_por_contexto = {
            "item": {"name", "base_item", "asset_path", "rarity", "stack_size", "fire_immune"},
            "weapon": {"name", "base_item", "asset_path", "rarity", "damage", "durability", "attack_speed", "effect", "fire_immune", "crit_chance"},
            "recipe": {"result", "amount", "ingredients"},
            "mob": {"name", "base_model", "asset_path", "behavior", "hp", "damage", "defense", "armor", "hitbox_w", "hitbox_h", "scale", "effect"},
            "modify_mob": {"hp", "damage", "defense", "armor", "scale"},
            "modify_item": {"damage", "durability", "attack_speed", "crit_chance", "stack_size", "fire_immune"},
        }

        self.rarities_validas = {"common", "uncommon", "rare", "epic"}
        self.behaviors_validos = {"aggressive", "passive", "neutral"}

    def visitProgram(self, ctx: NeoJSParser.ProgramContext):
        for decl in ctx.declaration():
            self.visit(decl)
        # Validación post-recorrido para Error #8 (Referencias en recetas a ítems declarados)
        self._validar_referencias_recetas()
        return None

    # ==========================================
    # DECLARACIÓN DE ÍTEMS
    # ==========================================
    def visitItemDecl(self, ctx: NeoJSParser.ItemDeclContext):
        nombre = ctx.ID().getText()
        linea = ctx.start.line

        # Error #1: Identificador duplicado
        if nombre in self.items_declarados or nombre in self.weapons_declaradas:
            self.errores.append(
                f"[Línea {linea}] (Error #1 - Identificador Duplicado) El ítem '{nombre}' ya fue declarado previamente."
            )

        attrs = self._procesar_atributos(ctx.attrList(), "item", nombre)
        self._validar_dominios_comunes(attrs, linea, nombre)
        self.items_declarados[nombre] = attrs

    # ==========================================
    # DECLARACIÓN DE ARMAS
    # ==========================================
    def visitWeaponDecl(self, ctx: NeoJSParser.WeaponDeclContext):
        nombre = ctx.ID().getText()
        linea = ctx.start.line

        # Error #1: Identificador duplicado (entre armas o colisión con ítems)
        if nombre in self.weapons_declaradas or nombre in self.items_declarados:
            self.errores.append(
                f"[Línea {linea}] (Error #1 - Identificador Duplicado) El arma '{nombre}' ya fue declarada previamente."
            )

        attrs = self._procesar_atributos(ctx.attrList(), "weapon", nombre)

        # Error #7: Atributo obligatorio en weapon
        if "damage" not in attrs:
            self.errores.append(
                f"[Línea {linea}] (Error #7 - Atributo Obligatorio Faltante) El arma '{nombre}' debe especificar el atributo 'damage'."
            )

        self._validar_dominios_comunes(attrs, linea, nombre)
        self.weapons_declaradas[nombre] = attrs

    # ==========================================
    # DECLARACIÓN DE RECETAS
    # ==========================================
    def visitRecipeDecl(self, ctx: NeoJSParser.RecipeDeclContext):
        nombre = ctx.ID().getText()
        linea = ctx.start.line

        # Error #1: Identificador duplicado
        if nombre in self.recipes_declaradas:
            self.errores.append(
                f"[Línea {linea}] (Error #1 - Identificador Duplicado) La receta '{nombre}' ya fue declarada previamente."
            )

        attrs = self._procesar_atributos(ctx.attrList(), "recipe", nombre)

        # Error #7: Atributos obligatorios en recipe
        if "result" not in attrs or "ingredients" not in attrs:
            self.errores.append(
                f"[Línea {linea}] (Error #7 - Atributo Obligatorio Faltante) La receta '{nombre}' requiere obligatoriamente 'result' e 'ingredients'."
            )

        self._validar_dominios_comunes(attrs, linea, nombre)
        self.recipes_declaradas[nombre] = {"linea": linea, "attrs": attrs}

    # ==========================================
    # DECLARACIÓN DE MOBS
    # ==========================================
    def visitMobDecl(self, ctx: NeoJSParser.MobDeclContext):
        nombre = ctx.ID().getText()
        linea = ctx.start.line

        # Error #1: Identificador duplicado
        if nombre in self.mobs_declarados:
            self.errores.append(
                f"[Línea {linea}] (Error #1 - Identificador Duplicado) El mob '{nombre}' ya fue declarado previamente."
            )

        attrs = self._procesar_atributos(ctx.attrList(), "mob", nombre)
        self._validar_dominios_comunes(attrs, linea, nombre)

        # Error #10: Inconsistencia lógica entre behavior "passive" y damage > 0
        if "behavior" in attrs and "damage" in attrs:
            tipo_b, val_b = attrs["behavior"]
            tipo_d, val_d = attrs["damage"]
            if tipo_b == "STRING" and tipo_d == "NUMBER":
                if val_b.lower() == "passive" and val_d > 0:
                    self.errores.append(
                        f"[Línea {linea}] (Error #10 - Inconsistencia de Comportamiento) El mob '{nombre}' es 'passive' pero tiene damage={val_d} (> 0). Un mob pacífico debe tener damage: 0."
                    )

        self.mobs_declarados[nombre] = attrs

    # ==========================================
    # DECLARACIÓN MODIFY (VANILLA OVERRIDES)
    # ==========================================
    def visitModifyDecl(self, ctx: NeoJSParser.ModifyDeclContext):
        target_id = ctx.ID().getText()
        linea = ctx.start.line
        kind = "mob" if ctx.TK_MOB() else "item"
        contexto = f"modify_{kind}"

        # Error #9: Identificador objetivo sin namespace en modify
        if ":" not in target_id:
            self.errores.append(
                f"[Línea {linea}] (Error #9 - Namespace Faltante) Para modificar el {kind} '{target_id}' debes incluir su namespace (ej. 'minecraft:{target_id}')."
            )

        attrs = self._procesar_atributos(ctx.attrList(), contexto, target_id)
        self._validar_dominios_comunes(attrs, linea, target_id)
        self.modificaciones.append({"kind": kind, "target": target_id, "attributes": attrs})

    # ==========================================
    # PROCESAMIENTO Y VALIDACIONES AUXILIARES
    # ==========================================
    def _procesar_atributos(self, attr_list_ctx: NeoJSParser.AttrListContext, contexto: str, entidad: str):
        atributos = {}
        permitidos = self.atributos_por_contexto.get(contexto, set())

        for attr_ctx in attr_list_ctx.attr():
            linea = attr_ctx.start.line
            nombre_attr = attr_ctx.ID().getText()
            tipo_actual, valor_limpio = self.visit(attr_ctx.value())

            # Error #4: Propiedad duplicada dentro del mismo bloque
            if nombre_attr in atributos:
                self.errores.append(
                    f"[Línea {linea}] (Error #4 - Propiedad Duplicada) El atributo '{nombre_attr}' está repetido dentro de '{entidad}'."
                )

            # Error #3: Atributo desconocido o fuera de contexto
            if nombre_attr not in self.reglas_tipos:
                self.errores.append(
                    f"[Línea {linea}] (Error #3 - Atributo No Reconocido) El atributo '{nombre_attr}' no existe en la especificación de NeoJS."
                )
            elif nombre_attr not in permitidos:
                self.errores.append(
                    f"[Línea {linea}] (Error #3 - Atributo Fuera de Contexto) El atributo '{nombre_attr}' no es válido dentro de un bloque '{contexto}' ('{entidad}')."
                )
            else:
                # Error #2: Incompatibilidad de tipos
                tipo_esperado = self.reglas_tipos[nombre_attr]
                if tipo_actual != tipo_esperado:
                    self.errores.append(
                        f"[Línea {linea}] (Error #2 - Tipo Incompatible) '{nombre_attr}' en '{entidad}' requiere {tipo_esperado}, pero recibió {tipo_actual} ({valor_limpio})."
                    )

            atributos[nombre_attr] = (tipo_actual, valor_limpio)

        return atributos

    def _validar_dominios_comunes(self, attrs: dict, linea: int, entidad: str):
        # Error #5: Valores de enumeración inválidos (rarity, behavior)
        if "rarity" in attrs and attrs["rarity"][0] == "STRING":
            val = attrs["rarity"][1].lower()
            if val not in self.rarities_validas:
                self.errores.append(
                    f"[Línea {linea}] (Error #5 - Enumeración Inválida) '{entidad}' tiene rarity '{val}'. Valores permitidos: {sorted(self.rarities_validas)}."
                )

        if "behavior" in attrs and attrs["behavior"][0] == "STRING":
            val = attrs["behavior"][1].lower()
            if val not in self.behaviors_validos:
                self.errores.append(
                    f"[Línea {linea}] (Error #5 - Enumeración Inválida) '{entidad}' tiene behavior '{val}'. Valores permitidos: {sorted(self.behaviors_validos)}."
                )

        # Error #6: Rangos numéricos y porcentajes fuera de límite
        if "stack_size" in attrs and attrs["stack_size"][0] == "NUMBER":
            val = attrs["stack_size"][1]
            if val < 1 or val > 64 or int(val) != val:
                self.errores.append(
                    f"[Línea {linea}] (Error #6 - Rango Numérico Inválido) 'stack_size' en '{entidad}' debe ser un entero entre 1 y 64 (recibió {val})."
                )

        for prop_positiva in ("hp", "durability", "hitbox_w", "hitbox_h", "scale", "amount"):
            if prop_positiva in attrs and attrs[prop_positiva][0] == "NUMBER":
                val = attrs[prop_positiva][1]
                if val <= 0:
                    self.errores.append(
                        f"[Línea {linea}] (Error #6 - Rango Numérico Inválido) '{prop_positiva}' en '{entidad}' debe ser mayor que 0 (recibió {val})."
                    )

        for prop_no_negativa in ("damage", "defense", "armor"):
            if prop_no_negativa in attrs and attrs[prop_no_negativa][0] == "NUMBER":
                val = attrs[prop_no_negativa][1]
                if val < 0:
                    self.errores.append(
                        f"[Línea {linea}] (Error #6 - Rango Numérico Inválido) '{prop_no_negativa}' en '{entidad}' no puede ser negativo (recibió {val})."
                    )

        if "crit_chance" in attrs and attrs["crit_chance"][0] == "PERCENTAGE":
            val = attrs["crit_chance"][1]
            if val < 0 or val > 100:
                self.errores.append(
                    f"[Línea {linea}] (Error #6 - Rango de Porcentaje Inválido) 'crit_chance' en '{entidad}' debe estar entre 0% y 100% (recibió {val}%)."
                )

        # Error #9: base_item y base_model deben tener namespace (ej. minecraft:diamond)
        for prop_ns in ("base_item", "base_model"):
            if prop_ns in attrs and attrs[prop_ns][0] == "ID":
                val = attrs[prop_ns][1]
                if ":" not in val:
                    self.errores.append(
                        f"[Línea {linea}] (Error #9 - Namespace Faltante) '{prop_ns}' en '{entidad}' debe incluir namespace (ej. 'minecraft:{val}')."
                    )

    def _validar_referencias_recetas(self):
        # Error #8: Validar que result e ingredients existan si no son de minecraft:
        simbolos_items = set(self.items_declarados.keys()) | set(self.weapons_declaradas.keys())
        for nombre_receta, info in self.recipes_declaradas.items():
            linea = info["linea"]
            attrs = info["attrs"]

            if "result" in attrs and attrs["result"][0] == "ID":
                res_id = attrs["result"][1]
                if ":" not in res_id and res_id not in simbolos_items:
                    self.errores.append(
                        f"[Línea {linea}] (Error #8 - Referencia No Declarada) La receta '{nombre_receta}' produce '{res_id}', pero no existe ningún item o weapon declarado con ese ID."
                    )

            if "ingredients" in attrs and attrs["ingredients"][0] == "STRING":
                ing_raw = attrs["ingredients"][1]
                partes = [p.strip() for p in ing_raw.split("+") if p.strip()]
                for p in partes:
                    tokens = p.split()
                    item_ref = tokens[-1] if tokens else ""
                    if item_ref and ":" not in item_ref and item_ref not in simbolos_items:
                        self.errores.append(
                            f"[Línea {linea}] (Error #8 - Referencia No Declarada) La receta '{nombre_receta}' usa el ingrediente '{item_ref}', pero no ha sido declarado."
                        )

    def visitValue(self, ctx: NeoJSParser.ValueContext):
        if ctx.NUMBER():
            return ("NUMBER", float(ctx.NUMBER().getText()))
        elif ctx.STRING():
            return ("STRING", ctx.STRING().getText()[1:-1])
        elif ctx.PERCENTAGE():
            return ("PERCENTAGE", float(ctx.PERCENTAGE().getText().replace("%", "")))
        elif ctx.TRUE() or ctx.FALSE():
            return ("BOOLEAN", ctx.getText() == "true")
        elif ctx.ID():
            return ("ID", ctx.ID().getText())
        return ("UNKNOWN", ctx.getText())