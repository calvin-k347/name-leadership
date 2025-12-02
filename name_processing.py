import pronouncing
from g2p_en import G2p
g2p = G2p()
vowels = {
    "AA", "AE", "AH", "AO", "AW", "AY",
    "EH", "ER", "EY",
    "IH", "IY",
    "OW", "OY",
    "UH", "UW"
}
nasals = {"M", "N", "NG"}
glides_approx = {"W", "Y", "L", "R"}
affricates = {"CH", "JH"}
diphthongs = {"AW","AY","EY","OW","OY"}
fricatives = {"F", "V", "TH", "DH", "S", "Z", "SH", "ZH", "HH"}
stops = {"P", "B", "T", "D", "K", "G"}
def find_first_vowel(phonemes_as_list):
    for phoneme in phonemes_as_list:
        if phoneme[0:2] in vowels:
            return phoneme[0:2]
    return "NAME ERROR"
def vowel_ratio(phonemes_as_list):
    vowel_count = 0
    for phoneme in phonemes_as_list:
        if phoneme[0:2] in vowels:
            vowel_count +=1
    return len(phonemes_as_list) / vowel_count
def annotate_name(name):
    cmu_phonemes = pronouncing.phones_for_word(name)
    if not cmu_phonemes:
        phonemes_as_list = [p.upper() for p in g2p(name)]
        phonemes = " ".join(phonemes_as_list)
    else:
        phonemes = cmu_phonemes[0]
    phonemes_as_list = phonemes.split()
    stress = pronouncing.stresses(phonemes)
    num_syllables = pronouncing.syllable_count(phonemes)
    ends_in_vowel = 1 if phonemes_as_list[len(phonemes_as_list)-1][0:2] in vowels else 0
    first_vowel = find_first_vowel(phonemes_as_list)
    v_ratio = vowel_ratio(phonemes_as_list)
    count_glides = sum(p in glides_approx for p in phonemes_as_list)
    count_nasals = sum(p in nasals for p in phonemes_as_list)
    count_affricates = sum(p in affricates for p in phonemes_as_list)
    count_fricatives = sum(p in fricatives for p in phonemes_as_list)
    count_stops = sum(p in stops for p in phonemes_as_list)
    count_consonants = -1 if sum(len(p) < 3 for p in phonemes_as_list) == 0 else sum(len(p) < 3 for p in phonemes_as_list)

    if first_vowel == "NAME ERROR":
        return "NAME ERROR"
    return {"stress": stress, 
            "syll_count": num_syllables, 
            "ends_in_vowel": ends_in_vowel, 
            "initial_vowel": first_vowel,
            "vowel_ratio": v_ratio ,
            "consonants": count_consonants,
            "glides": count_glides,
            "nasals": count_nasals,
            "affricates": count_affricates,
            "fricitives": count_fricatives,
            "stops": count_stops,
            "glides_r": count_glides / count_consonants,
            "nasals_r": count_nasals / count_consonants,
            "affricates_r": count_affricates / count_consonants,
            "fricitives_r": count_fricatives / count_consonants,
            "stops_r": count_stops / count_consonants,
            "pronouncation": phonemes}
