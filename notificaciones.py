import otrostrabajadores as oT; from otrostrabajadores import *
from winotify import Notification

if oT.veri_win == True:
	toast = Notification(app_id="windows app", title="Winotify Test Toast", msg="New Notification!", icon=r"c:\path\to\icon.png")
	toast.add_actions(label="ver solicitudes",
					launch="cmd /c python adquisiciones.py")

	toast.show()