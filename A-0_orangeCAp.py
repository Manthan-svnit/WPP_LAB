test1 = {
    "kohli": int(input("enter the run of kohli in first test: ")),
    "dhoni": int(input("enter the run of dhoni in first test: ")),
    "sachin": int(input("ente the run of sachin in first test: ")),
}
test2={
     "kohli": int(input("enter the run of kohli in second test: ")),
    "dhoni": int(input("enter the run of dhoni in second test: ")),
    "sachin": int(input("ente the run of sachin in second test: ")),
}
sum_k=test1["kohli"] + test2["kohli"]
sum_d= test1["dhoni"] + test2["dhoni"]
sum_s=test1["sachin"] + test2["sachin"]
if(sum_k>sum_d and sum_k>sum_s):
    print("kohli have orange cap")
elif(sum_d>sum_k and sum_d>sum_s):
    print("dhoni have orange cap")
elif(sum_s>sum_k and sum_s > sum_d):
    print("sachin have orange cap")