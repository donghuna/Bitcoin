import logging

logging.basicConfig(level=logging.ERROR)


def get_logger(name=None):
	default = "__app__"

	# 로그 생성
	if name:
		__logger = logging.getLogger(name)
	else:
		__logger = logging.getLogger(default)
	__logger.propagate = False


	# 로그의 출력 기준 설정
	__logger.setLevel(logging.INFO)

	# log 출력 형식
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	simple_formatter = logging.Formatter("[%(name)s] %(message)s")
	complex_formatter = logging.Formatter(
		"%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s"
	)

	# log 출력
	stream_handler = logging.StreamHandler()
	stream_handler.setFormatter(formatter)
	__logger.addHandler(stream_handler)

	# log를 파일에 출력
	file_handler = logging.FileHandler('my.log')
	file_handler.setFormatter(formatter)
	__logger.addHandler(file_handler)

	return __logger
