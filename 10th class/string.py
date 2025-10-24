s ="Hello,World!"

s2 = s[0:5]
print(s2)
s3 = s[:]
s4 = s[::]
print(s3)
print(s4)
s5 = s[6:]
print(s5)
s6 = s[:8]
print(s6)
print(s[::4])
print(s[-4:])
print(s[:-3])
print(s[-5:-2])
print(s[::-1])



def get_sub(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)


print('H{}SO{}'.format)
