from core import info
from core import colors
from core.moduleop import count

Garuda = r"""
"#####################################################################"
"#                           ______                                  #"
"#                        .-.      .-.                               #"
"#                       /    404      \                             #"
"#                      | Garuda Tools |                             #"
"#                      |,  .-.  .-.  ,|                             #"
"#                      | )(z_/  \z_)( |                             #"
"#                      |/     /\     \|                             #"
"#              _       (_     ^^     _)                             #"
"#      _\ ____) \_______\__|IIIIII|__/_________________________     #"
"#     (_)[___]{}<________|-\IIIIII/-|__zRR__zRR__zRR___________\    #"
"#       /     )_/        \          /                               #"
"#                         \ ______ /                                #"
"#                                                                   #"
"#                    MASTER LINUX INDONESIA                         #"
"#                      by  Jhon Islanskha  !!                       #"
"#####################################################################"
def print_info():
	count()

	print("\t" + colors.bold + "Garuda Tools\n" + colors.end)
	print("\t" + colors.bold + "Core "+colors.end+"\t[ "+info.version+" "+info.codename+"\t]" + colors.end)
	print("\t" + colors.bold + "API"+colors.end+"\t[ "+info.apiversion+"\t\t]"+colors.end)
	print("\t" + colors.bold + "Date"+colors.end+"\t[ "+info.update_date+"\t\t]"+colors.end)
	print("\t" + colors.bold + "Modules "+colors.end+"[ "+count.mod+" modules"+"\t\t]"+colors.end)
	print("\n")
