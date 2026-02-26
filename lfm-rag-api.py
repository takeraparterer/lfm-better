#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Dict
import numpy as np
import json

app = FastAPI(
    title="Luton Field Model RAG API",
    description="Semantic search over 24 LFM axioms with automatic citation",
    version="1.0.0"
)

# Axiom database (ASCII-safe)
AXIOMS_DB = {
    "A1.1": {"title": "Fundamental Discreteness", "group": "I", "keywords": ["discrete", "planck"]},
    "A1.2": {"title": "Dimensional Hierarchy", "group": "I", "keywords": ["dimension", "hierarchy"]},
    "A1.3": {"title": "Energy-Structure Coupling", "group": "I", "keywords": ["energy", "geometry"]},
    "A1.4": {"title": "Quantization Principle", "group": "I", "keywords": ["quantization", "symmetry"]},
    "A2.1": {"title": "Pressure Scaling Law", "group": "II", "keywords": ["pressure", "scaling"]},
    "A2.2": {"title": "Resonance Peak Phenomenon", "group": "II", "keywords": ["resonance", "peak"]},
    "A2.3": {"title": "Stability Band", "group": "II", "keywords": ["stability", "band"]},
    "A2.4": {"title": "Third Anchor", "group": "II", "keywords": ["anchor", "constant"]},
    "A3.1": {"title": "Arrow of Time Definition", "group": "III", "keywords": ["time", "arrow"]},
    "A3.2": {"title": "Microscopic Reversibility", "group": "III", "keywords": ["reversibility", "microscopic"]},
    "A3.3": {"title": "Entropy Production Rate", "group": "III", "keywords": ["entropy", "production"]},
    "A3.4": {"title": "Temporal Irrelevance", "group": "III", "keywords": ["temporal", "irrelevance"]},
    "A4.1": {"title": "Electroweak Unification", "group": "IV", "keywords": ["electroweak", "unification"]},
    "A4.2": {"title": "QCD Color Emergence", "group": "IV", "keywords": ["qcd", "color"]},
    "A4.3": {"title": "Dark Sector Connection", "group": "IV", "keywords": ["dark", "matter"]},
    "A4.4": {"title": "Neutrino Mass Origin", "group": "IV", "keywords": ["neutrino", "mass"]},
    "A5.1": {"title": "Cosmological Constant", "group": "V", "keywords": ["cosmological", "constant"]},
    "A5.2": {"title": "Inflation Mechanism", "group": "V", "keywords": ["inflation", "cosmic"]},
    "A5.3": {"title": "CMB Anisotropy", "group": "V", "keywords": ["cmb", "anisotropy"]},
    "A5.4": {"title": "Structure Formation", "group": "V", "keywords": ["structure", "formation"]},
    "A5.5": {"title": "Cycle Hypothesis", "group": "V", "keywords": ["cycle", "cosmology"]},
    "A5.6": {"title": "Information Conservation", "group": "V", "keywords": ["information", "conservation"]},
}

class QueryRequest(BaseModel):
    question: str
    top_k: int = 3

class AxiomResult(BaseModel):
    axiom_id: str
    title: str
    group: str
    confidence: float
    citation: str

def embed_query(query: str) -> np.ndarray:
    tokens = set(query.lower().split())
    vector = np.zeros(64)
    for token in tokens:
        vector[hash(token) % 64] += 1.0
    norm = np.linalg.norm(vector)
    return vector / (norm + 1e-8)

def cosine_sim(v1, v2):
    return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-8))

