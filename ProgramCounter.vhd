----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 		 Cristian David Gutierrez Osorio - Ronald Felipe Gonzalez
-- 
-- Create Date:    16:41:41 03/21/2017 
-- Design Name: 
-- Module Name:    ProgramCounter - Behavioral 
-- Project Name: 
-- Target Devices: 
-- Tool versions: 
-- Description: 
--
-- Dependencies: 
--
-- Revision: 
-- Revision 0.01 - File Created
-- Additional Comments: 
--
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity ProgramCounter is
    Port ( clk : in  STD_LOGIC;
           rst : in  STD_LOGIC;
           pc_in : in  STD_LOGIC_VECTOR (31 downto 0);
           pc_out : out  STD_LOGIC_VECTOR (31 downto 0));
end ProgramCounter;

architecture Behavioral of ProgramCounter is

begin

process (clk, rst, pc_in)
	begin
		if (rst = '1') then
			pc_out <= (others => '0');
		else
			if(rising_edge(clk)) then
				pc_out <= pc_in;
			end if;
		end if;
end process;

end Behavioral;

