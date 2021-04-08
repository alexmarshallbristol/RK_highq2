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

make_plots = True
# make_plots = False

# selection_columns = ["BDTGfixedRun3T","BDTGETOSRun3T","cascadeBDTGfixedRun3T", "e_plus_PIDe", 
# 					"e_minus_PIDe", "K_Kst_MC15TuneV1_ProbNNk", "K_Kst_PIDe", "Kemu_MKl", 
# 					"Kemu_TRACK_MKl_l2pi", "J_psi_1S_M", "B_plus_M", "passTrigCat0", "passTrigCat1", "passTrigCat2"
# 					]

selection_columns = ["cascadeBDTGfixedRun3T", "Kemu_MKl", "e_plus_PIDe", 
					"passTrigCat0", "passTrigCat1", "passTrigCat2", 
					"BDTGfixedRun3T", "BDTGETOSRun3T", "B_plus_M",
					"e_plus_PE", "e_plus_BremPE", "K_Kst_PE", "e_plus_PX", "e_plus_BremPX", "e_plus_BremPY", "e_plus_BremPZ", "K_Kst_P", "e_plus_P","e_minus_P",
					"e_plus_BremPX", "K_Kst_PX", "e_plus_PY", "e_plus_BremPY", 
					"K_Kst_PY", "e_plus_PZ", "e_plus_BremPZ", "K_Kst_PZ", "K_Kst_ID", "e_plus_ID",
					"e_minus_PE","e_minus_PX","e_minus_PY","e_minus_PZ" 
					,"K_Kst_TRACK_P", "K_Kst_TRACK_PX", "K_Kst_TRACK_PY", "K_Kst_TRACK_PZ", "K_Kst_M"
					,"e_plus_TRACK_P", "e_plus_TRACK_PX", "e_plus_TRACK_PY", "e_plus_TRACK_PZ", "e_plus_M"
					,"e_minus_TRACK_P", "e_minus_TRACK_PX", "e_minus_TRACK_PY", "e_minus_TRACK_PZ", "e_minus_M", "Kemu_TRACK_MKl_l2pi", 
					"K_Kst_MC15TuneV1_ProbNNk", "K_Kst_PIDe", "K_Kst_isMuon", "K_Kst_PIDmu"
					]

signal = uproot3.open("tuples/sim09g_Kee_truthed_2018_preselec.root")["DecayTree"] # no PID selection
cascade = uproot3.open("tuples/cascades_truthed_2018_preselec.root")["DecayTree"] # no PID selection
kemu = uproot3.open("tuples/B2Kemu_Strip34_2018_customPresel_highq2_triggered.root")["DecayTree"] # no PID selection

a_signal = signal.arrays(selection_columns+["e_minus_PIDe"])
a_cascade = cascade.arrays(selection_columns+["e_minus_PIDe"])
a_kemu = kemu.arrays(selection_columns)

num = np.shape(a_kemu[b"cascadeBDTGfixedRun3T"])[0]


# # print(a_kemu[b"e_plus_M"])
# # quit()

# # TMath::Sqrt(139.57*139.57+TMath::Power(e_plus_PE,2))
# # string massOfJesusPiSubst_cut("sqrt((((K_Kst_ID/321)*(e_plus_ID/11) == 1 ))*(TMath::Power(TMath::Sqrt(139.57*139.57+TMath::Power(e_plus_PE,2))+K_Kst_PE, 2)-TMath::Power(e_plus_PY+K_Kst_PY, 2)-TMath::Power(e_plus_PX+K_Kst_PX, 2)-TMath::Power(e_plus_PZ+K_Kst_PZ, 2)))");


# # plt.hist(np.sqrt(139.57018**2+a_kemu[b"e_plus_TRACK_P"]**2)-np.sqrt(a_kemu[b"e_plus_M"]**2+a_kemu[b"e_plus_TRACK_P"]**2),bins=50,histtype='step')
# # plt.yscale('log')
# # plt.show()
# # quit()

# # print(a_kemu[b"e_plus_TRACK_PX"], a_kemu[b"e_plus_PX"], a_kemu[b"e_plus_BremPX"])
# # print(a_kemu[b"e_plus_BremPE"])
# print(a_kemu[b"K_Kst_M"])

# print(np.where(a_kemu[b"e_plus_BremPE"]!=0.))
# print(np.where(a_kemu[b"e_plus_BremPX"]!=0.))
# print(np.where(a_kemu[b"e_plus_BremPY"]!=0.))
# print(np.where(a_kemu[b"e_plus_BremPZ"]!=0.))

# print(a_kemu[b"e_minus_M"][0], a_kemu[b"e_plus_M"][0])

# # quit()

# E_K_TRACK = np.sqrt(a_kemu[b"K_Kst_M"]**2+a_kemu[b"K_Kst_TRACK_P"]**2)
# E_e_plus_TRACK = np.sqrt(139.57018**2+a_kemu[b"e_plus_TRACK_P"]**2)

# mkpi = np.sqrt((E_K_TRACK+E_e_plus_TRACK)**2
# 		-(a_kemu[b"K_Kst_TRACK_PX"]+a_kemu[b"e_plus_TRACK_PX"])**2
# 		-(a_kemu[b"K_Kst_TRACK_PY"]+a_kemu[b"e_plus_TRACK_PY"])**2
# 		-(a_kemu[b"K_Kst_TRACK_PZ"]+a_kemu[b"e_plus_TRACK_PZ"])**2)

# # E_K_TRACK = np.sqrt(a_kemu[b"K_Kst_M"]**2+a_kemu[b"K_Kst_TRACK_P"]**2)
# # E_e_plus_TRACK = np.sqrt(139.57018**2+a_kemu[b"e_minus_TRACK_P"]**2)

# # mkpi = np.sqrt((E_K_TRACK+E_e_plus_TRACK)**2
# # 		-(a_kemu[b"K_Kst_TRACK_PX"]+a_kemu[b"e_minus_TRACK_PX"])**2
# # 		-(a_kemu[b"K_Kst_TRACK_PY"]+a_kemu[b"e_minus_TRACK_PY"])**2
# # 		-(a_kemu[b"K_Kst_TRACK_PZ"]+a_kemu[b"e_minus_TRACK_PZ"])**2)


# E_K_mke = np.sqrt(a_kemu[b"K_Kst_M"]**2+a_kemu[b"K_Kst_P"]**2)
# E_e_plus_mke = np.sqrt(a_kemu[b"e_plus_M"]**2+a_kemu[b"e_plus_P"]**2)

# mke = np.sqrt((E_K_mke+E_e_plus_mke)**2
# 		-(a_kemu[b"K_Kst_PX"]+a_kemu[b"e_plus_PX"])**2
# 		-(a_kemu[b"K_Kst_PY"]+a_kemu[b"e_plus_PY"])**2
# 		-(a_kemu[b"K_Kst_PZ"]+a_kemu[b"e_plus_PZ"])**2)

# # E_K_mke = np.sqrt(a_kemu[b"K_Kst_M"]**2+a_kemu[b"K_Kst_P"]**2)
# # E_e_plus_mke = np.sqrt(a_kemu[b"e_minus_M"]**2+a_kemu[b"e_minus_P"]**2)

# # mke = np.sqrt((E_K_mke+E_e_plus_mke)**2
# # 		-(a_kemu[b"K_Kst_PX"]+a_kemu[b"e_minus_PX"])**2
# # 		-(a_kemu[b"K_Kst_PY"]+a_kemu[b"e_minus_PY"])**2
# # 		-(a_kemu[b"K_Kst_PZ"]+a_kemu[b"e_minus_PZ"])**2)

# print(np.where(mke==a_kemu[b"Kemu_MKl"]))
# print(np.where(mkpi==a_kemu[b"Kemu_TRACK_MKl_l2pi"]))

# print(mkpi[:5])
# print(a_kemu[b"Kemu_TRACK_MKl_l2pi"][:5])

# plt.hist([a_kemu[b"Kemu_MKl"], mke],bins=50,histtype='step',label=['Kemu_MKl','mke'])
# plt.hist([mkpi],bins=50,histtype='step',label=['mkpi'])
# plt.hist([a_kemu[b"Kemu_TRACK_MKl_l2pi"]],bins=50,histtype='step',label=['Kemu_TRACK_MKl_l2pi'])
# plt.legend()
# plt.show()
# quit()

	# string massOfJesus("sqrt((((K_Kst_ID/321)*(e_plus_ID/11) == 1 ))*(TMath::Power(e_plus_PE-e_plus_BremPE+K_Kst_PE, 2)-TMath::Power(e_plus_PY-e_plus_BremPY+K_Kst_PY, 2)-TMath::Power(e_plus_PX-e_plus_BremPX+K_Kst_PX, 2)-TMath::Power(e_plus_PZ-e_plus_BremPZ+K_Kst_PZ, 2)))");


