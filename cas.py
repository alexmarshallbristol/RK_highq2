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

BDT_cut = 0.63

# make_plots = True
make_plots = False

# selection_columns = ["BDTGfixedRun3T","BDTGETOSRun3T","cascadeBDTGfixedRun3T", "e_plus_PIDe", 
# 					"e_minus_PIDe", "K_Kst_MC15TuneV1_ProbNNk", "K_Kst_PIDe", "Kemu_MKl", 
# 					"Kemu_TRACK_MKl_l2pi", "J_psi_1S_M", "B_plus_M", "passTrigCat0", "passTrigCat1", "passTrigCat2"
# 					]

selection_columns = ["cascadeBDTGfixedRun3T", "passTrigCat0", "passTrigCat1", "passTrigCat2", "BDTGfixedRun3T", 
						"BDTGETOSRun3T", "Kemu_TRACK_MKl_l2pi", "e_plus_PIDe", "B_plus_M", "K_Kst_MC15TuneV1_ProbNNk", "K_Kst_PIDe", "K_Kst_isMuon", "K_Kst_PIDmu"]

signal = uproot3.open("tuples/sim09g_Kee_truthed_2018_preselec.root")["DecayTree"] # no PID selection
cas = uproot3.open("tuples/cascades_truthed_2018_preselec.root")["DecayTree"] # no PID selection
kemu = uproot3.open("tuples/B2Kemu_Strip34_2018_customPresel_highq2_triggered.root")["DecayTree"] # no PID selection
Prc = uproot3.open("tuples/Kstee2018_truthed_preselec.root")["DecayTree"] # no PID selection



a_signal = signal.arrays(selection_columns+["DataCondKinWeight_MUTOSLong", "trigWeightR_trigCat0", "trigWeightR_trigCat1", "trigWeightR_trigCat2", "e_minus_PIDe"])
a_kcas = cas.arrays(selection_columns+["e_minus_PIDe"])
a_kemu = kemu.arrays(selection_columns)
a_Prc = Prc.arrays(selection_columns+["DataCondKinWeight_MUTOSLong", "trigWeightR_trigCat0", "trigWeightR_trigCat1", "trigWeightR_trigCat2", "e_minus_PIDe"])

def compute_where_combiBDT_PIDe4_window(array):
		where = np.where((((array[b"passTrigCat0"]==1)&(array[b"BDTGETOSRun3T"]>0.78))|((array[b"passTrigCat1"]==1)&(array[b"BDTGfixedRun3T"]>0.75))|((array[b"passTrigCat2"]==1)&(array[b"BDTGfixedRun3T"]>0.8)) )
						& ((array[b"Kemu_TRACK_MKl_l2pi"]<1825)|(array[b"Kemu_TRACK_MKl_l2pi"]>1905))
						& (array[b"e_plus_PIDe"]>4) & (array[b"e_minus_PIDe"]>4)
						& (array[b"K_Kst_MC15TuneV1_ProbNNk"]>0.2) & (array[b"K_Kst_PIDe"]<0) & (array[b"K_Kst_isMuon"]==0) & (array[b"K_Kst_PIDmu"]<5)
						& (array[b"B_plus_M"]>4880) & (array[b"B_plus_M"]<6200)
						)[0]
		return where

def compute_where_combiBDT_PIDe4_window_kemu(array):
		where = np.where((((array[b"passTrigCat0"]==1)&(array[b"BDTGETOSRun3T"]>0.78))|((array[b"passTrigCat1"]==1)&(array[b"BDTGfixedRun3T"]>0.75))|((array[b"passTrigCat2"]==1)&(array[b"BDTGfixedRun3T"]>0.8)) )
						& ((array[b"Kemu_TRACK_MKl_l2pi"]<1825)|(array[b"Kemu_TRACK_MKl_l2pi"]>1905))
						& (array[b"e_plus_PIDe"]>4)
						& (array[b"B_plus_M"]>4880) & (array[b"B_plus_M"]<6200)
						)[0]
		return where

where_sig = compute_where_combiBDT_PIDe4_window(a_signal)
where_cas = compute_where_combiBDT_PIDe4_window(a_kcas)
where_kemu = compute_where_combiBDT_PIDe4_window_kemu(a_kemu)
where_Prc = compute_where_combiBDT_PIDe4_window(a_Prc)


