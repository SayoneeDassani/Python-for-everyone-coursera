text = "X-DSPAM-Confidence:    0.8475"
e=text.replace(" ","")
f=e.find(":")
val=e[f+1:]
print(float(val))
