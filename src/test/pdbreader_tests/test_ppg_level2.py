#!/usr/bin/env python
from pdbreader import System
import unittest, os

FILE = os.path.join(os.path.dirname(__file__), 'ppg.pdb')

class TestConcapsLevel1( unittest.TestCase ):
    def setUp(self):
        """ Default arguments used for program 
        equivalent of argparser in pdbreader """

        self.ch = S = System.read_protein_from_file ( FILE )

        for chain in self.ch:
            chain.connect_residues()
            for res in chain:
                res.gather_ready( c = True, level = 2 )
                res.gather_ready( r = True, level = 2 )

    def test_prolines_concaps_level1( self, ):
        """ At level 1 all concaps have 12 atoms"""
        for chain in self.ch:
            for res in chain:
                if res.res_name == "PRO":
                    if res.c_term:
                        continue
                    assert len( res.con ) == 12

    def test_concaps_level1( self, ):
        """ At level 1 all concaps have 12 atoms"""
        for chain in self.ch:
            for res in chain:
                if res.res_name != "PRO":
                    if res.c_term:
                        continue
                    assert len( res.con ) == 12

    def test_collagen_level_1( self, ):
        """ At level 2, assert how many atoms each concap and ready residue has.
        
        For ready made residues:
        For N-terminal, total = N-4
        For C-terminal, total = N-5

        Res | N
        --------
        PRO | 26
        HYP | 27
        GLY | 19
        ALA | 22

        """
        for chain in self.ch:
            for res in chain:
                if res.res_name == "PRO":
                    if res.n_term:
                        assert len( res.ready ) == 22
                    elif res.c_term:
                        assert len( res.ready ) == 21
                    else:
                        assert len( res.ready ) == 26
                elif res.res_name == "HYP":
                    assert len( res.ready ) == 27
                elif res.res_name == "GLY":
                    if res.c_term:
                        assert len( res.ready ) == 15
                    else:
                        assert len( res.ready ) == 19
                elif res.res_name == "ALA":
                    assert len( res.ready ) == 22

if __name__ == '__main__':
    unittest.main(  )