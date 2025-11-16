def merge_sort_pacientes(pacientes):
    if len(pacientes) <= 1:
        return pacientes
    
    mid   = len(pacientes) // 2
    left  = merge_sort_pacientes(pacientes[:mid])
    right = merge_sort_pacientes(pacientes[mid:])

    return merge (left, right)

def merge (left, right):
    return 0