#!/usr/bin/env ruby
# A regular expression that is matches the hbtn pattern
puts ARGV[0].scan(/hbt{2,5}n/).join
