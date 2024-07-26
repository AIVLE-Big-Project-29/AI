import replicate

image = open("../imgs/before.png", "rb")

input = {
    "prompt": "Leave the image as it is and plant ginkgo trees along the road in the image",
    "image": image,
}

output = replicate.run(
    "jyoung105/playground-v2.5:e9f13772a98366f2dc1cab993da27b5676a7d3cd4fc8d06753f09397a8cc01b9",
    input=input
)
print(output)