Prc_weight = np.empty(np.shape(a_Prc[b"DataCondKinWeight_MUTOSLong"])[0])
for i in range(0, np.shape(a_Prc[b"DataCondKinWeight_MUTOSLong"])[0]):
	trig = [a_Prc[b"passTrigCat0"][i],a_Prc[b"passTrigCat1"][i],a_Prc[b"passTrigCat2"][i]]
	if trig[0] == 1:
		Prc_weight[i] = a_Prc[b"DataCondKinWeight_MUTOSLong"][i]*a_Prc[b"trigWeightR_trigCat0"][i]
	elif trig[1] == 1:
		Prc_weight[i] = a_Prc[b"DataCondKinWeight_MUTOSLong"][i]*a_Prc[b"trigWeightR_trigCat1"][i]
	elif trig[2] == 1:
		Prc_weight[i] = a_Prc[b"DataCondKinWeight_MUTOSLong"][i]*a_Prc[b"trigWeightR_trigCat2"][i]

sig_weight = np.empty(np.shape(a_signal[b"DataCondKinWeight_MUTOSLong"])[0])
for i in range(0, np.shape(a_signal[b"DataCondKinWeight_MUTOSLong"])[0]):
	trig = [a_signal[b"passTrigCat0"][i],a_signal[b"passTrigCat1"][i],a_signal[b"passTrigCat2"][i]]
	if trig[0] == 1:
		sig_weight[i] = a_signal[b"DataCondKinWeight_MUTOSLong"][i]*a_signal[b"trigWeightR_trigCat0"][i]
	elif trig[1] == 1:
		sig_weight[i] = a_signal[b"DataCondKinWeight_MUTOSLong"][i]*a_signal[b"trigWeightR_trigCat1"][i]
	elif trig[2] == 1:
		sig_weight[i] = a_signal[b"DataCondKinWeight_MUTOSLong"][i]*a_signal[b"trigWeightR_trigCat2"][i]



# plt.figure(figsize=(5,4))
# plt.hist([a_signal[b"cascadeBDTGfixedRun3T"], a_kcas[b"cascadeBDTGfixedRun3T"], a_kemu[b"cascadeBDTGfixedRun3T"], a_Prc[b"cascadeBDTGfixedRun3T"]], density=True, label=['Signal','Cascades', 'Kemu','K*ee'], histtype='step', bins=50, linewidth=1, color=['tab:blue','tab:orange','tab:green','tab:red'])
# # plt.hist([a_signal[b"cascadeBDTGfixedRun3T"][where_sig], a_kcas[b"cascadeBDTGfixedRun3T"][where_cas], a_kemu[b"cascadeBDTGfixedRun3T"][where_kemu], a_Prc[b"cascadeBDTGfixedRun3T"][where_Prc]], label=['Signal','Cascades', 'Kemu','K*ee'], density=True, histtype='step', bins=50, linewidth=1, color=['tab:blue','tab:orange','tab:green','tab:red'])
# plt.legend()
# plt.xlabel('Cascade BDT response')
# plt.ylabel('Normalised frequency')
# # plt.savefig('plots/BDT_response_1D_2_overlay_all.pdf',bbox_inches='tight')
# # plt.close('all')
# plt.show()

data_list = [a_signal, a_Prc, a_kcas, a_kemu]
weight_list = [sig_weight, Prc_weight, np.ones(np.shape(a_kcas[b"cascadeBDTGfixedRun3T"])[0]), np.ones(np.shape(a_kemu[b"cascadeBDTGfixedRun3T"])[0])]
label = ["signal", "K*ee", "Cascades", "Kemu"]

plt.figure(figsize=(5,4))
for i in range(0, 4):
	weight_list[i] = weight_list[i]/np.sum(weight_list[i])
	n, bins = np.histogram(data_list[i][b"cascadeBDTGfixedRun3T"], range=[0,1], bins=50, weights=weight_list[i])
	n_err = np.sqrt(np.histogram(data_list[i][b"cascadeBDTGfixedRun3T"], range=[0,1], bins=50, weights=weight_list[i]**2)[0])
	x = bins[:-1] + ((bins[1]-bins[0])/2.)
	print(np.shape(x), np.shape(n), np.shape(n_err))
	plt.errorbar(x, n, yerr=n_err,label=label[i])
plt.legend()
plt.xlabel('Cascade BDT response')
plt.ylabel('Normalised frequency')
plt.savefig('plots/BDT_response_1D_2_overlay_all_err.pdf',bbox_inches='tight')
plt.close('all')


data_list = [a_signal, a_Prc, a_kcas, a_kemu]
where_list = [where_sig, where_Prc, where_cas, where_kemu]
weight_list = [sig_weight[where_sig], Prc_weight[where_Prc], np.ones(np.shape(a_kcas[b"cascadeBDTGfixedRun3T"][where_cas])[0]), np.ones(np.shape(a_kemu[b"cascadeBDTGfixedRun3T"][where_kemu])[0])]
label = ["signal", "K*ee", "Cascades", "Kemu"]

