#!/usr/bin/env bash
# Generate an animated 3D futuristic robot working from home.
#
# Uses inference.sh CLI with Google Gemini 3 Pro image generation.
#
# Prerequisites:
#   curl -fsSL https://cli.inference.sh | sh
#   infsh auth login
#
# Usage:
#   ./examples/generate_robot_wfh_infsh.sh

set -euo pipefail

OUTPUT_DIR="${OUTPUT_IMAGE_PATH:-$HOME/gen_image}"
FILENAME="futuristic_robot_working_from_home.png"
MODEL="google/gemini-3-pro-image-preview"

PROMPT='Create a stunning, Pixar-quality 3D animated render of a friendly futuristic robot working from home just like a human. The robot is sitting at a sleek wooden desk in a cozy, warmly-lit home office. It has a glowing soft-blue visor for eyes, smooth rounded metallic-white body panels with subtle chrome accents, and articulated humanoid hands typing on a slim holographic keyboard. A steaming mug of coffee sits beside the keyboard with a small heart-shaped steam wisp. The robot is wearing tiny over-ear headphones and a miniature hoodie draped casually over its shoulders. Behind the robot is a large window showing a futuristic cityscape at golden hour with flying vehicles, neon-lit skyscrapers, and a soft sunset gradient sky. The desk has a small potted succulent, a framed photo of another robot, and a desk lamp with warm ambient glow. A cat-shaped mini robot companion is curled up sleeping on the corner of the desk. Pixar animation style, soft global illumination, warm inviting color palette, shallow depth of field. Do not include any text, words, letters, or written characters anywhere in the image.'

if ! command -v infsh &>/dev/null; then
  echo "ERROR: infsh CLI not found. Install it with:"
  echo "  curl -fsSL https://cli.inference.sh | sh"
  exit 1
fi

mkdir -p "$OUTPUT_DIR"

echo "Generating image with $MODEL ..."
infsh app run "$MODEL" --input "{\"prompt\": \"$PROMPT\"}" --output "$OUTPUT_DIR/$FILENAME"

echo "Image saved to $OUTPUT_DIR/$FILENAME"
