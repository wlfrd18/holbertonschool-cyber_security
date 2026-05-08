require 'net/http'
require 'json'

def get_request(url)
  uri = URI(url)
  response = Net::HTTP.get_response(uri)

  puts "Response status: #{response.code} #{response.message}"

  if response.is_a?(Net::HTTPSuccess)
    begin
      json_body = JSON.pretty_generate(JSON.parse(response.body))
      puts "Response body:\n#{json_body}"
    rescue JSON::ParserError
      puts "Response body:\n{\n}"
    end
  else
    puts "Response body:\n{\n}"
  end
end
