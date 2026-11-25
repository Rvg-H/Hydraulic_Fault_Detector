`default_nettype none

module tt_um_hydraulic_fault (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire ena,
    input  wire clk,
    input  wire rst_n
);

    // Entradas
    wire presion_baja = ui_in[0];
    wire presion_alta = ui_in[1];
    wire caudal_bajo  = ui_in[2];
    wire caudal_alto  = ui_in[3];

    // Validacion de entradas
    wire error_entrada;

    assign error_entrada =
        (presion_baja & presion_alta) |
        (caudal_bajo & caudal_alto);

    // Deteccion de fallas
    wire fuga;
    wire obstruccion;
    wire baja_presion;
    wire alarma;

    assign fuga =
        presion_baja & caudal_alto & ~error_entrada;

    assign obstruccion =
        presion_alta & caudal_bajo & ~error_entrada;

    assign baja_presion =
        presion_baja & ~error_entrada;

    assign alarma =
        fuga | obstruccion | baja_presion | error_entrada;

    // Salidas
    assign uo_out[0] = fuga;
    assign uo_out[1] = obstruccion;
    assign uo_out[2] = baja_presion;
    assign uo_out[3] = alarma;

    // Pines no utilizados
    assign uo_out[7:4] = 4'b0000;
    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    wire _unused = &{ena, clk, rst_n,
                     ui_in[7:4], uio_in, 1'b0};

endmodule
