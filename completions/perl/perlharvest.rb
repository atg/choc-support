require 'open-uri'
require 'rubygems'
require 'json'
# so this script is probably terrible but I know nothing about
# ruby so piss off!

the_functions 	= []

page_contents = open('http://perldoc.perl.org/index-functions.html') do |f|
	f.each do |line|
		if line.strip.start_with? '<li><a href="functions/'
			item_name = line.match(/>([^<]+)/)[1]
			if item_name
				the_functions.push(item_name)
			end
		end
	end
end

# do the stupid functions...
the_functions_h = {}
the_functions_h['icon']    = "function"
the_functions_h['snippet'] = "$$%{0}"
the_functions_h['items']   = the_functions

File.open('functions.json', 'w') do |f2|
	f2.puts the_functions_h.to_json
end