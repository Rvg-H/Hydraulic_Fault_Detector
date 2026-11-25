import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_hydraulic_fault(dut):

    dut._log.info("DETECTOR DE FALLAS HIDRAULICAS")

    # Inicializacion
    dut.ena.value = 1
    dut.clk.value = 0
    dut.rst_n.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    await Timer(1, unit="us")

    # Entrada, salida esperada y descripcion
    pruebas = [
        (0b0000, 0b0000, "Normal"),
        (0b0001, 0b1100, "Presion baja"),
        (0b0010, 0b0000, "Presion alta"),
        (0b0011, 0b1000, "Error de presion"),
        (0b0100, 0b0000, "Caudal bajo"),
        (0b0101, 0b1100, "Presion y caudal bajos"),
        (0b0110, 0b1010, "Obstruccion"),
        (0b0111, 0b1000, "Error de presion"),
        (0b1000, 0b0000, "Caudal alto"),
        (0b1001, 0b1101, "Posible fuga"),
        (0b1010, 0b0000, "Presion y caudal altos"),
        (0b1011, 0b1000, "Error de presion"),
        (0b1100, 0b1000, "Error de caudal"),
        (0b1101, 0b1000, "Error de caudal"),
        (0b1110, 0b1000, "Error de caudal"),
        (0b1111, 0b1000, "Entradas contradictorias"),
    ]

    for entrada, esperado, descripcion in pruebas:

        dut.ui_in.value = entrada

        await Timer(1, unit="us")

        resultado = int(dut.uo_out.value)

        assert resultado == esperado, (
            f"ERROR: {descripcion} | "
            f"Esperado: {esperado:04b} | "
            f"Obtenido: {resultado:04b}"
        )

        assert int(dut.uio_out.value) == 0
        assert int(dut.uio_oe.value) == 0

        dut._log.info(
            f"CORRECTO: {descripcion} | "
            f"Entrada: {entrada:04b} | "
            f"Salida: {resultado:04b}"
        )

    dut._log.info("16 DE 16 PRUEBAS SUPERADAS")
