"""
desk_switch: A lightweight Python utility that lives in your Windows system tray
and lets you swap between virtual desktops with a single click.
"""
import pystray
from PIL import Image, ImageDraw
from pyvda import VirtualDesktop, get_virtual_desktops


def create_image(color1=(64, 128, 255), color2=(255, 255, 255)):
    """
    Generate a 64×64 tray icon with two horizontal bars representing desktops.

    :param color1: Background color tuple (R, G, B).
    :param color2: Bar color tuple (R, G, B).
    :return: PIL.Image object for the tray icon.
    """
    width = 64
    height = 64

    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle([12, 12, 52, 28], fill=color2)
    dc.rectangle([12, 36, 52, 52], fill=color2)
    return image


def get_current_desktop_number():
    """
    Retrieve the index of the currently active virtual desktop.

    :return: Integer index of the current desktop (1-based).
    """
    vds = get_virtual_desktops()
    current_vd = VirtualDesktop.current()
    for i, vd in enumerate(vds, start=1):
        if vd.id == current_vd.id:
            return i
    return 1

def go_to_desktop_number(nr):
    """
    Get the matching virtual desktop
    """
    vds = get_virtual_desktops()
    if 1 <= nr <= len(vds):
        vds[nr-1].go()

def switch_desktop():
    """
    Toggle between virtual desktops 1 and 2.
    """
    current = get_current_desktop_number()
    if current == 1:
        go_to_desktop_number(2)
    else:
        go_to_desktop_number(1)




def main():
    """
    Create and run the system tray icon application.
    """
    icon = pystray.Icon("desk_switch")
    icon.icon = create_image()
    icon.title = "DeskSwitch"
    icon.menu = pystray.Menu(
        pystray.MenuItem('Swap Desktop', switch_desktop, default=True),
        pystray.MenuItem('Quit', lambda icon, item: icon.stop())
    )
    icon.run()

if __name__ == "__main__":
    main()
