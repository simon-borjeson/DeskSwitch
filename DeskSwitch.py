import pystray
from PIL import Image, ImageDraw
import pyvda

def create_image():
    width = 64
    height = 64
    color1 = (64, 128, 255)
    color2 = (255, 255, 255)
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle([12, 12, 52, 28], fill=color2)
    dc.rectangle([12, 36, 52, 52], fill=color2)
    return image


def get_current_desktop_number():
    vds = pyvda.get_virtual_desktops()
    current_vd = pyvda.VirtualDesktop.current()
    for i, vd in enumerate(vds, start=1):
        if vd.id == current_vd.id:
            return i
    return 1


def go_to_desktop_number(nr):
    vds = pyvda.get_virtual_desktops()
    if 1 <= nr <= len(vds):
        vds[nr-1].go()

def switch_desktop(icon, item):
    current = get_current_desktop_number()
    if current == 1:
        go_to_desktop_number(2)
    else:
        go_to_desktop_number(1)


def main():
    icon = pystray.Icon("DeskSwitch")
    icon.icon = create_image()
    icon.menu = pystray.Menu(
        pystray.MenuItem('Swap Desktop', switch_desktop, default=True),
        pystray.MenuItem('Quit', lambda icon, item: icon.stop())
    )
    icon.run()

if __name__ == '__main__':
    main()
