def first_tool_position(tools, needed):
    i=0
    for i in range(len(tools)):
        if tools[i]==needed:
            return i
    return -1
def all_tool_positions(tools, needed):
    indexes=[]
    for i in range(len(tools)):
        if tools[i]==needed:
            indexes.append(i)
    return indexes
tools=["hammer", "drill", "saw", "drill", "wrench"]
drill_first=first_tool_position(tools, "drill")
drill_all=all_tool_positions(tools, "drill")
print(f"first position={drill_first}, all positions= {drill_all}")
tape_first=first_tool_position(tools, "tape")
tape_all=all_tool_positions(tools, "tape")
print(f"first position={tape_first}, all positions= {tape_all}")