import unittest
import libpysal
import geopandas as gpd
import numpy as np
from segregation.aspatial import SimpsonsInteraction


class Simpsons_Interaction_Tester(unittest.TestCase):
    def test_Simpsons_Interaction(self):
        s_map = gpd.read_file(libpysal.examples.get_path("sacramentot2.shp"))
        groups_list = ['WHITE_', 'BLACK_', 'ASIAN_','HISP_']
        df = s_map[groups_list]
        index = SimpsonsInteraction(df, groups_list)
        np.testing.assert_almost_equal(index.statistic, 0.508175868480421)


if __name__ == '__main__':
    unittest.main()