from enpypher.cipher_machine import CipherMachine


class Railfence(CipherMachine):
    def _cipher(self, text: str, encipher: bool) -> str:
        N = self.input_key - 1
        rails = [[] for i in range(self.input_key)]
        for i in range(len(text)):
            rails[(i % N) if i // N % 2 == 0 else (N - (i % N))].append(i)

        # Idea for mapping from reddit users u/adrian17 and u/jetRink
        # https://www.reddit.com/r/dailyprogrammer/comments/2rnwzf/20150107_challenge_196_intermediate_rail_fence/
        mapping = {
            i: v for i, v in enumerate(i for rail in rails for i in rail)
        }
        if not encipher:
            mapping = {v: k for k, v in mapping.items()}

        new_text = [text[mapping[i]] for i in range(len(text))]

        return "".join(new_text)

    def set_key(self, key):
        self.input_key = key