plt.figure(figsize=(5,4))
for i in range(0, 4):
	weight_list[i] = weight_list[i]/np.sum(weight_list[i])
	n, bins = np.histogram(data_list[i][b"cascadeBDTGfixedRun3T"][where_list[i]], range=[0,1], bins=50, weights=weight_list[i])
	n_err = np.sqrt(np.histogram(data_list[i][b"cascadeBDTGfixedRun3T"][where_list[i]], range=[0,1], bins=50, weights=weight_list[i]**2)[0])
	x = bins[:-1] + ((bins[1]-bins[0])/2.)
	print(np.shape(x), np.shape(n), np.shape(n_err))
	plt.errorbar(x, n, yerr=n_err,label=label[i])
plt.legend()
plt.xlabel('Cascade BDT response')
plt.ylabel('Normalised frequency')
plt.savefig('plots/BDT_response_1D_2_overlay_err.pdf',bbox_inches='tight')
plt.close('all')



quit()
plt.figure(figsize=(5,4))
# plt.hist([a_signal[b"cascadeBDTGfixedRun3T"], a_kcas[b"cascadeBDTGfixedRun3T"], a_kemu[b"cascadeBDTGfixedRun3T"], a_Prc[b"cascadeBDTGfixedRun3T"]], density=True, label=['Signal','Cascades', 'Kemu','K*ee'], histtype='step', bins=50, linewidth=1, color=['tab:blue','tab:orange','tab:green','tab:red'])
plt.hist([a_signal[b"cascadeBDTGfixedRun3T"][where_sig], a_kcas[b"cascadeBDTGfixedRun3T"][where_cas], a_kemu[b"cascadeBDTGfixedRun3T"][where_kemu], a_Prc[b"cascadeBDTGfixedRun3T"][where_Prc]], label=['Signal','Cascades', 'Kemu','K*ee'], density=True, histtype='step', bins=50, linewidth=1, color=['tab:blue','tab:orange','tab:green','tab:red'])
plt.legend()
plt.xlabel('Cascade BDT response')
plt.ylabel('Normalised frequency')
plt.savefig('plots/BDT_response_1D_2_overlay.pdf',bbox_inches='tight')
plt.close('all')
quit()

plt.figure(figsize=(8,8))
plt.subplot(2,2,1)
plt.hist(a_signal[b"cascadeBDTGfixedRun3T"], range=[0,1], density=True, label=['Signal preselc'], histtype='step', bins=50, linewidth=1, color=['tab:blue'])
plt.hist(a_signal[b"cascadeBDTGfixedRun3T"][where_sig], range=[0,1], density=True, label=['Signal preselc + PID + combiBDT + window cut'], histtype='step', bins=50, linewidth=1, color=['tab:blue'], linestyle='--')
plt.legend()
plt.xlabel('Cascade BDT response')
plt.ylabel('Normalised frequency')
plt.subplot(2,2,2)
plt.hist(a_kcas[b"cascadeBDTGfixedRun3T"], range=[0,1], density=True, label=['Cascades'], histtype='step', bins=50, linewidth=1, color=['tab:orange'])
plt.hist(a_kcas[b"cascadeBDTGfixedRun3T"][where_cas], range=[0,1], density=True, histtype='step', bins=50, linewidth=1, color=['tab:orange'], linestyle='--')
plt.legend()
plt.xlabel('Cascade BDT response')
plt.ylabel('Normalised frequency')
plt.subplot(2,2,3)
plt.hist(a_kemu[b"cascadeBDTGfixedRun3T"], range=[0,1], density=True, label=['Kemu'], histtype='step', bins=50, linewidth=1, color=['tab:green'])
plt.hist(a_kemu[b"cascadeBDTGfixedRun3T"][where_kemu], range=[0,1], density=True, histtype='step', bins=50, linewidth=1, color=['tab:green'], linestyle='--')
plt.legend()
plt.xlabel('Cascade BDT response')
plt.ylabel('Normalised frequency')
plt.subplot(2,2,4)
plt.hist(a_Prc[b"cascadeBDTGfixedRun3T"], range=[0,1], density=True, label=['K*ee'], histtype='step', bins=50, linewidth=1, color=['tab:red'])
plt.hist(a_Prc[b"cascadeBDTGfixedRun3T"][where_Prc], range=[0,1], density=True, histtype='step', bins=50, linewidth=1, color=['tab:red'], linestyle='--')
plt.legend()
plt.xlabel('Cascade BDT response')
plt.ylabel('Normalised frequency')
plt.savefig('plots/BDT_response_1D_2.pdf',bbox_inches='tight')
plt.close('all')

quit()
print(num)

# print(a_kemu[b"e_plus_M"])
# quit()

