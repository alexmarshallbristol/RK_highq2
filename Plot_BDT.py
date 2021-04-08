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

make_plots = True

find_BDT_point = True

# BDT_cut = 0.65
BDT_cut = 0.55

def compute_where_PID(array):

		where = np.where((array[b"e_plus_PIDe"]>4) &
						(array[b"e_minus_PIDe"]>4) &
						(array[b"K_Kst_MC15TuneV1_ProbNNk"]>0.2) &
						(array[b"K_Kst_PIDe"]<0)
						)[0]
		return where

def compute_where_PID_and_combiBDT(array):

		where = np.where((array[b"e_plus_PIDe"]>4) &
						(array[b"e_minus_PIDe"]>4) &
						(array[b"K_Kst_MC15TuneV1_ProbNNk"]>0.2) &
						(array[b"K_Kst_PIDe"]<0)
						& (((array[b"passTrigCat0"]==1)&(array[b"BDTGETOSRun3T"]>0.78))|((array[b"passTrigCat1"]==1)&(array[b"BDTGfixedRun3T"]>0.75))|((array[b"passTrigCat2"]==1)&(array[b"BDTGfixedRun3T"]>0.8)) )
						)[0]
		return where

def compute_where_PID_under_cascade(array):

		where = np.where( (array[b"Kemu_MKl"]<1885) & 
						((array[b"Kemu_TRACK_MKl_l2pi"]<1825)|(array[b"Kemu_TRACK_MKl_l2pi"]>1905)) &
						(array[b"e_plus_PIDe"]>4) &
						(array[b"e_minus_PIDe"]>4) &
						(array[b"K_Kst_MC15TuneV1_ProbNNk"]>0.2) &
						(array[b"K_Kst_PIDe"]<0)
						# & (array[b"B_plus_M"]>4880)
						# & (array[b"B_plus_M"]<6200)
						)[0]
		return where

selection_columns = ["BDTGfixedRun3T","BDTGETOSRun3T","cascadeBDTGfixedRun3T", "e_plus_PIDe", 
					"e_minus_PIDe", "K_Kst_MC15TuneV1_ProbNNk", "K_Kst_PIDe", "Kemu_MKl", 
					"Kemu_TRACK_MKl_l2pi", "J_psi_1S_M", "B_plus_M", "passTrigCat0", "passTrigCat1", "passTrigCat2"
					]

