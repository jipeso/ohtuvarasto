import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_uudella_varastolla_negatiivinen_tilavuus(self):
        varasto = Varasto(-10)

        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_uudella_varastolla_negatiivinen_alku_saldo(self):
        varasto = Varasto(10, -10)

        self.assertAlmostEqual(varasto.saldo, 0)

    def test_negatiivisen_maaran_lisays(self):
        self.varasto.lisaa_varastoon(-10)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisaa_enemman_kuin_tilavuus(self):
        self.varasto.lisaa_varastoon(20)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_alku_saldo_suurempi_kuin_tilavuus(self):
        varasto = Varasto(10, 20)

        self.assertAlmostEqual(varasto.saldo, 10)

    def test_ota_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(-5)

        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_ota_enemman_kuin_saldo(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varasto_str(self):
        self.assertAlmostEqual(str(self.varasto), "saldo = 0, vielä tilaa 100")