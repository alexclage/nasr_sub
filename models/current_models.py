
from typing import List, Optional
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
	pass


class APT_ARS(Base):

	__tablename__ = 'apt_ars'
	__mapper_args__ = {'primary_key': ['site_no', 'arpt_id', 'site_type_code', 'rwy_id', 'rwy_end_id', 'arrest_device_code']}


	eff_date: Mapped[str] = mapped_column(String(10))
	site_no: Mapped[str] = mapped_column(String(9), primary_key=True)
	site_type_code: Mapped[str] = mapped_column(String(1), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	arpt_id: Mapped[str] = mapped_column(String(4), primary_key=True)
	city: Mapped[str] = mapped_column(String(40))
	country_code: Mapped[str] = mapped_column(String(2))
	rwy_id: Mapped[str] = mapped_column(String(7), primary_key=True)
	rwy_end_id: Mapped[str] = mapped_column(String(3), primary_key=True)
	arrest_device_code: Mapped[str] = mapped_column(String(9), primary_key=True)

class APT_ATT(Base):

	__tablename__ = 'apt_att'
	__mapper_args__ = {'primary_key': ['site_no', 'site_type_code', 'sked_seq_no']}


	eff_date: Mapped[str] = mapped_column(String(10))
	site_no: Mapped[str] = mapped_column(String(9), primary_key=True)
	site_type_code: Mapped[str] = mapped_column(String(1), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	arpt_id: Mapped[str] = mapped_column(String(4))
	city: Mapped[str] = mapped_column(String(40))
	country_code: Mapped[str] = mapped_column(String(2))
	sked_seq_no: Mapped[int] = mapped_column(Integer, primary_key=True)
	month: Mapped[str] = mapped_column(String(50), nullable=True)
	day: Mapped[str] = mapped_column(String(16), nullable=True)
	hour: Mapped[str] = mapped_column(String(40), nullable=True)

class APT_BASE(Base):

	__tablename__ = 'apt_base'
	__mapper_args__ = {'primary_key': ['site_no', 'site_type_code']}


	eff_date: Mapped[str] = mapped_column(String(10))
	site_no: Mapped[str] = mapped_column(String(9), primary_key=True)
	site_type_code: Mapped[str] = mapped_column(String(1), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	arpt_id: Mapped[str] = mapped_column(String(4))
	city: Mapped[str] = mapped_column(String(40))
	country_code: Mapped[str] = mapped_column(String(2))
	region_code: Mapped[str] = mapped_column(String(3), nullable=True)
	ado_code: Mapped[str] = mapped_column(String(3), nullable=True)
	state_name: Mapped[str] = mapped_column(String(30), nullable=True)
	county_name: Mapped[str] = mapped_column(String(21))
	county_assoc_state: Mapped[str] = mapped_column(String(2))
	arpt_name: Mapped[str] = mapped_column(String(50))
	ownership_type_code: Mapped[str] = mapped_column(String(2))
	facility_use_code: Mapped[str] = mapped_column(String(2))
	lat_deg: Mapped[int] = mapped_column(Integer)
	lat_min: Mapped[int] = mapped_column(Integer)
	lat_sec: Mapped[int] = mapped_column(Integer)
	lat_hemis: Mapped[str] = mapped_column(String(1))
	lat_decimal: Mapped[int] = mapped_column(Integer)
	long_deg: Mapped[int] = mapped_column(Integer)
	long_min: Mapped[int] = mapped_column(Integer)
	long_sec: Mapped[int] = mapped_column(Integer)
	long_hemis: Mapped[str] = mapped_column(String(1))
	long_decimal: Mapped[int] = mapped_column(Integer)
	survey_method_code: Mapped[str] = mapped_column(String(1), nullable=True)
	elev: Mapped[int] = mapped_column(Integer)
	elev_method_code: Mapped[str] = mapped_column(String(1), nullable=True)
	mag_varn: Mapped[int] = mapped_column(Integer, nullable=True)
	mag_hemis: Mapped[str] = mapped_column(String(1), nullable=True)
	mag_varn_year: Mapped[int] = mapped_column(Integer, nullable=True)
	tpa: Mapped[int] = mapped_column(Integer, nullable=True)
	chart_name: Mapped[str] = mapped_column(String(30), nullable=True)
	dist_city_to_airport: Mapped[int] = mapped_column(Integer, nullable=True)
	direction_code: Mapped[str] = mapped_column(String(3), nullable=True)
	acreage: Mapped[int] = mapped_column(Integer, nullable=True)
	resp_artcc_id: Mapped[str] = mapped_column(String(4))
	computer_id: Mapped[str] = mapped_column(String(3))
	artcc_name: Mapped[str] = mapped_column(String(30))
	fss_on_arpt_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	fss_id: Mapped[str] = mapped_column(String(4))
	fss_name: Mapped[str] = mapped_column(String(30))
	phone_no: Mapped[str] = mapped_column(String(16), nullable=True)
	toll_free_no: Mapped[str] = mapped_column(String(16), nullable=True)
	alt_fss_id: Mapped[str] = mapped_column(String(4), nullable=True)
	alt_fss_name: Mapped[str] = mapped_column(String(30), nullable=True)
	alt_toll_free_no: Mapped[str] = mapped_column(String(16), nullable=True)
	notam_id: Mapped[str] = mapped_column(String(4), nullable=True)
	notam_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	activation_date: Mapped[str] = mapped_column(String(7), nullable=True)
	arpt_status: Mapped[str] = mapped_column(String(2))
	far_139_type_code: Mapped[str] = mapped_column(String(5), nullable=True)
	far_139_carrier_ser_code: Mapped[str] = mapped_column(String(1), nullable=True)
	arff_cert_type_date: Mapped[str] = mapped_column(String(7), nullable=True)
	nasp_code: Mapped[str] = mapped_column(String(7), nullable=True)
	asp_anlys_dtrm_code: Mapped[str] = mapped_column(String(13), nullable=True)
	cust_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	lndg_rights_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	joint_use_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	mil_lndg_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	inspect_method_code: Mapped[str] = mapped_column(String(1), nullable=True)
	inspector_code: Mapped[str] = mapped_column(String(1))
	last_inspection: Mapped[str] = mapped_column(String(10), nullable=True)
	last_info_response: Mapped[str] = mapped_column(String(10), nullable=True)
	fuel_types: Mapped[str] = mapped_column(String(40), nullable=True)
	airframe_repair_ser_code: Mapped[str] = mapped_column(String(5), nullable=True)
	pwr_plant_repair_ser: Mapped[str] = mapped_column(String(5), nullable=True)
	bottled_oxy_type: Mapped[str] = mapped_column(String(8), nullable=True)
	bulk_oxy_type: Mapped[str] = mapped_column(String(8), nullable=True)
	lgt_sked: Mapped[str] = mapped_column(String(7), nullable=True)
	bcn_lgt_sked: Mapped[str] = mapped_column(String(7), nullable=True)
	twr_type_code: Mapped[str] = mapped_column(String(12))
	seg_circle_mkr_flag: Mapped[str] = mapped_column(String(3), nullable=True)
	bcn_lens_color: Mapped[str] = mapped_column(String(3), nullable=True)
	lndg_fee_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	medical_use_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	arpt_psn_source: Mapped[str] = mapped_column(String(16), nullable=True)
	position_src_date: Mapped[str] = mapped_column(String(10), nullable=True)
	arpt_elev_source: Mapped[str] = mapped_column(String(16), nullable=True)
	elevation_src_date: Mapped[str] = mapped_column(String(10), nullable=True)
	contr_fuel_avbl: Mapped[str] = mapped_column(String(1), nullable=True)
	trns_strg_buoy_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	trns_strg_hgr_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	trns_strg_tie_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	other_services: Mapped[str] = mapped_column(String(110), nullable=True)
	wind_indcr_flag: Mapped[str] = mapped_column(String(3), nullable=True)
	icao_id: Mapped[str] = mapped_column(String(7), nullable=True)
	min_op_network: Mapped[str] = mapped_column(String(1))
	user_fee_flag: Mapped[str] = mapped_column(String(26), nullable=True)
	cta: Mapped[str] = mapped_column(String(4), nullable=True)

class APT_CON(Base):

	__tablename__ = 'apt_con'
	__mapper_args__ = {'primary_key': ['site_no', 'site_type_code', 'title']}


	eff_date: Mapped[str] = mapped_column(String(10))
	site_no: Mapped[str] = mapped_column(String(9), primary_key=True)
	site_type_code: Mapped[str] = mapped_column(String(1), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	arpt_id: Mapped[str] = mapped_column(String(4))
	city: Mapped[str] = mapped_column(String(40))
	country_code: Mapped[str] = mapped_column(String(2))
	title: Mapped[str] = mapped_column(String(10), primary_key=True)
	name: Mapped[str] = mapped_column(String(35), nullable=True)
	address1: Mapped[str] = mapped_column(String(35), nullable=True)
	address2: Mapped[str] = mapped_column(String(35), nullable=True)
	title_city: Mapped[str] = mapped_column(String(30), nullable=True)
	state: Mapped[str] = mapped_column(String(2), nullable=True)
	zip_code: Mapped[str] = mapped_column(String(5), nullable=True)
	zip_plus_four: Mapped[str] = mapped_column(String(4), nullable=True)
	phone_no: Mapped[str] = mapped_column(String(16), nullable=True)

class APT_RMK(Base):

	__tablename__ = 'apt_rmk'
	__mapper_args__ = {'primary_key': ['site_no', 'arpt_id', 'site_type_code', 'tab_name', 'ref_col_name', 'element', 'ref_col_seq_no']}


	eff_date: Mapped[str] = mapped_column(String(10))
	site_no: Mapped[str] = mapped_column(String(9), primary_key=True)
	site_type_code: Mapped[str] = mapped_column(String(1), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	arpt_id: Mapped[str] = mapped_column(String(4), primary_key=True)
	city: Mapped[str] = mapped_column(String(40))
	country_code: Mapped[str] = mapped_column(String(2))
	legacy_element_number: Mapped[str] = mapped_column(String(30))
	tab_name: Mapped[str] = mapped_column(String(30), primary_key=True)
	ref_col_name: Mapped[str] = mapped_column(String(30), primary_key=True)
	element: Mapped[str] = mapped_column(String(30), nullable=True, primary_key=True)
	ref_col_seq_no: Mapped[int] = mapped_column(Integer, primary_key=True)
	remark: Mapped[str] = mapped_column(String(1500))

class APT_RWY(Base):

	__tablename__ = 'apt_rwy'
	__mapper_args__ = {'primary_key': ['site_no', 'site_type_code', 'rwy_id']}


	eff_date: Mapped[str] = mapped_column(String(10))
	site_no: Mapped[str] = mapped_column(String(9), primary_key=True)
	site_type_code: Mapped[str] = mapped_column(String(1), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	arpt_id: Mapped[str] = mapped_column(String(4))
	city: Mapped[str] = mapped_column(String(40))
	country_code: Mapped[str] = mapped_column(String(2))
	rwy_id: Mapped[str] = mapped_column(String(7), primary_key=True)
	rwy_len: Mapped[int] = mapped_column(Integer)
	rwy_width: Mapped[int] = mapped_column(Integer)
	surface_type_code: Mapped[str] = mapped_column(String(10), nullable=True)
	cond: Mapped[str] = mapped_column(String(9), nullable=True)
	treatment_code: Mapped[str] = mapped_column(String(4), nullable=True)
	pcn: Mapped[int] = mapped_column(Integer, nullable=True)
	pavement_type_code: Mapped[str] = mapped_column(String(1), nullable=True)
	subgrade_strength_code: Mapped[str] = mapped_column(String(1), nullable=True)
	tire_pres_code: Mapped[str] = mapped_column(String(1), nullable=True)
	dtrm_method_code: Mapped[str] = mapped_column(String(1), nullable=True)
	rwy_lgt_code: Mapped[str] = mapped_column(String(4), nullable=True)
	rwy_len_source: Mapped[str] = mapped_column(String(16), nullable=True)
	length_source_date: Mapped[str] = mapped_column(String(10), nullable=True)
	gross_wt_sw: Mapped[int] = mapped_column(Integer, nullable=True)
	gross_wt_dw: Mapped[int] = mapped_column(Integer, nullable=True)
	gross_wt_dtw: Mapped[int] = mapped_column(Integer, nullable=True)
	gross_wt_ddtw: Mapped[int] = mapped_column(Integer, nullable=True)

class APT_RWY_END(Base):

	__tablename__ = 'apt_rwy_end'
	__mapper_args__ = {'primary_key': ['site_no', 'site_type_code', 'rwy_id', 'rwy_end_id']}


	eff_date: Mapped[str] = mapped_column(String(10))
	site_no: Mapped[str] = mapped_column(String(9), primary_key=True)
	site_type_code: Mapped[str] = mapped_column(String(1), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	arpt_id: Mapped[str] = mapped_column(String(4))
	city: Mapped[str] = mapped_column(String(40))
	country_code: Mapped[str] = mapped_column(String(2))
	rwy_id: Mapped[str] = mapped_column(String(7), primary_key=True)
	rwy_end_id: Mapped[str] = mapped_column(String(3), primary_key=True)
	true_alignment: Mapped[int] = mapped_column(Integer, nullable=True)
	ils_type: Mapped[str] = mapped_column(String(10), nullable=True)
	right_hand_traffic_pat_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	rwy_marking_type_code: Mapped[str] = mapped_column(String(4), nullable=True)
	rwy_marking_cond: Mapped[str] = mapped_column(String(4), nullable=True)
	rwy_end_lat_deg: Mapped[int] = mapped_column(Integer, nullable=True)
	rwy_end_lat_min: Mapped[int] = mapped_column(Integer, nullable=True)
	rwy_end_lat_sec: Mapped[int] = mapped_column(Integer, nullable=True)
	rwy_end_lat_hemis: Mapped[str] = mapped_column(String(1), nullable=True)
	lat_decimal: Mapped[int] = mapped_column(Integer, nullable=True)
	rwy_end_long_deg: Mapped[int] = mapped_column(Integer, nullable=True)
	rwy_end_long_min: Mapped[int] = mapped_column(Integer, nullable=True)
	rwy_end_long_sec: Mapped[int] = mapped_column(Integer, nullable=True)
	rwy_end_long_hemis: Mapped[str] = mapped_column(String(1), nullable=True)
	long_decimal: Mapped[int] = mapped_column(Integer, nullable=True)
	rwy_end_elev: Mapped[int] = mapped_column(Integer, nullable=True)
	thr_crossing_hgt: Mapped[int] = mapped_column(Integer, nullable=True)
	visual_glide_path_angle: Mapped[int] = mapped_column(Integer, nullable=True)
	displaced_thr_lat_deg: Mapped[int] = mapped_column(Integer, nullable=True)
	displaced_thr_lat_min: Mapped[int] = mapped_column(Integer, nullable=True)
	displaced_thr_lat_sec: Mapped[int] = mapped_column(Integer, nullable=True)
	displaced_thr_lat_hemis: Mapped[str] = mapped_column(String(1), nullable=True)
	lat_displaced_thr_decimal: Mapped[int] = mapped_column(Integer, nullable=True)
	displaced_thr_long_deg: Mapped[int] = mapped_column(Integer, nullable=True)
	displaced_thr_long_min: Mapped[int] = mapped_column(Integer, nullable=True)
	displaced_thr_long_sec: Mapped[int] = mapped_column(Integer, nullable=True)
	displaced_thr_long_hemis: Mapped[str] = mapped_column(String(1), nullable=True)
	long_displaced_thr_decimal: Mapped[int] = mapped_column(Integer, nullable=True)
	displaced_thr_elev: Mapped[int] = mapped_column(Integer, nullable=True)
	displaced_thr_len: Mapped[int] = mapped_column(Integer, nullable=True)
	tdz_elev: Mapped[int] = mapped_column(Integer, nullable=True)
	vgsi_code: Mapped[str] = mapped_column(String(4), nullable=True)
	rwy_visual_range_equip_code: Mapped[str] = mapped_column(String(3), nullable=True)
	rwy_vsby_value_equip_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	apch_lgt_system_code: Mapped[str] = mapped_column(String(8), nullable=True)
	rwy_end_lgts_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	cntrln_lgts_avbl_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	tdz_lgt_avbl_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	obstn_type: Mapped[str] = mapped_column(String(11), nullable=True)
	obstn_mrkd_code: Mapped[str] = mapped_column(String(2), nullable=True)
	far_part_77_code: Mapped[str] = mapped_column(String(5), nullable=True)
	obstn_clnc_slope: Mapped[int] = mapped_column(Integer, nullable=True)
	obstn_hgt: Mapped[int] = mapped_column(Integer, nullable=True)
	dist_from_thr: Mapped[int] = mapped_column(Integer, nullable=True)
	cntrln_offset: Mapped[int] = mapped_column(Integer, nullable=True)
	cntrln_dir_code: Mapped[str] = mapped_column(String(3), nullable=True)
	rwy_grad: Mapped[int] = mapped_column(Integer, nullable=True)
	rwy_grad_direction: Mapped[str] = mapped_column(String(4), nullable=True)
	rwy_end_psn_source: Mapped[str] = mapped_column(String(16), nullable=True)
	rwy_end_psn_date: Mapped[str] = mapped_column(String(10), nullable=True)
	rwy_end_elev_source: Mapped[str] = mapped_column(String(16), nullable=True)
	rwy_end_elev_date: Mapped[str] = mapped_column(String(10), nullable=True)
	dspl_thr_psn_source: Mapped[str] = mapped_column(String(16), nullable=True)
	rwy_end_dspl_thr_psn_date: Mapped[str] = mapped_column(String(10), nullable=True)
	dspl_thr_elev_source: Mapped[str] = mapped_column(String(16), nullable=True)
	rwy_end_dspl_thr_elev_date: Mapped[str] = mapped_column(String(10), nullable=True)
	tdz_elev_source: Mapped[str] = mapped_column(String(16), nullable=True)
	rwy_end_tdz_elev_date: Mapped[str] = mapped_column(String(10), nullable=True)
	tkof_run_avbl: Mapped[int] = mapped_column(Integer, nullable=True)
	tkof_dist_avbl: Mapped[int] = mapped_column(Integer, nullable=True)
	aclt_stop_dist_avbl: Mapped[int] = mapped_column(Integer, nullable=True)
	lndg_dist_avbl: Mapped[int] = mapped_column(Integer, nullable=True)
	lahso_ald: Mapped[int] = mapped_column(Integer, nullable=True)
	rwy_end_intersect_lahso: Mapped[str] = mapped_column(String(7), nullable=True)
	lahso_desc: Mapped[str] = mapped_column(String(40), nullable=True)
	lahso_lat: Mapped[str] = mapped_column(String(14), nullable=True)
	lat_lahso_decimal: Mapped[int] = mapped_column(Integer, nullable=True)
	lahso_long: Mapped[str] = mapped_column(String(15), nullable=True)
	long_lahso_decimal: Mapped[int] = mapped_column(Integer, nullable=True)
	lahso_psn_source: Mapped[str] = mapped_column(String(16), nullable=True)
	rwy_end_lahso_psn_date: Mapped[str] = mapped_column(String(10), nullable=True)

class ARB_BASE(Base):

	__tablename__ = 'arb_base'
	__mapper_args__ = {'primary_key': ['location_id']}


	eff_date: Mapped[str] = mapped_column(String(10))
	location_id: Mapped[str] = mapped_column(String(4), primary_key=True)
	location_name: Mapped[str] = mapped_column(String(30), nullable=True)
	computer_id: Mapped[str] = mapped_column(String(3))
	icao_id: Mapped[str] = mapped_column(String(7), nullable=True)
	location_type: Mapped[str] = mapped_column(String(5))
	city: Mapped[str] = mapped_column(String(40))
	state: Mapped[str] = mapped_column(String(2), nullable=True)
	country_code: Mapped[str] = mapped_column(String(2))
	lat_deg: Mapped[int] = mapped_column(Integer)
	lat_min: Mapped[int] = mapped_column(Integer)
	lat_sec: Mapped[int] = mapped_column(Integer)
	lat_hemis: Mapped[str] = mapped_column(String(1))
	lat_decimal: Mapped[int] = mapped_column(Integer)
	long_deg: Mapped[int] = mapped_column(Integer)
	long_min: Mapped[int] = mapped_column(Integer)
	long_sec: Mapped[int] = mapped_column(Integer)
	long_hemis: Mapped[str] = mapped_column(String(1))
	long_decimal: Mapped[int] = mapped_column(Integer)
	cross_ref: Mapped[str] = mapped_column(String(50), nullable=True)

class ARB_SEG(Base):

	__tablename__ = 'arb_seg'
	__mapper_args__ = {'primary_key': ['rec_id']}


	eff_date: Mapped[str] = mapped_column(String(10))
	rec_id: Mapped[str] = mapped_column(String(14), primary_key=True)
	location_id: Mapped[str] = mapped_column(String(4))
	location_name: Mapped[str] = mapped_column(String(30), nullable=True)
	altitude: Mapped[str] = mapped_column(String(10))
	type: Mapped[str] = mapped_column(String(10))
	point_seq: Mapped[int] = mapped_column(Integer)
	lat_deg: Mapped[int] = mapped_column(Integer)
	lat_min: Mapped[int] = mapped_column(Integer)
	lat_sec: Mapped[int] = mapped_column(Integer)
	lat_hemis: Mapped[str] = mapped_column(String(1))
	lat_decimal: Mapped[int] = mapped_column(Integer)
	long_deg: Mapped[int] = mapped_column(Integer)
	long_min: Mapped[int] = mapped_column(Integer)
	long_sec: Mapped[int] = mapped_column(Integer)
	long_hemis: Mapped[str] = mapped_column(String(1))
	long_decimal: Mapped[int] = mapped_column(Integer)
	bndry_pt_descrip: Mapped[str] = mapped_column(String(300), nullable=True)
	nas_descrip_flag: Mapped[str] = mapped_column(String(1), nullable=True)

class ATC_ATIS(Base):

	__tablename__ = 'atc_atis'
	__mapper_args__ = {'primary_key': ['site_no', 'site_type_code', 'atis_no']}


	eff_date: Mapped[str] = mapped_column(String(10))
	site_no: Mapped[str] = mapped_column(String(9), primary_key=True)
	site_type_code: Mapped[str] = mapped_column(String(1), primary_key=True)
	facility_type: Mapped[str] = mapped_column(String(12))
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	facility_id: Mapped[str] = mapped_column(String(4))
	city: Mapped[str] = mapped_column(String(40))
	country_code: Mapped[str] = mapped_column(String(2))
	atis_no: Mapped[int] = mapped_column(Integer, primary_key=True)
	description: Mapped[str] = mapped_column(String(100), nullable=True)
	atis_hrs: Mapped[str] = mapped_column(String(200))
	atis_phone_no: Mapped[str] = mapped_column(String(18), nullable=True)

class ATC_BASE(Base):

	__tablename__ = 'atc_base'
	__mapper_args__ = {'primary_key': ['facility_type', 'facility_id']}


	eff_date: Mapped[str] = mapped_column(String(10))
	site_no: Mapped[str] = mapped_column(String(9), nullable=True)
	site_type_code: Mapped[str] = mapped_column(String(1), nullable=True)
	facility_type: Mapped[str] = mapped_column(String(12), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	facility_id: Mapped[str] = mapped_column(String(4), primary_key=True)
	city: Mapped[str] = mapped_column(String(40))
	country_code: Mapped[str] = mapped_column(String(2))
	icao_id: Mapped[str] = mapped_column(String(7), nullable=True)
	facility_name: Mapped[str] = mapped_column(String(50))
	region_code: Mapped[str] = mapped_column(String(3), nullable=True)
	twr_operator_code: Mapped[str] = mapped_column(String(6), nullable=True)
	twr_call: Mapped[str] = mapped_column(String(26), nullable=True)
	twr_hrs: Mapped[str] = mapped_column(String(200), nullable=True)
	primary_apch_radio_call: Mapped[str] = mapped_column(String(26), nullable=True)
	apch_p_provider: Mapped[str] = mapped_column(String(700), nullable=True)
	apch_p_prov_type_cd: Mapped[str] = mapped_column(String(1), nullable=True)
	secondary_apch_radio_call: Mapped[str] = mapped_column(String(26), nullable=True)
	apch_s_provider: Mapped[str] = mapped_column(String(700), nullable=True)
	apch_s_prov_type_cd: Mapped[str] = mapped_column(String(1), nullable=True)
	primary_dep_radio_call: Mapped[str] = mapped_column(String(26), nullable=True)
	dep_p_provider: Mapped[str] = mapped_column(String(700), nullable=True)
	dep_p_prov_type_cd: Mapped[str] = mapped_column(String(1), nullable=True)
	secondary_dep_radio_call: Mapped[str] = mapped_column(String(26), nullable=True)
	dep_s_provider: Mapped[str] = mapped_column(String(700), nullable=True)
	dep_s_prov_type_cd: Mapped[str] = mapped_column(String(1), nullable=True)
	ctl_fac_apch_dep_calls: Mapped[str] = mapped_column(String(54), nullable=True)
	apch_dep_oper_code: Mapped[str] = mapped_column(String(1), nullable=True)
	ctl_prvding_hrs: Mapped[str] = mapped_column(String(200), nullable=True)
	secondary_ctl_prvding_hrs: Mapped[str] = mapped_column(String(200), nullable=True)

class ATC_RMK(Base):

	__tablename__ = 'atc_rmk'
	__mapper_args__ = {'primary_key': ['facility_type', 'facility_id', 'ref_col_name', 'remark_no']}


	eff_date: Mapped[str] = mapped_column(String(10))
	site_no: Mapped[str] = mapped_column(String(9), nullable=True)
	site_type_code: Mapped[str] = mapped_column(String(1), nullable=True)
	facility_type: Mapped[str] = mapped_column(String(12), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	facility_id: Mapped[str] = mapped_column(String(4), primary_key=True)
	city: Mapped[str] = mapped_column(String(40))
	country_code: Mapped[str] = mapped_column(String(2))
	legacy_element_number: Mapped[str] = mapped_column(String(30))
	tab_name: Mapped[str] = mapped_column(String(30))
	ref_col_name: Mapped[str] = mapped_column(String(30), primary_key=True)
	remark_no: Mapped[int] = mapped_column(Integer, primary_key=True)
	remark: Mapped[str] = mapped_column(String(1500))

class ATC_SVC(Base):

	__tablename__ = 'atc_svc'
	__mapper_args__ = {'primary_key': ['facility_type', 'facility_id', 'ctl_svc']}


	eff_date: Mapped[str] = mapped_column(String(10))
	site_no: Mapped[str] = mapped_column(String(9), nullable=True)
	site_type_code: Mapped[str] = mapped_column(String(1), nullable=True)
	facility_type: Mapped[str] = mapped_column(String(12), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	facility_id: Mapped[str] = mapped_column(String(4), primary_key=True)
	city: Mapped[str] = mapped_column(String(40))
	country_code: Mapped[str] = mapped_column(String(2))
	ctl_svc: Mapped[str] = mapped_column(String(200), primary_key=True)

class AWOS(Base):

	__tablename__ = 'awos'
	__mapper_args__ = {'primary_key': ['asos_awos_id', 'asos_awos_type']}


	eff_date: Mapped[str] = mapped_column(String(10))
	asos_awos_id: Mapped[str] = mapped_column(String(4), primary_key=True)
	asos_awos_type: Mapped[str] = mapped_column(String(10), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	city: Mapped[str] = mapped_column(String(40))
	country_code: Mapped[str] = mapped_column(String(2))
	commissioned_date: Mapped[str] = mapped_column(String(10), nullable=True)
	navaid_flag: Mapped[str] = mapped_column(String(1))
	lat_deg: Mapped[int] = mapped_column(Integer, nullable=True)
	lat_min: Mapped[int] = mapped_column(Integer, nullable=True)
	lat_sec: Mapped[int] = mapped_column(Integer, nullable=True)
	lat_hemis: Mapped[str] = mapped_column(String(1), nullable=True)
	lat_decimal: Mapped[int] = mapped_column(Integer, nullable=True)
	long_deg: Mapped[int] = mapped_column(Integer, nullable=True)
	long_min: Mapped[int] = mapped_column(Integer, nullable=True)
	long_sec: Mapped[int] = mapped_column(Integer, nullable=True)
	long_hemis: Mapped[str] = mapped_column(String(1), nullable=True)
	long_decimal: Mapped[int] = mapped_column(Integer, nullable=True)
	elev: Mapped[int] = mapped_column(Integer, nullable=True)
	survey_method_code: Mapped[str] = mapped_column(String(1), nullable=True)
	phone_no: Mapped[str] = mapped_column(String(14), nullable=True)
	second_phone_no: Mapped[str] = mapped_column(String(14), nullable=True)
	site_no: Mapped[str] = mapped_column(String(9), nullable=True)
	site_type_code: Mapped[str] = mapped_column(String(1), nullable=True)
	remark: Mapped[str] = mapped_column(String(1500), nullable=True)

class AWY_BASE(Base):

	__tablename__ = 'awy_base'
	__mapper_args__ = {'primary_key': ['awy_location', 'awy_id']}


	eff_date: Mapped[str] = mapped_column(String(10))
	regulatory: Mapped[str] = mapped_column(String(1))
	awy_designation: Mapped[str] = mapped_column(String(2))
	awy_location: Mapped[str] = mapped_column(String(1), primary_key=True)
	awy_id: Mapped[str] = mapped_column(String(12), primary_key=True)
	update_date: Mapped[str] = mapped_column(String(10))
	remark: Mapped[str] = mapped_column(String(1500), nullable=True)
	airway_string: Mapped[str] = mapped_column(String(1500))

class AWY_SEG(Base):

	__tablename__ = 'awy_seg'
	__mapper_args__ = {'primary_key': ['awy_location', 'awy_id', 'seg_value']}


	eff_date: Mapped[str] = mapped_column(String(10))
	regulatory: Mapped[str] = mapped_column(String(1))
	awy_location: Mapped[str] = mapped_column(String(1), primary_key=True)
	awy_id: Mapped[str] = mapped_column(String(12), primary_key=True)
	point_seq: Mapped[int] = mapped_column(Integer)
	seg_value: Mapped[str] = mapped_column(String(30), primary_key=True)
	seg_type: Mapped[str] = mapped_column(String(25), nullable=True)
	nav_name: Mapped[str] = mapped_column(String(30), nullable=True)
	nav_city: Mapped[str] = mapped_column(String(40), nullable=True)
	icao_region_code: Mapped[str] = mapped_column(String(2), nullable=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	country_code: Mapped[str] = mapped_column(String(2), nullable=True)
	next_seg: Mapped[str] = mapped_column(String(30), nullable=True)
	mag_course: Mapped[int] = mapped_column(Integer, nullable=True)
	opp_mag_course: Mapped[int] = mapped_column(Integer, nullable=True)
	mag_course_dist: Mapped[int] = mapped_column(Integer, nullable=True)
	chgovr_pt: Mapped[str] = mapped_column(String(4), nullable=True)
	chgovr_pt_name: Mapped[str] = mapped_column(String(30), nullable=True)
	chgovr_pt_dist: Mapped[int] = mapped_column(Integer, nullable=True)
	awy_seg_gap_flag: Mapped[str] = mapped_column(String(1))
	signal_gap_flag: Mapped[str] = mapped_column(String(1))
	dogleg: Mapped[str] = mapped_column(String(1))
	remark: Mapped[str] = mapped_column(String(1500), nullable=True)

class AWY_ALT(Base):

	__tablename__ = 'awy_alt'
	__mapper_args__ = {'primary_key': ['awy_location', 'awy_id', 'mea_pt']}


	eff_date: Mapped[str] = mapped_column(String(10))
	regulatory: Mapped[str] = mapped_column(String(1))
	awy_location: Mapped[str] = mapped_column(String(1), primary_key=True)
	awy_id: Mapped[str] = mapped_column(String(12), primary_key=True)
	point_seq: Mapped[int] = mapped_column(Integer)
	mea_pt: Mapped[str] = mapped_column(String(30), primary_key=True)
	mea_pt_type: Mapped[str] = mapped_column(String(25), nullable=True)
	nav_name: Mapped[str] = mapped_column(String(30), nullable=True)
	nav_city: Mapped[str] = mapped_column(String(40), nullable=True)
	icao_region_code: Mapped[str] = mapped_column(String(2), nullable=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	country_code: Mapped[str] = mapped_column(String(2), nullable=True)
	next_mea_pt: Mapped[str] = mapped_column(String(30))
	min_enroute_alt: Mapped[int] = mapped_column(Integer, nullable=True)
	min_enroute_alt_dir: Mapped[str] = mapped_column(String(7), nullable=True)
	min_enroute_alt_opposite: Mapped[int] = mapped_column(Integer, nullable=True)
	min_enroute_alt_opposite_dir: Mapped[str] = mapped_column(String(7), nullable=True)
	gps_min_enroute_alt: Mapped[int] = mapped_column(Integer, nullable=True)
	gps_min_enroute_alt_dir: Mapped[str] = mapped_column(String(7), nullable=True)
	gps_min_enroute_alt_opposite: Mapped[int] = mapped_column(Integer, nullable=True)
	gps_mea_opposite_dir: Mapped[str] = mapped_column(String(7), nullable=True)
	dd_iru_mea: Mapped[int] = mapped_column(Integer, nullable=True)
	dd_iru_mea_dir: Mapped[str] = mapped_column(String(7), nullable=True)
	dd_i_mea_opposite: Mapped[int] = mapped_column(Integer, nullable=True)
	dd_i_mea_opposite_dir: Mapped[str] = mapped_column(String(7), nullable=True)
	min_obstn_clnc_alt: Mapped[int] = mapped_column(Integer, nullable=True)
	min_cross_alt: Mapped[int] = mapped_column(Integer, nullable=True)
	min_cross_alt_dir: Mapped[str] = mapped_column(String(7), nullable=True)
	min_cross_alt_nav_pt: Mapped[str] = mapped_column(String(30), nullable=True)
	min_cross_alt_opposite: Mapped[int] = mapped_column(Integer, nullable=True)
	min_cross_alt_opposite_dir: Mapped[str] = mapped_column(String(7), nullable=True)
	min_recep_alt: Mapped[int] = mapped_column(Integer, nullable=True)
	max_auth_alt: Mapped[int] = mapped_column(Integer, nullable=True)
	mea_gap: Mapped[str] = mapped_column(String(1), nullable=True)
	reqd_nav_performance: Mapped[int] = mapped_column(Integer, nullable=True)
	remark: Mapped[str] = mapped_column(String(1500), nullable=True)

class AWY_SEG_ALT(Base):

	__tablename__ = 'awy_seg_alt'
	__mapper_args__ = {'primary_key': ['awy_location', 'awy_id', 'from_point']}


	eff_date: Mapped[str] = mapped_column(String(10))
	regulatory: Mapped[str] = mapped_column(String(1))
	awy_location: Mapped[str] = mapped_column(String(1), primary_key=True)
	awy_id: Mapped[str] = mapped_column(String(12), primary_key=True)
	point_seq: Mapped[int] = mapped_column(Integer)
	from_point: Mapped[str] = mapped_column(String(30), primary_key=True)
	from_pt_type: Mapped[str] = mapped_column(String(25), nullable=True)
	nav_name: Mapped[str] = mapped_column(String(30), nullable=True)
	nav_city: Mapped[str] = mapped_column(String(40), nullable=True)
	artcc: Mapped[str] = mapped_column(String(4), nullable=True)
	icao_region_code: Mapped[str] = mapped_column(String(2), nullable=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	country_code: Mapped[str] = mapped_column(String(2), nullable=True)
	to_point: Mapped[str] = mapped_column(String(30), nullable=True)
	mag_course: Mapped[int] = mapped_column(Integer, nullable=True)
	opp_mag_course: Mapped[int] = mapped_column(Integer, nullable=True)
	mag_course_dist: Mapped[int] = mapped_column(Integer, nullable=True)
	chgovr_pt: Mapped[str] = mapped_column(String(4), nullable=True)
	chgovr_pt_name: Mapped[str] = mapped_column(String(30), nullable=True)
	chgovr_pt_dist: Mapped[int] = mapped_column(Integer, nullable=True)
	awy_seg_gap_flag: Mapped[str] = mapped_column(String(1))
	signal_gap_flag: Mapped[str] = mapped_column(String(1))
	dogleg: Mapped[str] = mapped_column(String(1))
	min_enroute_alt: Mapped[int] = mapped_column(Integer, nullable=True)
	min_enroute_alt_dir: Mapped[str] = mapped_column(String(7), nullable=True)
	min_enroute_alt_opposite: Mapped[int] = mapped_column(Integer, nullable=True)
	min_enroute_alt_opposite_dir: Mapped[str] = mapped_column(String(7), nullable=True)
	gps_min_enroute_alt: Mapped[int] = mapped_column(Integer, nullable=True)
	gps_min_enroute_alt_dir: Mapped[str] = mapped_column(String(7), nullable=True)
	gps_min_enroute_alt_opposite: Mapped[int] = mapped_column(Integer, nullable=True)
	gps_mea_opposite_dir: Mapped[str] = mapped_column(String(7), nullable=True)
	dd_iru_mea: Mapped[int] = mapped_column(Integer, nullable=True)
	dd_iru_mea_dir: Mapped[str] = mapped_column(String(7), nullable=True)
	dd_i_mea_opposite: Mapped[int] = mapped_column(Integer, nullable=True)
	dd_i_mea_opposite_dir: Mapped[str] = mapped_column(String(7), nullable=True)
	min_obstn_clnc_alt: Mapped[int] = mapped_column(Integer, nullable=True)
	min_cross_alt: Mapped[int] = mapped_column(Integer, nullable=True)
	min_cross_alt_dir: Mapped[str] = mapped_column(String(7), nullable=True)
	min_cross_alt_nav_pt: Mapped[str] = mapped_column(String(30), nullable=True)
	min_cross_alt_opposite: Mapped[int] = mapped_column(Integer, nullable=True)
	min_cross_alt_opposite_dir: Mapped[str] = mapped_column(String(7), nullable=True)
	min_recep_alt: Mapped[int] = mapped_column(Integer, nullable=True)
	max_auth_alt: Mapped[int] = mapped_column(Integer, nullable=True)
	mea_gap: Mapped[str] = mapped_column(String(1), nullable=True)
	reqd_nav_performance: Mapped[int] = mapped_column(Integer, nullable=True)
	remark: Mapped[str] = mapped_column(String(1500), nullable=True)
	next_mea_pt: Mapped[str] = mapped_column(String(30), nullable=True)

class CDR(Base):

	__tablename__ = 'cdr'
	__mapper_args__ = {'primary_key': ['rcode']}


	rcode: Mapped[str] = mapped_column(String(8), primary_key=True)
	orig: Mapped[str] = mapped_column(String(4))
	dest: Mapped[str] = mapped_column(String(4))
	depfix: Mapped[str] = mapped_column(String(6))
	route_string: Mapped[str] = mapped_column(String(200))
	dcntr: Mapped[str] = mapped_column(String(3))
	acntr: Mapped[str] = mapped_column(String(3))
	tcntrs: Mapped[str] = mapped_column(String(100), nullable=True)
	coordreq: Mapped[str] = mapped_column(String(1))
	play: Mapped[str] = mapped_column(String(25), nullable=True)
	naveqp: Mapped[int] = mapped_column(Integer)
	length: Mapped[int] = mapped_column(Integer, nullable=True)

class CLS_ARSP(Base):

	__tablename__ = 'cls_arsp'
	__mapper_args__ = {'primary_key': ['site_no']}


	eff_date: Mapped[str] = mapped_column(String(10))
	site_no: Mapped[str] = mapped_column(String(9), primary_key=True)
	site_type_code: Mapped[str] = mapped_column(String(1))
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	arpt_id: Mapped[str] = mapped_column(String(4))
	city: Mapped[str] = mapped_column(String(40))
	country_code: Mapped[str] = mapped_column(String(2))
	class_b_airspace: Mapped[str] = mapped_column(String(1), nullable=True)
	class_c_airspace: Mapped[str] = mapped_column(String(1), nullable=True)
	class_d_airspace: Mapped[str] = mapped_column(String(1), nullable=True)
	class_e_airspace: Mapped[str] = mapped_column(String(1), nullable=True)
	airspace_hrs: Mapped[str] = mapped_column(String(300), nullable=True)
	remark: Mapped[str] = mapped_column(String(1500), nullable=True)

class COM(Base):

	__tablename__ = 'com'
	__mapper_args__ = {'primary_key': ['comm_loc_id', 'comm_type', 'state_code', 'comm_outlet_name', 'facility_id']}


	eff_date: Mapped[str] = mapped_column(String(10))
	comm_loc_id: Mapped[str] = mapped_column(String(6), nullable=True, primary_key=True)
	comm_type: Mapped[str] = mapped_column(String(5), primary_key=True)
	nav_id: Mapped[str] = mapped_column(String(4), nullable=True)
	nav_type: Mapped[str] = mapped_column(String(25), nullable=True)
	city: Mapped[str] = mapped_column(String(40), nullable=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True, primary_key=True)
	region_code: Mapped[str] = mapped_column(String(3), nullable=True)
	country_code: Mapped[str] = mapped_column(String(2))
	comm_outlet_name: Mapped[str] = mapped_column(String(30), primary_key=True)
	lat_deg: Mapped[int] = mapped_column(Integer)
	lat_min: Mapped[int] = mapped_column(Integer)
	lat_sec: Mapped[int] = mapped_column(Integer)
	lat_hemis: Mapped[str] = mapped_column(String(1))
	lat_decimal: Mapped[int] = mapped_column(Integer)
	long_deg: Mapped[int] = mapped_column(Integer)
	long_min: Mapped[int] = mapped_column(Integer)
	long_sec: Mapped[int] = mapped_column(Integer)
	long_hemis: Mapped[str] = mapped_column(String(1))
	long_decimal: Mapped[int] = mapped_column(Integer)
	facility_id: Mapped[str] = mapped_column(String(4), primary_key=True)
	facility_name: Mapped[str] = mapped_column(String(30))
	alt_fss_id: Mapped[str] = mapped_column(String(4), nullable=True)
	alt_fss_name: Mapped[str] = mapped_column(String(30), nullable=True)
	opr_hrs: Mapped[str] = mapped_column(String(65), nullable=True)
	comm_status_code: Mapped[str] = mapped_column(String(1), nullable=True)
	comm_status_date: Mapped[str] = mapped_column(String(10), nullable=True)
	remark: Mapped[str] = mapped_column(String(1500), nullable=True)

class DP_BASE(Base):

	__tablename__ = 'dp_base'
	__mapper_args__ = {'primary_key': ['dp_name', 'amendment_no', 'dp_computer_code']}


	eff_date: Mapped[str] = mapped_column(String(10))
	dp_name: Mapped[str] = mapped_column(String(30), primary_key=True)
	amendment_no: Mapped[str] = mapped_column(String(5), primary_key=True)
	artcc: Mapped[str] = mapped_column(String(12), nullable=True)
	dp_amend_eff_date: Mapped[str] = mapped_column(String(10))
	rnav_flag: Mapped[str] = mapped_column(String(1))
	dp_computer_code: Mapped[str] = mapped_column(String(12), primary_key=True)
	graphical_dp_type: Mapped[str] = mapped_column(String(9))
	served_arpt: Mapped[str] = mapped_column(String(200))

class DP_APT(Base):

	__tablename__ = 'dp_apt'
	__mapper_args__ = {'primary_key': ['dp_computer_code', 'body_name', 'arpt_id', 'rwy_end_id']}


	eff_date: Mapped[str] = mapped_column(String(10))
	dp_name: Mapped[str] = mapped_column(String(30))
	artcc: Mapped[str] = mapped_column(String(12), nullable=True)
	dp_computer_code: Mapped[str] = mapped_column(String(12), primary_key=True)
	body_name: Mapped[str] = mapped_column(String(110), primary_key=True)
	body_seq: Mapped[int] = mapped_column(Integer)
	arpt_id: Mapped[str] = mapped_column(String(4), primary_key=True)
	rwy_end_id: Mapped[str] = mapped_column(String(3), nullable=True, primary_key=True)

class DP_RTE(Base):

	__tablename__ = 'dp_rte'
	__mapper_args__ = {'primary_key': ['dp_name', 'dp_computer_code', 'body_seq', 'point_seq', 'route_portion_type', 'route_name']}


	eff_date: Mapped[str] = mapped_column(String(10))
	dp_name: Mapped[str] = mapped_column(String(30), primary_key=True)
	artcc: Mapped[str] = mapped_column(String(12), nullable=True)
	dp_computer_code: Mapped[str] = mapped_column(String(12), primary_key=True)
	route_portion_type: Mapped[str] = mapped_column(String(10), primary_key=True)
	route_name: Mapped[str] = mapped_column(String(110), primary_key=True)
	body_seq: Mapped[int] = mapped_column(Integer, primary_key=True)
	transition_computer_code: Mapped[str] = mapped_column(String(20), nullable=True)
	point_seq: Mapped[int] = mapped_column(Integer, primary_key=True)
	point: Mapped[str] = mapped_column(String(10))
	icao_region_code: Mapped[str] = mapped_column(String(2), nullable=True)
	point_type: Mapped[str] = mapped_column(String(25))
	next_point: Mapped[str] = mapped_column(String(10), nullable=True)
	arpt_rwy_assoc: Mapped[str] = mapped_column(String(1500), nullable=True)

class FIX_BASE(Base):

	__tablename__ = 'fix_base'
	__mapper_args__ = {'primary_key': ['fix_id', 'icao_region_code']}


	eff_date: Mapped[str] = mapped_column(String(10))
	fix_id: Mapped[str] = mapped_column(String(30), primary_key=True)
	icao_region_code: Mapped[str] = mapped_column(String(2), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	country_code: Mapped[str] = mapped_column(String(2))
	lat_deg: Mapped[int] = mapped_column(Integer)
	lat_min: Mapped[int] = mapped_column(Integer)
	lat_sec: Mapped[int] = mapped_column(Integer)
	lat_hemis: Mapped[str] = mapped_column(String(1))
	lat_decimal: Mapped[int] = mapped_column(Integer)
	long_deg: Mapped[int] = mapped_column(Integer)
	long_min: Mapped[int] = mapped_column(Integer)
	long_sec: Mapped[int] = mapped_column(Integer)
	long_hemis: Mapped[str] = mapped_column(String(1))
	long_decimal: Mapped[int] = mapped_column(Integer)
	fix_id_old: Mapped[str] = mapped_column(String(30), nullable=True)
	charting_remark: Mapped[str] = mapped_column(String(38), nullable=True)
	fix_use_code: Mapped[str] = mapped_column(String(5))
	artcc_id_high: Mapped[str] = mapped_column(String(4), nullable=True)
	artcc_id_low: Mapped[str] = mapped_column(String(4))
	pitch_flag: Mapped[str] = mapped_column(String(1))
	catch_flag: Mapped[str] = mapped_column(String(1))
	sua_atcaa_flag: Mapped[str] = mapped_column(String(1))
	min_recep_alt: Mapped[int] = mapped_column(Integer, nullable=True)
	compulsory: Mapped[str] = mapped_column(String(8), nullable=True)
	charts: Mapped[str] = mapped_column(String(600), nullable=True)

class FIX_CHRT(Base):

	__tablename__ = 'fix_chrt'
	__mapper_args__ = {'primary_key': ['fix_id', 'icao_region_code', 'charting_type_desc']}


	eff_date: Mapped[str] = mapped_column(String(10))
	fix_id: Mapped[str] = mapped_column(String(30), primary_key=True)
	icao_region_code: Mapped[str] = mapped_column(String(2), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	country_code: Mapped[str] = mapped_column(String(2))
	charting_type_desc: Mapped[str] = mapped_column(String(22), primary_key=True)

class FIX_NAV(Base):

	__tablename__ = 'fix_nav'
	__mapper_args__ = {'primary_key': ['fix_id', 'icao_region_code', 'nav_id', 'nav_type']}


	eff_date: Mapped[str] = mapped_column(String(10))
	fix_id: Mapped[str] = mapped_column(String(30), primary_key=True)
	icao_region_code: Mapped[str] = mapped_column(String(2), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	country_code: Mapped[str] = mapped_column(String(2))
	nav_id: Mapped[str] = mapped_column(String(6), primary_key=True)
	nav_type: Mapped[str] = mapped_column(String(25), primary_key=True)
	bearing: Mapped[int] = mapped_column(Integer, nullable=True)
	distance: Mapped[int] = mapped_column(Integer, nullable=True)

class FRQ(Base):

	__tablename__ = 'frq'
	__mapper_args__ = {'primary_key': ['facility', 'serviced_facility', 'serviced_site_type', 'serviced_state', 'freq', 'sectorization', 'freq_use']}


	eff_date: Mapped[str] = mapped_column(String(10))
	facility: Mapped[str] = mapped_column(String(30), nullable=True, primary_key=True)
	fac_name: Mapped[str] = mapped_column(String(50), nullable=True)
	facility_type: Mapped[str] = mapped_column(String(12))
	artcc_or_fss_id: Mapped[str] = mapped_column(String(4), nullable=True)
	cpdlc: Mapped[str] = mapped_column(String(100), nullable=True)
	tower_hrs: Mapped[str] = mapped_column(String(200), nullable=True)
	serviced_facility: Mapped[str] = mapped_column(String(30), primary_key=True)
	serviced_fac_name: Mapped[str] = mapped_column(String(50), nullable=True)
	serviced_site_type: Mapped[str] = mapped_column(String(25), nullable=True, primary_key=True)
	lat_decimal: Mapped[int] = mapped_column(Integer, nullable=True)
	long_decimal: Mapped[int] = mapped_column(Integer, nullable=True)
	serviced_city: Mapped[str] = mapped_column(String(40), nullable=True)
	serviced_state: Mapped[str] = mapped_column(String(2), nullable=True, primary_key=True)
	serviced_country: Mapped[str] = mapped_column(String(2), nullable=True)
	tower_or_comm_call: Mapped[str] = mapped_column(String(30), nullable=True)
	primary_approach_radio_call: Mapped[str] = mapped_column(String(26), nullable=True)
	freq: Mapped[str] = mapped_column(String(40), nullable=True, primary_key=True)
	sectorization: Mapped[str] = mapped_column(String(50), nullable=True, primary_key=True)
	freq_use: Mapped[str] = mapped_column(String(600), nullable=True, primary_key=True)
	remark: Mapped[str] = mapped_column(String(1500), nullable=True)

class FSS_BASE(Base):

	__tablename__ = 'fss_base'
	__mapper_args__ = {'primary_key': ['fss_id']}


	eff_date: Mapped[str] = mapped_column(String(10))
	fss_id: Mapped[str] = mapped_column(String(4), primary_key=True)
	name: Mapped[str] = mapped_column(String(30))
	update_date: Mapped[str] = mapped_column(String(10), nullable=True)
	fss_fac_type: Mapped[str] = mapped_column(String(8))
	voice_call: Mapped[str] = mapped_column(String(30), nullable=True)
	city: Mapped[str] = mapped_column(String(40))
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	country_code: Mapped[str] = mapped_column(String(2))
	lat_deg: Mapped[int] = mapped_column(Integer)
	lat_min: Mapped[int] = mapped_column(Integer)
	lat_sec: Mapped[int] = mapped_column(Integer)
	lat_hemis: Mapped[str] = mapped_column(String(1))
	lat_decimal: Mapped[int] = mapped_column(Integer)
	long_deg: Mapped[int] = mapped_column(Integer)
	long_min: Mapped[int] = mapped_column(Integer)
	long_sec: Mapped[int] = mapped_column(Integer)
	long_hemis: Mapped[str] = mapped_column(String(1))
	long_decimal: Mapped[int] = mapped_column(Integer)
	opr_hours: Mapped[str] = mapped_column(String(65))
	fac_status: Mapped[str] = mapped_column(String(1), nullable=True)
	alternate_fss: Mapped[str] = mapped_column(String(4), nullable=True)
	wea_radar_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	phone_no: Mapped[str] = mapped_column(String(16), nullable=True)
	toll_free_no: Mapped[str] = mapped_column(String(16), nullable=True)

class FSS_RMK(Base):

	__tablename__ = 'fss_rmk'
	__mapper_args__ = {'primary_key': ['fss_id', 'ref_col_name', 'ref_col_seq_no']}


	eff_date: Mapped[str] = mapped_column(String(10))
	fss_id: Mapped[str] = mapped_column(String(4), primary_key=True)
	name: Mapped[str] = mapped_column(String(30))
	city: Mapped[str] = mapped_column(String(40))
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	country_code: Mapped[str] = mapped_column(String(2))
	ref_col_name: Mapped[str] = mapped_column(String(30), primary_key=True)
	ref_col_seq_no: Mapped[int] = mapped_column(Integer, primary_key=True)
	remark: Mapped[str] = mapped_column(String(300))

class HPF_BASE(Base):

	__tablename__ = 'hpf_base'
	__mapper_args__ = {'primary_key': ['hp_name', 'hp_no']}


	eff_date: Mapped[str] = mapped_column(String(10))
	hp_name: Mapped[str] = mapped_column(String(80), primary_key=True)
	hp_no: Mapped[int] = mapped_column(Integer, primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	fix_id: Mapped[str] = mapped_column(String(30), nullable=True)
	icao_region_code: Mapped[str] = mapped_column(String(2), nullable=True)
	nav_id: Mapped[str] = mapped_column(String(6), nullable=True)
	nav_type: Mapped[str] = mapped_column(String(25), nullable=True)
	hold_direction: Mapped[str] = mapped_column(String(3), nullable=True)
	hold_deg_or_crs: Mapped[str] = mapped_column(String(3), nullable=True)
	azimuth: Mapped[str] = mapped_column(String(4))
	course_inbound_deg: Mapped[int] = mapped_column(Integer, nullable=True)
	turn_direction: Mapped[str] = mapped_column(String(3))
	leg_length_dist: Mapped[int] = mapped_column(Integer, nullable=True)
	country_code: Mapped[str] = mapped_column(String(2), nullable=True)

class HPF_CHRT(Base):

	__tablename__ = 'hpf_chrt'
	__mapper_args__ = {'primary_key': ['hp_name', 'hp_no', 'charting_type_desc']}


	eff_date: Mapped[str] = mapped_column(String(10))
	hp_name: Mapped[str] = mapped_column(String(80), primary_key=True)
	hp_no: Mapped[int] = mapped_column(Integer, primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	charting_type_desc: Mapped[str] = mapped_column(String(22), primary_key=True)
	country_code: Mapped[str] = mapped_column(String(2), nullable=True)

class HPF_RMK(Base):

	__tablename__ = 'hpf_rmk'
	__mapper_args__ = {'primary_key': ['hp_name', 'hp_no', 'tab_name', 'ref_col_name', 'ref_col_seq_no']}


	eff_date: Mapped[str] = mapped_column(String(10))
	hp_name: Mapped[str] = mapped_column(String(80), primary_key=True)
	hp_no: Mapped[int] = mapped_column(Integer, primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	tab_name: Mapped[str] = mapped_column(String(30), primary_key=True)
	ref_col_name: Mapped[str] = mapped_column(String(30), primary_key=True)
	ref_col_seq_no: Mapped[int] = mapped_column(Integer, primary_key=True)
	remark: Mapped[str] = mapped_column(String(300))
	country_code: Mapped[str] = mapped_column(String(2), nullable=True)

class HPF_SPD_ALT(Base):

	__tablename__ = 'hpf_spd_alt'
	__mapper_args__ = {'primary_key': ['hp_name', 'hp_no', 'speed_range', 'altitude']}


	eff_date: Mapped[str] = mapped_column(String(10))
	hp_name: Mapped[str] = mapped_column(String(80), primary_key=True)
	hp_no: Mapped[int] = mapped_column(Integer, primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	speed_range: Mapped[str] = mapped_column(String(7), primary_key=True)
	altitude: Mapped[str] = mapped_column(String(10), primary_key=True)
	country_code: Mapped[str] = mapped_column(String(2), nullable=True)

class ILS_BASE(Base):

	__tablename__ = 'ils_base'
	__mapper_args__ = {'primary_key': ['site_no', 'site_no', 'site_type_code', 'rwy_end_id']}


	eff_date: Mapped[str] = mapped_column(String(10))
	site_no: Mapped[str] = mapped_column(String(9), primary_key=True)
	site_type_code: Mapped[str] = mapped_column(String(1), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	arpt_id: Mapped[str] = mapped_column(String(4))
	city: Mapped[str] = mapped_column(String(40))
	country_code: Mapped[str] = mapped_column(String(2))
	rwy_end_id: Mapped[str] = mapped_column(String(3), primary_key=True)
	ils_loc_id: Mapped[str] = mapped_column(String(6))
	system_type_code: Mapped[str] = mapped_column(String(2))
	state_name: Mapped[str] = mapped_column(String(30), nullable=True)
	region_code: Mapped[str] = mapped_column(String(3))
	rwy_len: Mapped[int] = mapped_column(Integer)
	rwy_width: Mapped[int] = mapped_column(Integer)
	category: Mapped[str] = mapped_column(String(4), nullable=True)
	owner: Mapped[str] = mapped_column(String(40))
	operator: Mapped[str] = mapped_column(String(40))
	apch_bear: Mapped[int] = mapped_column(Integer)
	mag_var: Mapped[int] = mapped_column(Integer)
	mag_var_hemis: Mapped[str] = mapped_column(String(1))
	component_status: Mapped[str] = mapped_column(String(30))
	component_status_date: Mapped[str] = mapped_column(String(10))
	lat_deg: Mapped[int] = mapped_column(Integer)
	lat_min: Mapped[int] = mapped_column(Integer)
	lat_sec: Mapped[int] = mapped_column(Integer)
	lat_hemis: Mapped[str] = mapped_column(String(1))
	lat_decimal: Mapped[int] = mapped_column(Integer)
	long_deg: Mapped[int] = mapped_column(Integer)
	long_min: Mapped[int] = mapped_column(Integer)
	long_sec: Mapped[int] = mapped_column(Integer)
	long_hemis: Mapped[str] = mapped_column(String(1))
	long_decimal: Mapped[int] = mapped_column(Integer)
	lat_long_source_code: Mapped[str] = mapped_column(String(2), nullable=True)
	site_elevation: Mapped[int] = mapped_column(Integer, nullable=True)
	loc_freq: Mapped[int] = mapped_column(Integer)
	bk_course_status_code: Mapped[str] = mapped_column(String(1), nullable=True)

class ILS_DME(Base):

	__tablename__ = 'ils_dme'
	__mapper_args__ = {'primary_key': ['site_no', 'site_type_code', 'rwy_end_id']}


	eff_date: Mapped[str] = mapped_column(String(10))
	site_no: Mapped[str] = mapped_column(String(9), primary_key=True)
	site_type_code: Mapped[str] = mapped_column(String(1), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	arpt_id: Mapped[str] = mapped_column(String(4))
	city: Mapped[str] = mapped_column(String(40))
	country_code: Mapped[str] = mapped_column(String(2))
	rwy_end_id: Mapped[str] = mapped_column(String(3), primary_key=True)
	ils_loc_id: Mapped[str] = mapped_column(String(6))
	system_type_code: Mapped[str] = mapped_column(String(2))
	component_status: Mapped[str] = mapped_column(String(30))
	component_status_date: Mapped[str] = mapped_column(String(10))
	lat_deg: Mapped[int] = mapped_column(Integer)
	lat_min: Mapped[int] = mapped_column(Integer)
	lat_sec: Mapped[int] = mapped_column(Integer)
	lat_hemis: Mapped[str] = mapped_column(String(1))
	lat_decimal: Mapped[int] = mapped_column(Integer)
	long_deg: Mapped[int] = mapped_column(Integer)
	long_min: Mapped[int] = mapped_column(Integer)
	long_sec: Mapped[int] = mapped_column(Integer)
	long_hemis: Mapped[str] = mapped_column(String(1))
	long_decimal: Mapped[int] = mapped_column(Integer)
	lat_long_source_code: Mapped[str] = mapped_column(String(2), nullable=True)
	site_elevation: Mapped[int] = mapped_column(Integer, nullable=True)
	channel: Mapped[str] = mapped_column(String(4))

class ILS_GS(Base):

	__tablename__ = 'ils_gs'
	__mapper_args__ = {'primary_key': ['site_no', 'site_type_code', 'rwy_end_id']}


	eff_date: Mapped[str] = mapped_column(String(10))
	site_no: Mapped[str] = mapped_column(String(9), primary_key=True)
	site_type_code: Mapped[str] = mapped_column(String(1), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	arpt_id: Mapped[str] = mapped_column(String(4))
	city: Mapped[str] = mapped_column(String(40))
	country_code: Mapped[str] = mapped_column(String(2))
	rwy_end_id: Mapped[str] = mapped_column(String(3), primary_key=True)
	ils_loc_id: Mapped[str] = mapped_column(String(6))
	system_type_code: Mapped[str] = mapped_column(String(2))
	component_status: Mapped[str] = mapped_column(String(30))
	component_status_date: Mapped[str] = mapped_column(String(10))
	lat_deg: Mapped[int] = mapped_column(Integer)
	lat_min: Mapped[int] = mapped_column(Integer)
	lat_sec: Mapped[int] = mapped_column(Integer)
	lat_hemis: Mapped[str] = mapped_column(String(1))
	lat_decimal: Mapped[int] = mapped_column(Integer)
	long_deg: Mapped[int] = mapped_column(Integer)
	long_min: Mapped[int] = mapped_column(Integer)
	long_sec: Mapped[int] = mapped_column(Integer)
	long_hemis: Mapped[str] = mapped_column(String(1))
	long_decimal: Mapped[int] = mapped_column(Integer)
	lat_long_source_code: Mapped[str] = mapped_column(String(2), nullable=True)
	site_elevation: Mapped[int] = mapped_column(Integer, nullable=True)
	g_s_type_code: Mapped[str] = mapped_column(String(2))
	g_s_angle: Mapped[int] = mapped_column(Integer)
	g_s_freq: Mapped[int] = mapped_column(Integer)

class ILS_MKR(Base):

	__tablename__ = 'ils_mkr'
	__mapper_args__ = {'primary_key': ['site_no', 'site_type_code', 'rwy_end_id', 'ils_comp_type_code']}


	eff_date: Mapped[str] = mapped_column(String(10))
	site_no: Mapped[str] = mapped_column(String(9), primary_key=True)
	site_type_code: Mapped[str] = mapped_column(String(1), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	arpt_id: Mapped[str] = mapped_column(String(4))
	city: Mapped[str] = mapped_column(String(40))
	country_code: Mapped[str] = mapped_column(String(2))
	rwy_end_id: Mapped[str] = mapped_column(String(3), primary_key=True)
	ils_loc_id: Mapped[str] = mapped_column(String(6))
	system_type_code: Mapped[str] = mapped_column(String(2))
	ils_comp_type_code: Mapped[str] = mapped_column(String(3), primary_key=True)
	component_status: Mapped[str] = mapped_column(String(30))
	component_status_date: Mapped[str] = mapped_column(String(10))
	lat_deg: Mapped[int] = mapped_column(Integer)
	lat_min: Mapped[int] = mapped_column(Integer)
	lat_sec: Mapped[int] = mapped_column(Integer)
	lat_hemis: Mapped[str] = mapped_column(String(1))
	lat_decimal: Mapped[int] = mapped_column(Integer)
	long_deg: Mapped[int] = mapped_column(Integer)
	long_min: Mapped[int] = mapped_column(Integer)
	long_sec: Mapped[int] = mapped_column(Integer)
	long_hemis: Mapped[str] = mapped_column(String(1))
	long_decimal: Mapped[int] = mapped_column(Integer)
	lat_long_source_code: Mapped[str] = mapped_column(String(2), nullable=True)
	site_elevation: Mapped[int] = mapped_column(Integer, nullable=True)
	mkr_fac_type_code: Mapped[str] = mapped_column(String(2))
	marker_id_beacon: Mapped[str] = mapped_column(String(2), nullable=True)
	compass_locator_name: Mapped[str] = mapped_column(String(30), nullable=True)
	freq: Mapped[int] = mapped_column(Integer, nullable=True)
	nav_id: Mapped[str] = mapped_column(String(6), nullable=True)
	nav_type: Mapped[str] = mapped_column(String(25), nullable=True)
	low_powered_ndb_status: Mapped[str] = mapped_column(String(30), nullable=True)

class ILS_RMK(Base):

	__tablename__ = 'ils_rmk'
	__mapper_args__ = {'primary_key': ['site_no', 'site_type_code', 'rwy_end_id', 'ils_comp_type_code', 'tab_name', 'ref_col_name', 'ref_col_seq_no']}


	eff_date: Mapped[str] = mapped_column(String(10))
	site_no: Mapped[str] = mapped_column(String(9), primary_key=True)
	site_type_code: Mapped[str] = mapped_column(String(1), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	arpt_id: Mapped[str] = mapped_column(String(4))
	city: Mapped[str] = mapped_column(String(40))
	country_code: Mapped[str] = mapped_column(String(2))
	rwy_end_id: Mapped[str] = mapped_column(String(3), primary_key=True)
	ils_loc_id: Mapped[str] = mapped_column(String(6))
	system_type_code: Mapped[str] = mapped_column(String(2))
	tab_name: Mapped[str] = mapped_column(String(30), primary_key=True)
	ils_comp_type_code: Mapped[str] = mapped_column(String(3), nullable=True, primary_key=True)
	ref_col_name: Mapped[str] = mapped_column(String(30), primary_key=True)
	ref_col_seq_no: Mapped[int] = mapped_column(Integer, primary_key=True)
	remark: Mapped[str] = mapped_column(String(300))

class LID(Base):

	__tablename__ = 'lid'
	__mapper_args__ = {'primary_key': ['loc_id', 'city', 'fac_type']}


	eff_date: Mapped[str] = mapped_column(String(10))
	country_code: Mapped[str] = mapped_column(String(2))
	loc_id: Mapped[str] = mapped_column(String(4), primary_key=True)
	region_code: Mapped[str] = mapped_column(String(3), nullable=True)
	state: Mapped[str] = mapped_column(String(30), nullable=True)
	city: Mapped[str] = mapped_column(String(40), primary_key=True)
	lid_group: Mapped[str] = mapped_column(String(30))
	fac_type: Mapped[str] = mapped_column(String(30), primary_key=True)
	fac_name: Mapped[str] = mapped_column(String(75), nullable=True)
	resp_artcc_id: Mapped[str] = mapped_column(String(4), nullable=True)
	artcc_computer_id: Mapped[str] = mapped_column(String(3), nullable=True)
	fss_id: Mapped[str] = mapped_column(String(4), nullable=True)

class MAA_BASE(Base):

	__tablename__ = 'maa_base'
	__mapper_args__ = {'primary_key': ['maa_id']}


	eff_date: Mapped[str] = mapped_column(String(10))
	maa_id: Mapped[str] = mapped_column(String(6), primary_key=True)
	maa_type_name: Mapped[str] = mapped_column(String(20))
	nav_id: Mapped[str] = mapped_column(String(4), nullable=True)
	nav_type: Mapped[str] = mapped_column(String(25), nullable=True)
	nav_radial: Mapped[int] = mapped_column(Integer, nullable=True)
	nav_distance: Mapped[int] = mapped_column(Integer, nullable=True)
	state_code: Mapped[str] = mapped_column(String(2))
	city: Mapped[str] = mapped_column(String(30), nullable=True)
	latitude: Mapped[str] = mapped_column(String(14), nullable=True)
	longitude: Mapped[str] = mapped_column(String(15), nullable=True)
	arpt_ids: Mapped[str] = mapped_column(String(50), nullable=True)
	nearest_arpt: Mapped[str] = mapped_column(String(4), nullable=True)
	nearest_arpt_dist: Mapped[int] = mapped_column(Integer, nullable=True)
	nearest_arpt_dir: Mapped[str] = mapped_column(String(2), nullable=True)
	maa_name: Mapped[str] = mapped_column(String(120), nullable=True)
	max_alt: Mapped[str] = mapped_column(String(8), nullable=True)
	min_alt: Mapped[str] = mapped_column(String(8), nullable=True)
	maa_radius: Mapped[int] = mapped_column(Integer, nullable=True)
	description: Mapped[str] = mapped_column(String(450), nullable=True)
	maa_use: Mapped[str] = mapped_column(String(8), nullable=True)
	check_notams: Mapped[str] = mapped_column(String(50), nullable=True)
	time_of_use: Mapped[str] = mapped_column(String(300), nullable=True)
	user_group_name: Mapped[str] = mapped_column(String(300), nullable=True)

class MAA_CON(Base):

	__tablename__ = 'maa_con'
	__mapper_args__ = {'primary_key': ['maa_id', 'freq_seq']}


	eff_date: Mapped[str] = mapped_column(String(10))
	maa_id: Mapped[str] = mapped_column(String(6), primary_key=True)
	freq_seq: Mapped[int] = mapped_column(Integer, primary_key=True)
	fac_id: Mapped[str] = mapped_column(String(4), nullable=True)
	fac_name: Mapped[str] = mapped_column(String(30))
	commercial_freq: Mapped[int] = mapped_column(Integer)
	commercial_chart_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	mil_freq: Mapped[int] = mapped_column(Integer, nullable=True)
	mil_chart_flag: Mapped[str] = mapped_column(String(1), nullable=True)

class MAA_RMK(Base):

	__tablename__ = 'maa_rmk'
	__mapper_args__ = {'primary_key': ['maa_id', 'tab_name', 'ref_col_name', 'ref_col_seq_no']}


	eff_date: Mapped[str] = mapped_column(String(10))
	maa_id: Mapped[str] = mapped_column(String(6), primary_key=True)
	tab_name: Mapped[str] = mapped_column(String(30), primary_key=True)
	ref_col_name: Mapped[str] = mapped_column(String(30), primary_key=True)
	ref_col_seq_no: Mapped[int] = mapped_column(Integer, primary_key=True)
	remark: Mapped[str] = mapped_column(String(300))

class MAA_SHP(Base):

	__tablename__ = 'maa_shp'
	__mapper_args__ = {'primary_key': ['maa_id', 'point_seq']}


	eff_date: Mapped[str] = mapped_column(String(10))
	maa_id: Mapped[str] = mapped_column(String(6), primary_key=True)
	point_seq: Mapped[int] = mapped_column(Integer, primary_key=True)
	latitude: Mapped[str] = mapped_column(String(14))
	longitude: Mapped[str] = mapped_column(String(15))

class MIL_OPS(Base):

	__tablename__ = 'mil_ops'
	__mapper_args__ = {'primary_key': ['site_no', 'site_type_code']}


	eff_date: Mapped[str] = mapped_column(String(10))
	site_no: Mapped[str] = mapped_column(String(9), primary_key=True)
	site_type_code: Mapped[str] = mapped_column(String(1), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	arpt_id: Mapped[str] = mapped_column(String(4))
	city: Mapped[str] = mapped_column(String(40))
	country_code: Mapped[str] = mapped_column(String(2))
	mil_ops_oper_code: Mapped[str] = mapped_column(String(1), nullable=True)
	mil_ops_call: Mapped[str] = mapped_column(String(26), nullable=True)
	mil_ops_hrs: Mapped[str] = mapped_column(String(200), nullable=True)
	amcp_hrs: Mapped[str] = mapped_column(String(200), nullable=True)
	pmsv_hrs: Mapped[str] = mapped_column(String(200), nullable=True)
	remark: Mapped[str] = mapped_column(String(1500), nullable=True)

class MTR_BASE(Base):

	__tablename__ = 'mtr_base'
	__mapper_args__ = {'primary_key': ['route_type_code', 'route_id']}


	eff_date: Mapped[str] = mapped_column(String(10))
	route_type_code: Mapped[str] = mapped_column(String(2), primary_key=True)
	route_id: Mapped[str] = mapped_column(String(5), primary_key=True)
	artcc: Mapped[str] = mapped_column(String(80), nullable=True)
	fss: Mapped[str] = mapped_column(String(160), nullable=True)
	time_of_use: Mapped[str] = mapped_column(String(175), nullable=True)

class MTR_AGY(Base):

	__tablename__ = 'mtr_agy'
	__mapper_args__ = {'primary_key': ['route_type_code', 'route_id', 'agency_type']}


	eff_date: Mapped[str] = mapped_column(String(10))
	route_type_code: Mapped[str] = mapped_column(String(2), primary_key=True)
	route_id: Mapped[str] = mapped_column(String(5), primary_key=True)
	artcc: Mapped[str] = mapped_column(String(80), nullable=True)
	agency_type: Mapped[str] = mapped_column(String(2), primary_key=True)
	agency_name: Mapped[str] = mapped_column(String(30))
	station: Mapped[str] = mapped_column(String(30), nullable=True)
	address: Mapped[str] = mapped_column(String(35), nullable=True)
	city: Mapped[str] = mapped_column(String(30), nullable=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	zip_code: Mapped[str] = mapped_column(String(10), nullable=True)
	commercial_no: Mapped[str] = mapped_column(String(40), nullable=True)
	dsn_no: Mapped[str] = mapped_column(String(40), nullable=True)
	hours: Mapped[str] = mapped_column(String(175), nullable=True)

class MTR_PT(Base):

	__tablename__ = 'mtr_pt'
	__mapper_args__ = {'primary_key': ['route_type_code', 'route_id', 'route_pt_id']}


	eff_date: Mapped[str] = mapped_column(String(10))
	route_type_code: Mapped[str] = mapped_column(String(2), primary_key=True)
	route_id: Mapped[str] = mapped_column(String(5), primary_key=True)
	artcc: Mapped[str] = mapped_column(String(80), nullable=True)
	route_pt_seq: Mapped[int] = mapped_column(Integer)
	next_route_pt_id: Mapped[str] = mapped_column(String(4), nullable=True)
	segment_text: Mapped[str] = mapped_column(String(228), nullable=True)
	lat_deg: Mapped[int] = mapped_column(Integer)
	lat_min: Mapped[int] = mapped_column(Integer)
	lat_sec: Mapped[int] = mapped_column(Integer)
	lat_hemis: Mapped[str] = mapped_column(String(1))
	lat_decimal: Mapped[int] = mapped_column(Integer)
	long_deg: Mapped[int] = mapped_column(Integer)
	long_min: Mapped[int] = mapped_column(Integer)
	long_sec: Mapped[int] = mapped_column(Integer)
	long_hemis: Mapped[str] = mapped_column(String(1))
	long_decimal: Mapped[int] = mapped_column(Integer)
	nav_id: Mapped[str] = mapped_column(String(4), nullable=True)
	navaid_bearing: Mapped[int] = mapped_column(Integer, nullable=True)
	navaid_dist: Mapped[int] = mapped_column(Integer, nullable=True)
	route_pt_id: Mapped[str] = mapped_column(String(4), nullable=True, primary_key=True)

class MTR_SOP(Base):

	__tablename__ = 'mtr_sop'
	__mapper_args__ = {'primary_key': ['route_type_code', 'route_id', 'sop_seq_no']}


	eff_date: Mapped[str] = mapped_column(String(10))
	route_type_code: Mapped[str] = mapped_column(String(2), primary_key=True)
	route_id: Mapped[str] = mapped_column(String(5), primary_key=True)
	artcc: Mapped[str] = mapped_column(String(80), nullable=True)
	sop_seq_no: Mapped[int] = mapped_column(Integer, primary_key=True)
	sop_text: Mapped[str] = mapped_column(String(100))

class MTR_TERR(Base):

	__tablename__ = 'mtr_terr'
	__mapper_args__ = {'primary_key': ['route_type_code', 'route_id', 'terrain_seq_no']}


	eff_date: Mapped[str] = mapped_column(String(10))
	route_type_code: Mapped[str] = mapped_column(String(2), primary_key=True)
	route_id: Mapped[str] = mapped_column(String(5), primary_key=True)
	artcc: Mapped[str] = mapped_column(String(80), nullable=True)
	terrain_seq_no: Mapped[int] = mapped_column(Integer, primary_key=True)
	terrain_text: Mapped[str] = mapped_column(String(100))

class MTR_WDTH(Base):

	__tablename__ = 'mtr_wdth'
	__mapper_args__ = {'primary_key': ['route_type_code', 'route_id', 'width_seq_no']}


	eff_date: Mapped[str] = mapped_column(String(10))
	route_type_code: Mapped[str] = mapped_column(String(2), primary_key=True)
	route_id: Mapped[str] = mapped_column(String(5), primary_key=True)
	artcc: Mapped[str] = mapped_column(String(80), nullable=True)
	width_seq_no: Mapped[int] = mapped_column(Integer, primary_key=True)
	width_text: Mapped[str] = mapped_column(String(100))

class NAV_BASE(Base):

	__tablename__ = 'nav_base'
	__mapper_args__ = {'primary_key': ['nav_id', 'nav_type', 'city', 'country_code']}


	eff_date: Mapped[str] = mapped_column(String(10))
	nav_id: Mapped[str] = mapped_column(String(4), primary_key=True)
	nav_type: Mapped[str] = mapped_column(String(25), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	city: Mapped[str] = mapped_column(String(40), primary_key=True)
	country_code: Mapped[str] = mapped_column(String(2), primary_key=True)
	nav_status: Mapped[str] = mapped_column(String(30))
	name: Mapped[str] = mapped_column(String(30))
	state_name: Mapped[str] = mapped_column(String(30), nullable=True)
	region_code: Mapped[str] = mapped_column(String(3), nullable=True)
	country_name: Mapped[str] = mapped_column(String(30))
	fan_marker: Mapped[str] = mapped_column(String(30), nullable=True)
	owner: Mapped[str] = mapped_column(String(50), nullable=True)
	operator: Mapped[str] = mapped_column(String(50), nullable=True)
	nas_use_flag: Mapped[str] = mapped_column(String(1))
	public_use_flag: Mapped[str] = mapped_column(String(1))
	ndb_class_code: Mapped[str] = mapped_column(String(11), nullable=True)
	oper_hours: Mapped[str] = mapped_column(String(11), nullable=True)
	high_alt_artcc_id: Mapped[str] = mapped_column(String(4), nullable=True)
	high_artcc_name: Mapped[str] = mapped_column(String(30), nullable=True)
	low_alt_artcc_id: Mapped[str] = mapped_column(String(4), nullable=True)
	low_artcc_name: Mapped[str] = mapped_column(String(30), nullable=True)
	lat_deg: Mapped[int] = mapped_column(Integer)
	lat_min: Mapped[int] = mapped_column(Integer)
	lat_sec: Mapped[int] = mapped_column(Integer)
	lat_hemis: Mapped[str] = mapped_column(String(1))
	lat_decimal: Mapped[int] = mapped_column(Integer)
	long_deg: Mapped[int] = mapped_column(Integer)
	long_min: Mapped[int] = mapped_column(Integer)
	long_sec: Mapped[int] = mapped_column(Integer)
	long_hemis: Mapped[str] = mapped_column(String(1))
	long_decimal: Mapped[int] = mapped_column(Integer)
	survey_accuracy_code: Mapped[str] = mapped_column(String(1), nullable=True)
	tacan_dme_status: Mapped[str] = mapped_column(String(30), nullable=True)
	tacan_dme_lat_deg: Mapped[int] = mapped_column(Integer, nullable=True)
	tacan_dme_lat_min: Mapped[int] = mapped_column(Integer, nullable=True)
	tacan_dme_lat_sec: Mapped[int] = mapped_column(Integer, nullable=True)
	tacan_dme_lat_hemis: Mapped[str] = mapped_column(String(1), nullable=True)
	tacan_dme_lat_decimal: Mapped[int] = mapped_column(Integer, nullable=True)
	tacan_dme_long_deg: Mapped[int] = mapped_column(Integer, nullable=True)
	tacan_dme_long_min: Mapped[int] = mapped_column(Integer, nullable=True)
	tacan_dme_long_sec: Mapped[int] = mapped_column(Integer, nullable=True)
	tacan_dme_long_hemis: Mapped[str] = mapped_column(String(1), nullable=True)
	tacan_dme_long_decimal: Mapped[int] = mapped_column(Integer, nullable=True)
	elev: Mapped[int] = mapped_column(Integer, nullable=True)
	mag_varn: Mapped[int] = mapped_column(Integer, nullable=True)
	mag_varn_hemis: Mapped[str] = mapped_column(String(1), nullable=True)
	mag_varn_year: Mapped[int] = mapped_column(Integer, nullable=True)
	simul_voice_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	pwr_output: Mapped[int] = mapped_column(Integer, nullable=True)
	auto_voice_id_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	mnt_cat_code: Mapped[str] = mapped_column(String(1), nullable=True)
	voice_call: Mapped[str] = mapped_column(String(60), nullable=True)
	chan: Mapped[str] = mapped_column(String(4), nullable=True)
	freq: Mapped[int] = mapped_column(Integer, nullable=True)
	mkr_ident: Mapped[str] = mapped_column(String(30), nullable=True)
	mkr_shape: Mapped[str] = mapped_column(String(1), nullable=True)
	mkr_brg: Mapped[int] = mapped_column(Integer, nullable=True)
	alt_code: Mapped[str] = mapped_column(String(2), nullable=True)
	dme_ssv: Mapped[str] = mapped_column(String(2), nullable=True)
	low_nav_on_high_chart_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	z_mkr_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	fss_id: Mapped[str] = mapped_column(String(4), nullable=True)
	fss_name: Mapped[str] = mapped_column(String(30), nullable=True)
	fss_hours: Mapped[str] = mapped_column(String(65), nullable=True)
	notam_id: Mapped[str] = mapped_column(String(4), nullable=True)
	quad_ident: Mapped[str] = mapped_column(String(20), nullable=True)
	pitch_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	catch_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	sua_atcaa_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	restriction_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	hiwas_flag: Mapped[str] = mapped_column(String(1), nullable=True)

class NAV_CKPT(Base):

	__tablename__ = 'nav_ckpt'
	__mapper_args__ = {'primary_key': ['nav_id', 'nav_type', 'city', 'country_code', 'brg', 'air_gnd_code']}


	eff_date: Mapped[str] = mapped_column(String(10))
	nav_id: Mapped[str] = mapped_column(String(4), primary_key=True)
	nav_type: Mapped[str] = mapped_column(String(25), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	city: Mapped[str] = mapped_column(String(40), primary_key=True)
	country_code: Mapped[str] = mapped_column(String(2), primary_key=True)
	altitude: Mapped[int] = mapped_column(Integer, nullable=True)
	brg: Mapped[int] = mapped_column(Integer, primary_key=True)
	air_gnd_code: Mapped[str] = mapped_column(String(2), primary_key=True)
	chk_desc: Mapped[str] = mapped_column(String(75))
	arpt_id: Mapped[str] = mapped_column(String(4), nullable=True)
	state_chk_code: Mapped[str] = mapped_column(String(2))

class NAV_RMK(Base):

	__tablename__ = 'nav_rmk'
	__mapper_args__ = {'primary_key': ['nav_id', 'nav_type', 'ref_col_seq_no', 'city', 'country_code', 'tab_name', 'ref_col_name']}


	eff_date: Mapped[str] = mapped_column(String(10))
	nav_id: Mapped[str] = mapped_column(String(4), primary_key=True)
	nav_type: Mapped[str] = mapped_column(String(25), primary_key=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	city: Mapped[str] = mapped_column(String(40), primary_key=True)
	country_code: Mapped[str] = mapped_column(String(2), primary_key=True)
	tab_name: Mapped[str] = mapped_column(String(30), primary_key=True)
	ref_col_name: Mapped[str] = mapped_column(String(30), primary_key=True)
	ref_col_seq_no: Mapped[int] = mapped_column(Integer, primary_key=True)
	remark: Mapped[str] = mapped_column(String(600))

class PFR_BASE(Base):

	__tablename__ = 'pfr_base'
	__mapper_args__ = {'primary_key': ['origin_id', 'dstn_id', 'pfr_type_code', 'route_no']}


	eff_date: Mapped[str] = mapped_column(String(10))
	origin_id: Mapped[str] = mapped_column(String(5), primary_key=True)
	origin_city: Mapped[str] = mapped_column(String(40), nullable=True)
	origin_state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	origin_country_code: Mapped[str] = mapped_column(String(2))
	dstn_id: Mapped[str] = mapped_column(String(5), primary_key=True)
	dstn_city: Mapped[str] = mapped_column(String(40), nullable=True)
	dstn_state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	dstn_country_code: Mapped[str] = mapped_column(String(2))
	pfr_type_code: Mapped[str] = mapped_column(String(3), primary_key=True)
	route_no: Mapped[int] = mapped_column(Integer, primary_key=True)
	special_area_descrip: Mapped[str] = mapped_column(String(75), nullable=True)
	alt_descrip: Mapped[str] = mapped_column(String(40), nullable=True)
	aircraft: Mapped[str] = mapped_column(String(50), nullable=True)
	hours: Mapped[str] = mapped_column(String(15), nullable=True)
	route_dir_descrip: Mapped[str] = mapped_column(String(20), nullable=True)
	designator: Mapped[str] = mapped_column(String(5), nullable=True)
	nar_type: Mapped[str] = mapped_column(String(20), nullable=True)
	inland_fac_fix: Mapped[str] = mapped_column(String(5), nullable=True)
	coastal_fix: Mapped[str] = mapped_column(String(5), nullable=True)
	destination: Mapped[str] = mapped_column(String(40), nullable=True)
	route_string: Mapped[str] = mapped_column(String(300), nullable=True)

class PFR_SEG(Base):

	__tablename__ = 'pfr_seg'
	__mapper_args__ = {'primary_key': ['origin_id', 'dstn_id', 'pfr_type_code', 'route_no', 'seg_value', 'next_seg']}


	eff_date: Mapped[str] = mapped_column(String(10))
	origin_id: Mapped[str] = mapped_column(String(5), primary_key=True)
	dstn_id: Mapped[str] = mapped_column(String(5), primary_key=True)
	pfr_type_code: Mapped[str] = mapped_column(String(3), primary_key=True)
	route_no: Mapped[int] = mapped_column(Integer, primary_key=True)
	segment_seq: Mapped[int] = mapped_column(Integer)
	seg_value: Mapped[str] = mapped_column(String(30), primary_key=True)
	seg_type: Mapped[str] = mapped_column(String(6))
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	country_code: Mapped[str] = mapped_column(String(2), nullable=True)
	icao_region_code: Mapped[str] = mapped_column(String(2), nullable=True)
	nav_type: Mapped[str] = mapped_column(String(25), nullable=True)
	next_seg: Mapped[str] = mapped_column(String(30), nullable=True, primary_key=True)

class PFR_RMT_FMT(Base):

	__tablename__ = 'pfr_rmt_fmt'
	__mapper_args__ = {'primary_key': ['orig', 'dest', 'type', 'seq']}


	orig: Mapped[str] = mapped_column(String(5), primary_key=True)
	route_string: Mapped[str] = mapped_column(String(300), nullable=True)
	dest: Mapped[str] = mapped_column(String(5), primary_key=True)
	hours1: Mapped[str] = mapped_column(String(15), nullable=True)
	type: Mapped[str] = mapped_column(String(3), primary_key=True)
	area: Mapped[str] = mapped_column(String(75), nullable=True)
	altitude: Mapped[str] = mapped_column(String(40), nullable=True)
	aircraft: Mapped[str] = mapped_column(String(50), nullable=True)
	direction: Mapped[str] = mapped_column(String(20), nullable=True)
	seq: Mapped[int] = mapped_column(Integer, primary_key=True)
	dcntr: Mapped[str] = mapped_column(String(4), nullable=True)
	acntr: Mapped[str] = mapped_column(String(4), nullable=True)

class PJA_BASE(Base):

	__tablename__ = 'pja_base'
	__mapper_args__ = {'primary_key': ['pja_id']}


	eff_date: Mapped[str] = mapped_column(String(10))
	pja_id: Mapped[str] = mapped_column(String(6), primary_key=True)
	nav_id: Mapped[str] = mapped_column(String(4), nullable=True)
	nav_type: Mapped[str] = mapped_column(String(25), nullable=True)
	radial: Mapped[int] = mapped_column(Integer, nullable=True)
	distance: Mapped[int] = mapped_column(Integer, nullable=True)
	navaid_name: Mapped[str] = mapped_column(String(30), nullable=True)
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	city: Mapped[str] = mapped_column(String(30), nullable=True)
	latitude: Mapped[str] = mapped_column(String(14))
	lat_decimal: Mapped[int] = mapped_column(Integer)
	longitude: Mapped[str] = mapped_column(String(15))
	long_decimal: Mapped[int] = mapped_column(Integer)
	arpt_id: Mapped[str] = mapped_column(String(4), nullable=True)
	site_no: Mapped[str] = mapped_column(String(9), nullable=True)
	site_type_code: Mapped[str] = mapped_column(String(1), nullable=True)
	drop_zone_name: Mapped[str] = mapped_column(String(50), nullable=True)
	max_altitude: Mapped[int] = mapped_column(Integer, nullable=True)
	max_altitude_type_code: Mapped[str] = mapped_column(String(3), nullable=True)
	pja_radius: Mapped[int] = mapped_column(Integer, nullable=True)
	chart_request_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	publish_criteria: Mapped[str] = mapped_column(String(1), nullable=True)
	description: Mapped[str] = mapped_column(String(100), nullable=True)
	time_of_use: Mapped[str] = mapped_column(String(150), nullable=True)
	fss_id: Mapped[str] = mapped_column(String(4), nullable=True)
	fss_name: Mapped[str] = mapped_column(String(30), nullable=True)
	pja_use: Mapped[str] = mapped_column(String(8), nullable=True)
	volume: Mapped[str] = mapped_column(String(1), nullable=True)
	pja_user: Mapped[str] = mapped_column(String(150), nullable=True)
	remark: Mapped[str] = mapped_column(String(600), nullable=True)

class PJA_CON(Base):

	__tablename__ = 'pja_con'
	__mapper_args__ = {'primary_key': ['pja_id', 'fac_name']}


	eff_date: Mapped[str] = mapped_column(String(10))
	pja_id: Mapped[str] = mapped_column(String(6), primary_key=True)
	fac_id: Mapped[str] = mapped_column(String(4), nullable=True)
	fac_name: Mapped[str] = mapped_column(String(50), primary_key=True)
	loc_id: Mapped[str] = mapped_column(String(4))
	commercial_freq: Mapped[int] = mapped_column(Integer)
	commercial_chart_flag: Mapped[str] = mapped_column(String(1))
	mil_freq: Mapped[int] = mapped_column(Integer, nullable=True)
	mil_chart_flag: Mapped[str] = mapped_column(String(1), nullable=True)
	sector: Mapped[str] = mapped_column(String(30), nullable=True)
	contact_freq_altitude: Mapped[str] = mapped_column(String(20), nullable=True)

class RDR(Base):

	__tablename__ = 'rdr'
	__mapper_args__ = {'primary_key': ['facility_id', 'country_code', 'radar_no']}


	eff_date: Mapped[str] = mapped_column(String(10))
	facility_id: Mapped[str] = mapped_column(String(4), primary_key=True)
	facility_type: Mapped[str] = mapped_column(String(7))
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	country_code: Mapped[str] = mapped_column(String(2), primary_key=True)
	radar_type: Mapped[str] = mapped_column(String(10))
	radar_no: Mapped[int] = mapped_column(Integer, primary_key=True)
	radar_hrs: Mapped[str] = mapped_column(String(200))
	remark: Mapped[str] = mapped_column(String(1500), nullable=True)

class STAR_BASE(Base):

	__tablename__ = 'star_base'
	__mapper_args__ = {'primary_key': ['star_computer_code']}


	eff_date: Mapped[str] = mapped_column(String(10))
	arrival_name: Mapped[str] = mapped_column(String(30))
	amendment_no: Mapped[str] = mapped_column(String(5))
	artcc: Mapped[str] = mapped_column(String(12), nullable=True)
	star_amend_eff_date: Mapped[str] = mapped_column(String(10))
	rnav_flag: Mapped[str] = mapped_column(String(1))
	star_computer_code: Mapped[str] = mapped_column(String(12), primary_key=True)
	served_arpt: Mapped[str] = mapped_column(String(200))

class STAR_APT(Base):

	__tablename__ = 'star_apt'
	__mapper_args__ = {'primary_key': ['star_computer_code', 'body_name', 'body_seq', 'arpt_id', 'rwy_end_id']}


	eff_date: Mapped[str] = mapped_column(String(10))
	star_computer_code: Mapped[str] = mapped_column(String(12), primary_key=True)
	artcc: Mapped[str] = mapped_column(String(12), nullable=True)
	body_name: Mapped[str] = mapped_column(String(110), primary_key=True)
	body_seq: Mapped[int] = mapped_column(Integer, primary_key=True)
	arpt_id: Mapped[str] = mapped_column(String(4), primary_key=True)
	rwy_end_id: Mapped[str] = mapped_column(String(3), nullable=True, primary_key=True)

class STAR_RTE(Base):

	__tablename__ = 'star_rte'
	__mapper_args__ = {'primary_key': ['star_computer_code', 'route_portion_type', 'route_name', 'body_seq', 'point_seq']}


	eff_date: Mapped[str] = mapped_column(String(10))
	star_computer_code: Mapped[str] = mapped_column(String(12), primary_key=True)
	artcc: Mapped[str] = mapped_column(String(12), nullable=True)
	route_portion_type: Mapped[str] = mapped_column(String(10), primary_key=True)
	route_name: Mapped[str] = mapped_column(String(110), primary_key=True)
	body_seq: Mapped[int] = mapped_column(Integer, primary_key=True)
	transition_computer_code: Mapped[str] = mapped_column(String(20), nullable=True)
	point_seq: Mapped[int] = mapped_column(Integer, primary_key=True)
	point: Mapped[str] = mapped_column(String(10))
	icao_region_code: Mapped[str] = mapped_column(String(2), nullable=True)
	point_type: Mapped[str] = mapped_column(String(25))
	next_point: Mapped[str] = mapped_column(String(10), nullable=True)
	arpt_rwy_assoc: Mapped[str] = mapped_column(String(200), nullable=True)

class WXL_BASE(Base):

	__tablename__ = 'wxl_base'
	__mapper_args__ = {'primary_key': ['wea_id', 'country_code']}


	eff_date: Mapped[str] = mapped_column(String(10))
	wea_id: Mapped[str] = mapped_column(String(4), primary_key=True)
	city: Mapped[str] = mapped_column(String(40))
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	country_code: Mapped[str] = mapped_column(String(2), primary_key=True)
	lat_deg: Mapped[int] = mapped_column(Integer)
	lat_min: Mapped[int] = mapped_column(Integer)
	lat_sec: Mapped[int] = mapped_column(Integer)
	lat_hemis: Mapped[str] = mapped_column(String(1))
	lat_decimal: Mapped[int] = mapped_column(Integer)
	long_deg: Mapped[int] = mapped_column(Integer)
	long_min: Mapped[int] = mapped_column(Integer)
	long_sec: Mapped[int] = mapped_column(Integer)
	long_hemis: Mapped[str] = mapped_column(String(1))
	long_decimal: Mapped[int] = mapped_column(Integer)
	elev: Mapped[int] = mapped_column(Integer)
	survey_method_code: Mapped[str] = mapped_column(String(1))

class WXL_SVC(Base):

	__tablename__ = 'wxl_svc'
	__mapper_args__ = {'primary_key': ['wea_id', 'country_code', 'wea_svc_type_code']}


	eff_date: Mapped[str] = mapped_column(String(10))
	wea_id: Mapped[str] = mapped_column(String(4), primary_key=True)
	city: Mapped[str] = mapped_column(String(40))
	state_code: Mapped[str] = mapped_column(String(2), nullable=True)
	country_code: Mapped[str] = mapped_column(String(2), primary_key=True)
	wea_svc_type_code: Mapped[str] = mapped_column(String(5), primary_key=True)
	wea_affect_area: Mapped[str] = mapped_column(String(200), nullable=True)

