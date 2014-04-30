import dbus
import subprocess
import time

update_time = 3 #The time to wait between checks

global current_track
current_track = ""

def update():
    bus = dbus.SessionBus()
    player = bus.get_object('com.spotify.qt', '/')
    iface = dbus.Interface(player, 'org.freedesktop.MediaPlayer2')
    info = iface.GetMetadata()
    # OUT: [dbus.String(u'xesam:album'), dbus.String(u'xesam:title'), dbus.String(u'xesam:trackNumber'), dbus.String(u'xesam:artist'), dbus.String(u'xesam:discNumber'), dbus.String(u'mpris:trackid'), dbus.String(u'mpris:length'), dbus.String(u'mpris:artUrl'), dbus.String(u'xesam:autoRating'), dbus.String(u'xesam:contentCreated'), dbus.String(u'xesam:url')]
    return "Title: \t\t" + str(info['xesam:title'])+"\nArtist: \t\t" + str(info['xesam:artist'][0]) + "\nAlbum: \t" +  str(info['xesam:album'])


def notify():
    global current_track
    track_now = update()
    if track_now != current_track:
        current_track = track_now
        subprocess.Popen(['notify-send', update()])

while True:
    notify()
    time.sleep(update_time)
    


