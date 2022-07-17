import pywhatkit as pw
txt = """Republic of Bangladesh, is a country in South Asia. 
It is the eighth-most populous country in the world, with a population exceeding 163 million people in an area of either 148,460 square kilometres (57,320 sq mi) or 147,570 square kilometres (56,980 sq mi),[7][15] making it one of the most densely populated countries in the world. 
Bangladesh shares land borders with India to the west, north, and east, and Myanmar to the southeast; to the south it has a coastline along the Bay of Bengal. 
It is narrowly separated from Nepal and Bhutan by the Siliguri Corridor; and from China by 100 km of the Indian state of Sikkim in the north.
 Dhaka, the capital and largest city, is the nation's economic, political, and cultural hub."""
pw.text_to_handwriting(txt,'handWrite.png',[0,0,1,130])
print('Bye')