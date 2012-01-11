function expect_char(f) {
    // I have no idea how this is going to work.
    // Some vim commands take a char argument, like *f*
    // We need to consume the next char the user types
}
function expect_line(f) {
    // Show a text field (somewhere) that the user can type in
    // When they press return/enter/esc, execute the command return
    // focus back to text view
}
function motion(func) {
   // func: function(idx, sel, info, rctx) -> idx
   Recipe.run(function(rctx)) {
      var idx = rctx.selection.last();
      var extra_info = {
         'line': rctx.rangeOfLinesInRange(Range(idx, 0)),
         'line_content': rctx.contentRangeOfLinesInRange(Range(idx, 0)),
      };
      
      var new_idx = func(idx, rctx.selection, extra_info, rctx);
      
      if (rctx.selection.is_singular())
         rctx.selection = Range(new_idx, 0);
      else if (new_idx < rctx.selection.location)
         rctx.selection = Range(new_idx, rctx.selection.location - new_idx);
      else
         rctx.selection = Range(rctx.selection.location, new_idx - rctx.selection.location);
   }
}


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

//! event vim.end-word: end_word
function end_word() { }
//! event vim.previous-word: previous_word
function previous_word() { }

//! event vim.next-WORD: next_WORD
function next_WORD() { }
//! event vim.end-WORD: end_WORD
function end_WORD() { }
//! event vim.previous-WORD: previous_WORD
function previous_WORD() { }

//! event vim.till: till
function till() { }
//! event vim.back-till: back_till
function back_till() { }

//! event vim.next-section: next_section
function next_section() { }
//! event vim.previous-section: previous_section
function previous_section() { }

//! event vim.begin-paragraph: begin_paragraph
function PARAGRAPH_REGEX() {
   return /\n[ \t]*\n\s*|^\t/gm;
}
function begin_paragraph() {
   motion(function(idx, sel, info, rctx) {
      if (idx == 0) {
         return 0;
      }
      
      var input = rctx.textInRange(Range(0, idx));
      var matches = PARAGRAPH_REGEX().exec(input);
      if (matches === null || matches === [])
         return 0;
      return matches[matches.length - 1].index;
   });
}
//! event vim.end-paragraph: end_paragraph
function end_paragraph() {
   motion(function(idx, sel, info, rctx) {
      idx += 1;
      if (idx == 0 || rctx.length() - idx <= 0) {
         return 0;
      }
      
      var input = rctx.textInRange(Range(idx, rctx.length() - idx));
      var matches = PARAGRAPH_REGEX().exec(input);
      if (matches === null || matches === [])
         return Range(0, rctx.length()).max();
      return matches[0].index;
   });
}


//! event vim.begin-sentence: begin_sentence
function SENTENCE_REGEX() {
   // We need to find the nearest space inbetween a sentence are 
   //   two newlines: \n[ \t]*\n\s*
   //   dot space: \.\s*
   return /\n[ \t]*\n\s*|\.\s*/g;
};
function begin_sentence() {
   motion(function(idx, sel, info, rctx) {
      if (idx == 0) {
         return 0;
      }
      
      var input = rctx.textInRange(Range(0, idx));
      var matches = SENTENCE_REGEX().exec(input);
      if (matches === null || matches === [])
         return 0;
      return matches[matches.length - 1].index;
   });
}
//! event vim.end-sentence: end_sentence
function end_sentence() {
   motion(function(idx, sel, info, rctx) {
      idx += 1;
      if (idx == 0 || rctx.length() - idx <= 0) {
         return 0;
      }
      
      var input = rctx.textInRange(Range(idx, rctx.length() - idx));
      var matches = SENTENCE_REGEX().exec(input);
      if (matches === null || matches === [])
         return Range(0, rctx.length()).max();
      return matches[0].index;
   });
}

//! event vim.find-char: find_char
function find_char() {
   expect_char(function(c) {   
      motion(function(idx, sel, info, rctx) {
         idx += 1;
         if (idx == 0 || rctx.length() - idx <= 0) {
            return 0;
         }
         
         var input = rctx.textInRange(Range(idx, rctx.length() - idx));
         var found_index = input.indexOf(c);
         if (found_index === -1) {
            return idx - 1;
         }
         return found_index;
      });
   });
}
//! event vim.find-char-backwards: find_char_backwards
function find_char_backwards() {
   expect_char(function(c) {   
      motion(function(idx, sel, info, rctx) {
         if (idx == 0) {
            return 0;
         }
         
         var input = rctx.textInRange(Range(0, idx));         
         var found_index = input.indexOf(c);
         if (found_index === -1) {
            return idx - 1;
         }
         return found_index;
      });
   });
}

//! event vim.document-start: document_start
function document_start() {
   motion(function(idx, sel, info, rctx) {
      return 0;
   });
}
//! event vim.document-end: document_end
function document_end() {
   motion(function(idx, sel, info, rctx) {
      if (rctx.length() == 0)
         return 0;
      return rctx.length() - 1;
   });
}

