n = File.read('input.txt').to_i
File.open('output.txt', 'w') do |file|
  (0...n).each { |i| file.puts " " * (n - i - 1) + "*" * (2 * i + 1) }
  (n-2).downto(0) { |i| file.puts " " * (n - i - 1) + "*" * (2 * i + 1) }
end