# TMath::Sqrt(139.57*139.57+TMath::Power(e_plus_PE,2))
# string massOfJesusPiSubst_cut("sqrt((((K_Kst_ID/321)*(e_plus_ID/11) == 1 ))*(TMath::Power(TMath::Sqrt(139.57*139.57+TMath::Power(e_plus_PE,2))+K_Kst_PE, 2)-TMath::Power(e_plus_PY+K_Kst_PY, 2)-TMath::Power(e_plus_PX+K_Kst_PX, 2)-TMath::Power(e_plus_PZ+K_Kst_PZ, 2)))");


# plt.hist(np.sqrt(139.57018**2+a_kemu[b"e_plus_TRACK_P"]**2)-np.sqrt(a_kemu[b"e_plus_M"]**2+a_kemu[b"e_plus_TRACK_P"]**2),bins=50,histtype='step')
# plt.yscale('log')
# plt.show()
# quit()

# print(a_kemu[b"e_plus_TRACK_PX"], a_kemu[b"e_plus_PX"], a_kemu[b"e_plus_BremPX"])
# print(a_kemu[b"e_plus_BremPE"])
# # plt.hist(a_kemu[b"e_plus_BremPX"], bins=50)
# # plt.show()

# print(np.where(a_kemu[b"e_plus_BremPE"]!=0.))
# print(np.where(a_kemu[b"e_plus_BremPX"]!=0.))
# print(np.where(a_kemu[b"e_plus_BremPY"]!=0.))
# print(np.where(a_kemu[b"e_plus_BremPZ"]!=0.))


print(a_kemu[b"e_plus_PX"],a_kemu[b"e_plus_TRACK_PX"], a_kemu[b"e_plus_BremPX"])
print(a_kemu[b"e_plus_TRACK_PX"]+a_kemu[b"e_plus_BremPX"])
quit()
plt.hist(a_kemu[b"e_plus_PX"]-a_kemu[b"e_plus_TRACK_PX"]+a_kemu[b"e_plus_BremPX"], bins=50, histtype='step')
plt.show()

quit()

E_K_TRACK = np.sqrt(a_kemu[b"K_Kst_M"]**2+a_kemu[b"K_Kst_TRACK_P"]**2)
E_e_plus_TRACK = np.sqrt(139.57018**2+a_kemu[b"e_plus_TRACK_P"]**2)

mkpi = np.sqrt((E_K_TRACK+E_e_plus_TRACK)**2
		-(a_kemu[b"K_Kst_TRACK_PX"]+a_kemu[b"e_plus_TRACK_PX"])**2
		-(a_kemu[b"K_Kst_TRACK_PY"]+a_kemu[b"e_plus_TRACK_PY"])**2
		-(a_kemu[b"K_Kst_TRACK_PZ"]+a_kemu[b"e_plus_TRACK_PZ"])**2)


# E_K_TRACK_mke = np.sqrt(a_kemu[b"K_Kst_M"]**2+a_kemu[b"K_Kst_TRACK_P"]**2)
# E_e_plus_TRACK_mke = np.sqrt(a_kemu[b"e_plus_M"]**2+a_kemu[b"e_plus_TRACK_P"]**2)

# mke_TRACK = np.sqrt((E_K_TRACK_mke-a_kemu[b"e_plus_BremPE"]+E_e_plus_TRACK_mke)**2
# 		-(a_kemu[b"K_Kst_TRACK_PX"]+a_kemu[b"e_plus_TRACK_PX"])**2
# 		-(a_kemu[b"K_Kst_TRACK_PY"]+a_kemu[b"e_plus_TRACK_PY"])**2
# 		-(a_kemu[b"K_Kst_TRACK_PZ"]+a_kemu[b"e_plus_TRACK_PZ"])**2)


E_K_mke = np.sqrt(a_kemu[b"K_Kst_M"]**2+a_kemu[b"K_Kst_P"]**2)
E_e_plus_mke = np.sqrt(a_kemu[b"e_plus_M"]**2+a_kemu[b"e_plus_P"]**2)

mke = np.sqrt((E_K_mke-a_kemu[b"e_plus_BremPE"]+E_e_plus_mke)**2
		-(a_kemu[b"K_Kst_PX"]+a_kemu[b"e_plus_PX"]-a_kemu[b"e_plus_BremPX"])**2
		-(a_kemu[b"K_Kst_PY"]+a_kemu[b"e_plus_PY"]-a_kemu[b"e_plus_BremPY"])**2
		-(a_kemu[b"K_Kst_PZ"]+a_kemu[b"e_plus_PZ"]-a_kemu[b"e_plus_BremPZ"])**2)

plt.hist([a_kemu[b"Kemu_MKl"], mke],bins=50,histtype='step',label=['Kemu_MKl','mke'])
plt.hist([mkpi],bins=50,histtype='step',label=['mkpi'])
plt.hist([a_kemu[b"Kemu_TRACK_MKl_l2pi"]],bins=50,histtype='step',label=['Kemu_TRACK_MKl_l2pi'])
plt.legend()
plt.show()
quit()





