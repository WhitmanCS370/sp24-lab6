import json
import sys
import ChainMap

def do_add(env, args):
    assert len(args) == 2
    left = do(env, args[0])
    right = do(env, args[1])
    return left + right

# [call]
def do_call(env, args):
    # Set up the call.
    assert len(args) >= 1
    func_or_name = args[0]
    
    # check if we have function or name.
    if not isinstance(func_or_name, str):
        func = do(env, func_or_name)
    else:
        func = env_set(env, func_or_name)

    values = [do(env, a) for a in args[1:]]

    # Find the function.
    assert isinstance(func, list) and (func[0] == "func")
    params, body = func[1], func[2]
    assert len(values) == len(params)

    # Run in new environment.
    d = {}
    for i,j in zip(params, values):
        d[i] = j
    env.new_child(d)
    
    # env.append(dict(zip(params, values)))
    result = do(env, body)
    env.pop()

    # Report.
    return result
# [/call]

def do_comment(env, args):
    return None

# [func]
def do_func(env, args):
    assert len(args) == 2 or len(args) == 3
    if len(args) == 3:
        name = args[0]
        params = args[1]
        body = args[2]
        env_set(env, name, body)
    else:
        params = args[0]
        body = args[1]
    return ["func", params, body]
# [/func]

def do_get(env, args):
    assert len(args) == 1
    return env_get(env, args[0])

def do_gt(env, args):
    assert len(args) == 2
    return do(env, args[0]) > do(env, args[1])

def do_if(env, args):
    assert len(args) == 3
    cond = do(env, args[0])
    choice = args[1] if cond else args[2]
    return do(env, choice)

def do_leq(env, args):
    assert len(args) == 2
    return do(env, args[0]) <= do(env, args[1])

def do_neg(env, args):
    assert len(args) == 1
    return -do(env, args[0])

def do_not(env, args):
    assert len(args) == 1
    return not do(env, args[0])

def do_or(env, args):
    assert len(args) == 2
    if temp := do(env, args[0]):
        return temp
    return do(env, args[1])

def do_print(env, args):
    args = [do(env, a) for a in args]
    print(*args)
    return None

def do_repeat(env, args):
    assert len(args) == 2
    count = do(env, args[0])
    for i in range(count):
        result = do(env, args[1])
    return result

def do_seq(env, args):
    for a in args:
        result = do(env, a)
    return result

def do_set(env, args):
    assert len(args) == 2
    name = args[0]
    value = do(env, args[1])
    env_set(env, name, value)
    return value

# Lookup table of operations.
OPERATIONS = {
    name.replace("do_", ""): func
    for (name, func) in globals().items()
    if name.startswith("do_")
}

def do(env, instruction):
    if not isinstance(instruction, list):
        return instruction
    op, args = instruction[0], instruction[1:]
    assert op in OPERATIONS
    return OPERATIONS[op](env, args)

# getting function names in environemnt.
def env_get(env, name):
    assert isinstance(name, str)
    for e in reversed(env):
        if name in e:
            return e[name]
    assert False, f"Unknown variable {name}"

# initializing the function names.
def env_set(env, name, value):
    assert isinstance(name, str)
    for e in reversed(env.values()):
        if name in e:
            env[name] = value
            return
    env[-1][name] = value

def main():
    assert len(sys.argv) == 2, "Usage: func.py filename"
    with open(sys.argv[1], "r") as reader:
        program = json.load(reader)
    merged = ChainMap({})
    result = do(merged, program)
    print(f"=> {result}")

if __name__ == "__main__":
    main()
