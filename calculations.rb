#!/usr/bin/ruby

class Parser
def parser(expression)
    expression = expression.split
    operands = []
    result = []

    expression.each do |x|
      case x
        when /\d+/
          result.push(x.to_f)
        when  "+", "-", "*", "/"
          operands = result.pop(2)
          result.push(operands[0].send(x, operands[1]))
      end
    end
    result
  end
end

if __FILE__ == $0
  parser = Parser.new
  #puts ARGV
  puts parser.parser(ARGV[0])
end