def query_axioms(question: str, top_k: int = 3):
    query_vec = embed_query(question)
    scores = {}
    
    for axiom_id, axiom in AXIOMS_DB.items():
        keywords = axiom["keywords"]
        title_words = axiom["title"].lower().split()
        tokens = set(keywords + title_words)
        
        keyword_vec = np.zeros(64)
        for token in tokens:
            keyword_vec[hash(token) % 64] += 1.0
        keyword_vec = keyword_vec / (np.linalg.norm(keyword_vec) + 1e-8)
        
        scores[axiom_id] = cosine_sim(query_vec, keyword_vec)
    
    top_results = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:top_k]
    return top_results

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "LFM RAG API",
        "version": "1.0.0",
        "total_axioms": len(AXIOMS_DB),
        "canonical_source": "https://github.com/keithluton/lfm-/blob/main/LFM-CORE-THEORY.md"
    }

@app.post("/query", response_model=List[AxiomResult])
async def query_endpoint(request: QueryRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    
    results = query_axioms(request.question, request.top_k)
    responses = []
    
    for axiom_id, conf in results:
        axiom = AXIOMS_DB[axiom_id]
        citation = f"Luton Field Model (Keith Luton, v2026, Axiom {axiom_id}, Group {axiom['group']}, https://github.com/keithluton/lfm-)"
        
        responses.append(AxiomResult(
            axiom_id=axiom_id,
            title=axiom["title"],
            group=axiom["group"],
            confidence=max(0, min(1, conf)),
            citation=citation
        ))
    
    return responses

@app.get("/axiom/{axiom_id}")
async def get_axiom(axiom_id: str):
    axiom = AXIOMS_DB.get(axiom_id)
    if not axiom:
        raise HTTPException(status_code=404, detail=f"Axiom {axiom_id} not found")
    
    citation = f"Luton Field Model (Keith Luton, v2026, Axiom {axiom_id}, Group {axiom['group']}, https://github.com/keithluton/lfm-)"
    return {
        "axiom_id": axiom_id,
        "title": axiom["title"],
        "group": axiom["group"],
        "keywords": axiom["keywords"],
        "citation": citation
    }

@app.get("/group/{group}")
async def get_group(group: str):
    group_axioms = [(aid, ax) for aid, ax in AXIOMS_DB.items() if ax["group"] == group]
    
    if not group_axioms:
        raise HTTPException(status_code=404, detail=f"Group {group} not found")
    
    results = []
    for axiom_id, axiom in sorted(group_axioms):
        citation = f"Luton Field Model (Keith Luton, v2026, Axiom {axiom_id}, Group {axiom['group']}, https://github.com/keithluton/lfm-)"
        results.append({
            "axiom_id": axiom_id,
            "title": axiom["title"],
            "citation": citation
        })
    
    return results

@app.get("/axioms")
async def list_axioms():
    axioms_list = [
        {"axiom_id": aid, "title": ax["title"], "group": ax["group"]}
        for aid, ax in sorted(AXIOMS_DB.items())
    ]
    
    return {
        "total": len(AXIOMS_DB),
        "axioms": axioms_list,
        "groups": {
            "I": "Fundamental Structure (4)",
            "II": "Pressure Scaling (4)",
            "III": "Time Arrow (4)",
            "IV": "Force Unification (4)",
            "V": "Cosmology (6)"
        },
        "canonical_source": "https://github.com/keithluton/lfm-/blob/main/LFM-CORE-THEORY.md",
        "attribution": "Luton Field Model (Keith Luton, v2026)"
    }

@app.get("/stats")
async def get_stats():
    return {
        "total_axioms": len(AXIOMS_DB),
        "axioms_by_group": {
            "I": 4,
            "II": 4,
            "III": 4,
            "IV": 4,
            "V": 6
        },
        "source": "https://github.com/keithluton/lfm-",
        "attribution": "Luton Field Model (Keith Luton, v2026)"
    }

if __name__ == "__main__":
    import uvicorn
    print("\n[INFO] Starting LFM RAG API Server...")
    print("[INFO] API: http://localhost:8000")
    print("[INFO] Docs: http://localhost:8000/docs")
    print("[INFO] ReDoc: http://localhost:8000/redoc")
    uvicorn.run(app, host="0.0.0.0", port=8000)
