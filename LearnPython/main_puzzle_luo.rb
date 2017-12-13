############################################################
#
#  Name:        Zhaowen Luo (Jack)
#  Assignment:  Puzzle
#  Date:        2/24/17
#  Class:       CIS 283
#  Description: Puzzle
#
############################################################


require_relative 'puzzle_luo.rb'
require "prawn"


puz = Puzzle.new(45, "words.txt")
puz.solve

puzstring = puz.to_s

finishpuz = puz.fill_puzzle

Prawn::Document.generate("jackpuzzle.pdf") do

  font "Courier" , :size => 24
  text "Word Search" , :align => :center
  font "Courier" , :size => 10

  text finishpuz, :character_spacing => 4.9 , :align => :center
  text " "
  text "Find the following #{puz.how_many_words} words", :align => :center


  text " "
  text " "
  column_box([0, cursor], :columns => 3, :width => bounds.width) do
    text puz.print_words, :align => :center
  end




  start_new_page

  font "Courier" , :size => 24
  text "Word Search Key" , :align => :center
  font "Courier" , :size => 10
  text puzstring, :character_spacing => 4.9 , :align => :center


end