# B_plus_M = np.sqrt(np.power(np.add(np.add(np.subtract(a_kemu[b"e_plus_PE"], a_kemu[b"e_plus_BremPE"]),a_kemu[b"K_Kst_PE"]),a_kemu[b"e_minus_PE"]),2.) 
# 	          -np.power(np.add(np.add(np.subtract(a_kemu[b"e_plus_PX"], a_kemu[b"e_plus_BremPX"]),a_kemu[b"K_Kst_PX"]),a_kemu[b"e_minus_PX"]),2.) 
# 	          -np.power(np.add(np.add(np.subtract(a_kemu[b"e_plus_PY"], a_kemu[b"e_plus_BremPY"]),a_kemu[b"K_Kst_PY"]),a_kemu[b"e_minus_PY"]),2.) 
# 	          	-np.power(np.add(np.add(np.subtract(a_kemu[b"e_plus_PZ"], a_kemu[b"e_plus_BremPZ"]),a_kemu[b"K_Kst_PZ"]),a_kemu[b"e_minus_PZ"]),2.))

# B_plus_M = np.sqrt(np.power(np.add(np.add(np.subtract(a_kemu[b"e_plus_PE"], a_kemu[b"e_plus_BremPE"]),a_kemu[b"K_Kst_PE"]),np.sqrt(139.57*139.57+np.power(a_kemu[b"e_minus_PE"],2.))),2.) 
# 	          -np.power(np.add(np.add(np.subtract(a_kemu[b"e_plus_PX"], a_kemu[b"e_plus_BremPX"]),a_kemu[b"K_Kst_PX"]),a_kemu[b"e_minus_PX"]),2.) 
# 	          -np.power(np.add(np.add(np.subtract(a_kemu[b"e_plus_PY"], a_kemu[b"e_plus_BremPY"]),a_kemu[b"K_Kst_PY"]),a_kemu[b"e_minus_PY"]),2.) 
# 	          	-np.power(np.add(np.add(np.subtract(a_kemu[b"e_plus_PZ"], a_kemu[b"e_plus_BremPZ"]),a_kemu[b"K_Kst_PZ"]),a_kemu[b"e_minus_PZ"]),2.))

# print(a_kemu[b"e_minus_M"][0], a_kemu[b"e_plus_M"][0])
# quit()
B_plus_M_mu = np.sqrt((a_kemu[b"e_plus_PE"]+a_kemu[b"K_Kst_PE"]+a_kemu[b"e_minus_PE"])**2. 
	          -(a_kemu[b"e_plus_PX"]+a_kemu[b"K_Kst_PX"]+a_kemu[b"e_minus_PX"])**2.
	          -(a_kemu[b"e_plus_PY"]+a_kemu[b"K_Kst_PY"]+a_kemu[b"e_minus_PY"])**2.
	          -(a_kemu[b"e_plus_PZ"]+a_kemu[b"K_Kst_PZ"]+a_kemu[b"e_minus_PZ"])**2.)

B_plus_M_e = np.sqrt((a_kemu[b"e_plus_PE"]+a_kemu[b"K_Kst_PE"]+np.sqrt(np.power(a_kemu[b"e_minus_PE"],2.)-105.14*105.14))**2. 
	          -(a_kemu[b"e_plus_PX"]+a_kemu[b"K_Kst_PX"]+a_kemu[b"e_minus_PX"])**2.
	          -(a_kemu[b"e_plus_PY"]+a_kemu[b"K_Kst_PY"]+a_kemu[b"e_minus_PY"])**2.
	          -(a_kemu[b"e_plus_PZ"]+a_kemu[b"K_Kst_PZ"]+a_kemu[b"e_minus_PZ"])**2.)


# plt.hist(B_plus_M_mu-B_plus_M_e,bins=50)
# plt.show()
# quit()




# plt.figure(figsize=(8,8))
# plt.subplot(2,2,1)
# plt.hist(a_kemu[b"B_plus_M"], bins=100)
# plt.subplot(2,2,2)
# plt.hist(B_plus_M, bins=100)
# # plt.subplot(2,2,3)
# # plt.hist2d(B_plus_M, a_kemu[b"Kemu_MKl"], bins=100, norm=LogNorm())
# # plt.subplot(2,2,4)
# # plt.hist2d(B_plus_M, B_plus_M_co, bins=100, norm=LogNorm())

# plt.subplot(2,2,3)
# plt.hist2d(B_plus_M, a_kemu[b"B_plus_M"], bins=100, norm=LogNorm())

# # plt.subplot(2,2,4)
# # plt.hist2d(B_plus_M, B_plus_e, bins=100, norm=LogNorm())

# plt.subplot(2,2,4)
# plt.hist(B_plus_M-B_plus_e, bins=100)

# plt.show()


# quit()




def compute_where_combiBDT(array):
		where = np.where((((array[b"passTrigCat0"]==1)&(array[b"BDTGETOSRun3T"]>0.78))|((array[b"passTrigCat1"]==1)&(array[b"BDTGfixedRun3T"]>0.75))|((array[b"passTrigCat2"]==1)&(array[b"BDTGfixedRun3T"]>0.8)) )
						& (array[b"B_plus_M"]>4880) & (array[b"B_plus_M"]<6200)
						)[0]
		return where

def compute_where_combiBDT_window(array):
		where = np.where((((array[b"passTrigCat0"]==1)&(array[b"BDTGETOSRun3T"]>0.78))|((array[b"passTrigCat1"]==1)&(array[b"BDTGfixedRun3T"]>0.75))|((array[b"passTrigCat2"]==1)&(array[b"BDTGfixedRun3T"]>0.8)) )
						& ((array[b"Kemu_TRACK_MKl_l2pi"]<1825)|(array[b"Kemu_TRACK_MKl_l2pi"]>1905))
						& (array[b"B_plus_M"]>4880) & (array[b"B_plus_M"]<6200)
						)[0]
		return where

def compute_where_combiBDT_PIDe4(array):
		where = np.where((((array[b"passTrigCat0"]==1)&(array[b"BDTGETOSRun3T"]>0.78))|((array[b"passTrigCat1"]==1)&(array[b"BDTGfixedRun3T"]>0.75))|((array[b"passTrigCat2"]==1)&(array[b"BDTGfixedRun3T"]>0.8)) )
						& (array[b"e_plus_PIDe"]>4)
						& (array[b"B_plus_M"]>4880) & (array[b"B_plus_M"]<6200)
						)[0]
		return where

def compute_where_combiBDT_PIDe4_window(array):
		where = np.where((((array[b"passTrigCat0"]==1)&(array[b"BDTGETOSRun3T"]>0.78))|((array[b"passTrigCat1"]==1)&(array[b"BDTGfixedRun3T"]>0.75))|((array[b"passTrigCat2"]==1)&(array[b"BDTGfixedRun3T"]>0.8)) )
						& ((array[b"Kemu_TRACK_MKl_l2pi"]<1825)|(array[b"Kemu_TRACK_MKl_l2pi"]>1905))
						& (array[b"e_plus_PIDe"]>4)
						& (array[b"B_plus_M"]>4880) & (array[b"B_plus_M"]<6200)
						)[0]
		return where

def compute_where_combiBDT_PIDe4_BOTH_E_window(array):
		where = np.where((((array[b"passTrigCat0"]==1)&(array[b"BDTGETOSRun3T"]>0.78))|((array[b"passTrigCat1"]==1)&(array[b"BDTGfixedRun3T"]>0.75))|((array[b"passTrigCat2"]==1)&(array[b"BDTGfixedRun3T"]>0.8)) )
						& ((array[b"Kemu_TRACK_MKl_l2pi"]<1825)|(array[b"Kemu_TRACK_MKl_l2pi"]>1905))
						& (array[b"e_plus_PIDe"]>4) & (array[b"e_minus_PIDe"]>4)
						& (array[b"K_Kst_MC15TuneV1_ProbNNk"]>0.2) & (array[b"K_Kst_PIDe"]<0) & (array[b"K_Kst_isMuon"]==0) & (array[b"K_Kst_PIDmu"]<5)
						& (array[b"B_plus_M"]>4880) & (array[b"B_plus_M"]<6200)
						)[0]
		return where

def compute_where_combiBDT_PIDe4_window_no_B_mass(array):
		where = np.where((((array[b"passTrigCat0"]==1)&(array[b"BDTGETOSRun3T"]>0.78))|((array[b"passTrigCat1"]==1)&(array[b"BDTGfixedRun3T"]>0.75))|((array[b"passTrigCat2"]==1)&(array[b"BDTGfixedRun3T"]>0.8)) )
						& ((array[b"Kemu_TRACK_MKl_l2pi"]<1825)|(array[b"Kemu_TRACK_MKl_l2pi"]>1905))
						& (array[b"e_plus_PIDe"]>4)
						)[0]
		return where
def compute_where_combiBDT_PIDe4_BOTH_E_window_no_B_mass(array):
		where = np.where((((array[b"passTrigCat0"]==1)&(array[b"BDTGETOSRun3T"]>0.78))|((array[b"passTrigCat1"]==1)&(array[b"BDTGfixedRun3T"]>0.75))|((array[b"passTrigCat2"]==1)&(array[b"BDTGfixedRun3T"]>0.8)) )
						& ((array[b"Kemu_TRACK_MKl_l2pi"]<1825)|(array[b"Kemu_TRACK_MKl_l2pi"]>1905))
						& (array[b"e_plus_PIDe"]>4) & (array[b"e_minus_PIDe"]>4)
						& (array[b"K_Kst_MC15TuneV1_ProbNNk"]>0.2) & (array[b"K_Kst_PIDe"]<0) & (array[b"K_Kst_isMuon"]==0) & (array[b"K_Kst_PIDmu"]<5)
						)[0]
		return where

