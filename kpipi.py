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

BDT_cut = 0.56

# make_plots = True
make_plots = False

# selection_columns = ["BDTGfixedRun3T","BDTGETOSRun3T","cascadeBDTGfixedRun3T", "e_plus_PIDe", 
# 					"e_minus_PIDe", "K_Kst_MC15TuneV1_ProbNNk", "K_Kst_PIDe", "Kemu_MKl", 
# 					"Kemu_TRACK_MKl_l2pi", "J_psi_1S_M", "B_plus_M", "passTrigCat0", "passTrigCat1", "passTrigCat2"
# 					]

selection_columns = ["cascadeBDTGfixedRun3T", "Kemu_MKl", "e_plus_PIDe", "e_minus_PIDe", 
					"passTrigCat0", "passTrigCat1", "passTrigCat2", 
					"BDTGfixedRun3T", "BDTGETOSRun3T", "B_plus_M",
					"e_plus_PE", "e_plus_BremPE", "K_Kst_PE", "e_plus_PX", "e_plus_BremPX", "e_plus_BremPY", "e_plus_BremPZ", "K_Kst_P", "e_plus_P","e_minus_P",
					"e_plus_BremPX", "K_Kst_PX", "e_plus_PY", "e_plus_BremPY", 
					"K_Kst_PY", "e_plus_PZ", "e_plus_BremPZ", "K_Kst_PZ", "K_Kst_ID", "e_plus_ID",
					"e_minus_PE","e_minus_PX","e_minus_PY","e_minus_PZ" 
					,"K_Kst_TRACK_P", "K_Kst_TRACK_PX", "K_Kst_TRACK_PY", "K_Kst_TRACK_PZ", "K_Kst_M"
					,"e_plus_TRACK_P", "e_plus_TRACK_PX", "e_plus_TRACK_PY", "e_plus_TRACK_PZ", "e_plus_M"
					,"e_minus_TRACK_P", "e_minus_TRACK_PX", "e_minus_TRACK_PY", "e_minus_TRACK_PZ", "e_minus_M", "Kemu_TRACK_MKl_l2pi"
					]

signal = uproot3.open("tuples/sim09g_Kee_truthed_2018_preselec.root")["DecayTree"] # no PID selection
cascade = uproot3.open("tuples/cascades_truthed_2018_preselec.root")["DecayTree"] # no PID selection
kemu = uproot3.open("tuples/B2Kemu_Strip34_2018_customPresel_highq2_triggered.root")["DecayTree"] # no PID selection
Prc = uproot3.open("tuples/Kstee2018_truthed_preselec.root")["DecayTree"] # no PID selection
kpipi = uproot3.open("tuples/B2Kpipi_truthed_2018_preslec.root")["DecayTree"] # no PID selection

a_signal = signal.arrays(selection_columns)
a_cascade = cascade.arrays(selection_columns)
a_kemu = kemu.arrays(selection_columns)
a_Prc = Prc.arrays(selection_columns)
a_kpipi = kpipi.arrays(selection_columns+['misPIDweight'])

data_list = [a_signal, a_cascade, a_kemu, a_Prc, a_kpipi]
data_labels = ['a_signal', 'a_cascade', 'a_kemu', 'a_Prc', 'a_kpipi']
for idx, data_i in enumerate(data_list):
	print(data_labels[idx], ":", np.shape(data_i[b"cascadeBDTGfixedRun3T"])[0])



# for idx, data_i in enumerate(data_list):

# 	plt.hist(data_i[b"B_plus_M"],label=data_labels[idx],bins=50,histtype='step',density=True)
# plt.legend()
# plt.show()

def compute_where_combiBDT_PIDe4_window(array):
		where = np.where((((array[b"passTrigCat0"]==1)&(array[b"BDTGETOSRun3T"]>0.78))|((array[b"passTrigCat1"]==1)&(array[b"BDTGfixedRun3T"]>0.75))|((array[b"passTrigCat2"]==1)&(array[b"BDTGfixedRun3T"]>0.8)) )
						& ((array[b"Kemu_TRACK_MKl_l2pi"]<1825)|(array[b"Kemu_TRACK_MKl_l2pi"]>1905))
						# & (array[b"e_plus_PIDe"]>4)
						# & (array[b"e_minus_PIDe"]>4)
						& (array[b"B_plus_M"]>4880) & (array[b"B_plus_M"]<6200)
						)[0]
		return where

where = compute_where_combiBDT_PIDe4_window(a_kpipi)

# plt.hist(a_kpipi[b"B_plus_M"],bins=50,histtype='step',density=True)
# plt.hist(a_kpipi[b"B_plus_M"],weights=a_kpipi[b"misPIDweight"],bins=50,histtype='step',density=True)
# plt.show()

plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.hist2d(a_kpipi[b"e_plus_PIDe"],a_kpipi[b"misPIDweight"],bins=50,norm=LogNorm())
plt.subplot(1,2,2)
plt.hist2d(a_kpipi[b"e_minus_PIDe"],a_kpipi[b"misPIDweight"],bins=50,norm=LogNorm())
plt.show()
quit()

plt.figure(figsize=(5*5,4))

for idx, data_i in enumerate(data_list):

	ax = plt.subplot(1,5,idx+1)
	plt.hist2d(data_i[b"e_plus_PIDe"],data_i[b"e_minus_PIDe"],bins=50,norm=LogNorm(), range=[[-17,17], [-17,17]])
	plt.colorbar()
	plt.text(0.95, 0.95,data_labels[idx],
	     horizontalalignment='right',
	     verticalalignment='top',
	     transform = ax.transAxes, fontsize=10)
	plt.axhline(y=4,c='k',linestyle='--')
	plt.axvline(x=4,c='k',linestyle='--')

plt.show()

