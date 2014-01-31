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
#player.start_thread

