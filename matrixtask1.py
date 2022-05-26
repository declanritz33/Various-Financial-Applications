
#declan ritzenthaler, declanr@bu.edu
#assignment 6, task 1
#assigning matrices to a class and perfroming methods on them

import random

class Matrix:
    '''
    this class defines a matrix
    '''
    def __init__(self, matrix_name):
        '''
        constructor initializes an object of type Matrix
        '''
        self.__matrix_name = matrix_name
        self.__matrix_rows = len(matrix_name)
        self.__matrix_columns = len(matrix_name[0])
        

    
    def __repr__(self):
        "takes a list(object) and prints it in matrix format"
        for i in self.__matrix_name:
            assert len(i) == self.__matrix_columns , "2-D list not a compatible matrix"
        r = len(self.__matrix_name)
        l = len(self.__matrix_name[0])
        first = True
        string_rep = f'[['
        for i in range(r):
            if first:
                first = False
            else:
                string_rep += f' ['
            for j in range(len(self.__matrix_name[0])):
                a_float = self.__matrix_name[i][j]
                if(j == len(self.__matrix_name[0])-1):
                    string_rep += "{:.2f}".format(a_float)
                else:
                    string_rep += "{:.2f}, ".format(a_float)
            if i == r - 1:
                string_rep += f']]'
            else:
                string_rep += f']\n'
                
                    
        return string_rep
    
    def __eq__(self, other):
        '''define the operator == for this Point class'''
        
        return self.__matrix_name == other.__matrix_name
    
    def  add_row_into(self, src, dest):
        "makes a new version of a specified row by adding each element from "
        "another specified row"
        if dest >= 0 and dest < len(self.__matrix_name):
            if src >= 0 and dest < len(self.__matrix_name):
                count1 = self.__matrix_name
                count2 = count1[:]
                
                s_row = count2[src]
                d_row = count2[dest]
            
                self.__matrix_name[dest] = [a + b for a, b in zip(s_row, d_row)]
                
    def add_mult_row_into(self, scalar, src, dest):
        "multiplies a specified row by a scalar quanitity and then adds it to another row"
        if src > len(self.__matrix_name) and dest > len(self.__matrix_name):
            quit
            
        else:
            if src >= 0 and src < len(self.__matrix_name):
                count1 = self.__matrix_name
                count2 = count1[:]
                
                row_length = count2[src]
                
                new_row_value = [scalar*i for i in row_length]
                
                if dest >= 0 and dest < len(self.__matrix_name):
                    if src >= 0 and dest < len(self.__matrix_name):
                        count1 = self.__matrix_name
                        count2 = count1[:]
                        
                        d_row = count2[dest]
                        
                        self.__matrix_name[dest] = [a + b for a, b in zip(d_row,new_row_value)]
                
                
            
            #self.__matrix_name[src] = new_row_value
    
    def swap_rows(self, src , dest):
        "swaps two specified rows within the matrix"
    
        M = self.__matrix_name
        if dest >= 0 and dest < len(M):
            if src >= 0 and src < len(M):
                M[src] , M[dest] = M[dest] , M[src]
                
    def mult_scalar(self,s):
        "multiplies a matrix values by a singular scalar quantity, returns a new matrix"
        lst = []
        for i in range(len(self.__matrix_name)):
            row = []
            for j in range(len(self.__matrix_name[0])):
                row.append(self.__matrix_name[i][j] * s)
            lst.append(row)

        return Matrix(lst)
    
    def add_scalar(self,s):
        'adds a scalar quantity to each element of the matrix'
        lst = []
        for i in range(len(self.__matrix_name)):
            row = []
            for j in range(len(self.__matrix_name[0])):
                row.append(self.__matrix_name[i][j] + s)
            lst.append(row)

        return Matrix(lst)
    
    def __add__(self, c):
        '''implement the operator +'''
        if type(c) == Matrix:
            return self.add_matrices(c)
        else:
            return self.add_scalar(c)
    
    def __sub__(self, c):
        '''implement the operator - '''
        if type(c) == Matrix:
            mat = c.mult_scalar(-1)
            return self.add_matrices(mat)
        else:
            return self.add_scalar(-c)
    
    def __mul__(self, c):
        '''implement the operator * '''
        if type(c) == Matrix:
            return self.dot_product(c)
        else:
            return self.mult_scalar(c)
    
    def __truediv__(self, c):
        '''implements the operator'''
        return self.mult_scalar(1/c)
    
    
    def transpose(self):
        'transposes self'
        zipped_rows = zip(*self.__matrix_name)
        transpose_matrix = [list(row) for row in zipped_rows]
    
        return Matrix(transpose_matrix)
    
    
    def zeros(m,n=None):
        "produces an array list of 0's with m number of rows and n number of columns"
        lst = []
        if n is None:
            n = m
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(0)
            lst.append(temp)
        return Matrix(lst)
        
    
    def dot_product(self, other):
        'returns the dot product of two compatitble matrices'
        assert self.__matrix_rows == other.__matrix_columns  , "incompatible dimensions"
        
        
        new_matrix = Matrix.zeros(len(self.__matrix_name))
        
        tN = Matrix.transpose(other)
        
        M = self.__matrix_name
        
        for i in range(len(M)):
            for j in range(len(other.__matrix_name[0])):
                for k in range(len(M[0])):
                    new_matrix.__matrix_name[i][j] += M[i][k] * tN.__matrix_name[j][k]
                
        return new_matrix
    
    def add_matrices(self, other):
        "adds two matrices together element-wise"
        assert len(self.__matrix_name)==len(other.__matrix_name)
        assert len(self.__matrix_name[0]) == len(other.__matrix_name[0])
        lst = []
        for i in range(len(self.__matrix_name)):
            assert len(self.__matrix_name) == len(other.__matrix_name) , "can only add matrices with the same number of rows and columns"
            assert len(self.__matrix_name[i]) == len(other.__matrix_name[i]) , "can only add matrices with the same number of rows and columns"
            row = []
            for j in range(len(self.__matrix_name[0])):
                row.append(self.__matrix_name[i][j]+other.__matrix_name[i][j])
            lst.append(row)
        return Matrix(lst)

        
    def identity(n):
        "prints a matrix with 1's along the diagonal"
        lst = []
        for i in range(n):
            temp = []
            for j in range(n):
                if i == j:
                    temp.append(1)
                else:
                    temp.append(0)
            lst.append(temp)
        return Matrix(lst)  
    
    def ones(m,n=None):
        'returns a matrix of all ones'
        lst = []
        if n is None:
            n = m
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(1)
            lst.append(temp)
        return Matrix(lst)
    
    def random_int_matrix(m,n=None,low=0,high=10):
        'generates a matrix of m*n dimensions and populates it with random numbers within a range'
        lst = []
        if n is None:
            n = m
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(random.randint(low, high))
            lst.append(temp)
        return Matrix(lst)
    
    def random_float_matrix(m,n=None):
        'generates a matrix of random float numbers between 0 and 1'
        lst = []
        if n is None:
            n = m
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(random.random())
            lst.append(temp)
        return Matrix(lst)
        
       
    def describe(self):
        'gives descriptive info about the matrix'
        r = len(self.__matrix_name)
        c = len(self.__matrix_name[0])
        
        dimensions = f'{r} x {c}'
        res = list()
        for j in range(0, len(self.__matrix_name[0])):
            tmp = 0
            for i in range(0, len(self.__matrix_name)):
                tmp = tmp + self.__matrix_name[i][j]
            res.append(tmp)   
        sum_elem = sum(res)
        mean_elem = sum_elem/(r*c)
        column_sums = res
        column_means = [i / r for i in res]
        #display = f'Matrix({self})'
        #dimensions = f'dimensions: {dimensions}'
        #sumstring = f'sum of elements: {sum_elem}'
        #meanstring = f'mean of elements: {round(mean_elem,4)}'
        #colsums = f'column sums: {column_sums}'
        #colmeans = f'column Means: {column_means}'
        
        return f'{self}\n dimensions: {dimensions}\n sum of elements: {sum_elem}\n mean of elements: {mean_elem}\n column sums: {column_sums}\n column means: {column_means}'
        

## unit test code
if __name__ == '__main__':

    A = Matrix([[0,2,0], [5,5,5],[6,3,0]])
    B = Matrix([[4,5,6],[1,2,34],[2,3,4]])
    C = Matrix([[7,8,4],[4,9,10],[12,11,12]])
    
    print(A)
    print(B)
    print(A == B)
    A.add_row_into(2,0)
    print(A)
    A.add_mult_row_into(-1,2,0)
    print(A)
    print(A + B)
    print(A - B)
    print(A * B)
    A.swap_rows(1,2)
    print(A)
    print(A.mult_scalar(5))
    print(A.add_scalar(1))
    print(A)
    print(Matrix.zeros(7,4))
    print(Matrix.zeros(4))
    print(Matrix.ones(2,3))
    print(Matrix.identity(4))
    print(Matrix.random_float_matrix(5))
    print(Matrix.random_int_matrix(5,4,0,50))
    
    print(A.describe())

##end unit test code