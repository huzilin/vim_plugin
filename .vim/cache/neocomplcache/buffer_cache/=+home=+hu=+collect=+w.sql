['DELIMITER', 'CREATE', 'DEFINER', 'root', 'localhost', 'PROCEDURE', 'WJK_LEFT_P_remain_ticket', 'oi_train_days_in', 'TINYINT', 'UNSIGNED', 'os_purposes_in', 'VARCHAR', 'assign_station_in', 'flag_in', 'plan_train_no_in', 'CHAR', 'plan_train_date_in', 'out_flag', 'INOUT', 'SWP_Ret_Value', 'SWL_return', 'BEGIN', 'DECLARE', 'share_flag', 'range2', 'Version', 'To_Range', 'transform_no', 'tmp_range', 'tmp_start_coach_no', 'tmp_end_coach_no', 'transform_bureau_code', 'transform_subbureau_code', 'sale_bureau', 'sale_subbureau', 'old_sale_station', 'transform_station_telecode', 'old_range', 'transform_date', 'original_station_telecode', 'share_string', '1300', 'ni_day', 'error', 'rowcount', 'ns_train_no', 'ns_station_train_code', 'ns_station_no', 'ns_train_date', 'ns_train_code', 'ns_limit_station_no', 'ns_limit_station_name', 'ns_start_station_name', 'ns_end_station_name', 'ns_direction_code', 'ns_direction_name', 'ns_arrive_time', 'ns_start_time', 'ns_station_telecode', 'yz_types', 'yw_types', 'rz_types', 'rw_types', 'wz_types', 'pTypes', 'yz_yn', 'yw_yn', 'rz_yn', 'rw_yn', 'wz_yn', 'yz_count', 'SMALLINT', 'yw_count', 'rz_count', 'rw_count', 'wz_count', 'c_date1', 'c_date2', 'c_date', 'c_current_date', 'c_today', 'c_train_no', 'c_station_name', 'c1_station_name', 'c_tmp_date', 'tmp_no', 'single_assign_station', 'c_count', 'tmp_train_code', 'temp_date', 'assign_station_name', 'my_center_code', 'my_bureau_code', 'ns_location_code', 'seat_type_count', 'seat_name', 'seat_type_belong', 'seat_type', 'seat_types', 'ret_code', 'nc_operate_time', 'DATETIME', 'nc_start_date', 'nc_stop_date', 'nc_train_no', 'nc_station_no', 'nc_station_telecode', 'nc_station_name', 'nc_board_train_code', 'nc_command_code', 'nc_day_difference', 'nc_arrive_time', 'nc_start_time', 'nc_time_interval', 'nc_running_style', 'nc_running_rule', 'tmp_limit_station_no', 'sta_in_str', 'sql_str', '1024', 'bureau_code', 'control_day', 'date_range_n_begin', 'date_range_n_end', 'date_range_f_begin', 'date_range_f_end', 'depart_date', 'from_day_diff', 'return_code', 'train_no', 'll_max_station_no', 'll_end_station_telecode', 'end_station_telecode', 'NO_DATA', 'DEFAULT', 'SWV_ns_train_code_Str', 'seat_type_string', 'declare', 'return_out', 'read_seattypes', 'CURSOR', 'SELECT', 'wjk_tt_tmp_seat_type_tmp', 'seat_type_code', 'FROM', 'WHERE', 'LOCATE', 'belong_seat_type_code', 'cur_notice', 'wjk_tt_tmp_center_notice', 'operate_time', 'start_date', 'stop_date', 'station_no', 'station_telecode', 'station_name', 'board_train_code', 'command_code', 'day_difference', 'arrive_time', 'start_time', 'time_interval', 'running_style', 'running_rule', 'where', 'order', 'cur_train', 'wjk_tt_tmp_stop_time', 'tmp_train_no', 'tmp_start_station_name', 'tmp_end_station_name', 'cur_dele', 'wjk_tt_tmp', 'train_code', 'CONTINUE', 'HANDLER', 'FOUND', 'null', 'then', 'Ver20101109', 'select', 'station_dictionary', 'INTO', 'from', 'basic', 'SUBSTRING', 'DJ50_train_sale_define', 'DATE_FORMAT', 'CURRENT_TIMESTAMP', 'inner_code', 'ticket_type', 'purpose_code', 'flag1', 'THEN', 'here', 'TIMESTAMPADD', '20991231', 'TEMPORARY', 'TABLE', 'EXISTS', 'wjk_tt_train_info', 'train_date', 'NULL', 'from_station', 'to_station', 'truncate', 'table', 'wjk_tt_tmp_left_base_center', 'assign_station', 'far_from_station_no', 'limit_station', 'coach_no', 'ticket_quantity', 'up_quantity', 'mid_quantity', 'down_quantity', 'ticket_source', 'range', 'wseat_type_code', 'seat_feature', 'INDEX', 'tmp_left_base_center_idx', 'tt_WJK_LEFT_remain_ticket', 'start_station_name', 'end_station_name', 'limit_station_no', 'limit_station_name', 'direction_name', 'ltrim', 'rtrim', 'DG30_my_center', 'center', 'seat_type_name', 'belong_seat_type_name', 'print_seat_type_name', 'display_seat_type_name', 'update', '×ù', 'Èí×ù', 'SWV_Error', 'OPEN', 'LEAVE', 'FETCH', 'WHILE', '30101', 'loop', 'cursor', 'CONCAT', 'CLOSE', '30102', '30103', '30104', 'tmp_station_no', 'tmp_start_date', 'tmp_stop_date', 'tmp_arrive_time', 'tmp_start_time', 'tmp_station_telecode', 'tmp_station_train_code', 'tmp_day_difference', 'tmp_count', 'unique', 'index', 'tt_tmp_stop_time_idx', 'wjk_tt_tmp_stoptime', 'tt_tmp_stop_time_idx1', 'CJ30_center_notice', 'left', 'right', 'insert', 'into', 'command_enable', 'LENGTH', 'distinct', 'stop_time', 'station_train_code', 'REGEXP', 'cast', 'signed', 'train_dir', 'subbureau_code', '00000000', 'double_id', 'schema_id', '22_1', 'limit', 'else', '22_2', 'open', 'fetch', 'while', '30111', 'exists', 'DG50_train_location_auth', 'start_station_telecode', 'on_net_station', 'area_center_code', 'close', '21_1', 'between', 'UPDATE', 'CASE', 'WHEN', '000000', '00000', '0000', 'ELSE', 'begin', 'cp_start_time', 'datetime', 'cp_end_time', 'concat', 'call', 'arith', 'DS60_ticket_left', 'CALL', 'finish', 'execute', 'time', 'TIMESTAMPDIFF', 'second', 'LIMIT', 'delete', 'step_two', 'step_one', 'count', 'SWL_Label13', 'ITERATE', 'CAST', 'char', 'CG40_station_group_train', 'direction_code', 'direction', 'CJ30_check_running', '15_4', 'tmp_row_count', 'lpad', '17_1', 'CJ30_train_code', 'oo_single_assign_station', 'varchar', '17_2', '000000000000', 'get_limit', 'values', 'leave', 'group', 'having', 'character_set_client', 'latin1', 'collation_connection', 'latin1_swedish_ci', 'Database', 'Collation']
