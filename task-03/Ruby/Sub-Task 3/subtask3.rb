n = gets.to_i
(0...n).each { |i| puts " " * (n - i - 1) + "*" * (2 * i + 1) }
(n-2).downto(0) { |i| puts " " * (n - i - 1) + "*" * (2 * i + 1) }


