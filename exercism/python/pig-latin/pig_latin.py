def translate(text: str) -> str:
    vowels = {"a", "e", "i", "o", "u"}

    new_text = ""

    for word in text.split():
        if word[0] in vowels or word.startswith("xr") or word.startswith("yt"):
            word = word + "ay"

        # now starts with zero or more consonants.
        else:
            first_vowel_idx = -1
            for char in word:
                first_vowel_idx += 1
                if char in vowels:
                    break

            # ignore if no vowel, i.e first_vowel_idx == -1

            if (qu_index := word.find("qu")) != -1 and first_vowel_idx > qu_index:
                word = word[qu_index + 2 :] + word[:qu_index] + "quay"
            elif (y_index := word.find("y")) > 1 and first_vowel_idx > y_index:
                word = word[y_index:] + word[:y_index] + "ay"
            else:
                word = word[first_vowel_idx:] + word[:first_vowel_idx] + "ay"

        new_text = (new_text + " " + word).strip()

    return new_text