def compute_where_combiBDT_PIDe4_window_and_less_than_1885(array):
		where = np.where((((array[b"passTrigCat0"]==1)&(array[b"BDTGETOSRun3T"]>0.78))|((array[b"passTrigCat1"]==1)&(array[b"BDTGfixedRun3T"]>0.75))|((array[b"passTrigCat2"]==1)&(array[b"BDTGfixedRun3T"]>0.8)) )
						& ((array[b"Kemu_TRACK_MKl_l2pi"]<1825)|(array[b"Kemu_TRACK_MKl_l2pi"]>1905))
						& (array[b"e_plus_PIDe"]>4)
						& (array[b"B_plus_M"]>4880) & (array[b"B_plus_M"]<6200)
						& (array[b"Kemu_MKl"]<1885)
						)[0]
		return where


def compute_where_BDT(array):
		where = np.where(((array[b"cascadeBDTGfixedRun3T"]>BDT_cut)|(array[b"Kemu_MKl"]>1885))
						& (((array[b"passTrigCat0"]==1)&(array[b"BDTGETOSRun3T"]>0.78))|((array[b"passTrigCat1"]==1)&(array[b"BDTGfixedRun3T"]>0.75))|((array[b"passTrigCat2"]==1)&(array[b"BDTGfixedRun3T"]>0.8)) )
						& (array[b"B_plus_M"]>4880) & (array[b"B_plus_M"]<6200)
						)[0]
		return where

def compute_where_BDT_window(array):
		where = np.where(((array[b"cascadeBDTGfixedRun3T"]>BDT_cut)|(array[b"Kemu_MKl"]>1885))
						& ((array[b"Kemu_TRACK_MKl_l2pi"]<1825)|(array[b"Kemu_TRACK_MKl_l2pi"]>1905))
						& (((array[b"passTrigCat0"]==1)&(array[b"BDTGETOSRun3T"]>0.78))|((array[b"passTrigCat1"]==1)&(array[b"BDTGfixedRun3T"]>0.75))|((array[b"passTrigCat2"]==1)&(array[b"BDTGfixedRun3T"]>0.8)) )
						& (array[b"B_plus_M"]>4880) & (array[b"B_plus_M"]<6200)
						)[0]
		return where

def compute_where_BDT_PIDe4(array):
		where = np.where(((array[b"cascadeBDTGfixedRun3T"]>BDT_cut)|(array[b"Kemu_MKl"]>1885))
						& (array[b"e_plus_PIDe"]>4)
						& (((array[b"passTrigCat0"]==1)&(array[b"BDTGETOSRun3T"]>0.78))|((array[b"passTrigCat1"]==1)&(array[b"BDTGfixedRun3T"]>0.75))|((array[b"passTrigCat2"]==1)&(array[b"BDTGfixedRun3T"]>0.8)) )
						& (array[b"B_plus_M"]>4880) & (array[b"B_plus_M"]<6200)
						)[0]
		return where
def compute_where_BDT_PIDe4_window(array):
		where = np.where(((array[b"cascadeBDTGfixedRun3T"]>BDT_cut)|(array[b"Kemu_MKl"]>1885))
						& ((array[b"Kemu_TRACK_MKl_l2pi"]<1825)|(array[b"Kemu_TRACK_MKl_l2pi"]>1905))
						& (array[b"e_plus_PIDe"]>4)
						& (((array[b"passTrigCat0"]==1)&(array[b"BDTGETOSRun3T"]>0.78))|((array[b"passTrigCat1"]==1)&(array[b"BDTGfixedRun3T"]>0.75))|((array[b"passTrigCat2"]==1)&(array[b"BDTGfixedRun3T"]>0.8)) )
						& (array[b"B_plus_M"]>4880) & (array[b"B_plus_M"]<6200)
						)[0]
		return where

def compute_where_BDT_PIDe4_window_no_B_mass(array):
		where = np.where(((array[b"cascadeBDTGfixedRun3T"]>BDT_cut)|(array[b"Kemu_MKl"]>1885))
						& ((array[b"Kemu_TRACK_MKl_l2pi"]<1825)|(array[b"Kemu_TRACK_MKl_l2pi"]>1905))
						& (array[b"e_plus_PIDe"]>4)
						& (((array[b"passTrigCat0"]==1)&(array[b"BDTGETOSRun3T"]>0.78))|((array[b"passTrigCat1"]==1)&(array[b"BDTGfixedRun3T"]>0.75))|((array[b"passTrigCat2"]==1)&(array[b"BDTGfixedRun3T"]>0.8)) )
						)[0]
		return where

def compute_where_BDT_PIDe4_window_and_less_than_1885(array):
		where = np.where(((array[b"cascadeBDTGfixedRun3T"]>BDT_cut)|(array[b"Kemu_MKl"]>1885))
						& ((array[b"Kemu_TRACK_MKl_l2pi"]<1825)|(array[b"Kemu_TRACK_MKl_l2pi"]>1905))
						& (array[b"e_plus_PIDe"]>4)
						& (((array[b"passTrigCat0"]==1)&(array[b"BDTGETOSRun3T"]>0.78))|((array[b"passTrigCat1"]==1)&(array[b"BDTGfixedRun3T"]>0.75))|((array[b"passTrigCat2"]==1)&(array[b"BDTGfixedRun3T"]>0.8)) )
						& (array[b"B_plus_M"]>4880) & (array[b"B_plus_M"]<6200)
						& (array[b"Kemu_MKl"]<1885)
						)[0]
		return where

def compute_where_both_cascades(array):
		where = np.where(((array[b"Kemu_TRACK_MKl_l2pi"]<1825)|(array[b"Kemu_TRACK_MKl_l2pi"]>1905))
						& (array[b"Kemu_MKl"]>1885)
						& (array[b"e_plus_PIDe"]>4)
						& (((array[b"passTrigCat0"]==1)&(array[b"BDTGETOSRun3T"]>0.78))|((array[b"passTrigCat1"]==1)&(array[b"BDTGfixedRun3T"]>0.75))|((array[b"passTrigCat2"]==1)&(array[b"BDTGfixedRun3T"]>0.8)) )
						& (array[b"B_plus_M"]>4880) & (array[b"B_plus_M"]<6200)
						)[0]
		return where

def compute_where_both_cascades_no_B_mass(array):
		where = np.where(((array[b"Kemu_TRACK_MKl_l2pi"]<1825)|(array[b"Kemu_TRACK_MKl_l2pi"]>1905))
						& (array[b"Kemu_MKl"]>1885)
						& (array[b"e_plus_PIDe"]>4)
						& (((array[b"passTrigCat0"]==1)&(array[b"BDTGETOSRun3T"]>0.78))|((array[b"passTrigCat1"]==1)&(array[b"BDTGfixedRun3T"]>0.75))|((array[b"passTrigCat2"]==1)&(array[b"BDTGfixedRun3T"]>0.8)) )
						)[0]
		return where


if make_plots == True:
	plt.figure(figsize=(12,8))

	string_name_list = ['Signal', 'Cascades', 'Kemu']

	for i, array_i in enumerate([a_signal, a_cascade, a_kemu]):

		string_name = string_name_list[i]

		ax = plt.subplot(2,3,i+1)

		

		# plt.title('All (preselec, PIDe>3)')
		plt.hist2d(array_i[b"cascadeBDTGfixedRun3T"], array_i[b"Kemu_MKl"], range=[[0,1],[800,5300]], bins=100, norm=LogNorm())
		plt.axvline(x=BDT_cut, c='r', linestyle='--')
		plt.colorbar()
		plt.xlabel('cascadeBDT')
		plt.ylabel('m(Ke)')
		plt.text(0.95, 0.95,string_name+'- preselec',
	     horizontalalignment='right',
	     verticalalignment='top',
	     transform = ax.transAxes, fontsize=10)

		if string_name == 'Kemu':
			where_combiBDT_PIDe4 = compute_where_combiBDT_PIDe4_window(array_i)
		else:
			where_combiBDT_PIDe4 = compute_where_combiBDT_PIDe4_BOTH_E_window(array_i)

		ax = plt.subplot(2,3,i+1+3)
		if i == 0:
			rect = patches.Rectangle((0, 800), BDT_cut, 1885-800, linewidth=1, edgecolor='r', facecolor='r',alpha=0.2)
			ax.add_patch(rect)
			rect = patches.Rectangle((BDT_cut, 800), 1-BDT_cut, 1885-800, linewidth=1, edgecolor='g', facecolor='g',alpha=0.2)
			ax.add_patch(rect)
		# plt.title('apply comiBDT, PIDe>4')
		plt.hist2d(array_i[b"cascadeBDTGfixedRun3T"][where_combiBDT_PIDe4], array_i[b"Kemu_MKl"][where_combiBDT_PIDe4], range=[[0,1],[800,5300]], bins=100, norm=LogNorm())
		plt.axvline(x=BDT_cut, c='r', linestyle='--')
		plt.axhline(y=1885, c='k', linestyle='--')
		plt.colorbar()
		plt.xlabel('cascadeBDT')
		plt.ylabel('m(Ke)')
		plt.text(0.95, 0.95,string_name+'- all cuts',
	     horizontalalignment='right',
	     verticalalignment='top',
	     transform = ax.transAxes, fontsize=10)

	plt.savefig('plots_kemu/6_mKe_BDT.pdf',bbox_inches='tight')
	plt.close('all')


