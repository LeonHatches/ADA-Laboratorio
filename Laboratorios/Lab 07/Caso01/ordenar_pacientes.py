def merge_sort_pacientes(pacientes):
    if len(pacientes) <= 1:
        return pacientes
    
    mid   = len(pacientes) // 2
    left  = merge_sort_pacientes(pacientes[:mid])
    right = merge_sort_pacientes(pacientes[mid:])

    return merge (left, right)

def merge (left, right):
    resultado = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]["gravedad"] > right[j]["gravedad"]:
            resultado.append(left[i])
            i += 1

        else:
            resultado.append(right[j])
            j += 1

    resultado.extend(left[i:])
    resultado.extend(right[j:])
    return resultado