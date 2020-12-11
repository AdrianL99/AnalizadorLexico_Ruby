import ply.lex as lex
import re
import codecs
import os
import sys
print ("------------------Analizador Lexico en RUBY-------------------------")

palabrasReservadas= [ 
    'END',
    'PRINT',
    'PUTS',
    'IF',
    'ELSE',
    'AND',
    'CASE',
    'DEF',
    'DO',
    'WHEN'
    ]
#Lista de TOKENS
tokens=palabrasReservadas+['VARIABLE','SUMAR','RESTAR','MULTIPLICAR','DIVIDIR','NUMBER','COMMA',
'RPARENT','LPARENT','COMILLA','STRING','MENOR_QUE','MAYOR_QUE','MENOR_IGUAL','MAYOR_IGUAL',
'DECIMAL','BOLEAN']

t_ignore = '\t'

t_RESTAR = r'\-'
t_SUMAR = r'\+'
t_MULTIPLICAR = r'\*'
t_DIVIDIR = r'\/'
t_COMMA = r'\,'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMILLA = r'\"'
t_MENOR_QUE = r'<'
t_MAYOR_QUE = r'>'
t_MENOR_IGUAL = r'\<\='
t_MAYOR_IGUAL = r'\>\='

def t_END(t):
    r'end'
    return t
def t_AND(t):
    r'and'
    return t
def t_CASE(t):
    r'case'
    return t
def t_DEF(t):
    r'def'
    return t
def t_DO(t):
    r'do' 
    return t
def t_WHEN(t):
    r'when'
    return t
def t_VARIABLE(t):
    r'\w+\=|\w+\s\='
    return t
def t_PRINT(t):
    r'print'
    return t
def t_PUTS(t):
    r'puts'
    return t
def t_IF(t):
    r'if'
    return t
def t_ELSE(t):
    r'else'
    return t

def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)
def t_error(t):
    print("Caracter ilegal '%s'"%t.value[0])
    t.lexer.skip(1)
def t_NUMBER(t):
    r'\d+\s'
    t.value = int(t.value)
    return t
def t_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
def t_BOLEAN(t):
    r'true|false'
    return t
def t_espacio(t):
    r"\s"
    pass
def t_STRING(t):
    r'\w+|:'
    return t
archivo= "Ejemplo.rb"
test=archivo
fp=codecs.open(test,"r","utf-8")
cadena=fp.read()
fp.close()

analizador = lex.lex()
analizador.input(cadena)

while True:
    tok=analizador.token()
    if not tok :break
    print(tok)