if make_plots == True:
	plt.figure(figsize=(12,8))

	string_name_list = ['Signal', 'Cascades', 'Kemu']

	for i, array_i in enumerate([a_signal, a_cascade, a_kemu]):

		num = np.shape(array_i[b"passTrigCat0"])[0]

		combiBDT_value = np.empty(num)
		for ii in range(0, num):
			trig = [array_i[b"passTrigCat0"][ii],array_i[b"passTrigCat1"][ii],array_i[b"passTrigCat2"][ii]]
			if trig[0] == 1:
				combiBDT_value[ii] = array_i[b"BDTGETOSRun3T"][ii]
			else:
				combiBDT_value[ii] = array_i[b"BDTGfixedRun3T"][ii]


		string_name = string_name_list[i]


		ax = plt.subplot(2,3,i+1)
		# plt.title('All (preselec, PIDe>3)')
		plt.hist2d(array_i[b"cascadeBDTGfixedRun3T"], combiBDT_value, range=[[0,1],[0,1]], bins=100, norm=LogNorm())
		plt.axvline(x=BDT_cut, c='r', linestyle='--')
		plt.colorbar()
		plt.xlabel('cascadeBDT')
		plt.ylabel('combinatorialBDT')
		plt.text(0.95, 0.05,string_name+'- preselec',
	     horizontalalignment='right',
	     verticalalignment='bottom',
	     transform = ax.transAxes, fontsize=10)

		if string_name == 'Kemu':
			where_combiBDT_PIDe4 = compute_where_combiBDT_PIDe4_window(array_i)
		else:
			where_combiBDT_PIDe4 = compute_where_combiBDT_PIDe4_BOTH_E_window(array_i)

		ax = plt.subplot(2,3,i+1+3)
		# plt.title('apply comiBDT, PIDe>4')
		plt.hist2d(array_i[b"cascadeBDTGfixedRun3T"][where_combiBDT_PIDe4], combiBDT_value[where_combiBDT_PIDe4], range=[[0,1],[0,1]], bins=100, norm=LogNorm())
		plt.axvline(x=BDT_cut, c='r', linestyle='--')
		plt.colorbar()
		plt.xlabel('cascadeBDT')
		plt.ylabel('combinatorialBDT')
		plt.text(0.95, 0.05,string_name+'- all cuts',
	     horizontalalignment='right',
	     verticalalignment='bottom',
	     transform = ax.transAxes, fontsize=10)
		
	plt.savefig('plots_kemu/6_BDT_BDT.pdf',bbox_inches='tight')
	plt.close('all')




# where_combiBDT_PIDe4 = compute_where_combiBDT_PIDe4_window_no_B_mass(a_cascade)
# print(np.shape(where_combiBDT_PIDe4))

# where_combiBDT_PIDe4 = compute_where_combiBDT_PIDe4_BOTH_E_window_no_B_mass(a_cascade)
# print(np.shape(where_combiBDT_PIDe4))
# plt.figure(figsize=(8,4))
# plt.subplot(1,2,1)
# plt.hist2d(a_cascade[b"e_plus_PIDe"], a_cascade[b"e_minus_PIDe"], bins=50, norm=LogNorm())
# plt.subplot(1,2,2)
# plt.hist2d(a_cascade[b"e_plus_PIDe"][where_combiBDT_PIDe4], a_cascade[b"e_minus_PIDe"][where_combiBDT_PIDe4], bins=50, norm=LogNorm())
# plt.show()
# quit()



plt.figure(figsize=(12,12))

string_name_list = ['Signal', 'Cascades', 'Kemu']

for i, array_i in enumerate([a_signal, a_cascade, a_kemu]):

	string_name = string_name_list[i]


	ax = plt.subplot(3,3,i+1)
	# plt.title('All (preselec, PIDe>3)')
	plt.hist2d(array_i[b"cascadeBDTGfixedRun3T"], array_i[b"B_plus_M"], range=[[0,1],[4400,6700]], bins=100, norm=LogNorm())
	plt.axvline(x=BDT_cut, c='r', linestyle='--')
	plt.colorbar()
	plt.xlabel('cascadeBDT')
	plt.ylabel('m(B)')
	plt.text(0.95, 0.05,string_name+'- preselec',
     horizontalalignment='right',
     verticalalignment='bottom',
     transform = ax.transAxes, fontsize=10)

	if i == 2:
		plt.axhspan(4880, 6200, alpha=1., color='r')

	where_combiBDT_PIDe4 = compute_where_combiBDT_PIDe4_window_no_B_mass(array_i)

	ax = plt.subplot(3,3,i+1+3)
	# plt.title('apply comiBDT, PIDe>4')
	plt.hist2d(array_i[b"cascadeBDTGfixedRun3T"][where_combiBDT_PIDe4], array_i[b"B_plus_M"][where_combiBDT_PIDe4], range=[[0,1],[4400,6700]], bins=100, norm=LogNorm())
	plt.axvline(x=BDT_cut, c='r', linestyle='--')
	plt.colorbar()
	plt.xlabel('cascadeBDT')
	plt.ylabel('m(B)')
	plt.text(0.95, 0.05,string_name+'- all cuts',
     horizontalalignment='right',
     verticalalignment='bottom',
     transform = ax.transAxes, fontsize=10)

	if i == 2:
		plt.axhspan(4880, 6200, alpha=1., color='r')

bin_count_list = [100, 100, 100]

for i2, array_i in enumerate([a_signal, a_cascade, a_kemu]):

	where_combiBDT_PIDe4 = compute_where_combiBDT_PIDe4_window_no_B_mass(array_i)

	# ax = plt.subplot(3,3,i+1+i2+1+3)
	# n, bins = np.histogram(array_i[b"B_plus_M"][where_combiBDT_PIDe4], range=[4400,6700], bins=50)
	# x = bins[:-1] + ((bins[1]-bins[0])/2.)
	# y = np.zeros(np.shape(x))
	# for index in range(0,np.shape(x)[0]):
	# 	counts_total = np.shape(np.where( (array_i[b"B_plus_M"]>bins[index])&(array_i[b"B_plus_M"]<bins[index+1]) ))[1]
	# 	counts_accept = np.shape(np.where( (array_i[b"B_plus_M"]>bins[index])&(array_i[b"B_plus_M"]<bins[index+1])&(array_i[b"cascadeBDTGfixedRun3T"]>BDT_cut) ))[1]
	# 	if counts_total != 0 and counts_accept != 0:
	# 		y[index] = counts_accept/counts_total
	# plt.plot(x,y)
	# plt.ylim(0,1)


	ax = plt.subplot(3,3,i+1+i2+1+3)

	data = np.swapaxes(np.asarray([array_i[b"cascadeBDTGfixedRun3T"], array_i[b"B_plus_M"]]),0,1)
	data = data[data[:,1].argsort()]
	size = np.shape(data)[0]
	bin_count = bin_count_list[i2]
	num_bins = np.floor_divide(size,bin_count)
	at_count = 0
	x = np.zeros(num_bins+1)
	y = np.zeros(num_bins+1)
	x_error = np.zeros((2,num_bins+1))
	y_error = np.zeros(num_bins+1)
	for index in range(0, num_bins):
		data_i = data[index*bin_count:(index+1)*bin_count]
		x[index] = np.mean(data_i[:,1])
		y[index] = np.shape(np.where(data_i[:,0]>BDT_cut))[1]/np.shape(np.where(data_i[:,0]>0.))[1]
		x_error[0][index] = np.mean(data_i[:,1])-np.amin(data_i[:,1])
		x_error[1][index] = np.amax(data_i[:,1])-np.mean(data_i[:,1])
		y_error[index] = y[index]*np.sqrt((np.sqrt(np.shape(np.where(data_i[:,0]>BDT_cut))[1])/np.shape(np.where(data_i[:,0]>BDT_cut))[1])**2+(np.sqrt(np.shape(np.where(data_i[:,0]>0.))[1])/np.shape(np.where(data_i[:,0]>0.))[1])**2)
		at_count += 100
	data_i = data[at_count:]
	x[-1] = np.mean(data_i[:,1])
	y[-1] = np.shape(np.where(data_i[:,0]>BDT_cut))[1]/np.shape(np.where(data_i[:,0]>0.))[1]
	x_error[0][-1] = np.mean(data_i[:,1])-np.amin(data_i[:,1])
	x_error[1][-1] = np.amax(data_i[:,1])-np.mean(data_i[:,1])
	y_error[-1] = y[-1]*np.sqrt((np.sqrt(np.shape(np.where(data_i[:,0]>BDT_cut))[1])/np.shape(np.where(data_i[:,0]>BDT_cut))[1])**2+(np.sqrt(np.shape(np.where(data_i[:,0]>0.))[1])/np.shape(np.where(data_i[:,0]>0.))[1])**2)
	plt.errorbar(x, y, xerr=x_error, yerr=y_error, fmt='o', c='tab:red', label='Pre_cuts', marker='s')

	data = np.swapaxes(np.asarray([array_i[b"cascadeBDTGfixedRun3T"][where_combiBDT_PIDe4], array_i[b"B_plus_M"][where_combiBDT_PIDe4]]),0,1)
	data = data[data[:,1].argsort()]
	size = np.shape(data)[0]
	bin_count = bin_count_list[i2]
	num_bins = np.floor_divide(size,bin_count)
	at_count = 0
	x = np.zeros(num_bins+1)
	y = np.zeros(num_bins+1)
	x_error = np.zeros((2,num_bins+1))
	y_error = np.zeros(num_bins+1)
	for index in range(0, num_bins):
		data_i = data[index*bin_count:(index+1)*bin_count]
		x[index] = np.mean(data_i[:,1])
		y[index] = np.shape(np.where(data_i[:,0]>BDT_cut))[1]/np.shape(np.where(data_i[:,0]>0.))[1]
		x_error[0][index] = np.mean(data_i[:,1])-np.amin(data_i[:,1])
		x_error[1][index] = np.amax(data_i[:,1])-np.mean(data_i[:,1])
		y_error[index] = y[index]*np.sqrt((np.sqrt(np.shape(np.where(data_i[:,0]>BDT_cut))[1])/np.shape(np.where(data_i[:,0]>BDT_cut))[1])**2+(np.sqrt(np.shape(np.where(data_i[:,0]>0.))[1])/np.shape(np.where(data_i[:,0]>0.))[1])**2)
		at_count += 100
	data_i = data[at_count:]
	x[-1] = np.mean(data_i[:,1])
	y[-1] = np.shape(np.where(data_i[:,0]>BDT_cut))[1]/np.shape(np.where(data_i[:,0]>0.))[1]
	x_error[0][-1] = np.mean(data_i[:,1])-np.amin(data_i[:,1])
	x_error[1][-1] = np.amax(data_i[:,1])-np.mean(data_i[:,1])
	y_error[-1] = y[-1]*np.sqrt((np.sqrt(np.shape(np.where(data_i[:,0]>BDT_cut))[1])/np.shape(np.where(data_i[:,0]>BDT_cut))[1])**2+(np.sqrt(np.shape(np.where(data_i[:,0]>0.))[1])/np.shape(np.where(data_i[:,0]>0.))[1])**2)
	plt.errorbar(x, y, xerr=x_error, yerr=y_error, fmt='o', c='tab:blue', label='Post_cuts', marker='s')
	
	if i2==1: 
		plt.legend()
	plt.xlabel('m(B)')
	plt.ylabel('BDT efficiency')
	plt.axvline(x=4880, c='k', linestyle='--')
	plt.axvline(x=6200, c='k', linestyle='--')
	plt.xlim(4400,6700)
	plt.ylim(0,1)

	# quit()


	
