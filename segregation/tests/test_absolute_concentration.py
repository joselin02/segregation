import unittest
import libpysal
import geopandas as gpd
import numpy as np
from segregation.spatial import AbsoluteConcentration


class Absolute_Concentration_Tester(unittest.TestCase):
    def test_Absolute_Concentration(self):
        s_map = gpd.read_file(libpysal.examples.get_path("sacramentot2.shp"))
        df = s_map[['geometry', 'HISP_', 'TOT_POP']]
        index = AbsoluteConcentration(df, 'HISP_', 'TOT_POP')
        np.testing.assert_almost_equal(index.statistic, 0.21492220758219194)


if __name__ == '__main__':
    unittest.main()
