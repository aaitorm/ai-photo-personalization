# AI Photo Personalization with Diffusion Models

End-to-end system for generating personalized images using fine-tuned diffusion models and a FastAPI backend.

---

## Overview

This project implements a system that generates personalized images of a specific subject in different contexts (e.g., superhero, pilot, beach scenes).

The system combines diffusion model fine-tuning with prompt-based generation and a backend API for controlled usage.

---

## Identity Conditioning

The model is trained to associate a special token (e.g., `TOK`) with a specific subject identity.

During inference, prompts including this token generate images of that subject:

Example:
"A portrait of TOK as a superhero"

This enables controlled personalization without modifying the model architecture.

---

## System Architecture

The system follows this pipeline:

1. Collect images of a subject
2. Fine-tune a diffusion model (via Replicate)
3. Generate images using prompt conditioning
4. Handle requests through a FastAPI backend
5. Control usage with rate limiting (Upstash Redis)

---

## Results

Examples of generated images using personalized prompts:

![example1](results/example1.png)
![example2](results/example2.png)
![example3](results/example3.png)

---

## Tech Stack

**Core**
- Python
- FastAPI

**ML & Generative AI**
- Diffusion models
- Replicate API

**Infrastructure**
- Upstash (Redis)
- Async API handling

---

## Repository Structure

- `src/` → backend and API logic
- `nbs/` → experimentation and development notebooks
- `data/references/` → visual reference images for style/context
- `results/` → generated outputs
- `requirements.txt` → dependencies

---

## Notes

This project was initially inspired by an online tutorial, but extended with backend integration, API usage control, and structured system design.

---

## Future Improvements

- Add web interface for user interaction
- Support multiple identities
- Improve prompt controllability
- Optimize fine-tuning workflow
