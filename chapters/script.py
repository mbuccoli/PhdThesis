import os

chapters=[('Conclusions','Chap:Concl'),\
		  ('The signal domain','Chap:LLFs'),\
		  ('The Semantic Codomain','Chap:HLFs'),\
		  ('Networked Music Performance','Chap:NMP'),\
		  ('Music Structure Analysis','Chap:MSA'),\
		  ('Bootleg Detection','Chap:Bootleg'),\
		  ('Valence-Arousal Anew','Chap:ANEW'),\
		  ('Violin Timbre Annotation','Chap:Violin'),\
		  ('Dimensional Contextual Semantic Model','Chap:DCSM'),\
		  ('WhoLoDance','Chap:Wholodance'),\
		  ('Mood Segmentation','Chap:MoodSegm'),\
]

with open('chapter.tex','r') as f:
	content=f.read()

for chap in chapters:
	namefile=chap[1].split(':')[1]
	chap_content=content.replace('title',chap[0]).replace('ref_label',chap[1])
	with open(namefile+'.tex','w') as f:
		f.write(chap_content)

	#print('\\input{chapters/%s}'%namefile)
	print('\\ref{%s}'%chap[1])