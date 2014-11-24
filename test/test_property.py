import unittest, os
import numpy as np

from molecules import Cluster, Property, Water, Rotator
from template import Template

FILE = os.path.join( os.path.dirname(__file__), 'tip3p44_10qm.mol' )

class WaterTest( unittest.TestCase ):
    def setUp(self):
        self.c = Cluster.get_water_cluster(
                FILE,
                in_AA = False,
                out_AA = False,
                N_waters = 10)
        

    def test_size(self):
        c = Cluster.get_water_cluster(
                FILE,
                in_AA = False,
                out_AA = False,
                N_waters = 10)

# Read in distributed properties, transform to atomic sites from waters euler angles
        for wat in c:
            t1, t2, t3  = wat.get_euler()
            kwargs_dict = Template().get( *("TIP3P", "HF", "ANOPVDZ",
                True , "0.0" ))
            for at in wat:
                Property.add_prop_from_template( at, kwargs_dict )
                at.Property.transform_ut_properties( t1, t2 ,t3)

# Read in the properties for the oxygen atom, the projected dipole vector should
# be the same
        for wat in c:
            q = np.zeros( (1, ) )
            d = np.zeros( (3, ) )
            a = np.zeros( (3,3, ) )
            b = np.zeros( (3,3,3, ) )

            kwargs_dict = Template().get( *("TIP3P", "HF", "ANOPVDZ",
                False , "0.0" ))
            d_ref = kwargs_dict[('O1','dipole')]
            b_ref = Rotator.ut_3_square( kwargs_dict[('O1','beta')] )
            for at in wat:
                q += at.Property["charge"]
                d += at.Property["dipole"] + at.Property["charge"] * at.r
                a += Rotator.ut_2_square( at.Property["alpha"] )
                b += Rotator.ut_3_square( at.Property["beta"] )

            self.eq( q, 0.0 )
            self.eq( np.dot( np.einsum('iij->j',b), d)/np.linalg.norm(d), 
                    np.dot( np.einsum('iij->j',b_ref),d_ref)/np.linalg.norm(d_ref) )

    def test_tensor_to_ut(self):
        t = np.zeros( (3, 6) )
        self.eq( t, np.zeros( ( 3, 6, )) )
#xxx component
        t[0,0] = -3.0
#yyy component
        t[1,3] = 0.25
#zzz component
        t[2,5] = 5.0

#xxy component
        t[0,1] = 3.5
        t[1,0] = 4.5

#xxz component
        t[0,2] = 2.0
        t[2,0] = 3.0

#xyy component
        t[0,3] = -2.0

#xyz component
        t[0,4] = 1.0
        t[1,2] = 3.0
        t[2,1] = 8.0
        t[1,1] = 2.0
#xzz component
        t[0,5] = 2.0
        t[2,2] = -1.0
#yyz component
        t[1,4] = 3.5
        t[2,3] = 7.5
#yzz component
        t[1,5] = -4.0
        t[2,4] = -6.0

# AFTER TRANSFORMAATION

        square = Rotator.tensor_to_ut( t )

#xxx, one permutations, -3.0
        self.eq( square[0], -3.0 )
#xxy, two permutations, 3.5 and 4.5 should be 3.0
        self.eq( square[1], 4.0 )
#xxz, two permutations, 2.0 and 3.0 should be 2.5
        self.eq( square[2], 2.5 )
#xyy, two permutations, -2.0 and 2.0 should be 0
        self.eq( square[3], 0.0 )
#xyz, three permutations, 1.0 and 3.0  and 8.0 should be 4.0
        self.eq( square[4], 4.0 )
#xzz, two permutations, 2.0 and -1.0 should be 0.5
        self.eq( square[5], 0.5 )
#yyy, one permutations, 0.25
        self.eq( square[6], 0.25 )
#yyz, two permutations, 3.5 and 7.5, should be 5.5
        self.eq( square[7], 5.5 )
#yzz, two permutations, -4.0 and -6.0, should be -5.0
        self.eq( square[8], -5.0 )
#zzz, one permutations, 5.0
        self.eq( square[9], 5.0 )

    def eq(self, a, b,):
        np.testing.assert_almost_equal( a, b, decimal = 2 )



if __name__ == '__main__':
    unittest.main()
