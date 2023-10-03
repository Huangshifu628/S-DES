import main
from main import *
import time

cleartext = ['00000000', '12345678', '1047973470']#明文
ciphertext = ['00000000', '·+RµÒj7Ê', '·0µ7	7Rµ70']#密文

#加密
def enc(code, key):
    s = ''
    K1, K2 = main.generate_key(key, p10_table, p8_table)
    for i in code:
        st = str.zfill(bin(ord(i))[2:], 8)
        sr = main.encrypt(st, K1, K2)
        ss = chr(eval('0b'+str(sr)))
        s = s + ss
    return s

#循环暴力破解
t1 = time.time()
for i in range(1024):

    k = str.zfill(bin(i)[2:], 10)
    flag = 0
    for text in range(len(cleartext)):
        if enc(cleartext[text], k) != ciphertext[text]:
            flag = 1
            break
    if flag == 0:
        print('密钥为:', k)
        t2 = time.time()
        print('耗时:', t2-t1)

'''
在S-DES算法中，对于每个明文-密文对，只有一个密钥被用于加密和解密。
每个密钥都是由10位二进制数字组成的。对于给定的明文分组P_n，如果选择不同的密钥K_i和K_j进行加密，通常情况下会得到不同的密文C_n。
但是，由于S-DES算法的特定设计，可能会出现一些特殊情况下，不同的密钥加密得到相同的密文。
这种情况被称为密钥冲突，但在实际应用中，这种情况非常罕见。
'''
'''
当然！S-DES（简化数据加密标准）算法是DES算法的简化版本。它对8位数据块进行操作，并使用10位密钥进行加密和解密。 
在S-DES中，密钥生成过程涉及对原始的10位密钥进行置换和移位，以生成两个8位子密钥：K1和K2。这些子密钥在加密和解密过程的不同轮中使用。 
现在，让我们考虑一种已知明文和相应密文的选择明文攻击场景。在这种情况下，攻击者可以尝试不同的密钥，看看是否有任何密钥可以将已知的密文转换为已知的明文。  
由于S-DES的密钥长度有限（10位），存在多个密钥可能会为特定明文产生相同的密文的可能性。这是因为密钥空间（所有可能的密钥）相对较小，增加了密钥冲突的机会。  
然而，需要注意的是，S-DES算法的设计旨在具有相对较低的密钥冲突概率。S-DES中的特定置换和替代操作旨在最小化这种冲突的发生。虽然理论上可能存在冲突，但在实践中，这种情况非常罕见。 
总结起来，在S-DES中，对于给定的明文，有可能存在多个密钥产生相同的密文，但由于算法的设计，这种情况很少发生。
'''