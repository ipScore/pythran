from test_env import TestEnv

class TestBlas(TestEnv):

    def test_matrix_multiply(self):
        code="""
def zero(n,m): return [[0 for row in xrange(n)] for col in xrange(m)]
def matrix_multiply(m0, m1):
    new_matrix = zero(len(m0),len(m1[0]))
    for i in xrange(len(m0)):
        for j in xrange(len(m1[0])):
            for k in xrange(len(m1)):
                new_matrix[i][j] += m0[i][k]*m1[k][j]
    return new_matrix"""
        self.run_test(code, [[0,1],[1,0]], [[1,2],[2,1]], matrix_multiply=[[[int]],[[int]]])