if find_BDT_point == True:

	make_cuts_first = True

	BRSignal = 5.5e-7
	BRCascade1 = 9.45e-4
	BRCascade3 = 1.5e-4
	relBF_cascade1 = BRCascade1/BRSignal
	relBF_cascade3 = BRCascade3/BRSignal
	print(relBF_cascade1, relBF_cascade3)
	decProdSignal = 0.16 
	decProdCascade1 = 0.0055
	decProdCascade3 = 0.0621
	relDec_cascade1 = decProdCascade1/decProdSignal
	relDec_cascade3 = decProdCascade3/decProdSignal
	print(relDec_cascade1, relDec_cascade3)

	events_signal = uproot3.open("tuples/sim09g_Kee_truthed_2018_preselec.root")["DecayTree"] # no PID selection
	events_cascade1 = uproot3.open("tuples/Bu_D0enu_Kenu2018_truthed_preselec.root")["DecayTree"] # no PID selection
	events_cascade3 = uproot3.open("tuples/Bu_D0pi_Kenu2018_truthed_preselec.root")["DecayTree"] # no PID selection

	a_signal = events_signal.arrays(selection_columns)
	a_cascade1 = events_cascade1.arrays(selection_columns)
	a_cascade3 = events_cascade3.arrays(selection_columns)

	num_signal = np.shape(a_signal[b"cascadeBDTGfixedRun3T"])[0]
	num_cascade1 = np.shape(a_cascade1[b"cascadeBDTGfixedRun3T"])[0]
	num_cascade3 = np.shape(a_cascade3[b"cascadeBDTGfixedRun3T"])[0]

	print('num_signal:',num_signal,'num_cascade1:',num_cascade1,'num_cascade3:',num_cascade3)

	print('Maybe cut on PID here later...')

	# if make_plots == True:
	# 	plt.figure(figsize=(5,4))
	# 	plt.hist([a_signal[b"cascadeBDTGfixedRun3T"], a_cascade1[b"cascadeBDTGfixedRun3T"], a_cascade3[b"cascadeBDTGfixedRun3T"]], density=True, label=['Signal','Cascade1','Cascade3'], histtype='step', bins=50, linewidth=2)
	# 	plt.legend()
	# 	plt.xlabel('Cascade BDT response')
	# 	plt.ylabel('Normalised frequency')
	# 	plt.savefig('plots/BDT_response_1D_split.pdf',bbox_inches='tight')
	# 	plt.close('all')

	where_sig = np.where(a_signal[b"cascadeBDTGfixedRun3T"]!=-99)[0]
	where_cas1 = np.where(a_cascade1[b"cascadeBDTGfixedRun3T"]!=-99)[0]
	where_cas3 = np.where(a_cascade3[b"cascadeBDTGfixedRun3T"]!=-99)[0]


	if make_cuts_first == True:
		where_sig = compute_where_PID_under_cascade(a_signal)
		where_cas1 = compute_where_PID_under_cascade(a_cascade1)
		where_cas3 = compute_where_PID_under_cascade(a_cascade3)
		print(np.shape(where_sig), np.shape(where_cas1), np.shape(where_cas3))

	significance = np.empty((0,5)) # BDT_cut, significance, signal_count, cascade1_count, cascade3_count

	for BDT_cut_i in np.linspace(0,1,50):
	# cout<<"frac cascade1: "<<100*(nCascade1*BRCascade1*decProdCascade1/n0Cascade1) / (nSignal*BRSignal*decProdSignal/n0Signal)<<"\%"<<endl;

		signal_n = np.shape(np.where(a_signal[b"cascadeBDTGfixedRun3T"][where_sig]>BDT_cut_i))[1]
		# cascade1_n = np.shape(np.where(a_cascade1[b"cascadeBDTGfixedRun3T"]>BDT_cut_i))[1]*(292174./88398.)*relBF_cascade1*(relDec_cascade1) # Think do not need the number of events here, the dec accounts for this... 2E6 events simulated in each sample?
		# cascade3_n = np.shape(np.where(a_cascade3[b"cascadeBDTGfixedRun3T"]>BDT_cut_i))[1]*(292174./113285.)*relBF_cascade3*(relDec_cascade3)
		cascade1_n = np.shape(np.where(a_cascade1[b"cascadeBDTGfixedRun3T"][where_cas1]>BDT_cut_i))[1]*(relBF_cascade1)*(relDec_cascade1)
		cascade3_n = np.shape(np.where(a_cascade3[b"cascadeBDTGfixedRun3T"][where_cas3]>BDT_cut_i))[1]*(relBF_cascade3)*(relDec_cascade3)

		significance_i = signal_n/np.sqrt(signal_n+cascade1_n+cascade3_n)
		if np.isnan(significance_i) == False:
			significance = np.append(significance, [[BDT_cut_i, significance_i, signal_n, cascade1_n, cascade3_n]], axis=0)

	BDT_cut = significance[np.where(significance[:,1]==np.amax(significance[:,1]))][0][0]
	BDT_cut = np.around(BDT_cut, decimals=2)
	print("BDT_cut:",BDT_cut)
	BDT_sig_eff = significance[np.where(significance[:,1]==np.amax(significance[:,1]))][0][2]/num_signal

	if make_plots == True:
		plt.figure(figsize=(10,4))
		plt.subplot(1,2,1)
		plt.scatter(significance[:,0], significance[:,1])
		plt.title('BDT cut at %.2f'%BDT_cut)
		plt.axvline(x=BDT_cut, c='k',linestyle='--')
		plt.xlabel('Cascade BDT value')
		plt.ylabel('significance, s/sqrt(s+b)')
		plt.subplot(1,2,2)
		plt.scatter(significance[:,0], significance[:,2],label='Signal')
		plt.scatter(significance[:,0], significance[:,3],label='Cascade1')
		plt.scatter(significance[:,0], significance[:,4],label='Cascade3')
		plt.legend()
		plt.title('BDT cut eff %.2f'%BDT_sig_eff)
		plt.axvline(x=BDT_cut, c='k',linestyle='--')
		plt.axhline(y=BDT_sig_eff, c='k',linestyle='--')
		plt.xlabel('Cascade BDT value')
		plt.ylabel('a.u.')
		plt.yscale('log')
		plt.savefig('plots/BDT_significance.pdf',bbox_inches='tight')
		plt.close('all')
	

