import json
import paddle


t = paddle.randn(shape=[64,208])

with open('dataset/word_tree.json', 'r') as f:
    word_tree = json.load(f)

# print(word_tree)
class_index = [eval(index) for index in word_tree.keys()]
t_T = t.T
t_transpose = t.transpose([1, 0])
print(t_T)
print(t_transpose)
print(t_T.shape)
print(t_T == t_transpose)


# np_t = t.numpy()
# np_t[:, class_index]
# print(cycles)