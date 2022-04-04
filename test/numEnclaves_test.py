import  unittest
import numEnclave

class numEnclavesTest(unittest.TestCase):
    def test_numEnclaves(self):
        solution = numEnclave.Solution()
        ans = solution.numEnclaves(grid=[[0,0,0,1,1,1,0,1,0,0],
            [1,1,0,0,0,1,0,1,1,1],
            [0,0,0,1,1,1,0,1,0,0],
            [0,1,1,0,0,0,1,0,1,0],
            [0,1,1,1,1,1,0,0,1,0],
            [0,0,1,0,1,1,1,1,0,1]])
        self.assertEqual(ans, 3)




if __name__=="__main__":
    unittest.main()