# plt.savefig('plots_kemu/6_BDT_Bmass.pdf',bbox_inches='tight')
plt.savefig('plots_kemu/6_BDT_Bmass.png',bbox_inches='tight')
plt.close('all')





plt.figure(figsize=(12,12))

string_name_list = ['Signal', 'Cascades', 'Kemu']

for i, array_i in enumerate([a_signal, a_cascade, a_kemu]):

	string_name = string_name_list[i]


	if string_name == 'Kemu':
		where_combiBDT_PIDe4 = compute_where_combiBDT_PIDe4_window_no_B_mass(array_i)
	else:
		where_combiBDT_PIDe4 = compute_where_combiBDT_PIDe4_BOTH_E_window_no_B_mass(array_i)

	ax = plt.subplot(3,3,i+1)
	# plt.title('apply comiBDT, PIDe>4')
	plt.hist2d(array_i[b"cascadeBDTGfixedRun3T"][where_combiBDT_PIDe4], array_i[b"B_plus_M"][where_combiBDT_PIDe4], range=[[0,1],[4400,6700]], bins=100, norm=LogNorm())
	plt.axvline(x=BDT_cut, c='r', linestyle='--')
	plt.colorbar()
	plt.xlabel('cascadeBDT')
	plt.ylabel('m(B)')
	plt.text(0.95, 0.05,string_name+'- all cuts (but before casBDT)',
     horizontalalignment='right',
     verticalalignment='bottom',
     transform = ax.transAxes, fontsize=10)

	if i == 2:
		plt.axhspan(4880, 6200, alpha=1., color='r')

bin_count_list = [100, 100, 100]

for i2, array_i in enumerate([a_signal, a_cascade, a_kemu]):

	string_name = string_name_list[i2]

	if string_name == 'Kemu':
		where_combiBDT_PIDe4 = compute_where_combiBDT_PIDe4_window_no_B_mass(array_i)
	else:
		where_combiBDT_PIDe4 = compute_where_combiBDT_PIDe4_BOTH_E_window_no_B_mass(array_i)

	# ax = plt.subplot(3,3,i+1+i2+1+3)
	# n, bins = np.histogram(array_i[b"B_plus_M"][where_combiBDT_PIDe4], range=[4400,6700], bins=50)
	# x = bins[:-1] + ((bins[1]-bins[0])/2.)
	# y = np.zeros(np.shape(x))
	# for index in range(0,np.shape(x)[0]):
	# 	counts_total = np.shape(np.where( (array_i[b"B_plus_M"]>bins[index])&(array_i[b"B_plus_M"]<bins[index+1]) ))[1]
	# 	counts_accept = np.shape(np.where( (array_i[b"B_plus_M"]>bins[index])&(array_i[b"B_plus_M"]<bins[index+1])&(array_i[b"cascadeBDTGfixedRun3T"]>BDT_cut) ))[1]
	# 	if counts_total != 0 and counts_accept != 0:
	# 		y[index] = counts_accept/counts_total
	# plt.plot(x,y)
	# plt.ylim(0,1)


	ax = plt.subplot(3,3,i+1+i2+1+3)

	data = np.swapaxes(np.asarray([array_i[b"cascadeBDTGfixedRun3T"][where_combiBDT_PIDe4], array_i[b"B_plus_M"][where_combiBDT_PIDe4], array_i[b"Kemu_MKl"][where_combiBDT_PIDe4]]),0,1)
	data = data[data[:,1].argsort()]
	size = np.shape(data)[0]
	bin_count = bin_count_list[i2]
	num_bins = np.floor_divide(size,bin_count)
	at_count = 0
	x = np.zeros(num_bins+1)
	y = np.zeros(num_bins+1)
	x_error = np.zeros((2,num_bins+1))
	y_error = np.zeros(num_bins+1)
	for index in range(0, num_bins):
		data_i = data[index*bin_count:(index+1)*bin_count]
		x[index] = np.mean(data_i[:,1])
		y[index] = np.shape(np.where( (data_i[:,0]>BDT_cut)|(data_i[:,2]>1885) ))[1]/np.shape(np.where(data_i[:,0]>0.))[1]
		x_error[0][index] = np.mean(data_i[:,1])-np.amin(data_i[:,1])
		x_error[1][index] = np.amax(data_i[:,1])-np.mean(data_i[:,1])
		y_error[index] = y[index]*np.sqrt((np.sqrt(np.shape(np.where(data_i[:,0]>BDT_cut))[1])/np.shape(np.where(data_i[:,0]>BDT_cut))[1])**2+(np.sqrt(np.shape(np.where(data_i[:,0]>0.))[1])/np.shape(np.where(data_i[:,0]>0.))[1])**2)
		at_count += 100
	data_i = data[at_count:]
	x[-1] = np.mean(data_i[:,1])
	y[-1] = np.shape(np.where(data_i[:,0]>BDT_cut))[1]/np.shape(np.where(data_i[:,0]>0.))[1]
	x_error[0][-1] = np.mean(data_i[:,1])-np.amin(data_i[:,1])
	x_error[1][-1] = np.amax(data_i[:,1])-np.mean(data_i[:,1])
	y_error[-1] = y[-1]*np.sqrt((np.sqrt(np.shape(np.where( (data_i[:,0]>BDT_cut)|(data_i[:,2]>1885) ))[1])/np.shape(np.where( (data_i[:,0]>BDT_cut)|(data_i[:,2]>1885) ))[1])**2+(np.sqrt(np.shape(np.where(data_i[:,0]>0.))[1])/np.shape(np.where(data_i[:,0]>0.))[1])**2)
	plt.errorbar(x, y, xerr=x_error, yerr=y_error, fmt='o', c='tab:blue', label='Post_cuts', marker='s')
	
	# if i2==1: 
		# plt.legend()
	plt.xlabel('m(B)')
	plt.ylabel('BDT efficiency')
	plt.axvline(x=4880, c='k', linestyle='--')
	plt.axvline(x=6200, c='k', linestyle='--')
	plt.xlim(4400,6700)
	plt.ylim(0,1)


	ax = plt.subplot(3,3,i+1+i2+1)

	data = np.swapaxes(np.asarray([array_i[b"cascadeBDTGfixedRun3T"][where_combiBDT_PIDe4], array_i[b"B_plus_M"][where_combiBDT_PIDe4], array_i[b"Kemu_MKl"][where_combiBDT_PIDe4]]),0,1)

	# print(np.shape(data))

	# print(np.where((data[:,0]>BDT_cut)|(data[:,2]>1885)), np.shape(np.where((data[:,0]>BDT_cut)|(data[:,2]>1885))))

	# print(data[:,1], data[np.where((data[:,0]>BDT_cut)|(data[:,2]>1885))][:,1])
	plt.hist([data[:,1], data[np.where((data[:,0]>BDT_cut)|(data[:,2]>1885))][:,1]], range=[4400,6700], bins=50, density=True, label=['Pre casBDT','Post casBDT'], histtype='step')
	# quit()
	# data = data[data[:,1].argsort()]
	# size = np.shape(data)[0]
	# bin_count = bin_count_list[i2]
	# num_bins = np.floor_divide(size,bin_count)
	# at_count = 0
	# x = np.zeros(num_bins+1)
	# y = np.zeros(num_bins+1)
	# x_error = np.zeros((2,num_bins+1))
	# y_error = np.zeros(num_bins+1)
	# for index in range(0, num_bins):
	# 	data_i = data[index*bin_count:(index+1)*bin_count]
	# 	x[index] = np.mean(data_i[:,1])
	# 	y[index] = np.shape(np.where( (data_i[:,0]>BDT_cut)|(data_i[:,2]>1885) ))[1]/np.shape(np.where(data_i[:,0]>0.))[1]
	# 	# x_error[0][index] = np.mean(data_i[:,1])-np.amin(data_i[:,1])
	# 	# x_error[1][index] = np.amax(data_i[:,1])-np.mean(data_i[:,1])
	# 	y_error[index] = y[index]*np.sqrt((np.sqrt(np.shape(np.where(data_i[:,0]>BDT_cut))[1])/np.shape(np.where(data_i[:,0]>BDT_cut))[1])**2+(np.sqrt(np.shape(np.where(data_i[:,0]>0.))[1])/np.shape(np.where(data_i[:,0]>0.))[1])**2)
	# 	at_count += 100
	# data_i = data[at_count:]
	# x[-1] = np.mean(data_i[:,1])
	# y[-1] = np.shape(np.where(data_i[:,0]>BDT_cut))[1]/np.shape(np.where(data_i[:,0]>0.))[1]
	# # x_error[0][-1] = np.mean(data_i[:,1])-np.amin(data_i[:,1])
	# # x_error[1][-1] = np.amax(data_i[:,1])-np.mean(data_i[:,1])
	# y_error[-1] = y[-1]*np.sqrt((np.sqrt(np.shape(np.where( (data_i[:,0]>BDT_cut)|(data_i[:,2]>1885) ))[1])/np.shape(np.where( (data_i[:,0]>BDT_cut)|(data_i[:,2]>1885) ))[1])**2+(np.sqrt(np.shape(np.where(data_i[:,0]>0.))[1])/np.shape(np.where(data_i[:,0]>0.))[1])**2)
	
	# plt.errorbar(x, y, yerr=y_error, fmt='o', c='tab:blue', label='Post_cuts', marker='s')
	if i2 == 2:
		plt.axvspan(4880, 6200, alpha=1., color='r')

	if i2==1: 
		plt.legend(loc='upper right')
	plt.xlabel('m(B)')
	plt.ylabel('normalised')
	plt.axvline(x=4880, c='k', linestyle='--')
	plt.axvline(x=6200, c='k', linestyle='--')
	# plt.xlim(4400,6700)
	# plt.ylim(0,1)

	# quit()


	