//! event vim.screen-top: screen_top
function screen_top() {
   motion(function(idx, sel, info, rctx) {
      return info.visible.location;
   });
}
//! event vim.screen-middle: screen_middle
function screen_middle() { /* this should be a remap */ }
//! event vim.screen-bottom: screen_bottom
function screen_bottom() {
   motion(function(idx, sel, info, rctx) {
      return info.visible.last();
   });
}

//! event vim.go-left: go_left
function go_left() {
   motion(function(idx, sel, info, rctx) {
      if (info.line.contains(idx - 1))
         return idx - 1;
      return idx;
   });
}
//! event vim.go-down: go_down
function go_down() { /* this should be a remap */ }
//! event vim.go-up: go_up
function go_up() { /* this should be a remap */ }
//! event vim.go-right: go_right
function go_right() {
   motion(function(idx, sel, info, rctx) {
      if (info.line.contains(idx + 1))
         return idx + 1;
      return idx;
   });
}

//! event vim.repeat-find-motion: repeat_find_motion
function repeat_find_motion() { }
//! event vim.reverse-find-motion: reverse_find_motion
function reverse_find_motion() { }

//! event vim.find-next: find_next
function find_next() { }
//! event vim.find-previous: find_previous
function find_previous() { }

//! event vim.regex: regex_forwards
function regex_forwards() { }
//! event vim.regex-backwards: regex_backwards
function regex_backwards() { }

//! event vim.go-to-mark: go_to_mark
function go_to_mark() { }
//! event vim.go-to-mark-beginning-of-line: go_to_mark_bol
function go_to_mark_bol() { }

//! event vim.next-ident: next_ident
function next_ident() { }
//! event vim.previous-ident: previous_ident
function previous_ident() { }

//! event vim.go-to-match: go_to_match
function go_to_match() { }

//! event vim.beginning-of-line-caret: beginning_of_line_caret
function beginning_of_line_caret() { }
//! event vim.beginning-of-line-zero: beginning_of_line_zero
function beginning_of_line_zero() { }
//! event vim.beginning-of-line-pipe: beginning_of_line_pipe
function beginning_of_line_pipe() { }
//! event vim.beginning-of-line-underscore: beginning_of_line_underscore
function beginning_of_line_underscore() { }

//! event vim.end-of-line: end_of_line
function end_of_line() {
   motion(function(idx, sel, info, rctx) {
      return info.line_content.last();
   });
}
//! event vim.next-line: next_line
function next_line() {
   motion(function(idx, sel, info, rctx) {
      return info.line.max();
   });
}

//! event vim.previous-line: previous_line
function previous_line() {
   motion(function(idx, sel, info, rctx) {
      if (info.line.location == 0) return 0;
      return rctx.rangeOfLinesInRange(Range(info.line.location - 1, 0)).location;
   });
}


//! event vim.record-macro: record_macro
function record_macro() {
   
}
//! event vim.change-to-eol: change_to_eol
function change_to_eol() {
   
   delete_to_eol();
   mode("insert");
}
//! event vim.delete-to-eol: delete_to_eol
function delete_to_eol() {
   
}
//! event vim.append-at-eol: append_at_eol
function append_at_eol() {
   
}
//! event vim.append: append_normal
function append_normal() {
   
}
//! event vim.sub-at-eol: sub_at_eol
function sub_at_eol() {
   
}
//! event vim.sub-character: sub_character
function sub_character() {
   
}
//! event vim.replace-mode: replace
function replace_mode() {
   mode("replace");
}
//! event vim.replace-character: replace_character
function replace_character() {
   expect_char(function(c) {
      // substitute the new character
   });
}

//! event vim.paste-before: paste_before
//! event vim.paste-after: paste_after
function paste_before() {
   
}
function paste_after() {
   
}

//! event vim.backspace: backspace
function backspace() {
   
}
//! event vim.delete-character: delete_character
function delete_character() {
   
}
//! event vim.insert-at-bol: insert_at_bol
function insert_at_bol() {
   
}
//! event vim.insert: insert_mode
function insert_mode() {
   mode("insert");
}

//! vim.newline-above: newline_above
function newline_above() {
   
}
//! vim.newline-below: newline_below
function newline_below() {
   
}
//! vim.visual-lines: visual_lines
function visual_lines() {
   
}
//! vim.visual: visual_mode
function visual_mode() {
   mode("visual");
}

//! vim.set-mark: set_mark
function set_mark() {
   
}
//! vim.repeat: repeat
function repeat() {
   
}
//! vim.extra-command: extra_command
function extra_command() {
   
}
//! vim.toggle-case: tOgGlE_cAsE
function tOgGlE_cAsE() {
   
}
//! vim.play-macro: play_macro
function play_macro() {
   
}
//! vim.repeat-extra: repeat_extra
function repeat_extra() {
   
}
//! vim.yank-line: yank_line
function yank_line() {
   
}


//! vim.filter: filter_op
function filter_op() {
   
}
//! vim.auto-format: auto_format
function auto_format() {
   
}
//! vim.yank: yank
function yank() {
   
}
//! vim.change: change
function change() {
   
}
//! vim.delete: delete
function delete() {
   
}
//! vim.unindent: unindent
function unindent() {
   
}
//! vim.indent: indent
function indent() {
   
}



