from copy import deepcopy
from typing import List, Set


class solve:
    def __init__(self):
        self.alpha = []
        self.KB = []
        self.newClause = []
        self.solution = False

    def readInput(self, filename:str):
        f = open(filename, 'r')
        self.alpha = f.readline()[:-1].split(" OR ")
        size = int(f.readline())
        for i in range(size):
            if i != size - 1:
                self.KB.append(f.readline()[:-1].split(" OR "))
            else:
                self.KB.append(f.readline().split(" OR "))
        f.close()

    def negateLiteral(self, literal):
        if literal[0] == '-':
            return literal[1]
        return '-' + literal
    
    @staticmethod
    def standard_clause(clause: list):
        temp = deepcopy(clause)
        temp = set(temp)

        return sorted(temp, key=lambda literal: literal[-1])
    
    @staticmethod
    def is_complentary_literals(literal1: str, literal2: str):
        return len(literal1) != len(literal2) and literal1[-1] == literal2[-1]

    def is_valid_clause(self, clause):
        for i in range(len(clause) - 1):
            if self.is_complentary_literals(clause[i], clause[i + 1]):
                return True
        return False
    
    def resolve(self, clause1: list, clause2: list):
        resolvents = []
        for i in range(len(clause1)):
            for j in range(len(clause2)):
                if self.is_complentary_literals(clause1[i], clause2[j]):
                    resolvent = clause1[:i] + clause1[i + 1:] + clause2[:j] + clause2[j + 1:]
                    resolvents.append(self.standard_clause(resolvent))
        return resolvents
    
    

    def pl_resolution(self):
        for clause in self.alpha:
            clause = self.negateLiteral(clause)
            if clause not in self.KB:
                self.KB.append([clause])

        while True:
            self.newClause.append([])

            for i in range(len(self.KB)):
                for j in range(i + 1, len(self.KB)):
                    resolvents = self.resolve(self.KB[i], self.KB[j])

                    if [] in resolvents:
                        self.solution = True
                        self.newClause[-1].append([])
                        return self.solution
                    for resolvent in resolvents:
                        if self.is_valid_clause(resolvent):
                            break
                        if resolvent not in self.KB and resolvent not in self.newClause[-1]:
                            self.newClause[-1].append(resolvent)

            if len(self.newClause[-1]) == 0:
                self.solution = False
                return self.solution
            self.KB += self.newClause[-1]

    def formatClause(self, clause):
        if(len(clause) == 0):
            return "{}"
        formatedClause = ''
        clause = list(clause)
        for i in range(len(clause) - 1):
            formatedClause += str(clause[i]) + " OR "
        formatedClause += str(clause[-1])

        return formatedClause
                    
            
    def writeOutput(self, filename: str):
        f = open(filename, 'w')
        for newClauses in self.newClause:
            f.write(str(len(newClauses)) + '\n')
            for clause in newClauses:
                f.write(self.formatClause(clause) + '\n')
        if self.solution == True:
            f.write('YES\n')     
        else:
            f.write('NO\n')
        f.close()


def main():
    ans = solve()
    ans.readInput("input.txt")
    ans.pl_resolution()
    ans.writeOutput("output.txt")

if __name__ == '__main__':
    main()