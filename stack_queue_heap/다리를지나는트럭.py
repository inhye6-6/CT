def solution(bridge_length, weight, truck_weights):
    total = truck_weights[0]
    heap = [[truck_weights.pop(0),bridge_length]] #[트럭 weights, 나가는 시간]
    time = bridge_length

    while truck_weights:
        time +=1 # 총 지난 시간
        
        #트럭이 다리를 건넜을 때 pop
        if time - heap[0][1] == bridge_length :
            total -= heap[0][0]
            heap.pop(0)
            
        #다음 트럭이 들어올 수 있을 때 
        if weight >= truck_weights[0]+total and len(heap) < bridge_length :
            total += truck_weights[0]
            heap.append([truck_weights.pop(0),time])
    return time + 1