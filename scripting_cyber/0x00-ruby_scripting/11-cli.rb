require 'optparse'

TASKS_FILE = 'tasks.txt'

File.write(TASKS_FILE, '', mode: 'a') unless File.exist?(TASKS_FILE)

def add_task(task)
  File.open(TASKS_FILE, 'a') do |file|
    file.puts(task)
  end
  puts "Task '#{task}' added."
end

def list_tasks
  tasks = File.readlines(TASKS_FILE).map(&:strip)
  if tasks.empty?
    puts 'No tasks available.'
  else
    puts 'Tasks:' # Encabezado requerido
    tasks.each_with_index do |task, index|
      puts "#{index + 1}. #{task}"
    end
  end
end

def remove_task(index)
  tasks = File.readlines(TASKS_FILE).map(&:strip)
  if index < 1 || index > tasks.size
    puts 'Invalid index.'
    return
  end
  removed_task = tasks.delete_at(index - 1)
  File.write(TASKS_FILE, tasks.join("\n"))
  puts "Task '#{removed_task}' removed."
end

options = {}
OptionParser.new do |opts|
  opts.banner = 'Usage: cli.rb [options]'

  opts.on('-a', '--add TASK', 'Add a new task') do |task|
    options[:add] = task
  end

  opts.on('-l', '--list', 'List all tasks') do
    options[:list] = true
  end

  opts.on('-r', '--remove INDEX', Integer, 'Remove a task by index') do |index|
    options[:remove] = index
  end

  opts.on('-h', '--help', 'Show help') do
    puts opts
    exit
  end
end.parse!

if options[:add]
  add_task(options[:add])
elsif options[:list]
  list_tasks
elsif options[:remove]
  remove_task(options[:remove])
else
  puts 'Use -h or --help for available options.'
end
