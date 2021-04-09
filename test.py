import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
colours_raw_root = [[250,242,108],
					[249,225,104],
					[247,206,99],
					[239,194,94],
					[222,188,95],
					[206,183,103],
					[181,184,111],
					[157,185,120],
					[131,184,132],
					[108,181,146],
					[105,179,163],
					[97,173,176],
					[90,166,191],
					[81,158,200],
					[69,146,202],
					[56,133,207],
					[40,121,209],
					[27,110,212],
					[25,94,197],
					[34,73,162]]

colours_raw_root = np.flip(np.divide(colours_raw_root,256.),axis=0)
cmp_root = mpl.colors.ListedColormap(colours_raw_root)
import uproot3
import ROOT
import matplotlib.patches as patches
from RK_functions import RK_func as RK

casBDT_cut = RK.get_default_casBDT_cut()

signal = uproot3.open("tuples/sim09g_Kee_truthed_2018_preselec.root")["DecayTree"]
cascade1 = uproot3.open("tuples/Bu_D0enu_Kenu2018_truthed_preselec.root")["DecayTree"]
cascade3 = uproot3.open("tuples/Bu_D0pi_Kenu2018_truthed_preselec.root")["DecayTree"]
kemu = uproot3.open("tuples/B2Kemu_Strip34_2018_customPresel_highq2_triggered.root")["DecayTree"]
Prc = uproot3.open("tuples/Kstee2018_truthed_preselec.root")["DecayTree"]
kpipi = uproot3.open("tuples/B2Kpipi_truthed_2018_preslec.root")["DecayTree"] 

a_signal = signal.arrays(RK.get_standard_columns()+RK.get_trigger_weight_columns()+['misPIDweight'])
a_cascade1 = cascade1.arrays(RK.get_standard_columns())
a_cascade3 = cascade3.arrays(RK.get_standard_columns())
a_kemu = kemu.arrays(RK.get_kemu_columns())
a_Prc = Prc.arrays(RK.get_standard_columns()+RK.get_trigger_weight_columns()+['misPIDweight','misPIDweight_SwaveWeight'])
a_kpipi = kpipi.arrays(RK.get_standard_columns()+['misPIDweight'])

data_labels = ['Signal', 'Cascade1', 'Cascade3', 'Kemu', 'Prc', 'Kpipi']
data_list = [a_signal, a_cascade1, a_cascade3, a_kemu, a_Prc, a_kpipi]

# contaminations = RK.get_contaminations(a_signal, a_cascade1, a_cascade3, a_Prc, a_kpipi, CasWindow=True, CasMkl=True, CasBDT=False)
# contaminations = RK.get_contaminations(a_signal, a_cascade1, a_cascade3, a_Prc, a_kpipi, CasWindow=True, CasMkl=False, CasBDT=False)
# contaminations = RK.get_contaminations(a_signal, a_cascade1, a_cascade3, a_Prc, a_kpipi, CasWindow=False, CasMkl=False, CasBDT=True)

weights_list = RK.compute_weights_list(a_signal, a_cascade1, a_cascade3, a_Prc, a_kpipi, CasWindow=False, CasMkl=False, CasBDT=True)





# plt.figure(figsize=(8,4))
# ax = plt.subplot(1,2,1)
# for idx, array_i in enumerate([a_signal, a_cascade, a_kemu, a_Prc, a_kpipi]):
# 	plt.hist(array_i[b"Kemu_MKl"], bins=50, range=[600,5000], label=data_labels[idx], histtype='step', density='True')
# plt.text(0.05, 0.95,'Before selection',horizontalalignment='left',verticalalignment='top',transform = ax.transAxes, fontsize=10)
# plt.xlabel('m(Ke)')
# ax = plt.subplot(1,2,2)
# for idx, array_i in enumerate([a_signal, a_cascade, a_kemu, a_Prc, a_kpipi]):
# 	if data_labels[idx] == 'Kemu':
# 		where = RK.full_selection(array_i, casBDT_cut=0.56, combiBDT=True, Bmass=True, CasWindow=False, CasMkl=False, CasBDT=False, PID=False, PID_Kemu=True)
# 	else:
# 		where = RK.full_selection(array_i, casBDT_cut=0.56, combiBDT=True, Bmass=True, CasWindow=False, CasMkl=False, CasBDT=False, PID=True, PID_Kemu=False)
# 	plt.hist(array_i[b"Kemu_MKl"][where], bins=50, range=[600,5000], label=data_labels[idx], histtype='step', density='True')
# plt.text(0.05, 0.95,'After selection',horizontalalignment='left',verticalalignment='top',transform = ax.transAxes, fontsize=10)
# plt.xlabel('m(Ke)')
# plt.legend()
# plt.show()



