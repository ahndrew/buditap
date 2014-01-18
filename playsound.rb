require 'audite'

player = Audite.new

player.events.on(:complete) do
    puts "COMPLETE"
end

player.events.on(:position_change) do |pos|
    puts "POSITION: #{pos} seconds  level #{player.level}"
end

puts "Load song"

player.load('budligt_real_chinese.mp3')
player.toggle
player.start_thread

=begin
  
// Pseudo NodeJS-style scripting -- Choosing a Theme

  var fs = require(‘fs’);  // module that reads local files

  /*  Returns an array of filenames
  *   @param {string}  themeName
  *   @return {array}  array of file names 
  */
  function getTheme(themeName) {
    var themeFolder = ‘./audio/’ + _theme;
    return fs.readdirSync(themeFolder);
  }

  // Returns a random integer between min and max
  function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
  }

  var currentTheme = getTheme('beer');
  var random =  getRandomInt(0,currentTheme.length);

  player.load(currentTheme[random]);
 
=end