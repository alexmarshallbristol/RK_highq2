import numpy as np

class RK_func:

	def __init__(self):
		''' Constructor for this class. '''
		print('RK_func module...')

	def get_default_casBDT_cut():
		return 0.56

	def get_branching_fraction(mode):
		BF_list = {
					  "signal": 5.5e-7,
					  "cas1": 9.45e-4,
					  "cas2": 1.06e-3,
					  "cas3": 1.5e-4,
					  "Kstree": 1.55e-6,
					  "Kpipi": 1.63e-5
					}
		return BF_list[mode]

	def get_decProd(mode):
		decProd_list = {
					  "signal": 0.16,
					  "cas1": 0.0055,
					  "cas2": 0.027777,
					  "cas3": 0.0621
					}
		return decProd_list[mode]

	def get_event_count_no_cuts(mode):
		event_count_no_cuts_list = {
					  "signal": 292174,
					  "cas1": 88398,
					  "cas2": 89943,
					  "cas3": 113285,
					  "Kstree": 537099,
					  "Kpipi": 7100
					}
		return event_count_no_cuts_list[mode]

	def get_event_weight_no_cuts(mode, sweights=True):
		if sweights:
			event_count_no_cuts_list = {
						  "signal": 311900,
						  "Kstree": 608400,
						  "Kpipi": 7130
						}
		else:
			event_count_no_cuts_list = {
						  "signal": 311900,
						  "Kstree": 607700,
						  "Kpipi": 7130
						}
		return event_count_no_cuts_list[mode]

	def get_standard_columns():
		cols = [
			# BDT and trigger categories
			"cascadeBDTGfixedRun3T", "BDTGfixedRun3T", "BDTGETOSRun3T",
			"passTrigCat0", "passTrigCat1", "passTrigCat2",

			# Reconstructed masses
			"B_plus_M", "Kemu_MKl", "Kemu_TRACK_MKl_l2pi",

			# PID information
			"e_plus_PIDe", "e_minus_PIDe", "K_Kst_MC15TuneV1_ProbNNk", "K_Kst_PIDe", "K_Kst_isMuon", "K_Kst_PIDmu",
		 	
		 	# Kinematical information
		 	"K_Kst_M", "K_Kst_PE", "K_Kst_P", "K_Kst_PX", "K_Kst_PY", "K_Kst_PZ",
			"e_plus_M", "e_plus_PE", "e_plus_P", "e_plus_BremPE", "e_plus_PX", "e_plus_BremPX", "e_plus_PY", "e_plus_BremPY", "e_plus_PZ", "e_plus_BremPZ",
			"e_minus_M", "e_minus_PE", "e_minus_P", "e_minus_BremPE", "e_minus_PX", "e_minus_BremPX", "e_minus_PY", "e_minus_BremPY", "e_minus_PZ", "e_minus_BremPZ",

			# TRACK information
			"K_Kst_TRACK_P", "K_Kst_TRACK_PX", "K_Kst_TRACK_PY", "K_Kst_TRACK_PZ",
			"e_plus_TRACK_P", "e_plus_TRACK_PX", "e_plus_TRACK_PY", "e_plus_TRACK_PZ",
			"e_minus_TRACK_P", "e_minus_TRACK_PX", "e_minus_TRACK_PY", "e_minus_TRACK_PZ",

			# q
			"J_psi_1S_M"
		]
		return cols

	def get_kemu_columns():
		cols = [
			# BDTs and trigger categories
			"cascadeBDTGfixedRun3T", "BDTGfixedRun3T", "BDTGETOSRun3T",
			"passTrigCat0", "passTrigCat1", "passTrigCat2",

			# Reconstructed masses
			"B_plus_M", "Kemu_MKl", "Kemu_TRACK_MKl_l2pi",

			# PID information
			"e_plus_PIDe", "K_Kst_MC15TuneV1_ProbNNk", "K_Kst_PIDe", "K_Kst_isMuon", "K_Kst_PIDmu",
		 	
		 	# Kinematical information
		 	"K_Kst_M", "K_Kst_PE", "K_Kst_P", "K_Kst_PX", "K_Kst_PY", "K_Kst_PZ",
			"e_plus_M", "e_plus_PE", "e_plus_P", "e_plus_BremPE", "e_plus_PX", "e_plus_BremPX", "e_plus_PY", "e_plus_BremPY", "e_plus_PZ", "e_plus_BremPZ",
			"e_minus_M", "e_minus_P", "e_minus_PX", "e_minus_PY", "e_minus_PZ",

			# TRACK information
			"K_Kst_TRACK_P", "K_Kst_TRACK_PX", "K_Kst_TRACK_PY", "K_Kst_TRACK_PZ",
			"e_plus_TRACK_P", "e_plus_TRACK_PX", "e_plus_TRACK_PY", "e_plus_TRACK_PZ",
			"e_minus_TRACK_P", "e_minus_TRACK_PX", "e_minus_TRACK_PY", "e_minus_TRACK_PZ",

			# q
			"J_psi_1S_M"
		]
		return cols

	def get_trigger_weight_columns():
		cols = [
			# Trigger weights
			"DataCondKinWeight_MUTOSLong", "trigWeightR_trigCat0", "trigWeightR_trigCat1", "trigWeightR_trigCat2"
		]
		return cols


	def full_selection(array, casBDT_cut=get_default_casBDT_cut(), combiBDT=True, Bmass=True, 
						CasWindow=False, CasMkl=False, CasBDT=True, PID=True, PID_Kemu=False):

		array_size = np.shape(array[b"B_plus_M"])[0]

		# Initialise mask as 1. (pass cuts)
		mask = np.ones(array_size) # 1 is pass, 0 is cut

		# # Pre-selection...
		# where_i = np.where(
		# 		# Add pre-selection things here at a later date...
		# 				)[0]
		# mask = np.zeros(np.shape(array[b"B_plus_M"])[0]) # 1 is pass, 0 is cut
		# mask[where_i] = 1.

		# Combinatorial BDT...
		if combiBDT:
			where_i = np.where((mask==1.)&
					(((array[b"passTrigCat0"]==1)&(array[b"BDTGETOSRun3T"]>0.78))|((array[b"passTrigCat1"]==1)&(array[b"BDTGfixedRun3T"]>0.75))|((array[b"passTrigCat2"]==1)&(array[b"BDTGfixedRun3T"]>0.8)))
							)[0]
			mask = np.zeros(array_size) # 1 is pass, 0 is cut
			mask[where_i] = 1.

		# B mass...
		if Bmass:
			where_i = np.where((mask==1.)&
					(array[b"B_plus_M"]>4880) & (array[b"B_plus_M"]<6200)
							)[0]
			mask = np.zeros(array_size) # 1 is pass, 0 is cut
			mask[where_i] = 1.

		# if np.shape(np.where(np.asarray([CasWindow, CasMkl, CasBDT])==True))[1] > 1:
		# 	print('Only one of CasWindow, CasMkl and CasBDT can be True.')
		# 	quit()
		if (CasWindow and CasBDT) or (CasMkl and CasBDT):
			print('Cascade BDT cannot be applied with another cascade cut!')
			quit()

		# Cascade window cut ...
		if CasWindow:
			where_i = np.where((mask==1.)&
					((array[b"Kemu_TRACK_MKl_l2pi"]<1825)|(array[b"Kemu_TRACK_MKl_l2pi"]>1905))
							)[0]
			mask = np.zeros(array_size) # 1 is pass, 0 is cut
			mask[where_i] = 1.

		# Cascade Mkl cut ...
		if CasMkl:
			where_i = np.where((mask==1.)&
					(array[b"Kemu_MKl"]>1885)
							)[0]
			mask = np.zeros(array_size) # 1 is pass, 0 is cut
			mask[where_i] = 1.

		# Cascade BDT cut ...
		if CasBDT:
			where_i = np.where((mask==1.)&
					((array[b"Kemu_TRACK_MKl_l2pi"]<1825)|(array[b"Kemu_TRACK_MKl_l2pi"]>1905))
					& ((array[b"cascadeBDTGfixedRun3T"]>casBDT_cut)|(array[b"Kemu_MKl"]>1885))
							)[0]
			mask = np.zeros(array_size) # 1 is pass, 0 is cut
			mask[where_i] = 1.

		if PID and PID_Kemu:
			print('Only one of PID and PID_Kemu can be True.')
			quit()

		# PID cuts ...
		if PID:
			where_i = np.where((mask==1.)&
					(array[b"e_plus_PIDe"]>4) & (array[b"e_minus_PIDe"]>4)
					& (array[b"K_Kst_MC15TuneV1_ProbNNk"]>0.2) & (array[b"K_Kst_PIDe"]<0) & (array[b"K_Kst_isMuon"]==0) & (array[b"K_Kst_PIDmu"]<5)
							)[0]
			mask = np.zeros(array_size) # 1 is pass, 0 is cut
			mask[where_i] = 1.

		# PID cut for Kemu ...
		if PID_Kemu:
			where_i = np.where((mask==1.)&
					(array[b"e_plus_PIDe"]>4)
							)[0]
			mask = np.zeros(array_size) # 1 is pass, 0 is cut
			mask[where_i] = 1.


		# Compute outgoing where vector...
		where = np.where(mask==1.)[0]

		return where


	def get_contaminations(signal, cas1, cas3, Prc, Kpipi, SwaveWeight=True, CasWindow=False, CasMkl=False, CasBDT=True, print_bool=True):

		if print_bool: print(" ")
		if print_bool: print(" --- Printing background contaiminations --- ")

		if print_bool: print(" - CasWindow",CasWindow,"- "," - CasMkl",CasMkl,"- "," - CasBDT",CasBDT,"- ")

		sig_eff = np.sum(signal[b"misPIDweight"][RK_func.full_selection(signal, CasWindow=CasWindow, CasMkl=CasMkl, CasBDT=CasBDT, PID=False)]) / RK_func.get_event_weight_no_cuts('signal')
		# print(sig_eff)
		if SwaveWeight:
			Prc_eff = np.sum(Prc[b"misPIDweight_SwaveWeight"][RK_func.full_selection(Prc, CasWindow=CasWindow, CasMkl=CasMkl, CasBDT=CasBDT, PID=False)]) / RK_func.get_event_weight_no_cuts('Kstree')
		else:
			Prc_eff = np.sum(Prc[b"misPIDweight"][RK_func.full_selection(Prc, CasWindow=CasWindow, CasMkl=CasMkl, CasBDT=CasBDT, PID=False)]) / RK_func.get_event_weight_no_cuts('Kstree')
		Prc_contamination = 100.* (RK_func.get_branching_fraction('Kstree') * Prc_eff) / (RK_func.get_branching_fraction('signal') * sig_eff);
		if print_bool: print('K*ee part-reco: %.3f %%'%Prc_contamination)
		kpipi_eff = np.sum(Kpipi[b"misPIDweight"][RK_func.full_selection(Kpipi, CasWindow=CasWindow, CasMkl=CasMkl, CasBDT=CasBDT, PID=False)]) / RK_func.get_event_weight_no_cuts('Kpipi')
		kpipi_contamination = 100.* (RK_func.get_branching_fraction('Kpipi') * kpipi_eff) / (RK_func.get_branching_fraction('signal') * sig_eff);
		if print_bool: print('Kpipi double mis-ID: %.3f %%'%kpipi_contamination)

		nSignal_no_cas = np.shape(np.where(signal[b"Kemu_MKl"][RK_func.full_selection(signal, CasWindow=False, CasMkl=False, CasBDT=False)]))[1]
		nSignal = np.shape(np.where(signal[b"Kemu_MKl"][RK_func.full_selection(signal, CasWindow=CasWindow, CasMkl=CasMkl, CasBDT=CasBDT)]))[1]
		nCascade1 = np.shape(np.where(cas1[b"Kemu_MKl"][RK_func.full_selection(cas1, CasWindow=CasWindow, CasMkl=CasMkl, CasBDT=CasBDT)]))[1]
		nCascade3 = np.shape(np.where(cas3[b"Kemu_MKl"][RK_func.full_selection(cas3, CasWindow=CasWindow, CasMkl=CasMkl, CasBDT=CasBDT)]))[1]

		cascade1_contamination = (100*(nCascade1*RK_func.get_branching_fraction('cas1')*RK_func.get_decProd('cas1'))/(nSignal*RK_func.get_branching_fraction('signal')*RK_func.get_decProd('signal')))
		cascade3_contamination = (100*(nCascade3*RK_func.get_branching_fraction('cas3')*RK_func.get_decProd('cas3'))/(nSignal*RK_func.get_branching_fraction('signal')*RK_func.get_decProd('signal')))

		if print_bool: print("Cascade 1: %.3f %%"%cascade1_contamination)
		if print_bool: print("Cascade 3: %.3f %%"%cascade3_contamination)
		if print_bool: print('-----')
		if print_bool: print("Signal eff (of cascade cut): %.3f"%((nSignal)/(nSignal_no_cas)))
		if print_bool: print(" ")

		return [Prc_contamination, kpipi_contamination, cascade1_contamination, cascade3_contamination]


	def compute_weights_list(a_signal, a_cascade1, a_cascade3, a_Prc, a_kpipi, CasWindow=False, CasMkl=False, CasBDT=True):

		weights_list = []
		contaiminations = RK_func.get_contaminations(a_signal, a_cascade1, a_cascade3, a_Prc, a_kpipi, CasWindow=False, CasMkl=False, CasBDT=True, print_bool=False)

		print(contaiminations)

		weights_i = np.ones(np.shape(np.where(signal[b"Kemu_MKl"][RK_func.full_selection(signal, CasWindow=False, CasMkl=False, CasBDT=False)]))[1])

		print('compute an array of weights for each set such as the events left over after cuts have correct contaimination with signal.')
		print('This array can then be used in plotting etc')
		print('Add 2nd cascade')
		quit()
		# weights_list.append(weights)


		return weights_list



















