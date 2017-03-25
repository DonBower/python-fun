bacon_type = 'crispy' 

2.times do
    puts bacon_type
    temperature = 300 
end

puts Math::PI

prices = { oscar: 4.55, boars: 5.23, wright: 4.65, beelers: 6.99 }
puts prices[:oscar] #=> 4.55 
puts prices[:boars] #=> 5.23

prices[:oscar] = 1.00 
puts prices.values #=> [4.55, 5.23, 4.65, 6.99] 