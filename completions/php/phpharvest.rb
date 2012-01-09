require 'open-uri'
require 'rubygems'
require 'json'
# so this script is probably terrible but I know nothing about
# ruby so piss off!

the_classes 		= []
the_functions 	= []
the_others			= []

page_contents = open('http://php.net/quickref.php') do |f|
	f.each do |line|
		if line.start_with? '<li><a href="/manual/en/'
			item_name = line.match(/>([^<]+)/)[1]
			if line.include? "en/class" and item_name
				the_classes.push(item_name)
			elsif line.include? "en/function" and item_name
				the_functions.push(item_name)
			elsif item_name
				the_others.push(item_name)
			end
		end
	end
end

# do the stupid classes...
the_classes_h = {}
the_classes_h['icon']    = "class"
the_classes_h['snippet'] = "$$%{0}"
the_classes_h['items']   = the_classes
	
File.open('classes.json', 'w') do |f1|
	f1.puts the_classes_h.to_json
end

# do the stupid classes...
the_functions_h = {}
the_functions_h['icon']    = "function"
the_functions_h['snippet'] = "$$%{0}"
the_functions_h['items']   = the_functions

File.open('functions.json', 'w') do |f2|
	f2.puts the_functions_h.to_json
end