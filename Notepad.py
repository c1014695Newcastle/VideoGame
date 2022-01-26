from ReusedCode import slow_print, checkn

def notepad(progress):
    slow_print("Notepad\n\nHere's what you know so far:\n")
    tareth_progress(progress)


def tareth_progress(progress):
    print("\n========== TARETH ==========")
    if progress["Tareth Issac"] == 1:
        print("""
Tareth was a childhood friend of Issac who later helped him found his company. The two used to run it together, however, ever since he got engaged, Issac hasn't been in the office much.""")
    if progress["Tareth Janet"] == 1:
        print("""
Tareth never really liked Janet and resented her for taking Issac away from the business.""")
    if progress["Tareth Mia"] == 1:
        print("""
Tareth never had much trouble with Mia. She was never interested in taking over the business from her dad so the two rarely had interactions.""")
    if progress["Tareth Andrew"] == 1:
        print("""
Tareth thinks very little of Andrew. He believes that, without his dad, he would have failed a long time ago.""")