import antlr4 as antlr4
from antlr_gen.decafLexer import decafLexer
from antlr_gen.decafListener import decafListener
from antlr_gen.decafParser import decafParser
from antlr_gen.decafVisitor import decafVisitor
from antlr4.tree.Trees import Trees
import sys

import codecs

# we are reserving the registers available for the operations
from logic.registry_control import reg_controller
# import the tables we are going to use to check
from tables import Tabla_simbolos, Tabla_tipos, Tabla_ambitos

class NewVisitor(decafVisitor):
    # declare the tables
    t_simbolos = 0
    t_tipos = 0
    t_ambitos = 0

    # lines
    line = ''

    def visitAll(self, ctx):
        self.generate_var_declr()
        self.visitChildren(ctx)
        return 0

    # -------------------------------------------- DECLARATION ---------------------------------------------- 
    # METHOD
    def visitMethoDeclaration(self, ctx):
        name = ctx.ID().getText()
        # START
        self.line += str(name) + ":\n"
        self.line += "func start\n"
        # CHILDREN
        self.visitChildren(ctx)
        # END
        self.line += "func end\n"
        return 0

    # VARIABLE
    def visitVarDeclaration(self, ctx):
        return 0

    # STRUCT
    def visitStructDeclaration(self, ctx):
        return 0

    # -------------------------------------------- STATEMENT ---------------------------------------------- 
    # IF
    def visitIfstmt(self, ctx):
        return 0

    # WHILE
    def visitWhilestmt(self, ctx):
        return 0

    # RETURN
    def visitReturnstmt(self, ctx):
        return 0

    # METHOD
    def visitMethodstmt(self, ctx):
        return 0

    # LOCATION
    def visitLocationstmt(self, ctx):
        left_operand = self.visit(ctx.left)


        right_operand = self.visit(ctx.right)
        self.line += str(left_operand) + "=" + str(right_operand) + "\n"
        return 0

    # -------------------------------------------- LOCATION ---------------------------------------------- 
    def visitLocation(self, ctx):
        value = ctx.getText()
        return value

    # -------------------------------------------- LITERAL ---------------------------------------------- 
    def visitLiteral(self, ctx):
        value = self.visitChildren(ctx)
        return value

    def visitInt_Literal(self, ctx):
        value = ctx.NUM()
        return value

    def visitChar_Literal(self, ctx):
        value = ctx.CHAR()
        return value
    
    def visitBool_Literal(self, ctx):
        value = ctx.getText()
        if value == 'true':
            return 1
        if value == 'false':
            return 0

    # -------------------------------------------- other crappers ---------------------------------------------- 

    def insert_tables(self, t_simbolos, t_tipos, t_ambitos):
        self.t_simbolos = t_simbolos
        self.t_tipos = t_tipos
        self.t_ambitos = t_ambitos
    
    def __init__(self):
        self.t_simbolos = []
        self.t_tipos = []
        self.t_ambitos = []

    def clear_tables(self):
        self.t_simbolos = 0
        self.t_tipos = 0
        self.t_ambitos = 0

    def conn(self):
        return self.line

    def generate_var_declr(self):
        # DATA TAG
        self.line += "DATA START\n"
        # iterate over every value in the simbol table
        for value in range(len(self.t_simbolos.t_id)):
            # get the type of the variable 
            t_type = self.t_simbolos.tipo[value]
            var_type = self.t_tipos.nombre[t_type]
            # get the scope the variable is found in
            t_scope = self.t_simbolos.ambito[value]
            scope = self.t_ambitos.nombre[t_scope]
            # get the name of the variable we are instantiating
            name = self.t_simbolos.simbolo[value]

            # insert the var declaration 
            self.line += str(scope) + "_" + str(name) + ":" + str(var_type) + "\n"

        # TEXT TAG
        self.line += "TEXT START\n"