'''
Created on 19 dic 2024

@author: alvar
'''
from mypyc.primitives import str_ops
from mypy.typeshed.stdlib.builtins import int
from test.support._hypothesis_stubs import strategies

if __name__ == '__main__':
    pass
import matplotlib.pyplot as plt
import networkx as nx
from __future__ import annotations
from typing import TypeVar, Generic, Dict, Set, Optional, Callable
from src.entrega3.Grafo import * 


class Gen:
   
    def __init__(self, nombre: str, tipo: str, num_mutaciones: int, loc_cromosomas: str):
        if num_mutaciones < 0:
            raise ValueError("num_mutaciones no es negativo")
        self.nombre = nombre
        self.tipo = tipo
        self.num_mutaciones = num_mutaciones
        self.loc_cromosomas = loc_cromosomas
        
    @staticmethod
    def of(nombre: str, tipo: str, num_mutaciones: int, loc_cromosomas:str) -> Gen:
        pass
    
    @staticmethod
    def parse(genes)-> str:
        pass
    
    
    class RelacionGenAGen:
    
        nombre_gen1:str
        nombre_gen2:str
        conexion:int[-1,1]
                 
    @staticmethod
    def of1(nombre_gen1: str, nombre_gen2: str, conexion:int[-1,1]) -> Gen:
        pass
    
    @staticmethod
    def parse1(red_genes)-> str:
        pass
    
    class RedGenica(Grafo[Gen, RelacionGenAGen]):
        def __init__(self, es_dirigido: bool = False) -> None:
            super().__init__(es_dirigido)
            self.genes_por_nombre: Dict[str,Gen] = {}
            
        @staticmethod
        def of(es_dirigido: bool = False) -> RedGenica:
                     
        @staticmethod
        def parse(f1: str, f2:str, es_dirigido: bool=False)-> RedGenica:
                    
        