import mpdclient2
m = mpdclient2.connect()

print m.status() # -> prints status object

outputs = m.outputs()

print 'i got %d output(s)' % len(outputs)

for output in outputs:
    print "here's an output"
    print "  id:", output.outputid
    print "  name:", output.outputname
    print "  enabled:", ('no', 'yes')[int(output.outputenabled)]

######

print "let's find some beck songs"

beck_songs = m.find("artist", "beck")

print 'i got %d beck song(s)' % len(beck_songs)

if len(beck_songs) > 5:
    print ".. but let's just look at the first 5"

for i, song in enumerate(beck_songs[:5]):
    print "%4d. %s -- %s" % (i+1, song.album, song.title)


print m.currentsong()

m.find('foo', 'bar')
print m.talker.ack