# plt.savefig('plots_kemu/6_BDT_Bmass.pdf',bbox_inches='tight')
plt.savefig('plots_kemu/6_BDT_Bmass_2.png',bbox_inches='tight')
plt.close('all')
quit()

where_both_cascades = compute_where_both_cascades(a_kemu)
where_BDT_PIDe4 = compute_where_BDT_PIDe4_window(a_kemu)
where_combiBDT_PIDe4 = compute_where_combiBDT_PIDe4_window(a_kemu)

where_BDT_PIDe4_and_less_than_1885 = compute_where_BDT_PIDe4_window_and_less_than_1885(a_kemu)
where_combiBDT_PIDe4_and_less_than_1885 = compute_where_combiBDT_PIDe4_window_and_less_than_1885(a_kemu)

import matplotlib.patches as mpatches


# plt.figure(figsize=(8,4))
# plt.subplot(1,2,1)
# plt.title('Kemu 2018 data')
# plt.hist([a_kemu[b"Kemu_MKl"][where_combiBDT_PIDe4]]
# 	, label=['just window'], bins=250, histtype='step')
# plt.legend()
# plt.xlabel('m(Ke) MeV')
# plt.subplot(1,2,2)
# plt.title('Log scale')
# plt.hist([a_kemu[b"Kemu_MKl"][where_combiBDT_PIDe4]]
# 	, label=['just window'], bins=250, histtype='step')
# plt.yscale('log')

# plt.xlabel('m(Ke) MeV')
# plt.show()

# if make_plots == True:
plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.title('Kemu 2018 data')
plt.hist([a_kemu[b"Kemu_MKl"][where_both_cascades], a_kemu[b"Kemu_MKl"][where_BDT_PIDe4], a_kemu[b"Kemu_MKl"][where_combiBDT_PIDe4]]
	, label=['Both cascades', 'window + BDT', 'just window'], bins=250, histtype='step')
plt.legend()
plt.xlabel('m(Ke) MeV')
plt.subplot(1,2,2)
plt.title('Log scale')
plt.hist([a_kemu[b"Kemu_MKl"][where_both_cascades], a_kemu[b"Kemu_MKl"][where_BDT_PIDe4], a_kemu[b"Kemu_MKl"][where_combiBDT_PIDe4]]
	, label=['Both cascades', 'window + BDT', 'just window'], bins=250, histtype='step')
plt.yscale('log')
# plt.legend()
green_patch = mpatches.Patch(color='tab:green', label='%d events'%np.shape(where_combiBDT_PIDe4)[0])
orange_patch = mpatches.Patch(color='tab:orange', label='%d events'%np.shape(where_BDT_PIDe4)[0])
blue_patch = mpatches.Patch(color='tab:blue', label='%d events'%np.shape(where_both_cascades)[0])
plt.legend(handles=[green_patch,orange_patch,blue_patch])
plt.xlabel('m(Ke) MeV')
plt.savefig('plots_kemu/6_Ke_mass_window.pdf',bbox_inches='tight')
plt.close('all')



plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.title('Kemu 2018 data')
plt.hist([a_kemu[b"Kemu_TRACK_MKl_l2pi"][where_both_cascades], a_kemu[b"Kemu_TRACK_MKl_l2pi"][where_BDT_PIDe4], a_kemu[b"Kemu_TRACK_MKl_l2pi"][where_combiBDT_PIDe4]]
	, label=['Both cascades', 'window + BDT', 'just window'], bins=250, histtype='step')
plt.legend()
plt.xlabel('m(Ke) MeV')
plt.subplot(1,2,2)
plt.title('Log scale')
plt.hist([a_kemu[b"Kemu_TRACK_MKl_l2pi"][where_both_cascades], a_kemu[b"Kemu_TRACK_MKl_l2pi"][where_BDT_PIDe4], a_kemu[b"Kemu_TRACK_MKl_l2pi"][where_combiBDT_PIDe4]]
	, label=['Both cascades', 'window + BDT', 'just window'], bins=250, histtype='step')
plt.yscale('log')
# plt.legend()
green_patch = mpatches.Patch(color='tab:green', label='%d events'%np.shape(where_combiBDT_PIDe4)[0])
orange_patch = mpatches.Patch(color='tab:orange', label='%d events'%np.shape(where_BDT_PIDe4)[0])
blue_patch = mpatches.Patch(color='tab:blue', label='%d events'%np.shape(where_both_cascades)[0])
plt.legend(handles=[green_patch,orange_patch,blue_patch])
plt.xlabel('m(Ke) MeV')
plt.savefig('plots_kemu/6_Ke2pi_mass_window.png',bbox_inches='tight')
plt.close('all')


plt.figure(figsize=(8,8))
plt.subplot(2,2,1)
plt.title('Kemu 2018 data')
plt.hist([a_kemu[b"Kemu_MKl"][where_both_cascades], a_kemu[b"Kemu_MKl"][where_BDT_PIDe4], a_kemu[b"Kemu_MKl"][where_combiBDT_PIDe4]]
	, label=['Both cascades', 'window + BDT', 'just window'], bins=250, histtype='step')
plt.legend()
plt.xlabel('m(Ke) MeV')


plt.subplot(2,2,2)
plt.hist([a_kemu[b"Kemu_TRACK_MKl_l2pi"][where_both_cascades], a_kemu[b"Kemu_TRACK_MKl_l2pi"][where_BDT_PIDe4], a_kemu[b"Kemu_TRACK_MKl_l2pi"][where_combiBDT_PIDe4]]
	, label=['Both cascades', 'window + BDT', 'just window'], bins=250, histtype='step')
plt.legend()
green_patch = mpatches.Patch(color='tab:green', label='%d events (with m(Ke)<1885: %d)'%(np.shape(where_combiBDT_PIDe4)[0],np.shape(where_combiBDT_PIDe4_and_less_than_1885)[0]))
orange_patch = mpatches.Patch(color='tab:orange', label='%d events (with m(Ke)<1885: %d)'%(np.shape(where_BDT_PIDe4)[0],np.shape(where_BDT_PIDe4_and_less_than_1885)[0]))
blue_patch = mpatches.Patch(color='tab:blue', label='%d events (with m(Ke)<1885: %d)'%(np.shape(where_both_cascades)[0],0))
plt.legend(handles=[green_patch,orange_patch,blue_patch])
plt.xlabel('m(Ke(pi)) MeV')