else:

	events_signal = uproot3.open("tuples/sim09g_Kee_truthed_2018_preselec.root")["DecayTree"] # no PID selection
	events_cascades = uproot3.open("tuples/cascades_truthed_2018_preselec.root")["DecayTree"]

	a_signal = events_signal.arrays(selection_columns)
	a_cascades = events_cascades.arrays(selection_columns)

	num_signal = np.shape(a_signal[b"cascadeBDTGfixedRun3T"])[0]
	num_cascades = np.shape(a_cascades[b"cascadeBDTGfixedRun3T"])[0]

	print('num_signal:',num_signal,'num_cascades:',num_cascades)

	if make_plots == True:
		plt.figure(figsize=(5,4))
		plt.hist([a_signal[b"cascadeBDTGfixedRun3T"], a_cascades[b"cascadeBDTGfixedRun3T"]], density=True, label=['Signal','Cascades'], histtype='step', bins=50, linewidth=2)
		plt.legend()
		plt.xlabel('Cascade BDT response')
		plt.ylabel('Normalised frequency')
		plt.savefig('plots/BDT_response_1D.pdf',bbox_inches='tight')
		plt.close('all')

	if make_plots == True:
		plt.figure(figsize=(10,4))
		plt.subplot(1,2,1)
		plt.hist2d(a_signal[b"cascadeBDTGfixedRun3T"], a_signal[b"e_plus_PIDe"], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[-16,17.5]])
		plt.xlabel('Cascade BDT')
		plt.ylabel('PIDe')
		plt.title("Signal")
		plt.axhline(y=4,c='k',linestyle='--')
		plt.axvline(x=BDT_cut, c='k', linestyle='--')
		plt.colorbar()
		plt.subplot(1,2,2)
		plt.hist2d(a_cascades[b"cascadeBDTGfixedRun3T"], a_cascades[b"e_plus_PIDe"], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[-16,17.5]])
		plt.xlabel('Cascade BDT')
		plt.ylabel('PIDe')
		plt.title("Cascades")
		plt.axhline(y=4,c='k',linestyle='--')
		plt.axvline(x=BDT_cut, c='k', linestyle='--')
		plt.colorbar()
		plt.savefig('plots/BDT_PID_response_2D.pdf',bbox_inches='tight')
		plt.close('all')

	if make_plots == True:
		plt.figure(figsize=(10,4))
		plt.subplot(1,2,1)
		plt.hist2d(a_signal[b"cascadeBDTGfixedRun3T"], a_signal[b"BDTGfixedRun3T"], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[0,1]])
		plt.xlabel('Cascade BDT')
		plt.ylabel('Combi BDT')
		plt.title("Signal")
		plt.colorbar()
		plt.subplot(1,2,2)
		plt.hist2d(a_cascades[b"cascadeBDTGfixedRun3T"], a_cascades[b"BDTGfixedRun3T"], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[0,1]])
		plt.xlabel('Cascade BDT')
		plt.ylabel('Combi BDT')
		plt.title("Cascades")
		plt.colorbar()
		plt.savefig('plots/BDT_vs_BDT_2D.pdf',bbox_inches='tight')
		plt.close('all')

	if make_plots == True:
		plt.figure(figsize=(10,8))
		plt.subplot(2,2,1)
		plt.hist([a_signal[b"Kemu_MKl"], a_cascades[b"Kemu_MKl"]], density=True, label=['Signal','Cascades'], histtype='step', bins=50, linewidth=2, range=[1000,5000])
		plt.axvline(x=1885, c='k', linestyle='--')
		plt.xlabel('mKe')
		plt.legend()
		plt.subplot(2,2,2)
		plt.hist([a_signal[b"Kemu_TRACK_MKl_l2pi"], a_cascades[b"Kemu_TRACK_MKl_l2pi"]], density=True, label=['Signal','Cascades'], histtype='step', bins=50, linewidth=2, range=[1700,2000])
		plt.xlabel('mKe, with pion swap')
		plt.axvline(x=1825, c='k', linestyle='--')
		plt.axvline(x=1905, c='k', linestyle='--')
		plt.legend()
		plt.subplot(2,2,3)
		plt.hist([a_signal[b"Kemu_MKl"], a_cascades[b"Kemu_MKl"]], density=True, label=['Signal','Cascades'], histtype='step', bins=50, linewidth=2, range=[1000,5000])
		plt.yscale('log')
		plt.xlabel('mKe')
		plt.axvline(x=1885, c='k', linestyle='--')
		plt.legend()
		plt.subplot(2,2,4)
		plt.hist([a_signal[b"Kemu_TRACK_MKl_l2pi"], a_cascades[b"Kemu_TRACK_MKl_l2pi"]], density=True, label=['Signal','Cascades'], histtype='step', bins=50, linewidth=2, range=[1700,2000])
		plt.yscale('log')
		plt.xlabel('mKe, with pion swap')
		plt.axvline(x=1825, c='k', linestyle='--')
		plt.axvline(x=1905, c='k', linestyle='--')
		plt.legend()
		plt.savefig('plots/mass_hypo_with_cuts.pdf',bbox_inches='tight')
		plt.close('all')


	eff_signal = np.shape(np.where( (a_signal[b"Kemu_MKl"]>1885) & ((a_signal[b"Kemu_TRACK_MKl_l2pi"]<1825)|(a_signal[b"Kemu_TRACK_MKl_l2pi"]>1905)) ))[1]/np.shape(a_signal[b"cascadeBDTGfixedRun3T"])[0]
	eff_cascade = np.shape(np.where( (a_cascades[b"Kemu_MKl"]>1885) & ((a_cascades[b"Kemu_TRACK_MKl_l2pi"]<1825)|(a_cascades[b"Kemu_TRACK_MKl_l2pi"]>1905)) ))[1]/np.shape(a_cascades[b"cascadeBDTGfixedRun3T"])[0]
	print(' ')
	print('simple cuts:')
	print('eff_signal:',eff_signal,'eff_cascade:',eff_cascade)

	eff_signal = np.shape(np.where(  ((a_signal[b"Kemu_TRACK_MKl_l2pi"]<1825)|(a_signal[b"Kemu_TRACK_MKl_l2pi"]>1905)) ))[1]/np.shape(a_signal[b"cascadeBDTGfixedRun3T"])[0]
	eff_cascade = np.shape(np.where( ((a_cascades[b"Kemu_TRACK_MKl_l2pi"]<1825)|(a_cascades[b"Kemu_TRACK_MKl_l2pi"]>1905)) ))[1]/np.shape(a_cascades[b"cascadeBDTGfixedRun3T"])[0]
	print(' ')
	print('only window cut:')
	print('eff_signal:',eff_signal,'eff_cascade:',eff_cascade)

	if make_plots == True:
		plt.figure(figsize=(10,4))
		ax = plt.subplot(1,2,1)
		rect = patches.Rectangle((0, 800), BDT_cut, 1885-800, linewidth=1, edgecolor='r', facecolor='r',alpha=0.2)
		ax.add_patch(rect)
		rect = patches.Rectangle((BDT_cut, 800), 1-BDT_cut, 1885-800, linewidth=1, edgecolor='g', facecolor='g',alpha=0.2)
		ax.add_patch(rect)
		plt.hist2d(a_signal[b"cascadeBDTGfixedRun3T"], a_signal[b"Kemu_MKl"], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[800,4750]])
		plt.title("Signal")
		plt.colorbar()
		plt.ylabel('m(Ke)')
		plt.xlabel('Cascade BDT response')
		plt.axvline(x=BDT_cut, c='k', linestyle='--')
		plt.axhline(y=1885, c='k', linestyle='--')
		ax = plt.subplot(1,2,2)
		rect = patches.Rectangle((0, 800), BDT_cut, 1885-800, linewidth=1, edgecolor='r', facecolor='r',alpha=0.2)
		ax.add_patch(rect)
		rect = patches.Rectangle((BDT_cut, 800), 1-BDT_cut, 1885-800, linewidth=1, edgecolor='g', facecolor='g',alpha=0.2)
		ax.add_patch(rect)
		plt.hist2d(a_cascades[b"cascadeBDTGfixedRun3T"], a_cascades[b"Kemu_MKl"], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[800,4750]])
		plt.title("Cascades")
		plt.colorbar()
		plt.ylabel('m(Ke)')
		plt.xlabel('Cascade BDT response')
		plt.axvline(x=BDT_cut, c='k', linestyle='--')
		plt.axhline(y=1885, c='k', linestyle='--')
		plt.savefig('plots/effect_of_window_cut.pdf',bbox_inches='tight')
		plt.close('all')

	where_post_window_cut_sig = compute_where_PID_and_combiBDT(a_signal)
	where_post_window_cut_cas = compute_where_PID_and_combiBDT(a_cascades)

	if make_plots == True:
		plt.figure(figsize=(10,4))
		ax = plt.subplot(1,2,1)
		rect = patches.Rectangle((0, 800), BDT_cut, 1885-800, linewidth=1, edgecolor='r', facecolor='r',alpha=0.2)
		ax.add_patch(rect)
		rect = patches.Rectangle((BDT_cut, 800), 1-BDT_cut, 1885-800, linewidth=1, edgecolor='g', facecolor='g',alpha=0.2)
		ax.add_patch(rect)
		plt.hist2d(a_signal[b"cascadeBDTGfixedRun3T"], a_signal[b"Kemu_MKl"], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[800,4750]],alpha=0.3)
		plt.hist2d(a_signal[b"cascadeBDTGfixedRun3T"][where_post_window_cut_sig], a_signal[b"Kemu_MKl"][where_post_window_cut_sig], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[800,4750]])
		plt.title("Signal")
		plt.colorbar()
		plt.ylabel('m(Ke)')
		plt.xlabel('Cascade BDT response')
		plt.axvline(x=BDT_cut, c='k', linestyle='--')
		plt.axhline(y=1885, c='k', linestyle='--')
		ax = plt.subplot(1,2,2)
		rect = patches.Rectangle((0, 800), BDT_cut, 1885-800, linewidth=1, edgecolor='r', facecolor='r',alpha=0.2)
		ax.add_patch(rect)
		rect = patches.Rectangle((BDT_cut, 800), 1-BDT_cut, 1885-800, linewidth=1, edgecolor='g', facecolor='g',alpha=0.2)
		ax.add_patch(rect)
		plt.hist2d(a_cascades[b"cascadeBDTGfixedRun3T"], a_cascades[b"Kemu_MKl"], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[800,4750]],alpha=0.3)
		plt.hist2d(a_cascades[b"cascadeBDTGfixedRun3T"][where_post_window_cut_cas], a_cascades[b"Kemu_MKl"][where_post_window_cut_cas], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[800,4750]])
		plt.title("Cascades")
		plt.colorbar()
		plt.ylabel('m(Ke)')
		plt.xlabel('Cascade BDT response')
		plt.axvline(x=BDT_cut, c='k', linestyle='--')
		plt.axhline(y=1885, c='k', linestyle='--')
		plt.savefig('plots/effect_of_window_cut_POST_CUTS.pdf',bbox_inches='tight')
		plt.close('all')

	if make_plots == True:
		plt.figure(figsize=(10,4))
		plt.subplot(1,2,1)
		plt.hist2d(a_signal[b"cascadeBDTGfixedRun3T"], a_signal[b"e_plus_PIDe"], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[-16,17.5]],alpha=0.3)
		plt.hist2d(a_signal[b"cascadeBDTGfixedRun3T"][where_post_window_cut_sig], a_signal[b"e_plus_PIDe"][where_post_window_cut_sig], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[-16,17.5]])
		plt.xlabel('Cascade BDT')
		plt.ylabel('PIDe')
		plt.title("Signal")
		plt.axhline(y=4,c='k',linestyle='--')
		plt.axvline(x=BDT_cut, c='k', linestyle='--')
		plt.colorbar()
		plt.subplot(1,2,2)
		plt.hist2d(a_cascades[b"cascadeBDTGfixedRun3T"], a_cascades[b"e_plus_PIDe"], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[-16,17.5]],alpha=0.3)
		plt.hist2d(a_cascades[b"cascadeBDTGfixedRun3T"][where_post_window_cut_cas], a_cascades[b"e_plus_PIDe"][where_post_window_cut_cas], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[-16,17.5]])
		plt.xlabel('Cascade BDT')
		plt.ylabel('PIDe')
		plt.title("Cascades")
		plt.axhline(y=4,c='k',linestyle='--')
		plt.axvline(x=BDT_cut, c='k', linestyle='--')
		plt.colorbar()
		plt.savefig('plots/BDT_PID_response_2D_POST_CUTS.pdf',bbox_inches='tight')
		plt.close('all')

	if make_plots == True:
		plt.figure(figsize=(10,4))
		plt.subplot(1,2,1)
		plt.hist2d(a_signal[b"cascadeBDTGfixedRun3T"], a_signal[b"BDTGfixedRun3T"], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[0,1]],alpha=0.3)
		plt.hist2d(a_signal[b"cascadeBDTGfixedRun3T"][where_post_window_cut_sig], a_signal[b"BDTGfixedRun3T"][where_post_window_cut_sig], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[0,1]])
		plt.xlabel('Cascade BDT')
		plt.ylabel('Combi BDT (BDTGfixedRun3T)')
		plt.axvline(x=BDT_cut, c='k', linestyle='--')
		plt.title("Signal")
		plt.colorbar()
		plt.subplot(1,2,2)
		plt.hist2d(a_cascades[b"cascadeBDTGfixedRun3T"], a_cascades[b"BDTGfixedRun3T"], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[0,1]],alpha=0.3)
		plt.hist2d(a_cascades[b"cascadeBDTGfixedRun3T"][where_post_window_cut_cas], a_cascades[b"BDTGfixedRun3T"][where_post_window_cut_cas], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[0,1]])
		plt.xlabel('Cascade BDT')
		plt.ylabel('Combi BDT (BDTGfixedRun3T)')
		plt.axvline(x=BDT_cut, c='k', linestyle='--')
		plt.title("Cascades")
		plt.colorbar()
		plt.savefig('plots/BDT_vs_BDT_2D_POST_CUTS.pdf',bbox_inches='tight')
		plt.close('all')

		plt.figure(figsize=(10,4))
		plt.subplot(1,2,1)
		plt.hist2d(a_signal[b"cascadeBDTGfixedRun3T"], a_signal[b"BDTGETOSRun3T"], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[0,1]],alpha=0.3)
		plt.hist2d(a_signal[b"cascadeBDTGfixedRun3T"][where_post_window_cut_sig], a_signal[b"BDTGETOSRun3T"][where_post_window_cut_sig], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[0,1]])
		plt.xlabel('Cascade BDT')
		plt.ylabel('Combi BDT (BDTGETOSRun3T)')
		plt.axvline(x=BDT_cut, c='k', linestyle='--')
		plt.title("Signal")
		plt.colorbar()
		plt.subplot(1,2,2)
		plt.hist2d(a_cascades[b"cascadeBDTGfixedRun3T"], a_cascades[b"BDTGETOSRun3T"], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[0,1]],alpha=0.3)
		plt.hist2d(a_cascades[b"cascadeBDTGfixedRun3T"][where_post_window_cut_cas], a_cascades[b"BDTGETOSRun3T"][where_post_window_cut_cas], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[0,1]])
		plt.xlabel('Cascade BDT')
		plt.ylabel('Combi BDT (BDTGETOSRun3T)')
		plt.axvline(x=BDT_cut, c='k', linestyle='--')
		plt.title("Cascades")
		plt.colorbar()
		plt.savefig('plots/BDT_vs_BDT_2D_POST_CUTS_2.pdf',bbox_inches='tight')
		plt.close('all')

	eff_signal = np.shape(np.where(  ((a_signal[b"Kemu_TRACK_MKl_l2pi"]<1825)|(a_signal[b"Kemu_TRACK_MKl_l2pi"]>1905)) & ((a_signal[b"Kemu_MKl"]>1825)|(a_signal[b"cascadeBDTGfixedRun3T"]>BDT_cut)) ))[1]/np.shape(a_signal[b"cascadeBDTGfixedRun3T"])[0]
	eff_cascade = np.shape(np.where( ((a_cascades[b"Kemu_TRACK_MKl_l2pi"]<1825)|(a_cascades[b"Kemu_TRACK_MKl_l2pi"]>1905)) & ((a_cascades[b"Kemu_MKl"]>1825)|(a_cascades[b"cascadeBDTGfixedRun3T"]>BDT_cut)) ))[1]/np.shape(a_cascades[b"cascadeBDTGfixedRun3T"])[0]
	print(' ')
	print('window cut + BDT below window:')
	print('eff_signal:',eff_signal,'eff_cascade:',eff_cascade)

	where_post_window_plus_BDT_sig = np.where(  ((a_signal[b"Kemu_TRACK_MKl_l2pi"]<1825)|(a_signal[b"Kemu_TRACK_MKl_l2pi"]>1905)) & ((a_signal[b"Kemu_MKl"]>1825)|(a_signal[b"cascadeBDTGfixedRun3T"]>BDT_cut)) )
	where_post_window_plus_BDT_cas = np.where(  ((a_cascades[b"Kemu_TRACK_MKl_l2pi"]<1825)|(a_cascades[b"Kemu_TRACK_MKl_l2pi"]>1905)) & ((a_cascades[b"Kemu_MKl"]>1825)|(a_cascades[b"cascadeBDTGfixedRun3T"]>BDT_cut)) )

	print(np.shape(where_post_window_plus_BDT_sig), np.shape(where_post_window_plus_BDT_cas))

	if make_plots == True:
		plt.figure(figsize=(5,4))
		plt.hist([a_signal[b"B_plus_M"][where_post_window_plus_BDT_sig], a_cascades[b"B_plus_M"][where_post_window_plus_BDT_cas]], density=True, label=['Signal','Cascades'], histtype='step', bins=50, linewidth=2, range=[4880,6250])
		plt.legend()
		plt.xlabel('m(B)')
		plt.ylabel('Normalised frequency')
		plt.savefig('plots/mass_after_window_plus_BDT.pdf',bbox_inches='tight')
		plt.close('all')


	if make_plots == True:

		where_post_remove_window_below_D_mass_sig = np.where(  ((a_signal[b"Kemu_TRACK_MKl_l2pi"]<1825)|(a_signal[b"Kemu_TRACK_MKl_l2pi"]>1905)) & (a_signal[b"Kemu_MKl"]<1825) )
		where_post_remove_window_below_D_mass_cas = np.where(  ((a_cascades[b"Kemu_TRACK_MKl_l2pi"]<1825)|(a_cascades[b"Kemu_TRACK_MKl_l2pi"]>1905)) & (a_cascades[b"Kemu_MKl"]<1825) )

		plt.figure(figsize=(10,4))
		plt.subplot(1,2,1)
		plt.hist2d(a_signal[b"cascadeBDTGfixedRun3T"][where_post_remove_window_below_D_mass_sig], a_signal[b"e_plus_PIDe"][where_post_remove_window_below_D_mass_sig], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[-16,17.5]])
		plt.xlabel('Cascade BDT')
		plt.ylabel('PIDe')
		plt.title("Signal")
		plt.axhline(y=4,c='k',linestyle='--')
		plt.axvline(x=BDT_cut,c='k',linestyle='--')
		plt.colorbar()
		plt.subplot(1,2,2)
		plt.hist2d(a_cascades[b"cascadeBDTGfixedRun3T"][where_post_remove_window_below_D_mass_cas], a_cascades[b"e_plus_PIDe"][where_post_remove_window_below_D_mass_cas], norm=LogNorm(), cmap=cmp_root, bins=50, range=[[0,1],[-16,17.5]])
		plt.xlabel('Cascade BDT')
		plt.ylabel('PIDe')
		plt.title("Cascades")
		plt.axhline(y=4,c='k',linestyle='--')
		plt.axvline(x=BDT_cut,c='k',linestyle='--')
		plt.colorbar()
		plt.savefig('plots/BDT_PID_response_2D_below_D_mass_apply_windows.pdf',bbox_inches='tight')
		plt.close('all')













