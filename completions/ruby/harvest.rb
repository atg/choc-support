require 'rubygems'
require 'json'

require 'core'
require 'stdlib'

def write name , data
  File.open("#{name}.json" , 'w') do |f|
    f.puts data.to_json
  end
end

CORE = CORE.map {|x| x.gsub(/^C|M/,"") }

struct = {}
#struct['snippet'] = "$$%{0}"

struct['icon']  = 'class'
struct['items'] = CORE + STDLIB

write 'classes', struct

struct['icon']  = 'method'
struct['items'] = CORE+STDLIB.map(&:methods).flatten.sort.uniq.reject {|i| i.chars.to_a.last == '=' }

write 'methods', struct

struct['icon']  = 'function'
struct['items'] = Kernel.methods.sort

write 'functions', struct