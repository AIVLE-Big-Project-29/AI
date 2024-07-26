import base64
import os
import requests

engine_id = "stable-diffusion-v1-6"
api_host = os.getenv("API_HOST", "https://api.stability.ai")
api_key = os.getenv("STABILITY_API_KEY")

if api_key is None:
    raise Exception("Missing Stability API key.")

response = requests.post(
    f"{api_host}/v1/generation/{engine_id}/image-to-image",
    headers={
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    },
    files={
        "init_image": open("./imgs/before.png", "rb")   # 이부분이 받는 이미지로 바뀌어야하고
    },
    data={
        "image_strength": 0.45,         # 이미지 강도 기본 값 0.35
        "init_image_mode": "IMAGE_STRENGTH",
        "text_prompts[0][text]": "Create a detailed aerial view of an urban forest within a city. The image should depict a modern cityscape with a mix of tall buildings and residential areas, surrounded by lush, green trees and well-maintained parks. Include walking paths, benches, and small water features like ponds or fountains. The urban forest should blend seamlessly with the city's architecture, providing a harmonious balance between nature and urban life. The overall atmosphere should be inviting and serene, showcasing the benefits of integrating green spaces into urban environments.",
        "cfg_scale": 7,     # 프롬프트 텍스트를 얼마나 준수하는지 기본값 7
        "samples": 1,       # 확산 과정에 사용할 샘플러, 생략시 자동으로 적절한 것 선택
        "steps": 50,        # 품질 10 ~ 50
        "style_preset": "3d-model",      # 이미지 모델을 특정 스타일로 안내하기 위해 스타일 사전 설정을 전달
        "clip_guidance_preset": "FAST_GREEN",   # 녹색톤 강조 FAST_GREEN / SLOWEST 느리지만 정확한 
    }
)

if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

data = response.json()

# 이부분을 바로 화면에 출력하게 해야하는데
for i, image in enumerate(data["artifacts"]):
    with open(f"./imgs/test{i}.png", "wb") as f:
        print(f.write(base64.b64decode(image["base64"]))) 