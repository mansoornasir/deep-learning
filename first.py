import tensorflow as tf

#node1 = tf.constant(3.0, tf.float32)
#node2 = tf.constant(4.0)

#sess = tf.Session()

# print(sess.run([node1, node2]))

# sess.close()


#with tf.Session() as sess:
#    output = sess.run([node1, node2])
#    print(output)

#a = tf.constant(5.0)
#b = tf.constant(6.0)

#c = a * b

#sess = tf.Session()

#File_Writer = tf.summary.FileWriter('D:\\tensorflow\graph', sess.graph)

#print (sess.run(c))

#sess.close()


# variables, placeholders and constants

# placeholders

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

adder_node = a + b

sess = tf.Session()
File_Writer = tf.summary.FileWriter('D:\\tensorflow\graph', sess.graph)
print (sess.run(adder_node, {a: [1,3], b: [3,4] }))