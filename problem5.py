def prepare_boards(lengths, needed):
    new_list=sorted(lengths)
    return(new_list, new_list[:needed])
lengths=[60,20,50,20,35]
needed=3
items=prepare_boards(lengths,needed)
sorted_list, selected=items
print(f"Original: {lengths}")
print(f"Sorted: {sorted_list}")
print(f"Selected:{selected}")
print(f"Total selected lengths:{sum(selected)}")