import os
import conllu

PATH_CONLLU_FOLDER_TO_MERGE = "/home/wran/Projects/arborator/treebanks/SUD_Naija-NSC/"
PATH_MERGED_CONLLU = "./naija_merged.conllu"

conllus_files = [file for file in os.listdir(PATH_CONLLU_FOLDER_TO_MERGE) if file.endswith(".conllu")]

merged_conllu = ""
i = 0
for conllu_file in conllus_files:
    i += 1
    path_conllu = os.path.join(PATH_CONLLU_FOLDER_TO_MERGE, conllu_file)
    with open(path_conllu, "r", encoding="utf-8") as infile:
        conllu_text = infile.read()
    merged_conllu += conllu_text + "\n"

with open(PATH_MERGED_CONLLU, "w", encoding="utf-8") as outfile:
    outfile.write(merged_conllu)


print("done", i)
