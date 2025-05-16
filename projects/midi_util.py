import pretty_midi
import numpy as np

class MidiUtil:
    @staticmethod
    def tokens_to_midi(tokens: list, program: int=0, tempo: float=120.0) -> pretty_midi.PrettyMIDI:
        pm = pretty_midi.PrettyMIDI(initial_tempo=tempo)
        inst = pretty_midi.Instrument(program=program)
        time, step = 0.0, 60.0/tempo/2
        for p in tokens:
            note = pretty_midi.Note(velocity=100, pitch=p, start=time, end=time+step)
            inst.notes.append(note)
            time += step
        pm.instruments.append(inst)
        return pm

    @staticmethod
    def save_midi(pm: pretty_midi.PrettyMIDI, path: str):
        pm.write(path)

    @staticmethod
    def extract_mir_features(pm: pretty_midi.PrettyMIDI) -> dict:
        """
        提取基本 MIR 特徵：chroma、節拍、音高分類直方圖
        """
        features = {}
        # 1. Chroma (12維)
        chroma = pm.get_chroma()  #pretty_midi 的 get_chroma 方法:contentReference[oaicite:3]{index=3}
        features['chroma_mean'] = np.mean(chroma, axis=1).tolist()
        # 2. 節拍位置 (beats)
        features['beats'] = pm.get_beats().tolist()
        # 3. 音高分類直方圖
        pitches = [n.pitch for inst in pm.instruments for n in inst.notes]
        hist, _ = np.histogram(pitches, bins=range(0,129))
        features['pitch_histogram'] = hist.tolist()
        return features
