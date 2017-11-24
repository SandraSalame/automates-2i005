# -*- coding: utf-8 -*-
from transition import Transition
from state import State
import os
import copy
import sp
from sp import *
from parser import Parser
from itertools import product
from automateBase import AutomateBase



class Automate(AutomateBase):
        
        def succElem(self, state, lettre):
                """State x str -> list[State]
                rend la liste des états accessibles à partir d'un état
                state par l'étiquette lettre
                """
                # successeurs : list[State]
                successeurs = []
                # t: Transitions
                for t in self.getListTransitionsFrom(state):
                        if t.etiquette == lettre and t.stateDest not in successeurs:
                                successeurs.append(t.stateDest)
                return successeurs

        def succ (self, listStates, lettre):
                """list[State] x str -> list[State]
                rend la liste des états accessibles à partir de la liste d'états
                listStates par l'étiquette lettre
                """
                
                successeurs = []

                for s in listStates :
                        for t in self.succElem(s, lettre) :
                                if not(t in successeurs) :
                                        successeurs.append(t)

                return successeurs



        
        def acc(self):
                """ -> list[State]
                rend la liste des états accessibles
                """            

                states = []

                for t in self.listTransitions :
                        if not(t.stateDest in states) :
                                states.append(t.stateDest)

                return states



        """ Définition d'une fonction déterminant si un mot est accepté par un automate.
        Exemple :
                a=Automate.creationAutomate("monAutomate.txt")
                if Automate.accepte(a,"abc"):
                        print "L'automate accepte le mot abc"
                else:
                        print "L'automate n'accepte pas le mot abc"
        """
        @staticmethod
        def accepte(auto,mot) :
                """ Automate x str -> bool
                rend True si auto accepte mot, False sinon
                """

                flag = False

                for s in auto.listStates :
                        if s.init :
                                flag = auto.accepteRec(s, mot, 0)
                        if flag :
                                return flag

                return flag


        def accepteRec(self, state, mot, index) :
                if index == len(mot) and state.fin :
                        return True
                elif index == len(mot) and not(state.fin) :
                        return False

                flag = False

                for t in self.transitions(state) :
                        if t.etiquette == mot[index] :
                                flag = self.accepteRec(t.stateDest, mot, index + 1)
                                if flag :
                                        return flag

                return flag


        def transitions(self, state) :
                trans = []

                for t in self.listTransitions :
                        if t.stateSrc == state :
                                trans.append(t)

                return trans


        @staticmethod
        def estComplet(auto,alphabet) :
                """ Automate x str -> bool
                rend True si auto est complet pour alphabet, False sinon
                """

                for s in auto.listStates :
                        for c in alphabet :
                                if not(auto.transExists(s, c)) :
                                        return False

                return True

        def transExists(self, state, etiquette) :
                for t in self.transitions(state) :
                        if t.etiquette == etiquette :
                                return True

                return False

        @staticmethod
        def estDeterministe(auto) :
                """ Automate  -> bool
                rend True si auto est déterministe, False sinon
                """

                ei = 0

                for s in auto.listStates :
                        if s.init :
                                ei += 1

                if ei != 1 :
                        return False

                for s in auto.listStates :
                        etiquettes = []
                        for t in auto.transitions(s) :
                                if t.etiquette in etiquettes :
                                        return False
                                else :
                                        etiquettes.append(t.etiquette)

                return True


       
        @staticmethod
        def completeAutomate(auto,alphabet) :
                """ Automate x str -> Automate
                rend l'automate complété d'auto, par rapport à alphabet
                """

                if Automate.estComplet(auto, alphabet) :
                        return auto

                newId = 0

                for s in auto.listStates :
                        newId += int(s.id)

                newState = State(newId, False, False, "Puit")
                auto.addState(newState)

                for s in auto.listStates :
                        etiquettes = []
                        for t in auto.transitions(s) :
                                if not(t.etiquette in etiquettes) :
                                        etiquettes.append(t.etiquette)
                        for c in alphabet :
                                if not(c in etiquettes) :
                                        auto.addTransition(Transition(s, c, newState))

                return auto


       
        @staticmethod
        def determinisation(auto) :
                """ Automate  -> Automate
                rend l'automate déterminisé d'auto
                """
                return 


        @staticmethod
        def complementaire(auto, alphabet):
                """ Automate x str -> Automate
                rend  l'automate acceptant pour langage le complémentaire du langage de auto
                """
                return


     
        @staticmethod
        def intersection (auto1, auto2):
                """ Automate x Automate -> Automate
                rend l'automate acceptant pour langage l'intersection des langages des deux automates
                """
                return 


        @staticmethod
        def union (auto1, auto2):
                """ Automate x Automate -> Automate
                rend l'automate acceptant pour langage l'union des langages des deux automates
                """
                return 


        
       
        @staticmethod
        def concatenation (auto1, auto2):
                """ Automate x Automate -> Automate
                rend l'automate acceptant pour langage la concaténation des langages des deux automates
                """
                return 

       
        @staticmethod
        def etoile (auto):
                """ Automate  -> Automate
                rend l'automate acceptant pour langage l'étoile du langage de a
                """
                return 





