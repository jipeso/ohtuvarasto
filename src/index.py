from varasto import Varasto


def main():
    mehua, olutta = Varasto(100.0), Varasto(100.0, 20.2)

    print(
        f"Luonnin jälkeen:"
        f"\nMehuvarasto: {mehua}"
        f"\nOlutvarasto: {olutta}"
        f"\nOlut getterit:"
        f"\nsaldo = {olutta.saldo}"
        f"\ntilavuus = {olutta.tilavuus}"
        f"\npaljonko_mahtuu = {olutta.paljonko_mahtuu()}"
        f"\nMehu setterit:"
        f"\nLisätään 50.7"
    )
    mehua.lisaa_varastoon(50.7)
    print(
        f"Mehuvarasto: {mehua}"
        f"\nOtetaan 3.14"
    )
    mehua.ota_varastosta(3.14)
    print(
        f"Mehuvarasto: {mehua}"
        f"\nVirhetilanteita:"
        "\nVarasto(-100.0)"
    )
    huono1, huono2 = Varasto(-100.0), Varasto(100.0, -50.7)
    print(
        f"{huono1}"
        "\nVarasto(100.0, -50.7)"
        f"\n{huono2}"
        f"\nOlutvarasto: {olutta}"
        "\nolutta.lisaa_varastoon(1000.0)"
    )
    olutta.lisaa_varastoon(1000.0)
    mehua.lisaa_varastoon(-666.0)
    print(
        f"Olutvarasto: {olutta}"
        f"\nMehuvarasto: {mehua}"
        "\nmehua.lisaa_varastoon(-666.0)"
        f"\nMehuvarasto: {mehua}"
        f"\nOlutvarasto: {olutta}"
        "\nolutta.ota_varastosta(1000.0)"
    )

    saatiin_olutta, saatiin_mehua = olutta.ota_varastosta(1000.0),\
                                    mehua.ota_varastosta(-32.9)

    print(
        f"saatiin {saatiin_olutta}"
        f"\nOlutvarasto: {olutta}"
        f"\nMehuvarasto: {mehua}"
        "\nmehua.otaVarastosta(-32.9)"
        f"saatiin {saatiin_mehua}"
        f"\nMehuvarasto: {mehua}"
    )
if __name__ == "__main__":
    main()