plt.subplot(2,2,3)
plt.hist([a_kemu[b"Kemu_MKl"][where_both_cascades], a_kemu[b"Kemu_MKl"][where_BDT_PIDe4], a_kemu[b"Kemu_MKl"][where_combiBDT_PIDe4]]
	, label=['Both cascades', 'window + BDT', 'just window'], bins=70, histtype='step', range=[600,1600])
plt.xlabel('m(Ke) MeV')

plt.subplot(2,2,4)
plt.hist([a_kemu[b"Kemu_TRACK_MKl_l2pi"][where_both_cascades], a_kemu[b"Kemu_TRACK_MKl_l2pi"][where_BDT_PIDe4], a_kemu[b"Kemu_TRACK_MKl_l2pi"][where_combiBDT_PIDe4]]
	, label=['Both cascades', 'window + BDT', 'just window'], bins=70, histtype='step', range=[600,1600])
plt.xlabel('m(Ke(pi)) MeV')

plt.savefig('plots_kemu/6_Ke_Ke2pi_mass_window.pdf',bbox_inches='tight')
plt.close('all')





where_both_cascades = compute_where_both_cascades_no_B_mass(a_kemu)
where_BDT_PIDe4 = compute_where_BDT_PIDe4_window_no_B_mass(a_kemu)
where_combiBDT_PIDe4 = compute_where_combiBDT_PIDe4_window_no_B_mass(a_kemu)

plt.figure(figsize=(5,4))
# plt.subplot(1,2,1)
plt.title('Kemu 2018 data')
plt.hist([B_plus_M_e[where_both_cascades], B_plus_M_e[where_BDT_PIDe4], B_plus_M_e[where_combiBDT_PIDe4]]
	, label=['Both cascades', 'window + BDT', 'just window'], bins=120, histtype='step',density='True')

# data_list = [B_plus_M_e[where_both_cascades], B_plus_M_e[where_BDT_PIDe4], B_plus_M_e[where_combiBDT_PIDe4]]
# label_list = ['Both cascades', 'window + BDT', 'just window']
# for i in range(0, 3):
# 	weights = np.ones(np.shape(data_list[i]))
# 	n, bins = np.histogram(data_list[i], range=[4300,6700], bins=120, weights=weights)
# 	n_err = np.sqrt(np.histogram(data_list[i], range=[4300,6700], bins=120, weights=weights**2)[0])
# 	x = bins[:-1] + ((bins[1]-bins[0])/2.)
# 	print(np.shape(x), np.shape(n), np.shape(n_err))
# 	plt.errorbar(x, n, yerr=n_err,label=label_list[i])

plt.axvspan(4880, 6200, alpha=1., color='r')

plt.legend()
plt.xlabel('m(Kee) MeV')
# plt.subplot(1,2,2)
# # plt.hist([B_plus_M_mu[where_both_cascades], B_plus_M_mu[where_BDT_PIDe4], B_plus_M_mu[where_combiBDT_PIDe4]]
# # 	, label=['Both cascades', 'window + BDT', 'just window'], bins=120, histtype='step')
# plt.hist([a_kemu[b"B_plus_M"][where_both_cascades], a_kemu[b"B_plus_M"][where_BDT_PIDe4], a_kemu[b"B_plus_M"][where_combiBDT_PIDe4]]
# 	, label=['Both cascades', 'window + BDT', 'just window'], bins=120, histtype='step')

# plt.axvspan(4880, 6200, alpha=1., color='r')

# plt.xlabel('m(Kemu) MeV')
plt.savefig('plots_kemu/6_Kee_mass_window.png',bbox_inches='tight')
plt.close('all')
quit()

'''
# plot_array = a_kemu[b"Kemu_MKl"]
# xlabel = 'Kemu_MKl'
# filename = 'plots_kemu/6_Kemu_MKl.pdf'

plot_array = a_kemu[b"Kemu_TRACK_MKl_l2pi"]
xlabel = 'Kemu_TRACK_MKl_l2pi'
filename = 'plots_kemu/6_Kemu_TRACK_MKl_l2pi.pdf'

plt.figure(figsize=(8,4*5))

plt.subplot(5,2,1)
plt.title('Kemu 2018 data')
plt.hist([plot_array[where_both_cascades], plot_array[where_BDT_PIDe4], plot_array[where_combiBDT_PIDe4]], 
	label=['Both cascade cuts', 'window cut + BDT', 'just window'], bins=250, histtype='step')
plt.xlabel(xlabel)
plt.legend()
plt.subplot(5,2,2)
plt.hist([plot_array[where_both_cascades], plot_array[where_BDT_PIDe4], plot_array[where_combiBDT_PIDe4]], 
	label=['Both cascade cuts', 'window cut + BDT', 'just window'], bins=250, histtype='step')
plt.yscale('log')
green_patch = mpatches.Patch(color='tab:green', label='%d events'%np.shape(where_combiBDT_PIDe4)[0])
orange_patch = mpatches.Patch(color='tab:orange', label='%d events'%np.shape(where_BDT_PIDe4)[0])
blue_patch = mpatches.Patch(color='tab:blue', label='%d events'%np.shape(where_both_cascades)[0])
plt.legend(handles=[green_patch,orange_patch,blue_patch])

plt.subplot(5,2,3)
plt.title('Kemu 2018 data')
plt.hist([plot_array[where_both_cascades], plot_array[where_BDT_PIDe4], plot_array[where_combiBDT_PIDe4]], range=[600,1600], 
	label=['Both cascade cuts', 'window cut + BDT', 'just window'], bins=150, histtype='step')
plt.xlabel(xlabel)
plt.subplot(5,2,4)
plt.hist([plot_array[where_both_cascades], plot_array[where_BDT_PIDe4], plot_array[where_combiBDT_PIDe4]], range=[600,1600], 
	label=['All (preselection and PIDe>3)', 'combBDT + casBDT>0.63, PIDe>3', 'combBDT + casBDT>0.63, PIDe>4', 'combBDT, PIDe>3'], bins=150, histtype='step')
plt.yscale('log')

plt.subplot(5,2,5)
plt.title('Kemu 2018 data')
plt.hist([plot_array[where_both_cascades], plot_array[where_BDT_PIDe4], plot_array[where_combiBDT_PIDe4]], range=[600,1600], 
	label=['All (preselection and PIDe>3)', 'combBDT + casBDT>0.63, PIDe>3', 'combBDT + casBDT>0.63, PIDe>4', 'combBDT, PIDe>3'], bins=50, histtype='step')
plt.xlabel(xlabel)
plt.subplot(5,2,6)
plt.hist([plot_array[where_both_cascades], plot_array[where_BDT_PIDe4], plot_array[where_combiBDT_PIDe4]], range=[600,1600], 
	label=['All (preselection and PIDe>3)', 'combBDT + casBDT>0.63, PIDe>3', 'combBDT + casBDT>0.63, PIDe>4', 'combBDT, PIDe>3'], bins=50, histtype='step')
plt.yscale('log')

plt.subplot(5,2,7)
plt.title('Kemu 2018 data')
plt.hist([plot_array[where_both_cascades], plot_array[where_BDT_PIDe4], plot_array[where_combiBDT_PIDe4]], range=[700,1100], 
	label=['All (preselection and PIDe>3)', 'combBDT + casBDT>0.63, PIDe>3', 'combBDT + casBDT>0.63, PIDe>4', 'combBDT, PIDe>3'], bins=150, histtype='step')
plt.xlabel(xlabel)
plt.subplot(5,2,8)
plt.hist([plot_array[where_both_cascades], plot_array[where_BDT_PIDe4], plot_array[where_combiBDT_PIDe4]], range=[700,1100], 
	label=['All (preselection and PIDe>3)', 'combBDT + casBDT>0.63, PIDe>3', 'combBDT + casBDT>0.63, PIDe>4', 'combBDT, PIDe>3'], bins=150, histtype='step')
plt.yscale('log')

plt.subplot(5,2,9)
plt.title('Kemu 2018 data')
plt.hist([plot_array[where_both_cascades], plot_array[where_BDT_PIDe4], plot_array[where_combiBDT_PIDe4]], range=[700,1100], 
	label=['All (preselection and PIDe>3)', 'combBDT + casBDT>0.63, PIDe>3', 'combBDT + casBDT>0.63, PIDe>4', 'combBDT, PIDe>3'], bins=30, histtype='step')
plt.xlabel(xlabel)
plt.subplot(5,2,10)
plt.hist([plot_array[where_both_cascades], plot_array[where_BDT_PIDe4], plot_array[where_combiBDT_PIDe4]], range=[700,1100], 
	label=['All (preselection and PIDe>3)', 'combBDT + casBDT>0.63, PIDe>3', 'combBDT + casBDT>0.63, PIDe>4', 'combBDT, PIDe>3'], bins=30, histtype='step')
plt.yscale('log')

plt.xlabel(xlabel)
plt.savefig(filename,bbox_inches='tight')
plt.close('all')
'''

quit()
















where_combiBDT = compute_where_combiBDT(a_kemu)

