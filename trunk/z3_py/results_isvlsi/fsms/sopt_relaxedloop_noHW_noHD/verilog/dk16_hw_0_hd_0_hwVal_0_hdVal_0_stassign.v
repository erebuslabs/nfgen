	parameter  st_state_14 =  5'b00000;
	parameter  st_state_12 =  5'b00001;
	parameter  st_state_27 =  5'b00010;
	parameter  st_state_9 =  5'b00011;
	parameter  st_state_4 =  5'b00100;
	parameter  st_state_7 =  5'b00101;
	parameter  st_state_13 =  5'b00110;
	parameter  st_state_18 =  5'b00111;
	parameter  st_state_19 =  5'b01000;
	parameter  st_state_3 =  5'b01001;
	parameter  st_state_22 =  5'b01010;
	parameter  st_state_8 =  5'b01011;
	parameter  st_state_6 =  5'b01100;
	parameter  st_state_20 =  5'b01101;
	parameter  st_state_26 =  5'b01110;
	parameter  st_state_24 =  5'b01111;
	parameter  st_state_5 =  5'b10000;
	parameter  st_state_2 =  5'b10001;
	parameter  st_state_10 =  5'b10010;
	parameter  st_state_17 =  5'b10011;
	parameter  st_state_1 =  5'b10100;
	parameter  st_state_25 =  5'b10101;
	parameter  st_state_11 =  5'b10110;
	parameter  st_state_23 =  5'b10111;
	parameter  st_state_16 =  5'b11000;
	parameter  st_state_21 =  5'b11001;
	parameter  st_state_15 =  5'b11010;
	reg[4:0] State;
	reg[4:0] NextState;
