def count_segments_containing_points(segments, points):

    events = []
    for (l, r) in segments:
        events.append((l, 'L'))
        events.append((r, 'R'))
    for i, point in enumerate(points):
        events.append((point, 'P', i))
   
    events.sort(key=lambda x: (x[0], x[1]))
   
    current_segments = 0
    result = [0] * len(points)
   
    for event in events:
        if event[1] == 'L':
            current_segments += 1
        elif event[1] == 'R':
            current_segments -= 1
        else:
            result[event[2]] = current_segments
   
    return result
 
n, m = map(int, input().split()) 
 
segments = []
for _ in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))
 
points = list(map(int, input().split())) 
 
result = count_segments_containing_points(segments, points)
 
print(" ".join(map(str, result)))