"""Tests for LLMOps."""
import pytest
from src.llmops import LLMOps

def test_init():
    obj = LLMOps()
    stats = obj.get_stats()
    assert stats["total_ops"] == 0

def test_operation():
    obj = LLMOps()
    result = obj.version_prompt(input="test")
    assert result["processed"] is True
    assert result["operation"] == "version_prompt"

def test_multiple_ops():
    obj = LLMOps()
    for m in ['version_prompt', 'diff_prompts', 'evaluate_prompt']:
        getattr(obj, m)(data="test")
    assert obj.get_stats()["total_ops"] == 3

def test_caching():
    obj = LLMOps()
    r1 = obj.version_prompt(key="same")
    r2 = obj.version_prompt(key="same")
    assert r2.get("cached") is True

def test_reset():
    obj = LLMOps()
    obj.version_prompt()
    obj.reset()
    assert obj.get_stats()["total_ops"] == 0

def test_stats():
    obj = LLMOps()
    obj.version_prompt(x=1)
    obj.diff_prompts(y=2)
    stats = obj.get_stats()
    assert stats["total_ops"] == 2
    assert "ops_by_type" in stats
