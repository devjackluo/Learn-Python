import pickle


# example_dict = {1:'ff2',2:'fr23',3:'f2g4g'}
# pickle_out = open('dict.pickle', 'wb')
# pickle.dump(example_dict, pickle_out)
# pickle_out.close()

pickle_in = open('dict.pickle', 'rb')
example_dict = pickle.load(pickle_in)

print(example_dict)
print(example_dict[2])




