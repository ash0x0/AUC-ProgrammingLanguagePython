import re

# As I'm submitting this I'm realizing there are more comments than code here. I may have gone overboard.

# open file read only
file = open("input.txt", 'r')
# read the entire file, don't like this but it's the best thing to close right away
lines = file.read()
# close file
file.close()
vowels = "aeiou"
# translate from vowels to dashes.
# len(vowels)*'-' is too scary but I trust this to be correct more than I trust my ability at the moment
# to count five letters.
lines = lines.translate(lines.maketrans(vowels, len(vowels) * '-'))
# this is a weird line but it's  because I don't want to index my slices
# later on output, I'd rather use lines because it's the reference which has fixed length
output = lines
# find the pattern that matches a paragraph, .* by default matches all except newline.
# for this match to work DOTALL flag must be default
match = re.search(r"\n\n.*\n\n", lines)
# if the match isn't found then it could mean the second paragraph precedes EOF
if match is None:
    # handle an edge case where the second paragraph is preceding EOF by
    # matching a paragraph with no subsequent newlines
    match = re.search(r"\n\n.*", lines)
# if neither matches then there is no second paragraph and no need to do any further manipulation
if match is not None:
    # slice the string to the the second paragraph first from the beginning of match +2 to the end of match
    # then the first paragraph from the beginning of file to beginning of match +2
    # then the remainder of file starting at the end of match
    # the +2 is for the "\n\n"
    output = lines[match.start()+2:match.end()] + lines[0:match.start()+2] + lines[match.end():]
# there is an edge case here where it's only one paragraph, no need to do anything there
# print the output
print(output)
