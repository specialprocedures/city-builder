# %%
from diffusers import StableDiffusionXLPipeline
import torch

pipeline = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16,
    variant="fp16",
    use_safetensors=True,
)

pipeline.enable_model_cpu_offload(gpu_id=0)


# %%
prompt = """
The Chasm of Shadows has inspired a range of creative endeavors throughout Tenebrous, from street art to subversive literature. Its influence can be seen in various musical genres, including hip hop, electronic, and experimental music, which often incorporate themes of social critique and technological experimentation.

Moreover, the Chasm of Shadows has become a cultural touchstone for Tenebrous's residents, representing their collective defiance against the city's oppressive forces. The space has also attracted attention from international media outlets, further solidifying its reputation as a hub for underground culture and revolutionary activism.
"""

image = pipeline(prompt=prompt, num_inference_steps=50, height=1024, width=1024).images[
    0
]
image
