class RailFenceCipher:
    def __init__(self):
        pass
    def rail_fence_encrypt(self,plain_text,num_rails):
        rails =[[] for _ in range(num_rails)]
        rails_index = 0
        direction = 1
        for char in plain_text:
            rails[rails_index].append(char)
            if rails_index == 0:
                direction = 1
            elif rails_index == num_rails -1:
                direction = -1
            rails_index += direction
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text
    
    def rail_fence_decrypt(self,cipher_text,num_rails):
        rails_lengths = [0]*num_rails
        rails_index = 0
        direction = 1
        for _ in range(len(cipher_text)):
            rails_lengths[rails_index]+=1
            if rails_index == 0:
                direction = 1
            elif rails_index == num_rails -1:
                direction = -1
            rails_index += direction
        rails=[]
        start = 0
        for length in rails_lengths:
            rails.append(cipher_text[start:start+length])
            start+=length
        plain_text =""
        rails_index=0
        direction=1
        for _ in range (len(cipher_text)):
            plain_text += rails[rails_index][0]
            rails[rails_index] = rails[rails_index][1:]
            if rails_index == 0:
                direction = 1
            elif rails_index ==num_rails -1:
                direction = -1
            rails_index += direction
        return plain_text