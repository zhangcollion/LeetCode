import  unittest
import numEnclave

class numEnclavesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = numEnclave.Solution()
        print("----------set up--------------")
    # def setUp(self):
    #     self.solution = numEnclave.Solution()
    #     print("----------set up--------------")

    def test_numEnclaves1(self):

        ans = self.solution.numEnclaves(grid=[[0,0,0,1,1,1,0,1,0,0],
            [1,1,0,0,0,1,0,1,1,1],
            [0,0,0,1,1,1,0,1,0,0],
            [0,1,1,0,0,0,1,0,1,0],
            [0,1,1,1,1,1,0,0,1,0],
            [0,0,1,0,1,1,1,1,0,1]])
        self.assertEqual(ans, 3)

        ans = self.solution.numEnclaves(grid=[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])
        self.assertEqual(ans, 3)
        print("----------test_numEnclaves1 test ok---------")

    def test_num(self):

        ans = self.solution.numEnclaves(grid=[[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]])
        self.assertEqual(ans, 3)
        print("----------test_num test ok---------")

    # def tearDown(self):
    #     print("----------test done-----------")
    @classmethod
    def tearDownClass(cls) :
        print("----------test done-----------")


if __name__=="__main__":
    unittest.main()