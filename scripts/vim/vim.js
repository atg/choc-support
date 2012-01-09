//! event vim.next-word: next_word
function next_word() {
   Recipe.run(function(rctx) {
      var sel = rctx.selection;
      // What type of character are we on? Alpha/Symbol/Whitespace
      if (sel.max() >= rctx.length)
         return;
      var c = rctx.textInRange(Range(sel.last(), 1));
      var is_space = /\s+/.test(c);
      var is_char = /[\w\d]+/.test(c);
      var is_symbol = !(is_space || is_char);
      
      // Search forward for the next character not of that type (and not whitespace)
      var r = null;
      if (is_char) r = /\s[^\s]/;
      else if (is_space) r = /[^\s]/;
      else if (is_symbol) r = /[\w\d]|\s[^\w\d\s]/;
      
   });
}
