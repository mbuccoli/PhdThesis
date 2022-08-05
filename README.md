# Linking signal and semantic representations of musical content for music information retrieval
PhD Thesis by [Michele Buccoli](https://mbuccoli.github.io), defended in February 2017. You can also download it [here](https://www.politesi.polimi.it/handle/10589/132057).
## Cite
```
@phdthesis{buccoli2017linking,
  title={Linking signal and semantic representations of musical content for music information retrieval},
  author={Buccoli, Michele},
  year={2017},
  school= {Politecnico di Milano},
  month = {2},
  publisher={Politecnico di Milano},
  address      = {Piazza Leonardo da Vinci, 32, 20133, Milan, Italy},
}
```
## Keywords
music information retrieval; deep learning; machine learning; signal processing; semantic model; natural language processing

## Abstract 
In recent years, the evolution of technology and connectivity has led to a major revolution in the music industry, which has led to novel content consumption scenarios. People, in fact, are suddenly given the possibility to easily access millions of songs through multiple browsing/diffusion/streaming platforms and are therefore in need of new navigational/browsing tools, music recommendation assistants, virtual clerks, etc. Music Information Retrieval (MIR) is a multi-disciplinary research field that addresses the issues raised by the design of search/navigation/annotation strategies, in order to develop those tools, like content classification and rich annotation algorithms, that are required to support such scenarios. The design of tools and applications for MIR-related scenarios requires us to model and account for two different levels of abstraction in the musical content description: the semantic level and the signal-based level. The former concerns how we subjectively perceive and interpret the musical properties, which terms we choose to describe them and how we use such terms to discuss about music. The latter involves nailing down the objective properties of the musical signals, ranging from those that can be directly computed from the signal to those that can be inferred from it, such as the rhythmic, tonal, etc. Such two description levels, however, are very separated from each other, which is why MIR research today is focusing exactly on bridging this critical gap. In order to develop MIR applications, the modern approaches must take into account all abstraction levels in the description of musical content. This means that, in addition to considering the signal domain and the semantic domain, such approaches focus on the linking function between them. In this work we follow a schema that involves the formalization of the signal and the semantic domains, as well as the design of the related linking function. The thesis begins with the discussion of the possible formalization of the signal domain based on the extraction of a feature representation of the musical content. This formalization requires a deep knowledge of the musical properties and the features that are able to capture them. As part of this formalization process, we show an example of application of feature-based analysis which is suitable for the scenario of Networked Music Performance. Through this scenario we show how to estimate some of the musical properties that appear to have an impact on the overall quality of the networked performance experience. We also discuss how deep learning techniques are suitable for automatically extracting (or learning) an effective feature representation of the musical content. We first describe how to design the linking function by means of rule-based techniques, which follow a manually-designed algorithm. More often, however, the link between the two domains is not clear and it is hard to design it by means of a procedural solution. In such cases, we show how to use machine learning techniques to automatically learn and predict the relation between the two domains. The semantic domain can be instead formalized following two main approaches: the categorical approach, that defines which descriptors are feasible to represent a given song; and the dimensional approach, that also specifies how much the aforementioned descriptors represent the given song. The set of semantic descriptors can be extended by including a semantic similarity among them, either manually-defined or automatically-inferred; the resulting set of semantic descriptors and similarities is referred to as semantic model. In this regard, we conduct a specific research activity to enrich a manually-defined generic dataset of dimensional descriptors with music-specific information automatically inferred from users' annotations. We also consider the structure of songs as a special case of formalization of the semantic domain. After the main components are defined and formalized, we apply the schema to a number of MIR-related application scenarios of gradually increasing complexity. The first application scenario involves the analysis and extraction of the song's structure. We rely on deep learning techniques to automatically extract a feature-based representation of the signal domain. By doing so, we address the uncertainty issue about which properties are suitable for describing the musical content for the task of musical structure analysis. Since the semantic domain is well formalized, we are able to apply rule-based techniques from the MIR literature to retrieve the structure. In the second application scenario, we address the detection of bootlegs, i.e., unauthorized recordings of live performances. We formalize the semantic domain by following the categorical approach, which consists of describing a given song as either a bootleg, or an official live performance, or a studio recording. We employ learned features to formalize the signal domain and machine learning techniques to tackle the complexity of the definition of the linking function. The third application scenario concerns the automatic annotation of the recording of violins with their timbral qualities. The timbral properties of violins are described by rather imprecise semantics, which we formalize through of a set of six dimensional descriptors. Albeit the number of employed descriptors is rather limited, the adoption of a dimensional approach helps us increase the expressiveness of this semantic model. As done in the previous application scenarios, we employ learned features to address the uncertainty in the formalization of the signal domain and machine learning techniques to automatically design the linking function and ultimately assess the timbral qualities of the instrument. In the last scenario we address the definition of a semantic model by considering the ambiguities that commonly occur in natural language. We investigate a formalization of the semantic domain that is able to address the ambiguity issues raised by polysemy, which occurs when descriptors take on different meanings when used within different semantic contexts. We embed the defined semantic model (which is based on overlapping semantic contexts and on context-dependent semantic similarities) in a prototype of music search engine. This prototype represents a novel application that allows users to retrieve musical content by using natural language queries.

## Related articles
The publications relative to the work presented in the thesis are listed in the following.
### Peer-reviewed journal papers
* Cristina Emma Margherita Rottondi, Michele Buccoli, Massimiliano Zanoni, Dario Garao, Giacomo Verticale, Augusto Sarti, _Feature-Based Analysis of the Effects of Packet Delay on Networked Musical Interactions_, in Journal of the Audio Engineering Society 63 (11), 864-875, November 2015.	

### Peer-reviewed conference proceedings
* Michele Buccoli; Davide Andreoletti; Massimiliano Zanoni; Augusto Sarti; Stefano Tubaro, _Unsupervised feature learning for Music Structural Analysis_, in Proceedings of 24th European Signal Processing Conference (EUSIPCO), Budapest, Hungary, August 2016;
* Michele Buccoli, Massimiliano Zanoni, Gy\"orgy Fazekas, Augusto Sarti, Mark Sandler and Stefano Tubaro, _A higher-dimensional expansion of affective norms for English terms for music tagging_, in Proceedings of 17th International Society for Music Information Retrieval Conference (ISMIR), New York City, USA, August 2016;
* Michele Buccoli, Massimiliano Zanoni, Francesco Setragno, Augusto Sarti, Fabio Antonacci, _An Unsupervised Approach To The Semantic Description Of The Sound Quality Of Violins_, in Proceedings of 23rd European Signal Processing Conference (EUSIPCO), Nice, France, August 2015;
* Michele Buccoli, Alessandro Gallo, Massimiliano Zanoni, Augusto Sarti, Stefano Tubaro, _A Dimensional Contextual Semantic Model For Music Description And Retrieval_, in Proceedings of IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Brisbane, Australia, 2015;
* Michele Buccoli, Paolo Bestagini, Massimiliano Zanoni, Augusto Sarti, Stefano Tubaro, _Unsupervised Feature Learning For Bootleg Detection Using Deep Learning Architectures_, in Proceedings of IEEE International Workshop on Information Forensics and Security (WIFS), Atlanta, USA, December 2014
