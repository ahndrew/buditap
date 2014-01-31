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


def get_theme(theme_name)
  dir = "./audio/" + theme_name
  files = Dir.foreach(dir).select do |x| 
    File.file?("#{dir}/#{x}") 
  end
  return files
end

@current_theme = get_theme("beer")

player.load(@current_theme.random)
