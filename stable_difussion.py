import base64
import os
import requests

engine_id = "stable-diffusion-v1-6"
# stable-diffusion-v1-6
# stable-diffusion-xl-1024-v1-0
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
        "init_image": open("./imgs/before.png", "rb")
    },
    data={
        "image_strength": 0.50,         # 이미지 강도 기본 값 0.35
        "init_image_mode": "IMAGE_STRENGTH",
        "text_prompts[0][text]": "Keep existing photos, Recognition of roads and buildings, Plant ginkgo trees on the sidewalk along the road",
        "cfg_scale": 7,     # 프롬프트 텍스트를 얼마나 준수하는지 기본값 7
        "samples": 1,       # 확산 과정에 사용할 샘플러, 생략시 자동으로 적절한 것 선택
        "steps": 30,
        "style_preset": "photographic"      # 이미지 모델을 특정 스타일로 안내하기 위해 스타일 사전 설정을 전달
    }
)

if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

data = response.json()

for i, image in enumerate(data["artifacts"]):
    with open(f"./imgs/v1_img2img{i}.png", "wb") as f:
        f.write(base64.b64decode(image["base64"]))