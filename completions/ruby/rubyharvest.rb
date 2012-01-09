require 'rubygems'
require 'json'

require 'core'
require 'stdlib'

def write name , data
  File.open("#{name}.json" , 'w') do |f|
    f.puts data.to_json
  end
end

CORE = CORE.map {|x| x.gsub(/^(C|M)/,"") }

struct = {}

struct['icon']  = 'class'
struct['items'] = CORE # (CORE + STDLIB)

write 'classes', struct

struct['icon']  = 'method'
struct['prefix']  = '.'
struct['items'] = CORE.map(&:methods).flatten.sort.uniq # CORE+STDLIB.map(&:methods).flatten.sort.uniq

write 'methods', struct

struct['icon']  = 'function'
struct['items'] = Kernel.methods.sort

write 'functions', struct