############################################
# removeprefix
# removesuffix
# split
############################################


# remove prefix or suffix from a list of strings
############################################
websites = [
    "www.google.com",
    "www.facebook.com",
    "www.twitter.com",
    "www.instagram.com",
    "www.youtube.com",
]

for website in websites:
    print(website.removeprefix("www.").removesuffix(".com"))

# output removeprefix:
# google.com
# facebook.com
# twitter.com
# instagram.com
# youtube.com

# output removesuffix:
# www.google
# www.facebook
# www.twitter
# www.instagram
# www.youtube

# split a string at a certain character and put it into a list
############################################
string = "step 1: learn python"
new_string = string.split(":")
print(new_string)
