from unittest import TestCase
from RabinKarp.hash_substring import RabinKarp
import time


class TestRabinKarp(TestCase):
    def test_find_occurrences_1(self):
        rk = RabinKarp("aba", "abacaba")
        occurrences = rk.find_occurrences()
        self.assertEqual(occurrences, [0,4])

    def test_find_occurrences_2(self):
        rk = RabinKarp("Test", "testTesttesT")
        occurrences = rk.find_occurrences()
        self.assertEqual(occurrences, [4])

    def test_find_occurrences_3(self):
        rk = RabinKarp("aaaaa", "baaaaaaa")
        occurrences = rk.find_occurrences()
        self.assertEqual(occurrences, [1, 2, 3])

    def test_find_occurrences_4(self):
        pattern = "lNoYhXmlwOscxnkTWjsyNJNhgvzMFbxFnbiWuBAGjZQlCRQHjTUX"
        text = "ZtonpqnFzlpvUKZrBbRlNoYhXmlwOscxnkTWjsyNJNhgvzMFbxFnbiWuBAGjZQlCRQHjTUXxtHmTxoLuMbRYsvSpxhtr" \
               "lvABBlFYmndFzHypOmJyFxjHEPlNoYhXmlwOscxnkTWjsyNJNhgvzMFbxFnbiWuBAGjZQlCRQHjTUXbDiEAvtPlNoYhXml" \
               "wOscxnkTWjsyNJNhgvzMFbxFnbiWuBAGjZQlCRQHjTUXRRNoBCUMQVOlNoYhXmlwOscxnkTWjsyNJNhgvzMFbxFnbiWuBA" \
               "GjZQlCRQHjTUXRLKlNoYhXmlwOscxnkTWjsyNJNhgvzMFbxFnbiWuBAGjZQlCRQHjTUXAYPDKWtVpShhclNoYhXmlwOscxn" \
               "kTWjsyNJNhgvzMFbxFnbiWuBAGjZQlCRQHjTUXOJlUlNoYhXmlwOscxnkTWjsyNJNhgvzMFbxFnbiWuBAGjZQlCRQHjTUXg" \
               "lmlNoYhXmlwOscxnkTWjsyNJNhgvzMFbxFnbiWuBAGjZQlCRQHjTUXuaOibGlVrwghvNTgLfltIbEdBlgjelFjQkBeFrdEV "
        rk = RabinKarp(pattern, text)
        occurrences = rk.find_occurrences()
        self.assertEqual(occurrences, [19, 118, 178, 241, 296, 361, 417, 472])

    def test_find_occurrences_5(self):
        pattern = 'abababababababababababababababababababababababababababababababab'
        text = ''.join('ababa' for _ in range(50000))
        str = time.time()
        rk = RabinKarp(pattern, text)
        occurrences = rk.find_occurrences()
        print(time.time() - str)
        self.assertEqual(occurrences, [])

    def test_find_occurrences_6(self):
        pattern = 'Lorem'
        text = "LoremipsumdolorsitametconsecteturadipiscingelitEtiamquisrhoncusleoAliquameratvolutpatUtfringillaleoeutellusgravidablanditAeneanidduialiquamaliquamvelitacmolestiefelisNullasednequerhoncussemfeugiatvestibulumsedsitametvelitUtjustotortortemporsitamettempusidconguealacusUtsuscipitultriciesvestibulumNuncloremsapiendictumsedsemperacvariusaelitVivamusnonleoatleomolestievulputatesediderosSuspendissesempernisisedexposueremattisInegettortoretnullasuscipitplacerategetsitametnislNamlobortismaurissitametsuscipitcommodoliberoarcueuismodnullaeuelementumarcufeliseuipsumFusceelementumegetodioegetconsecteturPraesentultriciesdolordoloregetmattistortorporttitorvelUtconsequatnequeanullamolestieconvallisAliquamluctusexurnaapellentesquemetusefficitursedSedrhoncusmauriselementumelitlaciniasitametpretiumauguerhoncusNullavelitrisusmaximussedmaximusutfacilisisvelloremQuisqueullamcorperurnauteratmollisinlobortismaurispharetraDonecvehiculanislnecplaceratsagittisDuissitametnuncornaremaurisrutrumfeugiatsitametetdolorVestibulumdiamerosegestasquisauguetinciduntaliquetconvallisligulaQuisquenonduisollicitudintellusaliquetplaceratProinetloremegestastellusfacilisisvariusinatloremMaecenasmaurisanteconsequatquisconsectetursedsemperpulvinaraugueDonecnonlacinialigulaQuisqueiaculisexaeleifendelementumodioleoconguesapieneuornareerattellussitametorciEtiamvehiculaaugueexnontristiquemassasollicitudinetIninterdumultriciesnullaactinciduntPellentesqueetmiturpisPraesentquisnibherosVestibulumcommodogravidamagnaatinciduntrisussuscipitinPellentesquehabitantmorbitristiquesenectusetnetusetmalesuadafamesacturpisegestasCrasacornaretellusInaligulanecdiambibendumsagittisatnonlectusInornareconsequaturnasedpellentesqueNullasedorcierosFusceegetmagnadolorPraesentsodalesnullanecelementumegestasmagnalacusmalesuadaelitidullamcorperrisusexvestibulumturpisMaurispellentesquenisiegettelluscommodovehiculaCurabiturpulvinarscelerisquelobortisDonecpretiumfelisidultriciesauctorSeddignissimliberovelmagnadapibusiaculisetatdiamNullanonanteerosVestibulumsollicitudinmetusinsapiencondimentumplaceratPellentesqueposueretortorsedsodalestempusFusceascelerisquetellusVestibulumanteipsumprimisinfaucibusorciluctusetultricesposuerecubiliaCuraeNamsitamethendreritloremEtiamliberonisiefficiturvelodiomaximusultricieseuismodligulaFuscenecaccumsanerosEtiamlaciniabibendumduieufacilisislectusSedorcilectusmalesuadaeuodiononcondimentummalesuadalacusInhachabitasseplateadictumstCurabiturtempusscelerisqueleoullamcorperegestasnullaimperdietegetLoremipsumdolorsitametconsecteturadipiscingelitNullafacilisiClassaptenttacitisociosquadlitoratorquentperconubianostraperinceptoshimenaeo"
        str = time.time()
        rk = RabinKarp(pattern, text)
        occurrences = rk.find_occurrences()
        print(time.time() - str)
        self.assertEqual(occurrences, [0, 2486])


