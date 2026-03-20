#!/usr/bin/env python3
"""
Generate an animated 3D futuristic robot working from home like a human.

Uses Google's Gemini API with the gemini-3.1-flash-image-preview model.

Usage:
    export GEMINI_API_KEY="your-api-key"
    python examples/generate_robot_wfh.py

The generated image will be saved to ~/gen_image/ (or OUTPUT_IMAGE_PATH).
"""

import os
import sys
from io import BytesIO

import PIL.Image
from google import genai

# ---------------------------------------------------------------------------
# Detailed prompt crafted for a high-quality 3D animated robot scene
# ---------------------------------------------------------------------------

ROBOT_WFH_PROMPT = """
Create a stunning, Pixar-quality 3D animated render of a friendly futuristic
robot working from home just like a human.

SCENE DETAILS:
- The robot is sitting at a sleek wooden desk in a cozy, warmly-lit home office.
- It has a glowing soft-blue visor for eyes, smooth rounded metallic-white body
  panels with subtle chrome accents, and articulated humanoid hands typing on a
  slim holographic keyboard.
- One hand rests on a futuristic translucent mouse.
- A steaming mug of coffee sits beside the keyboard — the mug has a small
  heart-shaped steam wisp rising from it.
- The robot is wearing a tiny pair of over-ear headphones and a miniature
  hoodie draped casually over its shoulders, giving it a relaxed human vibe.

ENVIRONMENT:
- Behind the robot is a large window showing a futuristic cityscape at golden
  hour — flying vehicles in the distance, neon-lit skyscrapers, soft sunset
  gradient sky (peach, lavender, soft orange).
- The desk has a small potted succulent, a framed photo of another robot (its
  family), and a desk lamp with warm ambient glow.
- A cat-shaped mini robot companion is curled up sleeping on the corner of the
  desk.
- The floor is light hardwood; a cozy rug is partially visible.

STYLE & MOOD:
- Pixar / DreamWorks 3D animation style — soft global illumination, subsurface
  scattering on translucent parts, depth of field with the background slightly
  blurred.
- Warm, inviting color palette: teal and white robot against warm amber room
  lighting.
- The mood is calm, productive, and wholesome — a slice-of-life moment
  capturing a robot living its best work-from-home life.
- The image should feel like a still frame from an animated short film.

CAMERA:
- Slightly low-angle, three-quarter view, the robot is centered in frame.
- Shallow depth of field — robot and desk sharp, background softly blurred.

IMPORTANT: Do not include any text, words, letters, or written characters
anywhere in the image.
"""

OUTPUT_DIR = os.getenv("OUTPUT_IMAGE_PATH") or os.path.expanduser("~/gen_image")
FILENAME = "futuristic_robot_working_from_home"


def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: Set the GEMINI_API_KEY environment variable first.")
        sys.exit(1)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    client = genai.Client(api_key=api_key)
    model = "gemini-3.1-flash-image-preview"

    print(f"Generating image with model {model} ...")

    response = client.models.generate_content(
        model=model,
        contents=[ROBOT_WFH_PROMPT],
    )

    # Extract and save the image
    out_path = os.path.join(OUTPUT_DIR, f"{FILENAME}.png")
    for part in response.candidates[0].content.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            image = PIL.Image.open(BytesIO(part.inline_data.data))
            image.save(out_path)
            print(f"Image saved to {out_path}")
            return out_path

    print("ERROR: No image data returned by Gemini.")
    sys.exit(1)


if __name__ == "__main__":
    main()
