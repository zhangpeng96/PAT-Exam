def main():
	data_map = {}
	mate_map = {}
	guest_map = {}
	input_count = int(input())

	for i in range(0, input_count):
		data_id = str(input())
		data_map[data_id] = False
		mate_map[data_id] = int(data_id[6:6+8])

	query_count = int(input())

	for i in range(0, query_count):
		query_id = str(input())
		if query_id in data_map:
			data_map[query_id] = True
		else:
			guest_map[query_id] = int(query_id[6:6+8])
	
	# print(mate_map, guest_map)
	
	visited_count = list(data_map.values()).count(True)
	print(visited_count)
	if visited_count:
		print(sorted(mate_map.items(), key = lambda x: x[1])[0][0])
	else:
		print(sorted(guest_map.items(), key = lambda x: x[1])[0][0])



if __name__ == '__main__':
	main()