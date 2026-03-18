"""Tests for LlmOpsPlatform."""
from src.core import LlmOpsPlatform
def test_init(): assert LlmOpsPlatform().get_stats()["ops"] == 0
def test_op(): c = LlmOpsPlatform(); c.detect(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = LlmOpsPlatform(); [c.detect() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = LlmOpsPlatform(); c.detect(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = LlmOpsPlatform(); r = c.detect(); assert r["service"] == "llm-ops-platform"
