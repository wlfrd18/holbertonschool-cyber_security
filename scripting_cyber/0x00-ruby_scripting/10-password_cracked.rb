#!/usr/bin/env ruby

require 'digest'

if ARGV.length != 2
  puts 'Usage: 10-password_cracked.rb HASHED_PASSWORD DICTIONARY_FILE'
  exit
end

hashed_password = ARGV[0]
dictionary_file = ARGV[1]
password_found = false

File.readlines(dictionary_file).each do |word|
  password = word.chomp
  hashed_word = Digest::SHA256.hexdigest(password)

  if hashed_word == hashed_password
    puts "Password found: #{password}"
    password_found = true
    break
  end
end

puts 'Password not found in dictionary.' unless password_found
