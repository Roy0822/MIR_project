import os
from musicagent.agent import MusicAgent
from musecoco.client import MuseCocoClient

class MIRAgent:
    def __init__(self, api_key: str, model_name: str="musecoco/melody-large"):
        self.agent = MusicAgent(api_key=api_key, model_name=model_name)
        self.client = MuseCocoClient(api_key=api_key, model_name=model_name)

    def generate_melody_tokens(self, prompt: str, length: int=64) -> list:
        # 直接呼叫 Muzic 原有 MusicAgent 內部的 generate_melody
        tokens = self.agent.client.generate_melody(prompt=prompt, length=length)
        return tokens
