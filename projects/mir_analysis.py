import os
import json
from midi_util import MidiUtil
import pandas as pd

def batch_extract(input_dir: str, output_path: str):
    records = []
    for fn in os.listdir(input_dir):
        if fn.endswith('.mid'):
            pm = pretty_midi.PrettyMIDI(os.path.join(input_dir, fn))
            feats = MidiUtil.extract_mir_features(pm)
            feats['filename'] = fn
            records.append(feats)
    df = pd.DataFrame(records)
    df.to_csv(output_path, index=False)
    print(f"儲存 MIR 特徵至 {output_path}")
