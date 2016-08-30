require 'nokogiri'
require 'time'

class EvernoteBackup
    attr_accessor :filename, :line_number, :file, :note_current

    def initialize(filename=nil)
        @filename = filename
        @line_number = 0
        @file = File.open(filename) unless filename.nil?
    end

    def find_tag_line(tag_pattern)
        while not((line=@file.readline()).match(tag_pattern)) do 
            @line_number+=1
            break if @file.eof
            yield(line) if block_given?
        end
        line
    end

    def print_title(line)
        nok = Nokogiri::XML.fragment(line.strip())
        begin
            print(nok.children[0].children[0].children[0].to_s + '.'*20)
        rescue => e
            print('[no title tag]' + '.'*20)
        end
    end

    def print_modified_time(n_modified)
        time_updated = Time.parse(n_modified.children[0].to_s)
        puts( " :: " + time_updated.to_s)
    end

    def note_children(note, *names)
        names.map do |name|
            child = note.children.find{|n| n.name==name}
            raise "No child with name #{name} found" unless child
            child
        end
    end

    def parse_note_string(xml_fragment_string)
        nok    = Nokogiri::XML.fragment(xml_fragment_string)
        nok.children[0]
    end

    def extract_note_string(init_string='')
        note_string = init_string.strip()
        line = find_tag_line(/<\/note>/) do |line|
            note_string += line.strip()
        end
        note_string += line.strip()
        note_string
    end

    def next_note(file)
        note_string = nil
        line = find_tag_line(/^<note>/)
        return note_string if @file.eof

        # hoping that the line containing <note> will have title as well
        print_title(line)
        extract_note_string(line)
    end

    def self.parse(filename)
        eb = EvernoteBackup.new(filename)
        eb.parse()
    end

    def parse()
        in_notes = 0
        while(!@file.eof())
            note_string = next_note(file)
            break if note_string.nil?

            @n_note = parse_note_string(note_string)
            n_title, n_modified = note_children(@n_note, 'title', 'updated')
            print_modified_time(n_modified)

            in_notes += 1
            # break if in_notes>2
        end
    end
end

filename = '/Users/dragon/Documents/backup/evernote-musings-2015-12-10.enex'
EvernoteBackup.parse(filename)