if make_plots == True:
	plt.figure(figsize=(8,4))
	plt.subplot(1,2,1)
	plt.title('Kemu 2018 data')
	plt.hist([a_kemu[b"cascadeBDTGfixedRun3T"],a_kemu[b"cascadeBDTGfixedRun3T"][where_combiBDT]], label=['all (after preselection + PID)','post combiBDT'], bins=50, histtype='step')
	plt.axvline(x=BDT_cut, c='k', linestyle='--')
	plt.legend()
	plt.xlabel('cascadeBDT')
	plt.subplot(1,2,2)
	plt.hist([a_kemu[b"cascadeBDTGfixedRun3T"],a_kemu[b"cascadeBDTGfixedRun3T"][where_combiBDT]], density=True, label=['all','post combiBDT'], bins=50, histtype='step')
	plt.axvline(x=BDT_cut, c='k', linestyle='--')
	plt.legend()
	plt.xlabel('cascadeBDT')
	plt.ylabel('normalised')
	plt.savefig('plots_kemu/BDT.png',bbox_inches='tight')
	plt.close('all')



where_BDT = compute_where_BDT(a_kemu)
where_BDT_PIDe4 = compute_where_BDT_PIDe4(a_kemu)
where_combiBDT_PIDe4 = compute_where_combiBDT_PIDe4(a_kemu)

if make_plots == True:
	plt.figure(figsize=(8,4))
	plt.subplot(1,2,1)
	plt.title('Kemu 2018 data')
	plt.hist([a_kemu[b"Kemu_MKl"], a_kemu[b"Kemu_MKl"][where_BDT], a_kemu[b"Kemu_MKl"][where_BDT_PIDe4], a_kemu[b"Kemu_MKl"][where_combiBDT]], label=['All (preselection and PIDe>3)', 'combBDT + casBDT>0.63, PIDe>3', 'combBDT + casBDT>0.63, PIDe>4', 'combBDT, PIDe>3'], bins=250, histtype='step')
	# plt.axvline(x=1825, c='k', linestyle='--', linewidth=0.5)
	# plt.axvline(x=1905, c='k', linestyle='--', linewidth=0.5)
	plt.legend()
	plt.xlabel('m(Ke) MeV')
	plt.subplot(1,2,2)
	plt.hist([a_kemu[b"Kemu_MKl"], a_kemu[b"Kemu_MKl"][where_BDT], a_kemu[b"Kemu_MKl"][where_BDT_PIDe4], a_kemu[b"Kemu_MKl"][where_combiBDT]], label=['All (preselection and PIDe>3)', 'combBDT + casBDT>0.63, PIDe>3', 'combBDT + casBDT>0.63, PIDe>4', 'combBDT, PIDe>3'], bins=250, histtype='step')
	plt.yscale('log')
	# plt.axvline(x=1825, c='k', linestyle='--', linewidth=0.5)
	# plt.axvline(x=1905, c='k', linestyle='--', linewidth=0.5)
	plt.legend()
	plt.xlabel('m(Ke) MeV')
	plt.savefig('plots_kemu/Ke_mass.png',bbox_inches='tight')
	plt.close('all')


	plt.figure(figsize=(8,4))
	plt.subplot(1,2,1)
	plt.title('Kemu 2018 data')
	plt.hist([a_kemu[b"Kemu_MKl"], a_kemu[b"Kemu_MKl"][where_BDT], a_kemu[b"Kemu_MKl"][where_BDT_PIDe4], a_kemu[b"Kemu_MKl"][where_combiBDT]], range=[600,1200], label=['All (preselection, PIDe>3)', 'combBDT + casBDT>0.63, PIDe>3', 'combBDT + casBDT>0.63, PIDe>4', 'combBDT, PIDe>3'], bins=100, histtype='step')
	# plt.axvline(x=1825, c='k', linestyle='--', linewidth=0.5)
	# plt.axvline(x=1905, c='k', linestyle='--', linewidth=0.5)
	# plt.legend()
	plt.xlabel('m(Ke) MeV')
	plt.subplot(1,2,2)
	plt.hist([a_kemu[b"Kemu_MKl"], a_kemu[b"Kemu_MKl"][where_BDT], a_kemu[b"Kemu_MKl"][where_BDT_PIDe4], a_kemu[b"Kemu_MKl"][where_combiBDT]], range=[600,1200], label=['All (preselection, PIDe>3)', 'combBDT + casBDT>0.63, PIDe>3', 'combBDT + casBDT>0.63, PIDe>4', 'combBDT, PIDe>3'], bins=100, histtype='step')
	plt.yscale('log')
	# plt.axvline(x=1825, c='k', linestyle='--', linewidth=0.5)
	# plt.axvline(x=1905, c='k', linestyle='--', linewidth=0.5)
	# plt.legend()
	plt.xlabel('m(Ke) MeV')
	plt.savefig('plots_kemu/Ke_mass_range.png',bbox_inches='tight')
	plt.close('all')


	plt.figure(figsize=(10,4))
	plt.subplot(1,2,1)
	plt.title('All (preselec, PIDe>3)')
	plt.hist2d(a_kemu[b"cascadeBDTGfixedRun3T"], a_kemu[b"Kemu_MKl"], range=[[0,1],[800,5300]], bins=100, norm=LogNorm())
	plt.axvline(x=BDT_cut, c='r', linestyle='--')
	plt.colorbar()
	# plt.axhline(y=1825, c='k', linestyle='--', linewidth=0.5)
	# plt.axhline(y=1905, c='k', linestyle='--', linewidth=0.5)
	plt.xlabel('cascadeBDT')
	plt.ylabel('m(Ke)')
	plt.subplot(1,2,2)
	plt.title('apply comiBDT, PIDe>4')
	plt.hist2d(a_kemu[b"cascadeBDTGfixedRun3T"][where_combiBDT_PIDe4], a_kemu[b"Kemu_MKl"][where_combiBDT_PIDe4], range=[[0,1],[800,5300]], bins=100, norm=LogNorm())
	plt.axvline(x=BDT_cut, c='r', linestyle='--')
	plt.colorbar()
	# plt.axhline(y=1825, c='k', linestyle='--', linewidth=0.5)
	# plt.axhline(y=1905, c='k', linestyle='--', linewidth=0.5)
	plt.xlabel('cascadeBDT')
	plt.ylabel('m(Ke)')
	plt.savefig('plots_kemu/mKe_casBDT.png',bbox_inches='tight')
	plt.close('all')


	plt.figure(figsize=(10,4))
	plt.subplot(1,2,1)
	plt.title('All (preselec, PIDe>3)')
	plt.hist2d(a_kemu[b"cascadeBDTGfixedRun3T"], a_kemu[b"e_plus_PIDe"], range=[[0,1],[3,16]], bins=100, norm=LogNorm())
	plt.axvline(x=BDT_cut, c='r', linestyle='--')
	plt.colorbar()
	plt.xlabel('cascadeBDT')
	plt.ylabel('PIDe')
	plt.subplot(1,2,2)
	plt.title('apply combiBDT')
	plt.hist2d(a_kemu[b"cascadeBDTGfixedRun3T"][where_combiBDT], a_kemu[b"e_plus_PIDe"][where_combiBDT], range=[[0,1],[3,16]], bins=100, norm=LogNorm())
	plt.axvline(x=BDT_cut, c='r', linestyle='--')
	plt.colorbar()
	plt.xlabel('cascadeBDT')
	plt.ylabel('PIDe')
	plt.savefig('plots_kemu/PIDe_casBDT.png',bbox_inches='tight')
	plt.close('all')


combiBDT_value = np.empty(num)
for i in range(0, num):
	trig = [a_kemu[b"passTrigCat0"][i],a_kemu[b"passTrigCat1"][i],a_kemu[b"passTrigCat2"][i]]
	if trig[0] == 1:
		combiBDT_value[i] = a_kemu[b"BDTGETOSRun3T"][i]
	else:
		combiBDT_value[i] = a_kemu[b"BDTGfixedRun3T"][i]

if make_plots == True:

	plt.figure(figsize=(10,4))
	plt.subplot(1,2,1)
	plt.title('All (preselec, PIDe>3)')
	plt.hist2d(a_kemu[b"cascadeBDTGfixedRun3T"], combiBDT_value, range=[[0,1],[0,1]], bins=100, norm=LogNorm())
	plt.axvline(x=BDT_cut, c='r', linestyle='--')
	plt.colorbar()
	plt.xlabel('cascadeBDT')
	plt.ylabel('combiBDT')

	plt.subplot(1,2,2)
	plt.title('apply comiBDT, PIDe>4')
	plt.hist2d(a_kemu[b"cascadeBDTGfixedRun3T"][where_combiBDT_PIDe4], combiBDT_value[where_combiBDT_PIDe4], range=[[0,1],[0,1]], bins=100, norm=LogNorm())
	plt.axvline(x=BDT_cut, c='r', linestyle='--')
	plt.colorbar()
	plt.xlabel('cascadeBDT')
	plt.ylabel('combiBDT')

	plt.savefig('plots_kemu/casBDT_vs_combiBDT.png',bbox_inches='tight')
	plt.close('all')



# plt.figure(figsize=(10,4))
# plt.subplot(1,2,1)
# plt.hist([B_plus_M_e, B_plus_M_e[where_combiBDT_PIDe4]],label=['all','cut'], bins=100,histtype='step')
# plt.axvspan(4880, 6200, alpha=1., color='r')
# plt.legend()
# plt.subplot(1,2,2)
# plt.hist([B_plus_M_mu, B_plus_M_mu[where_combiBDT_PIDe4]],label=['all','cut'], bins=100,histtype='step')
# plt.axvspan(4880, 6200, alpha=1., color='r')
# plt.legend()
# plt.show()











