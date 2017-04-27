['Copyright', 'Oracle', 'affiliates', 'rights', 'reserved', 'This', 'program', 'free', 'software', 'redistribute', 'modify', 'under', 'terms', 'General', 'Public', 'License', 'published', 'Free', 'Software', 'Foundation', 'version', 'distributed', 'hope', 'that', 'will', 'useful', 'WITHOUT', 'WARRANTY', 'without', 'even', 'implied', 'warranty', 'MERCHANTABILITY', 'FITNESS', 'PARTICULAR', 'PURPOSE', 'more', 'details', 'should', 'have', 'received', 'copy', 'along', 'with', 'this', 'write', 'Franklin', 'Fifth', 'Floor', 'Boston', 'addtogroup', 'Replication', 'file', 'brief', 'Binary', 'event', 'definitions', 'includes', 'generic', 'code', 'common', 'types', 'events', 'well', 'specific', 'each', 'type', '#ifndef', '_log_event_h', '#define', '#include', 'my_bitmap', 'rpl_constants', 'table_id', '#ifdef', 'MYSQL_CLIENT', 'sql_const', 'rpl_utility', 'hash', 'rpl_tblmap', '#endif', 'MYSQL_SERVER', 'rpl_record', 'rpl_reporting', 'sql_class', 'Hash_slave_rows', 'rpl_filter', 'key_copy', 'compare_keys', 'Forward', 'declarations', 'class', 'String', 'typedef', 'ulonglong', 'sql_mode_t', 'struct', 'st_db_worker_hash_entry', 'db_worker_hash_entry', 'PREFIX_SQL_LOAD', 'SQL_LOAD', 'Maximum', 'length', 'name', 'temporary', 'PREFIX', 'LENGTH', 'UUID', 'UUID_LENGTH', 'SEPARATORS', 'SERVER', 'range', 'server', 'FILE', 'uint', 'EXTENSION', 'Assuming', 'extension', 'always', 'less', 'than', 'characters', 'TEMP_FILE_MAX_LEN', 'Either', 'assert', 'return', 'error', 'debug', 'build', 'condition', 'checked', 'builds', 'given', 'returned', 'instead', 'param', 'COND', 'Condition', 'check', 'ERRNO', 'Error', 'number', 'DBUG_OFF', 'ASSERT_OR_RETURN_ERROR', 'while', '#else', 'DBUG_ASSERT', 'LOG_READ_EOF', 'LOG_READ_BOGUS', 'LOG_READ_IO', 'LOG_READ_MEM', 'LOG_READ_TRUNC', 'LOG_READ_TOO_LARGE', 'LOG_READ_CHECKSUM_FAILURE', 'LOG_EVENT_OFFSET', 'MySQL', 'Compared', 'different', 'Start_log_event', 'which', 'info', 'about', 'binary', 'sizes', 'headers', 'included', 'better', 'compatibility', 'master', 'from', 'slave', 'unique', 'triplet', 'server_id', 'timestamp', 'start', 'other', 'sure', 'executed', 'once', 'multimaster', 'setup', 'example', 'query', 'arrive', 'twice', 'need', 'remembers', 'last', 'processed', 'compare', 'know', 'skipped', 'Example', 'already', 'bytes', 'plus', 'timestamp_when_the_master_started', 'counter', 'sequence', 'increments', 'every', 'time', 'binlog', 'handle', 'when', 'overflowed', 'restarts', 'Query', 'Load', 'Create', 'Execute', 'precise', 'microseconds', 'matched', 'affected', 'warnings', 'rows', 'fields', 'session', 'variables', 'SQL_MODE', 'FOREIGN_KEY_CHECKS', 'UNIQUE_CHECKS', 'SQL_AUTO_IS_NULL', 'collations', 'charsets', 'PASSWORD', 'BINLOG_VERSION', 'could', 'used', 'SERVER_VERSION_LENGTH', 'introduces', 'obscure', 'dependency', 'somebody', 'decided', 'change', 'would', 'break', 'replication', 'protocol', 'ST_SERVER_VER_LEN', 'These', 'flags', 'structs', 'LOAD', 'DATA', 'INFILE', 'options', 'LINES', 'TERMINATED', 'DUMPFILE_FLAG', 'probably', 'useless', 'DUMPFILE', 'clause', 'SELECT', 'OPT_ENCLOSED_FLAG', 'REPLACE_FLAG', 'IGNORE_FLAG', 'FIELD_TERM_EMPTY', 'ENCLOSED_EMPTY', 'LINE_TERM_EMPTY', 'LINE_START_EMPTY', 'ESCAPED_EMPTY', 'old_sql_ex', 'char', 'field_term', 'enclosed', 'line_term', 'line_start', 'escaped', 'opt_flags', 'empty_flags', 'NUM_LOAD_DELIM_STRS', 'sql_ex_info', 'Remove', 'warning', 'const', 'cached_new_format', 'uint8', 'field_term_len', 'enclosed_len', 'line_term_len', 'line_start_len', 'escaped_len', 'store', 'format', 'possible', 'void', 'force_new_format', 'data_size', 'new_format', 'bool', 'write_data', 'IO_CACHE', 'init', 'buf_end', 'use_new_format', 'consists', 'Each', 'fixed', 'header', 'possibly', 'followed', 'variable', 'data', 'body', 'optional', 'segment', 'post', ' #defines', 'below', 'specifics', 'really', 'update', 'Query_log_event', 'Execute_load_query_log_event', 'Load_log_event', 'Execute_load_log_event', 'Execute_load_query', 'together', 'Begin_load_query', 'Append_block', 'replicate', 'Create_file', 'Execute_load', 'were', 'before', 'LOG_EVENT_HEADER_LEN', 'OLD_HEADER_LEN', 'Fixed', 'where', 'agree', 'That', 'longer', 'least', 'first', 'same', 'something', 'like', 'LOG_EVENT_MINIMAL_HEADER_LEN', 'remain', 'QUERY_HEADER_MINIMAL_LEN', 'differs', 'vars', 'QUERY_HEADER_LEN', 'STOP_HEADER_LEN', 'LOAD_HEADER_LEN', 'START_V3_HEADER_LEN', 'ROTATE_HEADER_LEN', 'FROZEN', 'Rotate', 'frozen', 'INTVAR_HEADER_LEN', 'CREATE_FILE_HEADER_LEN', 'APPEND_BLOCK_HEADER_LEN', 'EXEC_LOAD_HEADER_LEN', 'DELETE_FILE_HEADER_LEN', 'NEW_LOAD_HEADER_LEN', 'RAND_HEADER_LEN', 'USER_VAR_HEADER_LEN', 'FORMAT_DESCRIPTION_HEADER_LEN', 'LOG_EVENT_TYPES', 'XID_HEADER_LEN', 'BEGIN_LOAD_QUERY_HEADER_LEN', 'ROWS_HEADER_LEN_V1', 'TABLE_MAP_HEADER_LEN', 'EXECUTE_LOAD_QUERY_EXTRA_HEADER_LEN', 'EXECUTE_LOAD_QUERY_HEADER_LEN', 'INCIDENT_HEADER_LEN', 'HEARTBEAT_HEADER_LEN', 'IGNORABLE_HEADER_LEN', 'ROWS_HEADER_LEN_V2', 'maximum', 'updated', 'databases', 'status', 'carry', 'redefined', 'within', 'OVER_MAX_DBS_IN_EVENT_MTS', 'MAX_DBS_IN_EVENT_MTS', 'When', 'actual', 'exceeds', 'value', 'into', 'mts_accessed_dbs', 'extra', 'compared', 'packet', 'sent', 'client', 'First', 'auxiliary', 'log_event', 'estimation', 'MAX_SIZE_LOG_EVENT_STATUS', 'flags2', 'sql_mode', 'catalog', 'auto_increment', 'charset', 'time_zone', 'lc_time_names_number', 'charset_database_number', 'table_map_for_update', 'master_data_written', 'db_1', 'db_2', 'NAME_LEN', 'user_len', 'user', 'host_len', 'host', 'MAX_LOG_EVENT_HEADER', 'order', 'Query_log_event::write', 'write_header', 'write_post_header_for_derived', 'option', 'added', 'large', 'packets', 'increase', 'max_allowed', 'both', 'DUMP', 'thread', 'MAX_MAX_ALLOWED_PACKET', 'Event', 'offsets', 'these', 'point', 'places', 'inside', 'EVENT_TYPE_OFFSET', 'SERVER_ID_OFFSET', 'EVENT_LEN_OFFSET', 'LOG_POS_OFFSET', 'FLAGS_OFFSET', 'ST_BINLOG_VER_OFFSET', 'ST_SERVER_VER_OFFSET', 'ST_CREATED_OFFSET', 'ST_COMMON_HEADER_LEN_OFFSET', 'never', 'written', 'SL_MASTER_PORT_OFFSET', 'SL_MASTER_POS_OFFSET', 'SL_MASTER_HOST_OFFSET', 'Q_THREAD_ID_OFFSET', 'Q_EXEC_TIME_OFFSET', 'Q_DB_LEN_OFFSET', 'Q_ERR_CODE_OFFSET', 'Q_STATUS_VARS_LEN_OFFSET', 'Q_DATA_OFFSET', 'codes', 'values', 'byte', 'Q_FLAGS2_CODE', 'Q_SQL_MODE_CODE', 'Q_CATALOG_CODE', 'zero', 'stored', 'only', 'keep', 'able', 'masters', 'Q_AUTO_INCREMENT', 'Q_CHARSET_CODE', 'Q_TIME_ZONE_CODE', 'Q_CATALOG_NZ_CODE', 'withOUT', 'Saves', 'reason', 'didn', 'simply', 'then', 'crash', 'segfault', 'because', 'expect', 'there', 'none', 'Q_LC_TIME_NAMES_CODE', 'Q_CHARSET_DATABASE_CODE', 'Q_TABLE_MAP_FOR_UPDATE_CODE', 'Q_MASTER_DATA_WRITTEN_CODE', 'Q_INVOKER', 'Q_UPDATED_DB_NAMES', 'collects', 'total', 'their', 'names', 'propagated', 'facilitate', 'parallel', 'applying', 'Q_MICROSECONDS', 'Intvar', 'I_TYPE_OFFSET', 'I_VAL_OFFSET', 'Rand', 'RAND_SEED1_OFFSET', 'RAND_SEED2_OFFSET', 'User_var', 'UV_VAL_LEN_SIZE', 'UV_VAL_IS_NULL', 'UV_VAL_TYPE_SIZE', 'UV_NAME_LEN_SIZE', 'UV_CHARSET_NUMBER_SIZE', 'L_THREAD_ID_OFFSET', 'L_EXEC_TIME_OFFSET', 'L_SKIP_LINES_OFFSET', 'L_TBL_LEN_OFFSET', 'L_DB_LEN_OFFSET', 'L_NUM_FIELDS_OFFSET', 'L_SQL_EX_OFFSET', 'L_DATA_OFFSET', 'R_POS_OFFSET', 'R_IDENT_OFFSET', 'File', 'CF_FILE_ID_OFFSET', 'CF_DATA_OFFSET', 'Append', 'Block', 'AB_FILE_ID_OFFSET', 'AB_DATA_OFFSET', 'EL_FILE_ID_OFFSET', 'Delete', 'DF_FILE_ID_OFFSET', 'Table', 'TM_MAPID_OFFSET', 'TM_FLAGS_OFFSET', 'RoWs', 'RW_MAPID_OFFSET', 'RW_FLAGS_OFFSET', 'RW_VHLEN_OFFSET', 'RW_V_TAG_LEN', 'RW_V_EXTRAINFO_TAG', 'ELQ_FILE_ID_OFFSET', 'ELQ_FN_POS_START_OFFSET', 'ELQ_FN_POS_END_OFFSET', 'ELQ_DUP_HANDLING_OFFSET', 'binlogs', 'begin', 'BINLOG_MAGIC', 'second', 'anything', 'they', 'removed', 'place', 'later', 'reused', 'Then', 'must', 'remember', 'LOG_EVENT_FORCED_ROTATE_F', 'rely', 'replacing', 'flag', 'reading', 'defines', 'here', 'just', 'what', 'TO_BE_REMOVED', 'LOG_EVENT_TIME_F', 'makes', 'sense', 'Format_description_log_event', 'reset', 'closed', 'case', 'modifies', 'part', 'Thus', 'reliable', 'indicator', 'correctly', 'Stop_log_event', 'enough', 'small', 'chance', 'mysqld', 'crashes', 'middle', 'insert', 'look', 'detect', 'restart', 'after', 'provide', 'unbreakable', 'problem', 'storage', 'engines', 'rollback', 'automatically', 'does', 'solve', 'append', 'ROLLBACK', 'virtually', 'itself', 'changed', 'found', 'mysqlbinlog', 'prints', 'abort', 'corruption', 'takes', 'forces', 'Note', 'backward', 'compatible', 'behaviour', 'LOG_EVENT_BINLOG_IN_USE_F', 'LOG_EVENT_THREAD_SPECIFIC_F', 'depends', 'TEMPORARY', 'TABLE', 'Currently', 'print', 'PSEUDO_THREAD_ID', 'hurt', 'slow', 'LOG_EVENT_SUPPRESS_USE_F', 'Suppress', 'generation', 'statements', 'statement', 'current', 'database', 'function', 'Most', 'notable', 'cases', 'CREATE', 'DATABASE', 'DROP', 'exceptional', 'circumstances', 'since', 'introduce', 'significant', 'regarding', 'logic', 'replicated', 'holder', 'LOG_EVENT_UPDATE_TABLE_MAP_VERSION_F', 'please', 'LOG_EVENT_ARTIFICIAL_F', 'Artificial', 'created', 'arbitarily', 'position', 'executes', 'them', 'LOG_EVENT_RELAY_LOG_F', 'Events', 'relay', 'LOG_EVENT_IGNORABLE_F', 'carrying', 'recognize', 'ignored', 'Otherwise', 'acknowledges', 'unknown', 'LOG_EVENT_NO_FILTER_F', 'filtered', 'regardless', 'filters', 'x100', 'group', 'marked', 'force', 'execution', 'isolation', 'Workers', 'marker', 'Coordinator', 'memorize', 'perform', 'necessary', 'operations', 'guarantee', 'interference', 'terminates', 'Typically', 'done', 'transaction', 'contains', 'accessing', 'LOG_EVENT_MTS_ISOLATE_F', 'x200', 'OPTIONS_WRITTEN_TO_BIN_LOG', 'bits', 'want', 'contrary', 'doable', 'hard', 'decide', 'among', 'Guilhem', 'read', 'through', 'usage', 'looks', 'OPTION_AUTO_IS_NULL', 'OPTION_NO_FOREIGN_KEYS', 'ones', 'alter', 'table', 'good', 'OPTION_RELAXED_UNIQUE_CHECKS', 'otherwise', 'slower', 'InnoDB', 'OPTION_BIG_SELECTS', 'needed', 'runs', 'max_join_size', 'HA_POS_ERROR', 'OPTION_BIG_TABLES', 'either', 'manual', 'says', 'memory', 'temp', 'disk', 'OPTION_NO_FOREIGN_KEY_CHECKS', 'OPTION_NOT_AUTOCOMMIT', 'Shouldn', 'defined', 'EXPECTED_OPTIONS', '#error', '#undef', 'shouldn', 'enum', 'enum_binlog_checksum_alg', 'BINLOG_CHECKSUM_ALG_OFF', 'checksum', 'though', 'generator', 'capable', 'Master', 'BINLOG_CHECKSUM_ALG_CRC32', 'CRC32', 'zlib', 'algorithm', 'BINLOG_CHECKSUM_ALG_ENUM_END', 'line', 'valid', 'BINLOG_CHECKSUM_ALG_UNDEF', 'special', 'undetermined', 'unaware', 'servers', 'CHECKSUM_CRC32_SIGNATURE_LEN', 'statically', 'implemented', 'BINLOG_CHECKSUM_LEN', 'BINLOG_CHECKSUM_ALG_DESC_LEN', 'descriptor', 'Log_event_type', 'Enumeration', 'Every', 'Format_description_log_event::Format_description_log_event', 'UNKNOWN_EVENT', 'START_EVENT_V3', 'QUERY_EVENT', 'STOP_EVENT', 'ROTATE_EVENT', 'INTVAR_EVENT', 'LOAD_EVENT', 'SLAVE_EVENT', 'Unused', 'Slave_log_event', 'been', 'CREATE_FILE_EVENT', 'APPEND_BLOCK_EVENT', 'EXEC_LOAD_EVENT', 'DELETE_FILE_EVENT', 'NEW_LOAD_EVENT', 'except', 'sql_ex', 'allowing', 'multibyte', 'share', 'RAND_EVENT', 'USER_VAR_EVENT', 'FORMAT_DESCRIPTION_EVENT', 'XID_EVENT', 'BEGIN_LOAD_QUERY_EVENT', 'EXECUTE_LOAD_QUERY_EVENT', 'TABLE_MAP_EVENT', 'numbers', 'therefore', 'obsolete', 'PRE_GA_WRITE_ROWS_EVENT', 'PRE_GA_UPDATE_ROWS_EVENT', 'PRE_GA_DELETE_ROWS_EVENT', 'until', 'mysql', 'trunk', 'WRITE_ROWS_EVENT_V1', 'UPDATE_ROWS_EVENT_V1', 'DELETE_ROWS_EVENT_V1', 'Something', 'ordinary', 'happened', 'INCIDENT_EVENT', 'Heartbeat', 'send', 'idle', 'ensure', 'online', 'HEARTBEAT_LOG_EVENT', 'some', 'situations', 'over', 'ignorable', 'handling', 'recognized', 'IGNORABLE_LOG_EVENT', 'ROWS_QUERY_LOG_EVENT', 'Version', 'WRITE_ROWS_EVENT', 'UPDATE_ROWS_EVENT', 'DELETE_ROWS_EVENT', 'GTID_LOG_EVENT', 'ANONYMOUS_GTID_LOG_EVENT', 'PREVIOUS_GTIDS_LOG_EVENT', 'right', 'above', 'comment', 'Existing', 'ENUM_END_EVENT', 'handled', 'exist', 'Int_event_type', 'INVALID_INT_EVENT', 'LAST_INSERT_ID_EVENT', 'INSERT_ID_EVENT', 'MYSQL_BIN_LOG', 'Relay_log_info', 'Slave_worker', 'Slave_committed_queue', 'enum_base64_output_mode', 'BASE64_OUTPUT_NEVER', 'BASE64_OUTPUT_AUTO', 'BASE64_OUTPUT_UNSPEC', 'BASE64_OUTPUT_DECODE_ROWS', 'output', 'modes', 'BASE64_OUTPUT_MODE_COUNT', 'structure', 'passed', 'methods', 'There', 'settings', 'Last', 'comes', 'printed', 'They', 'commands', 'Other', 'information', 'short_form', 'hexdump_from', 'dependent', 'st_print_event_info', 'Settings', 'cache', 'unchanged', 'TODO', 'FN_REFLEN', 'make', 'LEX_STRING', 'flags2_inited', 'uint32', 'sql_mode_inited', 'ulong', 'auto_increment_increment', 'auto_increment_offset', 'charset_inited', 'storable', 'time_zone_str', 'MAX_TIME_ZONE_NAME_LENGTH', 'thread_id', 'thread_id_printed', 'server_id_from_fd_event', 'close_cached_file', 'head_cache', 'body_cache', 'init_ok', 'tells', 'construction', 'successful', 'my_b_inited', 'base64_output_mode', 'whenever', 'Format_description_event', 'Later', 'base64', 'tested', 'seen', 'unsafe', 'message', 'generated', 'printed_fd_event', 'my_off_t', 'common_header_len', 'delimiter', 'verbose', 'table_mapping', 'm_table_map', 'm_table_map_ignored', 'caches', 'based', 'collect', 'main', 'making', 'Indicate', 'unflushed', 'have_unflushed_events', 'True', 'printing', 'COMMIT', 'ever', 'triggered', 'False', 'skipped_event_in_transaction', 'true', 'gtid_next', 'is_gtid_next_set', 'Determines', 'needs', 'restored', 'AUTOMATIC', 'ends', 'false', 'happen', 'logs', 'transactions', 'split', 'multiple', 'initially', 'Gtid_log_event', 'is_gtid_next_valid', 'PRINT_EVENT_INFO', 'scheduled', 'st_mts_db_names', 'Mts_db_names', 'Log_event', 'abstract', 'base', 'section', 'Log_event_binary_format', 'Format', 'saved', 'following', 'three', 'components', 'Common', 'Header', 'Post', 'Body', 'documented', 'Table_common_header', 'form', 'specifies', 'formats', 'separately', 'subclass', 'follows', 'caption', 'Name', 'Description', 'unsigned', 'integer', 'started', 'seconds', 'enumeration', ' #Log_event_type', 'Server', 'total_size', 'size', 'words', 'master_position', 'next', 'beginning', 'bitfield', 'Log_event::flags', 'Summing', 'subsection', 'Log_event_format_of_atomic_primitives', 'Atomic', 'Primitives', 'whether', 'little', 'endian', 'unless', 'specified', 'anchor', 'packed_integer', 'Some', 'efficient', 'representation', 'integers', 'called', 'Packed', 'Integer', 'capacity', 'storing', 'still', 'determines', 'according', 'xffff', 'Three', 'xffffff', 'Eight', 'xffffffffffffffff', 'Strings', 'various', 'string', 'public', 'kinds', 'skipping', 'occur', 'shall_skip', 'do_shall_skip', 'enum_skip_reason', 'skip', 'EVENT_SKIP_NOT', 'Skip', 'ignoring', 'means', 'EVENT_SKIP_IGNORE', 'decrease', 'EVENT_SKIP_COUNT', 'protected', 'enum_event_cache_type', 'EVENT_INVALID_CACHE', 'transactional', 'being', 'flushed', 'correspondent', 'completed', 'EVENT_STMT_CACHE', 'upon', 'commit', 'EVENT_TRANSACTIONAL_CACHE', 'directly', 'going', 'EVENT_NO_CACHE', 'EVENT_CACHE_COUNT', 'enum_event_logging_type', 'EVENT_INVALID_LOGGING', 'EVENT_NORMAL_LOGGING', 'empty', 'immediatly', 'waiting', 'EVENT_IMMEDIATE_LOGGING', 'EVENT_CACHE_LOGGING_COUNT', 'definition', 'placed', 'manipulated', 'buffer', 'buffers', 'contain', 'containing', 'character', 'Byte', 'offset', 'originally', 'appeared', 'preserved', 'SHOW', 'SLAVE', 'STATUS', 'coordinates', 'wrapped', 'BEGIN', 'log_pos', 'queries', 'sees', 'logical', 'real', 'read_log_event', 'analysed', 'content', 'temp_buf', 'Timestamp', 'debugging', 'TIMESTAMP', 'important', 'creation', 'guarantees', 'timestamps', 'timeval', 'took', 'exec_time', 'Number', 'data_written', 'prevent', 'infinite', 'loops', 'circular', 'Binlog', 'lowest', 'opt_server_id_bits', 'unmasked_server_id', 'notes', 'uint16', 'global', 'system', 'Handling', 'separate', 'governed', 'member', 'slave_exec_mode', 'Defines', 'event_cache_type', 'event_logging_type', 'Placeholder', 'writing', 'ha_checksum', 'Index', 'array', 'indicate', 'purging', 'index', 'terminator', 'Worker', 'indexed', 'represent', 'progress', 'mts_group_idx', 'associating', 'assigned', 'Additionally', 'serves', 'deferred', 'avoid', 'regular', 'destruction', 'worker', 'pass', 'future_event_relay_log_pos', 'Partition', 'associate', 'deliver', 'applier', 'mts_assigned_partitions', 'cache_type_arg', 'logging_type_arg', 'thd_arg', 'flags_arg', 'functions', 'BINLOG', 'EVENTS', 'binlog_dump', 'reads', 'mutex', 'proceed', 'description_event', 'parse', 'fact', 'call', 'constructor', 'argument', 'static', 'mysql_mutex_t', 'log_lock', 'my_bool', 'crc_check', 'Reads', 'Used', 'dump', 'method', 'parsing', 'active', 'hold', 'lock', 'checksum_alg_arg', 'log_file_name_arg', 'is_binlog_active', 'retval', 'success', 'nothing', 'malformed', 'allocation', 'failed', 'partial', 'NULL', 'init_show_field_list', 'prepares', 'column', 'List', 'Item', 'field_list', 'HAVE_REPLICATION', 'net_send', 'Protocol', 'log_name', 'Stores', 'nonzero', 'virtual', 'pack_info', 'get_db', 'ifdef', 'having', 'link', 'against', 'libpthread', 'print_event_info', 'print_timestamp', 'time_t', 'print_header', 'is_more', 'print_base64', 'else', 'caller', 'Log_event::write_header', 'rest', 'post_header_len', 'FD::write', 'side', 'checksum_alg', 'operator', 'size_t', 'my_malloc', 'MY_WME', 'MY_FAE', 'delete', 'my_free', 'Placement', 'operators', 'wrapper_my_b_safe_write', 'uchar', 'data_length', 'write_footer', 'need_checksum', 'get_data_size', 'write_data_header', 'write_data_body', '__attribute__', 'unused', 'inline', 'get_time', 'tv_sec', 'tv_usec', 'previously', 'initialized', 'tmp_thd', 'current_thd', 'start_time', 'my_micro_time_to_timeval', 'my_micro_time', 'get_type_code', 'is_valid', 'set_artificial_event', 'set_relay_log_event', 'is_artificial_event', 'is_relay_log_event', 'is_ignorable_event', 'is_no_filter_event', 'is_using_trans_cache', 'is_using_stmt_cache', 'is_using_immediate_logging', 'free_temp_buf', 'register_temp_buf', 'simple', 'complicated', 'calculated', 'during', 'event_len', 'Returns', 'human', 'readable', 'get_type_str', 'Return', 'private', 'decisions', 'get_mts_execution_mode', 'mode', 'PARALLEL', 'thereby', 'sequential', 'impossible', 'further', 'breaks', 'ASYNChronous', 'SYNChronous', 'enum_mts_event_exec_mode', 'EVENT_EXEC_PARALLEL', 'EVENT_EXEC_ASYNC', 'requires', 'synchronization', 'EVENT_EXEC_SYNC', 'neither', 'EVENT_EXEC_CAN_NOT', 'TRUE', 'agaist', 'FALSE', 'note', 'incompatile', 'combinations', 'such', 'referred', 'Such', 'identified', 'treats', 'correspondingly', 'todo', 'support', 'related', 'is_mts_sequential_exec', 'finds', 'execute', 'Besides', 'parallelizable', 'applied', 'concurrently', 'require', 'wait_for_workers_to_finish', 'apply', 'slave_server_id', 'mts_in_group', 'very', 'fake', 'turned', 'stop', 'pool', 'get_slave_worker', 'fills', 'pointers', 'strings', 'supplied', 'item', 'pointer', 'filled', 'instances', 'intances', 'indicating', 'many', 'accesses', 'get_mts_dbs', 'mts_number_dbs', 'Group', 'Factually', 'remains', 'set_mts_isolate_group', 'ends_group', 'carries', 'partitioning', 'contains_partition_info', 'terminal', 'FASE', 'is_mts_group_isolated', 'certain', 'treated', 'transactionally', 'access', 'required', 'implementation', 'recovery', 'starts', 'starts_group', 'Apply', 'represents', 'interface', 'do_apply_event', 'apply_event', 'Update', 'stepping', 'do_update_pos', 'update_pos', 'Decide', 'shall', 'Primitive', 'made', 'primitive', 'hierarchy', 'actions', 'performed', 'Format_description_log_event::do_apply_event', 'Pointer', 'successfully', 'errno', 'application', 'Default', 'do_apply_event_worker', 'Helper', 'ignore', 'cannot', 'seeing', 'left', 'intact', 'processing', 'continue', 'typical', 'continue_group', 'endcode', 'Advance', 'advance', 'essential', 'coordinate', 'also', 'Normally', 'refer', 'Coordinates', 'advancing', 'usually', 'Observe', 'handler', 'errors', 'default', 'replicate_same_server_id', 'slave_skip_counter', 'greater', 'Log_event::EVENT_SKIP_NOT', 'Log_event::EVENT_SKIP_IGNORE', 'happends', 'originating', 'Log_event::EVENT_SKIP_COUNT', 'constructors', 'create', 'logging', 'acts', 'accepts', 'parameters', 'reproducing', 'tolerant', 'logged', 'Query_log_event_binary_format', 'general', 'discussion', 'introduction', 'five', 'slave_proxy_id', 'identifying', 'issued', 'however', 'threads', 'creates', 'local', 'distinguish', 'tables', 'belong', 'clients', 'db_len', 'currently', 'selected', 'error_code', 'fails', 'fail', 'ER_DB_CREATE_EXISTS', 'ER_DB_DROP_EXISTS', 'status_vars_len', 'status_vars', 'block', 'query_log_event_status_vars', 'Zero', 'listed', 'Table_query_log_event_status_vars', 'writes', 'null', 'terminated', 'trailing', 'redundant', 'known', 'extending', 'determined', 'field', 'lists', 'appear', 'Status', 'identifier', 'OPTIONS_WRITTEN', 'identifies', 'those', 'Specifically', 'equals', 'x0c084000', 'correspond', 'AUTOCOMMIT', 'Syntax', 'Manual', 'Modes', 'sql_priv', 'list', 'available', 'MODE_REAL_AS_FLOAT', 'MODE_PIPES_AS_CONCAT', 'MODE_ANSI_QUOTES', 'MODE_IGNORE_SPACE', 'MODE_NOT_USED', 'MODE_ONLY_FULL_GROUP_BY', 'MODE_NO_UNSIGNED_SUBTRACTION', 'MODE_NO_DIR_IN_CREATE', 'MODE_POSTGRESQL', 'MODE_ORACLE', 'MODE_MSSQL', 'x400', 'MODE_DB2', 'x800', 'MODE_MAXDB', 'x1000', 'MODE_NO_KEY_OPTIONS', 'x2000', 'MODE_NO_TABLE_OPTIONS', 'x4000', 'MODE_NO_FIELD_OPTIONS', 'x8000', 'MODE_MYSQL323', 'x10000', 'x20000', 'MODE_MYSQL40', 'x40000', 'MODE_ANSI', 'x80000', 'MODE_NO_AUTO_VALUE_ON_ZERO', 'x100000', 'MODE_NO_BACKSLASH_ESCAPES', 'x200000', 'MODE_STRICT_TRANS_TABLES', 'x400000', 'MODE_STRICT_ALL_TABLES', 'x800000', 'MODE_NO_ZERO_IN_DATE', 'x1000000', 'MODE_NO_ZERO_DATE', 'x2000000', 'MODE_INVALID_DATES', 'x4000000', 'MODE_ERROR_FOR_DIVISION_BY_ZERO', 'x8000000', 'MODE_TRADITIONAL', 'x10000000', 'MODE_NO_AUTO_CREATE_USER', 'x20000000', 'MODE_HIGH_NOT_PRECEDENCE', 'x40000000', 'MODE_PAD_CHAR_TO_FULL_LENGTH', 'x80000000', 'However', 'honored', 'preserves', 'rationale', 'Query_log_event::do_apply_event', 'Variable', 'most', 'belongs', 'totally', 'System', 'character_set_client', 'collation_connection', 'collation_server', 'collation', 'encode', 'converts', 'receives', 'comparing', 'literal', 'Connection', 'Character', 'Sets', 'Collations', 'pair', 'pairs', 'character_set_name', 'collation_name', 'FROM', 'COLLATIONS', 'Variables', 'Time', 'Zone', 'Support', 'zone', 'month', 'mapping', 'languages', 'sql_locale', 'locale', 'en_US', 'collation_database', 'source', 'holds', 'described', 'versions', 'WHEN', 'loaded', 'issuing', 'affect', 'newer', 'take', 'rather', 'difference', 'creating', 'another', 'plans', 'eventually', 'multi', 'corresponding', 'executing', 'filter', 'rules', 'opening', 'Query_log_event_notes_on_previous_versions', 'Notes', 'Previous', 'Versions', 'introduced', 'earlier', 'existed', 'identical', 'understood', 'adding', 'forget', 'code_name', 'Log_event::Byte', 'data_buf', 'q_len', 'strlen', 'compute', 'Load_log_event::do_apply_event', 'original', 'differ', 'members', 'concerned', 'catalog_len', 'uninited', 'generally', 'lose', 'Sometimes', 'short', 'autoinc', 'thing', 'plain', 'text', 'derived', 'benefit', 'work', 'mask', 'helps', 'between', 'meaning', 'down', 'influence', 'connections', 'soon', 'time_zone_len', 'Holds', 'binlog_version', 'augments', 'status_var', 'augmented', 'requested', 'mts_accessed_db_names', 'query_arg', 'query_length', 'using_trans', 'immediate', 'suppress_use', 'ignore_command', 'overfill', 'indicated', 'assigning', 'db_name', 'Only', 'rewritten', 'is_rewrite_empty', 'strcmp', 'dummy_len', 'db_filtered', 'get_rewrite_db', 'attach_temp_tables_worker', 'detach_temp_tables_worker', 'print_query_header', 'event_type', 'additionaly', 'get_post_header_size_for_derived', 'Writes', 'patch', 'allow', 'q_len_arg', 'is_trans_keyword', 'Before', 'SAVEPOINT', 'input', 'keywords', 'upper', 'lower', 'strncasecmp', 'binlogged', 'comments', 'front', 'examples', 'quiries', 'strncmp', 'Notice', 'parentheses', 'identification', 'single', 'occures', 'logics', 'STRING_WITH_LEN', 'corresponds', 'verbatim', 'CONCURRENT', 'LOCAL', 'file_name', 'REPLACE', 'IGNORE', 'INTO', 'table_name', 'FIELDS', 'OPTIONALLY', 'ENCLOSED', 'ESCAPED', 'STARTING', 'skip_lines', 'field_1', 'field_2', 'field_n', 'endverbatim', 'Load_log_event_binary_format', 'present', 'table_name_len', 'num_fields', 'Describes', 'lines', 'ndash', 'More', 'precisely', 'stores', 'presence', 'uses', 'long', 'Finally', 'boolean', 'combination', 'indicates', 'keyword', 'Therefore', 'field_lens', 'representing', 'zeros', 'table_len', 'actually', 'Load_log_event_notes_on_previous_versions', 'copy_log_event', 'body_offset', 'get_query_buffer_length', 'print_query', 'need_db', 'fn_start', 'fn_end', 'come', 'become', 'Dmitri', 'pushes', 'fname_len', 'field_block_len', 'fname', 'local_fname', 'Indicates', 'Since', 'coming', 'lacks', 'concurrent', 'object', 'mysql_load', 'construct', 'is_concurrent', 'doesn', 'Log_event::temp_buf', 'set_fname_outside_temp_buf', 'afname', 'alen', 'check_fname_outside_temp_buf', 'field_lens_buf', 'fields_buf', 'sql_exchange', 'db_arg', 'table_name_arg', 'fields_arg', 'is_concurrent_arg', 'enum_duplicates', 'handle_dup', 'set_fields', 'Name_resolution_context', 'context', 'commented', 'Exec', 'slave_net', 'use_rli_only_for_errors', 'extern', 'server_version', 'Start_log_event_v3', 'derives', 'describes', 'lengths', 'sending', 'naturally', 'Start_log_event_v3_binary_format', 'startup', 'FLUSH', 'LOGS', 'automatic', 'rotation', 'trick', 'slaves', 'drop', 'stale', 'unfinished', 'equal', 'indeed', 'Conclusion', 'attention', 'identity', 'the_date', 'rollover', 'dont_set_created', 'sized', 'ourself', 'future', 'decode', 'Format_description_log_event_binary_format', '_all_', 'number_of_event_types', 'decription', 'server_version_split', 'event_type_permutation', 'binlog_ver', 'server_ver', 'header_is_valid', 'version_is_valid', 'invalid', 'vector', 'considered', 'changes', 'calc_server_version_split', 'get_version_product', 'is_version_before_checksum', 'Intvar_log_event', 'LAST_INSERT_ID', 'INSERT_ID', 'Intvar_log_event_binary_format', 'identifiers', 'supported', 'type_arg', 'val_arg', 'get_var_type_name', 'sizeof', 'Rand_log_event', 'Logs', 'random', 'seed', 'RAND', 'repeatable', 'again', 'needn', 'waste', 'cause', 'bugs', 'state', 'internally', 'Rand_log_event_binary_format', 'seed1', 'seed2', 'seed1_arg', 'seed2_arg', 'Xid_log_event', 'committed', 'Xid_log_event_binary_format', 'my_xid', 'Log_event::EVENT_TRANSACTIONAL_CACHE', 'Log_event::EVENT_NORMAL_LOGGING', 'do_commit', 'User_var_log_event', 'User_var_log_event_binary_format', 'UNDEF_F', 'UNSIGNED_F', 'name_len', 'val_len', 'Item_result', 'charset_number', 'is_null', 'query_id_t', 'query_id', 'name_arg', 'name_len_arg', 'val_len_arg', 'charset_number_arg', 'Getter', 'setter', 'User', 'adjusts', 'path', 'is_deferred', 'deffered', 'instance', 'flagged', 'set_deferred', 'Stop_log_event_binary_format', 'Rotate_log_event', 'deprecated', 'move', 'using', 'Rotate_log_event_binary_format', 'component', 'rotate', 'new_log', 'DUP_NAME', 'RELAY_LOG', 'new_log_ident', 'ident_len', 'new_log_ident_arg', 'ident_len_arg', 'pos_arg', 'classes', 'Create_file_log_event', 'Create_file_log_event_binary_format', 'Pretend', 'fake_base', 'event_buf', 'block_len', 'file_id', 'inited_from_old', 'block_arg', 'block_len_arg', 'enable_local', 'Load_log_event::get_type_code', 'Load_log_event::get_data_size', 'extentions', 'write_base', 'Append_block_log_event', 'Append_block_log_event_binary_format', 'Append_block_log_event::write', 'filtering', 'inherited', 'get_create_or_append', 'Delete_file_log_event', 'Delete_file_log_event_binary_format', 'Begin_load_query_log_event', 'truncates', 'existing', 'Begin_load_query_log_event_binary_format', 'Elements', 'describe', 'handles', 'duplicates', 'enum_load_dup_handling', 'LOAD_DUP_ERROR', 'LOAD_DUP_IGNORE', 'LOAD_DUP_REPLACE', 'responsible', 'similar', 'substitutes', 'filename', 'Execute_load_query_log_event_binary_format', 'fn_pos_start', 'substituted', 'fn_pos_end', 'duplicate', 'explicitly', 'lost', 'dup_handling', 'fn_pos_start_arg', 'fn_pos_end_arg', 'dup_handling_arg', 'errcode', 'Prints', 'Query_log_event::is_valid', 'Unknown_log_event', 'Unknown_log_event_binary_format', 'Even', 'ctor', 'extract', 'str_to_hex', 'Table_map_log_event', 'operation', 'preceded', 'maps', 'Table_map_log_event_binary_format', 'Reserved', 'database_name', 'resides', 'represented', 'terminating', 'redundancy', 'encoded', 'column_count', 'columns', 'packed', 'column_type', 'mapped', 'enum_field_types', 'mysql_com', 'Table_table_map_log_event_column_types', 'description', 'associated', 'metadata', 'metadata_length', 'chunk', 'semantics', 'null_bits', 'rounded', 'nearest', 'ninth', 'numerical', 'interpretation', 'meta', 'Identifier', 'Size', 'MYSQL_TYPE_DECIMAL', 'MYSQL_TYPE_TINY', 'MYSQL_TYPE_SHORT', 'MYSQL_TYPE_LONG', 'MYSQL_TYPE_FLOAT', 'pack_length', 'float', 'originates', 'MYSQL_TYPE_DOUBLE', 'double', 'MYSQL_TYPE_NULL', 'MYSQL_TYPE_TIMESTAMP', 'MYSQL_TYPE_LONGLONG', 'MYSQL_TYPE_INT24', 'MYSQL_TYPE_DATE', 'MYSQL_TYPE_TIME', 'MYSQL_TYPE_DATETIME', 'MYSQL_TYPE_YEAR', 'MYSQL_TYPE_NEWDATE', 'MYSQL_TYPE_VARCHAR', 'MYSQL_TYPE_BIT', 'occupied', 'MYSQL_TYPE_NEWDECIMAL', 'precision', 'decimals', 'MYSQL_TYPE_ENUM', 'MYSQL_TYPE_SET', 'MYSQL_TYPE_TINY_BLOB', 'MYSQL_TYPE_MEDIUM_BLOB', 'MYSQL_TYPE_LONG_BLOB', 'MYSQL_TYPE_BLOB', 'pack', 'blob', 'MYSQL_TYPE_VAR_STRING', 'MYSQL_TYPE_STRING', 'MYSQL_TYPE_GEOMETRY', 'geometry', 'Constants', 'TYPE_CODE', 'enum_error', 'ERR_OPEN_FAILURE', 'Failure', 'open', 'ERR_OK', 'ERR_TABLE_LIMIT_EXCEEDED', 'room', 'ERR_OUT_OF_MEM', 'ERR_BAD_TABLE_DEF', 'match', 'ERR_RBR_TO_SBR', 'daisy', 'chanining', 'allowed', 'enum_flag', 'Nothing', 'preparation', 'Need', 'constant', 'compile', 'enumerations', 'ENUM_FLAG_COUNT', 'flag_set', 'Special', 'constants', 'sets', 'TM_NO_FLAGS', 'TM_BIT_LEN_EXACT_F', 'TM_REFERRED_FK_DB_F', 'get_flags', 'm_flags', 'Table_id', 'is_transactional', 'table_def', 'create_table_def', 'm_coltype', 'm_colcnt', 'm_field_metadata', 'm_field_metadata_size', 'm_null_bits', 'get_table_id', 'm_table_id', 'get_table_name', 'm_tblnam', 'get_db_name', 'm_dbnam', 'm_memory', 'malloc', 'm_data_size', 'save_field_metadata', 'reports', 'foreign', 'keys', 'constraint', 'm_table', 'm_dblen', 'm_tbllen', 'calling', 'm_meta_memory', 'Rows_log_event', 'RESPONSIBILITIES', 'Encode', 'parts', 'Write', 'Provide', 'individual', 'Rows_log_event_binary_format', 'row_lookup_mode', 'ROW_LOOKUP_UNDEFINED', 'ROW_LOOKUP_NOT_NEEDED', 'ROW_LOOKUP_INDEX_SCAN', 'ROW_LOOKUP_TABLE_SCAN', 'ROW_LOOKUP_HASH_SCAN', 'combine', 'appropriate', 'normal', 'bitwise', 'implicit', 'conversion', 'accepted', 'compiler', 'STMT_END_F', 'Value', 'NO_FOREIGN_KEY_CHECKS_F', 'RELAXED_UNIQUE_CHECKS_F', 'complete', 'COMPLETE_ROWS_F', 'RLE_NO_FLAGS', 'set_flags', 'clear_flags', 'm_type', 'Specific', 'get_general_type_code', 'direct', 'print_verbose', 'print_verbose_one_row', 'MY_BITMAP', 'cols_bitmap', 'prefix', 'add_row_data', 'do_add_row_data', 'Member', 'implement', 'superclass', 'get_cols', 'm_cols', 'get_cols_ai', 'm_cols_ai', 'get_width', 'm_width', 'compares', 'write_set', 'Comparison', 'account', 'correct', 'Delete_rows_log_event', 'Write_rows_log_event', 'Update_rows_log_event', 'bitmaps', 'bitmap_cmp', 'read_write_bitmaps_cmp', 'switch', 'read_set', 'Check', 'succeeded', 'allocating', 'COLS', 'Checking', 'Update_rows_log_event::is_valid', 'm_rows_buf', 'bitmap', 'm_row_count', 'get_extra_row_data', 'm_extra_row_data', 'supposed', 'inherit', 'cols', 'extra_row_info', 'row_data', 'print_helper', 'Bitmap', 'denoting', 'width', 'Hash', 'entries', 'HASH_SCAN', 'search', 'm_hash', 'searching', 'image', 'm_rows_lookup_algorithm', 'Update_rows', 'm_master_reclength', 'Length', 'record', 'm_bitbuf', 'm_bitbuf_ai', 'm_rows_cur', 'm_rows_end', 'allocated', 'space', 'Flags', 'level', 'Actual', 'helper', 'm_curr_row', 'Start', 'm_curr_row_end', 'm_key', 'Buffer', 'searches', 'm_key_index', 'm_key_info', 'Points', ' #m_key_index', 'Key_compare', 'Where', 'find', 'm_distinct_keys', 'instantiated', 'constructed', 'moment', 'comparisons', 'instantiation', 'Rows_log_event::m_key_info', 'elements', 'key_cmp2', 'key_part', 'key_length', 'std::set', 'iterator', 'm_itr', 'spare', 'saving', 'distinct', 'doing', 'scan', 'm_distinct_key_spare_buf', 'Unpack', 'unpack_current_row', 'HA_ERR_CORRUPT_EVENT', 'unpack_row', 'deciding', 'decide_row_lookup_algorithm_and_key', 'Encapsulates', 'row_operations_scan_and_key_setup', 'row_operations_scan_and_key_teardown', 'auto', 'increment', 'autoincrement', 'is_auto_inc_in_extra_columns', 'next_number_field', 'field_index', 'prepare', 'executions', 'DESCRIPTION', 'do_prepare_row', 'do_exec_row', 'calls', 'entire', 'allocate', 'mentioned', 'RETURN', 'VALUE', 'went', 'do_before_row_operations', 'Slave_reporting_capability', 'clean', 'After', 'release', 'do_after_row_operations', 'located', 'returns', 'Private', 'idempotent', 'cleared', 'handle_idempotent_and_ignored_errors', 'updating', 'deleting', 'performs', 'assertions', 'importantly', 'updates', 'loop', 'Rows_log_event::do_apply_event', 'do_post_row_operations', 'Commodity', 'wrapper', 'around', 'deals', 'resetting', 'reference', 'do_apply_row', 'Implementation', 'do_index_scan_and_update', 'hash_scan', 'positions', 'hashtable', 'unpacked', 'scans', 'matches', 'do_hash_scan_and_update', 'legacy', 'table_scan', 'engine', 'do_table_scan_and_update', 'Initializes', 'scanning', 'Opens', 'initailizes', 'open_record_scan', 'Does', 'cleanup', 'closes', 'opened', 'close_record_scan', 'Fetches', 'populates', 'indexes', 'contigous', 'ranges', 'fetches', 'parms', 'first_read', 'signifying', 'return_value', 'reeords', 'fetched', 'occured', 'next_record_scan', 'Populates', 'modified', 'Err_code', 'add_key_to_distinct_keyset', 'Thence', 'unpacks', 'saves', 'gets', 'do_hash_row', 'applies', 'hashed', 'MUST', 'do_scan_and_update', 'friend', 'Old_rows_log_event', 'insertions', 'several', 'Write_rows_log_event_binary_format', 'THD::binlog_prepare_pending_rows_event', 'binlog_row_logging_function', 'before_record', 'after_record', 'binlog_write_row', 'write_row', 'Also', 'Update_rows_log_event_binary_format', 'cols_bi', 'cols_ai', 'binlog_update_row', 'Rows_log_event::is_valid', 'deletions', 'container', 'deleted', 'COLLABORATION', 'Row_writer', 'Row_reader', 'Extract', 'Delete_rows_log_event_binary_format', 'binlog_delete_row', 'log_event_old', 'Incident_log_event', 'Class', 'incident', 'occurance', 'inform', 'might', 'inconsistent', 'IncidentFormat', 'Incident', 'Symbol', 'INCIDENT', 'align', 'MSGLEN', 'Message', 'MESSAGE', 'Log_event::EVENT_NO_CACHE', 'Log_event::EVENT_IMMEDIATE_LOGGING', 'm_incident', 'DBUG_ENTER', 'Incident_log_event::Incident_log_event', 'DBUG_PRINT', 'enter', 'm_message', 'Just', 'precaution', 'DBUG_VOID_RETURN', 'Mark', 'INCIDENT_NONE', 'strmake', 'descr_event', 'INCIDENT_COUNT', 'Ignorable_log_event', 'Base', 'deriving', 'safely', 'Newer', 'designed', 'ended', 'architecture', 'harm', 'mechanism', 'unrecognized', 'strictly', 'derive', 'Log_event::EVENT_STMT_CACHE', 'Ignorable_log_event::Ignorable_log_event', 'Rows_query_log_event', 'query_len', 'Rows_query_log_event::Rows_query_log_event', 'm_rows_query', 'my_snprintf', 'copy_event_cache_to_file_and_reinit', 'flush_stream', 'my_b_copy_to_file', 'fflush', 'ferror', 'reinit_io_cache', 'WRITE_CACHE', 'alive', 'originated', 'straight', 'Slave', 'checks', 'throws', 'away', 'log_ident', 'Log_event::log_pos', 'comprise', 'event_coordinates', 'heartbeat', 'Heartbeat_log_event', 'BIN_LOG_HEADER_SIZE', 'get_log_ident', 'get_ident_len', 'gathering', 'fate', 'slave_execute_deferred_events', 'append_query_string', 'CHARSET_INFO', 'csinfo', 'event_checksum_test', 'get_checksum_alg', 'TYPELIB', 'binlog_checksum_typelib', 'GTID', 'Gtid_specification', 'SESSION', 'GTID_NEXT', 'spec', 'Gtid_log_event::get_type_code', 'ANONYMOUS_GROUP', 'DBUG_RETURN', 'POST_HEADER_LENGTH', 'to_string', 'AUTOMATIC_GROUP', 'GTID_GROUP', 'enum_group_type', 'get_type', 'shared', 'rpl_sid', 'get_sid', 'SIDNO', 'relative', 'sid_map', 'lookup', 'global_sid_map', 'hence', 'global_sid_lock', 'held', 'need_lock', 'negative', 'acquired', 'released', 'prior', 'causes', 'rpl_sidno', 'get_sidno', 'gtid', 'sidno', 'rdlock', 'assert_some_lock', 'add_sid', 'unlock', 'Sid_map', 'assumes', 'thus', 'locks', 'rpl_gno', 'get_gno', 'get_commit_flag', 'commit_flag', 'holding', 'GLOBAL', 'SET_STRING_PREFIX', 'SET_STRING_PREFIX_LENGTH', 'maximal', 'MAX_SET_STRING_LENGTH', 'rpl_sid::TEXT_LENGTH', 'MAX_GNO_TEXT_LENGTH', 'encoding', 'ENCODED_FLAG_LENGTH', 'ENCODED_SID_LENGTH', 'rpl_sid::BYTE_LENGTH', 'ENCODED_GNO_LENGTH', 'Total', 'Internal', 'uninitialized', 'Previous_gtids_log_event', 'Gtid_set', 'buf_size', 'DBUG_EVALUATE_IF', 'skip_writing_previous_gtids_log_event', 'write_partial_previous_gtids_log_event', 'Log_event::write_data_header', 'Log_event::write_footer', 'get_buf', 'formatted', 'responsibility', 'get_str', 'Gtid_set::String_format', 'string_format', 'GTIDs', 'add_to_set', 'gtid_set', 'Gtid', 'copied', 'is_gtid_event', 'version_product', 'version_split', 'Splits', 'numeric', 'pieces', 'split_versions', 'Zabc', 'digit', 'Yabc', 'do_server_version_split', 'strtoul', 'utility', 'adds', 'quoted', 'escapes', 'existance', 'quote', 'my_strmov_quoted_identifier', 'my_strmov_quoted_identifier_helper']