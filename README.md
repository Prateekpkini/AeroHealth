# 🍃 AeroHealth: Autonomous Multi-Agent Healthcare Ecosystem

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Edge AI](https://img.shields.io/badge/Deployment-Edge_Native-success.svg)](#)

**Prana-Edge** is a decentralized, multi-agent healthcare orchestration platform designed to operate flawlessly in low-connectivity environments. By combining specialized AI agents with edge computing, it provides an autonomous, privacy-first "Digital Front Door" for rural clinics and high-volume hospitals.

---

## 📖 Table of Contents
- [The Problem](#-the-problem)
- [Our Solution](#-our-solution)
- [Core Features](#-core-features)
- [Architecture & Tech Stack](#-architecture--tech-stack)
- [Getting Started (Local Development)](#-getting-started)
- [API Endpoints](#-api-endpoints)
- [Roadmap](#-roadmap)
- [License & Contact](#-license)

---

## 🚨 The Problem: The "Triple Bottleneck"
Current digital healthcare systems face three critical failures, particularly in the Indian ecosystem:
1. **Connectivity:** Cloud-only LLMs fail in rural areas with sporadic internet.
2. **Clinical Safety:** Monolithic chatbots suffer from hallucinations and cannot handle complex, multi-step surgical scheduling or specialized triage.
3. **Linguistic Exclusion:** Existing platforms cater primarily to English speakers, ignoring millions of vernacular speakers.

## 💡 Our Solution
Prana-Edge abandons the standard cloud-API chatbot model. We deploy a **Multi-Agent System (MAS)** directly onto local edge hardware (like a Raspberry Pi 5). These agents collaborate to securely intake patient symptoms, triage acuity, and schedule appointments entirely offline, syncing to central Electronic Health Records (EHRs) only when connectivity is restored.

---

## ✨ Core Features
* 🤖 **Multi-Agent Orchestration:** Specialized, restricted agents (Intake, Triage, Scheduling) collaborate to ensure zero clinical hallucinations.
* ⚡ **Edge-Native "Degraded Mode":** Core inference happens locally. If the internet drops, the system continues to triage and queues data in a secure SQLite offline buffer.
* 🌍 **Multilingual Pipeline:** Integrated with Bhashini for real-time vernacular Voice-to-Text, enabling patients to describe symptoms in their native language.
* 🍃 **Green AI Sustainability:** By offloading inference to 10W edge NPUs instead of 300W cloud GPUs, we reduce the carbon footprint per query by 96%.
* 🔐 **Interoperability Ready:** Designed to output FHIR-compliant bundles compatible with the Ayushman Bharat Digital Mission (ABDM).

---

## 🏗️ Architecture & Tech Stack

### Software Layer
* **Backend:** FastAPI (Python 3.10+)
* **Agent Framework:** CrewAI / LangGraph
* **LLM Core:** Configured for local quantized models (Ollama/Phi-3) with modular fallback to standard APIs (OpenAI/Azure).
* **Database:** Local SQLite (Edge Buffer) -> Syncs to Postgres (Cloud).

### Hardware Deployment Target
* Raspberry Pi 5 (8GB) + Hailo-8L NPU
* Medical Grade Vital Sensors (ESP32)

---

## 🚀 Getting Started

Follow these instructions to run the Prana-Edge MAS and FastAPI backend on your local machine.

### Prerequisites
* Python 3.10 or higher installed.
* API Key for your chosen LLM provider (until local Ollama deployment is configured).
