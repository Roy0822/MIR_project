import os
from agent import MIRAgent
from midi_util import MidiUtil
from mir_analysis import batch_extract

def run_pipeline():
    api_key = os.getenv("MUSE_COCO_API_KEY", "MY_API_KEY(hidden)")
    agent = MIRAgent(api_key)
    prompts = ["Romantic Piano Solo", "Sci-fi element", "Jazz Fusion", "Classical Symphony", "Folk Melody"]

    out_dir = "output_midis"
    os.makedirs(out_dir, exist_ok=True)

    for prompt in prompts:
        tokens = agent.generate_melody_tokens(prompt, length=64)
        pm = MidiUtil.tokens_to_midi(tokens)
        fn = os.path.join(out_dir, f"{prompt.replace(' ','_')}.mid")
        MidiUtil.save_midi(pm, fn)
        print(f"已生成 MIDI：{fn}")

    # 批次提取 MIR 特徵
    batch_extract(out_dir, "mir_features.csv")

if __name__=="__main__":
    run_pipeline()
