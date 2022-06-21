import re
import unicodedata
from colorama import init, Fore, Back, Style
import time

ancilostomiase = {
    "Termo" : "Ancilostomíase",
    "Categoria" : "Termo médico/Doença",
    "Variação(ões) Denominativa(s)" : "Ancilostomose",
    "Variante(s) Popular(es)" :  "Amarelão, Marelão, Doença do Jeca Tatu",
    "Definição" : "Infecção intestinal causada por nematódeos cujos sintomas são palidez, tom amarelado da pele e anemia."
}

anus = {
    "Termo" : "Ânus",
    "Categoria" : "Termo médico/Anatomia",
    "Variação(ões) Denominativa(s)" : "Glândula anal, Esfíncter anal, Esfíncter",
    "Variante(s) Popular(es)" : "Cu, Fiofó, Toba, Boga",
    "Definição" : "Extremidade terminal do intestino grosso, por onde as fezes são expelidas."
}

articulacao = {
    "Termo" : "Articulação",
    "Categoria" : "Termo médico/Anatomia",
    "Variação(ões) Denominativa(s)" : "Junta, Junta, Juntas, Juntura",
    "Variante(s) Popular(es)" :  "Junta do Osso",
    "Definição" : "Junção ou articulação óssea, joelho."
}

ascite = {
    "Termo" : "Ascite",
    "Categoria" : "Termo médico/Doença",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "Barriga d'água",
    "Definição" : "Acúmulo de de líquido em região próxima ao estômago."
}

boca = {
    "Termo" : "Boca",
    "Categoria" : "Termo médico/Anatomia",
    "Variação(ões) Denominativa(s)" : "Cavidade Oral, Cavidade Bucal",
    "Variante(s) Popular(es)" :  "Beiço",
    "Definição" : "Contorno ovalado da parte externa da cavidade oral, boca."
}

camomila = {
    "Termo" : "Camomila",
    "Categoria" : "Termo médico/Medicina alternativa",
    "Variação(ões) Denominativa(s)" : "Macela-Fétida",
    "Variante(s) Popular(es)" : "Macela",
    "Definição" : "Planta amarga com propriedade medicinal, utilizada para infecções gástricas e intestinais."
}

conjuntivite = {
    "Termo" : "Conjuntivite",
    "Categoria" : "Termo médico/Doença",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "Dordói",
    "Definição" : "Doença similar a conjuntivite, inflamação nos olhos."
}

consternaçao = {
    "Termo" : "Consternação",
    "Categoria" : "Termo médico/Sintoma",
    "Variação(ões) Denominativa(s)" : "Lamentação, Tristeza",
    "Variante(s) Popular(es)" :  "Mocorongo",
    "Definição" : "Diz-se de quem apresenta tristeza e desânimo como sintoma de depressão."
}

constipacao_intestinal = {
    "Termo" : "Constipação Instestinal",
    "Categoria" : "Termo médico/Sintoma",
    "Variação(ões) Denominativa(s)" : "Obstipação, Prisão de Ventre",
    "Variante(s) Popular(es)" :  "Vento Igauzado",
    "Definição" : "Sintoma de prisão de ventre, retenção de gases."
}

debilidade_muscular = {
    "Termo" : "Debilidade Muscular",
    "Categoria" : "Termo médico/Doença",
    "Variação(ões) Denominativa(s)" : "Fraqueza Muscular",
    "Variante(s) Popular(es)" :  "Perrengue",
    "Definição" : "Estado debilitado por adoecimento ou mal-estar em função de alterações climáticas extremas ou do organismo humano."
}

dermatopatia = {
    "Termo" : "Dermatopatia",
    "Categoria" : "Termo médico/Sintoma",
    "Variação(ões) Denominativa(s)" : "Dermatose, Doenças de pele, Doença Cutânea, Doença Dermatológica",
    "Variante(s) Popular(es)" : "Pano",
    "Definição" : "Sintoma de dermatite, manchas esbranquiçadas que aparecem na parte superficial da pele em função de inflamação ou de fungos; dermatose."
}

desidratacao = {
    "Termo" : "Desidratação",
    "Categoria" : "Termo médico/Sintoma",
    "Variação(ões) Denominativa(s)" : "Stress hídrico, Estresse hídrico",
    "Variante(s) Popular(es)" :  "Geratação",
    "Definição" : "Perda de água pelo organismo."
}

diarreia = {
    "Termo" : "Diarréia",
    "Categoria" : "Termo médico/Sintoma",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "Colerina, Disandar, Obradera",
    "Definição" : "Expulsão líquida e contínua de fezes."
}

doenca = {
    "Termo" : "Doença",
    "Categoria" : "Termo médico/Doença",
    "Variação(ões) Denominativa(s)" : "Enfermidade, Moléstia",
    "Variante(s) Popular(es)" :  "Azangá, Zangá, Enfermagem",
    "Definição" : "Adoecimento decorrente de alteração das condições biológicas normais do organismo humano."
}

doente_terminal = { 
    "Termo" : "Doente Terminal",
    "Categoria" : "Termo médico/Sintoma",
    "Variação(ões) Denominativa(s)" : "Paciente Terminal",
    "Variante(s) Popular(es)" :  "Ismuricido, Dismilinguido",
    "Definição" : "Diz-se de pessoa ou animal em estado de agonia, relaciona-se à ausência de sinais vitais."
}

dorso = {
    "Termo" : "Dorso",
    "Categoria" : "Termo médico/Anatomia",
    "Variação(ões) Denominativa(s)" : "Costas",
    "Variante(s) Popular(es)" : "Cacunda, Carcunda, Corcunda",
    "Definição" : "Parte posterior do corpo que integra a coluna vertebral, do pescoço até a pelve; costas." 
}

emplastro = {
    "Termo" : "Emplastro",
    "Categoria" : "Termo médico/Medicina alternativa",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" : "Sinapismo, Pacho, Matutagem, Fumentação, Emprasto",
    "Definição" : "Loção fitoterápica que se fixa à pele conforme sua umidade e ao calor para amenizar dores."
}

enfermo = {
    "Termo" : "Enfermo",
    "Categoria" : "Termo médico/Sintoma",
    "Variação(ões) Denominativa(s)" : "Paciente, Doente, Cliente",
    "Variante(s) Popular(es)" : "Perrenguice, Pitimbado, Passando Mal",
    "Definição" : "Desânimo decorrente de problema de saúde; ausência de vigor físico."
}

escabiose = {
    "Termo" : "Escabiose",
    "Categoria" : "Termo médico/Sintoma",
    "Variação(ões) Denominativa(s)" : "Sarna Sarcóptica, Sarna",
    "Variante(s) Popular(es)" :  "Catita, Pereba",
    "Definição" : "Sintoma de lesão cutânea de origem infecciosa."
}

estomago = {
    "Termo" : "Estômago",
    "Categoria" : "Termo médico/Anatomia",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "Bucho, Estambo, Pandu",
    "Definição" : "Órgão do aparelho digestivo, estômago."
}

estrabismo = {
    "Termo" : "Estrabismo",
    "Categoria" : "Termo médico/Doença",
    "Variação(ões) Denominativa(s)" : "Forias, Vergo Estrabismo, Hipertropia",
    "Variante(s) Popular(es)" : "Zaroia, Vesgo(a)",
    "Definição" : "Alteração ou desvio ocular; desvio de um dos por ausência de paralelismo; estrábico."
}

face = {
    "Termo" : "Face",
    "Categoria" : "Termo médico/Anatomia",
    "Variação(ões) Denominativa(s)" : "Rosto",
    "Variante(s) Popular(es)" : "Cara, Fuça",
    "Definição" : "Região completa da face."
}

fadiga = {
    "Termo" : "Fadiga",
    "Categoria" : "Termo médico/Sintoma",
    "Variação(ões) Denominativa(s)" : "Lassitude",
    "Variante(s) Popular(es)" :  "Iscornado",
    "Definição" : "Sintoma de fadiga, ausência de ânimo."
}

faringe = {
    "Termo" : "Faringe",
    "Categoria" : "Termo médico/Anatomia",
    "Variação(ões) Denominativa(s)" : "Garganta",
    "Variante(s) Popular(es)" :  "Guela",
    "Definição" : "Região ligada ao esôfago, garganta."
}

fratura_ossea = {
    "Termo" : "Fratura Óssea",
    "Categoria" : "Termo médico/Sintoma",
    "Variação(ões) Denominativa(s)" : "Fratura",
    "Variante(s) Popular(es)" :  "Osso ringido",
    "Definição" : "Presença de trinca na formação óssea."
}

furunculose = {
    "Termo" : "Furunculose",
    "Categoria" : "Termo médico/Doença",
    "Variação(ões) Denominativa(s)" : "Furúnculo",
    "Variante(s) Popular(es)" : "Carnegão, Furunco, Nascida",
    "Definição" : "Inflamação formada por bactérias na pele como uma grande espinha com formação de pus."
}

hepatite = {
    "Termo" : "Hepatite",
    "Categoria" : "Termo médico/Doença",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "Amarelão",
    "Definição" : "Infecção hepática causada por agentes infecciosos ou tóxicos, Hepatite."
}

helmintiase = {
    "Termo" : "Helmintíase",
    "Categoria" : "Termo médico/Doença",
    "Variação(ões) Denominativa(s)" : "Verminose",
    "Variante(s) Popular(es)" :  "Bicha, Lombriga, Lumbriga",
    "Definição" : "Parasita causador de verminose."
}

intoxicaçao = {
    "Termo" : "Intoxicação",
    "Categoria" : "Termo médico/Sintoma",
    "Variação(ões) Denominativa(s)" : "Envenenamento",
    "Variante(s) Popular(es)" :  "Intuxicar",
    "Definição" : "Sintoma de envenenamento por alguma substância."
}

invalidez = {
    "Termo" : "Invalidez",
    "Categoria" : "Termo médico/Sintoma",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "Istrupiado",
    "Definição" : "Dificuldade em locomover-se sem apoio por má postura, acidente ou doença."
}

menopausa = {
    "Termo" : "Menopausa",
    "Categoria" : "Termo médico/Sintoma",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "Passagem",
    "Definição" : "Sintoma de menopausa, cessação fisiológica do ciclo menstrual."
}

miiase = {
    "Termo" : "Míiase",
    "Categoria" : "Termo médico/Doença",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "Bichera",
    "Definição" : "Doença parasitária ocasionada pela penetração na pele da larva da varejeira, mosca da família Dermatobia homini."
}

miliaria = {
    "Termo" : "Miliária",
    "Categoria" : "Termo médico/Doença",
    "Variação(ões) Denominativa(s)" : "Brotoeja, Miliária Rubra",
    "Variante(s) Popular(es)" :  "Bertueja",
    "Definição" : "Dermatite inflamatória responsável pela erupção cutânea devido à obstrução dos canais ou ductos que levam o suor das glândulas sudoríparas até a pele."
}

nariz = {
    "Termo" : "Nariz",
    "Categoria" : "Termo médico/Anatomia",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "Fuça",
    "Definição" : "Região nasal."
}

nausea = {
    "Termo" : "Náusea",
    "Categoria" : "Termo médico/Sintoma",
    "Variação(ões) Denominativa(s)" : "Enjoo, Ânsia de Vômito",
    "Variante(s) Popular(es)" :  "Embulia, Entojo",
    "Definição" : "Náusea é uma sensação de desconforto que afeta a porção superior do abdômen, mais ou menos na região da boca do estômago. Na náusea, o paciente apresenta sensibilidade local, como se de fato fosse vomitar."
}

palidez = {
    "Termo" : "Palidez",
    "Categoria" : "Termo médico/Sintoma",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "Opilado",
    "Definição" : "Palidez é a perda de coloração da pele. 'Opilado' se refere ao sintoma de verminose em função da palidez e tonalidade amarelada da pele."
}

pulmao = {
    "Termo" : "Pulmão",
    "Categoria" : "Termo médico/Anatomia",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "Bofe",
    "Definição" : "Órgão responsável pela respiração e fornecimento de oxigênio ao corpo humano, pulmão."
}

resfriado = {
    "Termo" : "Resfriado",
    "Categoria" : "Termo médico/Sintoma",
    "Variação(ões) Denominativa(s)" : "Constipação, Coriza Aguda",
    "Variante(s) Popular(es)" :  "Difruço, Infruenza",
    "Definição" : "Sintoma de doença viral, infecciosa e contagiosa que afeta as vias respiratórias, gripe."
}

secrecao = {
    "Termo" : "Secreção",
    "Categoria" : "Termo médico/Sintoma",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "Remela",
    "Definição" : "Produção e descarga de substâncias específicas no meio externo pelas células de um organismo.'Remela' se refere a secreção matinal da região das pálpebras."
}

sofrimento_fisico = {
    "Termo" : "Sofrimento Físico",
    "Categoria" : "Termo médico/Sintoma",
    "Variação(ões) Denominativa(s)" : "Dor generalizada",
    "Variante(s) Popular(es)" :  "Doraiada",
    "Definição" : "Sintoma de doença que traz sofrimento físico excessivo."
}

umbigo = {
    "Termo" : "Umbigo",
    "Categoria" : "Termo médico/Anatomia",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "Imbigo",
    "Definição" : "Região da cicatriz umbilical, umbigo."
}

urticaria = {
    "Termo" : "Urticária",
    "Categoria" : "Termo médico/Doença",
    "Variação(ões) Denominativa(s)" : "Ardência",
    "Variante(s) Popular(es)" :  "Incanjicada",
    "Definição" : "Sintoma de reação alérgica em que se espalham crostas pela pele."
}

vomitar = {
    "Termo" : "Vomitar",
    "Categoria" : "Termo médico/Sintoma",
    "Variação(ões) Denominativa(s)" : "Êmese",
    "Variante(s) Popular(es)" :  "Lançá",
    "Definição" : "Expelir golfo, vômito ou secreção similar."
}

dicionario_tecnico = {
    "ancilostomiase" : ancilostomiase,
    "anus" : anus,
    "articulacao" : articulacao, 
    "ascite" : ascite,
    "boca" : boca,
    "camomila" : camomila,
    "conjuntivite" : conjuntivite,
    "consternaçao" : consternaçao,
    "constipacao intestinal" : constipacao_intestinal,
    "debilidade muscular" : debilidade_muscular,
    "dermatopatia" : dermatopatia,
    "desidratacao" : desidratacao,
    "diarreia" : diarreia,
    "doenca" : doenca,
    "doente terminal" : doente_terminal,
    "dorso" : dorso,
    "emplastro" : emplastro,
    "enfermo" : enfermo,
    "escabiose" : escabiose,
    "estomago" : estomago,
    "estrabismo" : estrabismo,
    "face" : face,
    "fadiga" : fadiga,
    "faringe" : faringe,
    "fratura ossea" : fratura_ossea,
    "furunculose" : furunculose,
    "hepatite" : hepatite,
    "helmintiase" : helmintiase,
    "intoxicação" : intoxicaçao,
    "invalidez" : invalidez,
    "menopausa" : menopausa, 
    "miiase" : miiase,
    "miliaria" : miliaria,
    "nariz" : nariz, 
    "nausea" : nausea, 
    "palidez" : palidez,
    "pulmao" : pulmao,
    "resfriado" : resfriado,
    "secrecao" : secrecao,
    "sofrimento fisico" : sofrimento_fisico,
    "umbigo" : umbigo,
    "urticaria" : urticaria,
    "vomitar" : vomitar, 
}

amarelao = {
    "Termo" : "Amarelão",
    "Termo(s) técnico(s)" : "Ancilostomíase ou Hepatite\n",
    "Categoria [Ancilostomiase]" : "Termo Popular Informal/Doença",
    "Variação(ões) Denominativa(s) [Ancilostomiase]" : "Ancilostomose",
    "Variante(s) Popular(es) [Ancilostomiase]" :  "Marelão, Doença do Jeca Tatu",
    "Definição [Ancilostomiase]" : "Infecção intestinal causada por nematódeos cujos sintomas são palidez, tom amarelado da pele e anemia.\n",
    "Categoria [Hepatite]" : "Termo Popular Informal/Doença",
    "Variação(ões) Denominativa(s) [Hepatite]" : "-",
    "Variante(s) Popular(es) [Hepatite]" :  "Amarelão",
    "Definição [Hepatite]" : "Infecção hepática causada por agentes infecciosos ou tóxicos, Hepatite."
}

marelao = {
    "Termo" : "Marelão",
    "Categoria" : "Termo Popular Informal/Doença",
    "Termo(s) técnico(s)" : "Ancilostomíase",
    "Variação(ões) Denominativa(s)" : "Ancilostomose",
    "Variante(s) Popular(es)" :  "Amarelão, Doença do Jeca Tatu",
    "Definição" : "Infecção intestinal causada por nematódeos cujos sintomas são palidez, tom amarelado da pele e anemia."
}

doenca_do_jeca_tatu = {
    "Termo" : "Doença do Jeca Tatu",
    "Categoria" : "Termo Popular Informal/Doença",
    "Termo(s) técnico(s)" : "Ancilostomíase",
    "Variação(ões) Denominativa(s)" : "Ancilostomose",
    "Variante(s) Popular(es)" :  "Amarelão, Marelão",
    "Definição" : "Infecção intestinal causada por nematódeos cujos sintomas são palidez, tom amarelado da pele e anemia."
}

cu = {
    "Termo" : "Cu",
    "Categoria" : "Termo Popular Informal/Anatomia",
    "Termo Técnico" : "Ânus",
    "Variação(ões) Denominativa(s)" : "Glândula anal, Esfíncter anal, Esfíncter",
    "Variante(s) Popular(es)" : "Fiofó, Toba, Boga",
    "Definição" : "Extremidade terminal do intestino grosso, por onde as fezes são expelidas."
}

fiofo = {
    "Termo" : "Fiofó",
    "Categoria" : "Termo Popular Informal/Anatomia",
    "Termo Técnico" : "Ânus",
    "Variação(ões) Denominativa(s)" : "Glândula anal, Esfíncter anal, Esfíncter",
    "Variante(s) Popular(es)" : "Cu, Toba, Boga",
    "Definição" : "Extremidade terminal do intestino grosso, por onde as fezes são expelidas."
}

toba = {
    "Termo" : "Toba",
    "Categoria" : "Termo Popular Informal/Anatomia",
    "Termo Técnico" : "Ânus",
    "Variação(ões) Denominativa(s)" : "Glândula anal, Esfíncter anal, Esfíncter",
    "Variante(s) Popular(es)" : "Cu, Fiofó, Boga",
    "Definição" : "Extremidade terminal do intestino grosso, por onde as fezes são expelidas."
}

boga = {
    "Termo" : "Boga",
    "Categoria" : "Termo Popular Informal/Anatomia",
    "Termo Técnico" : "Ânus",
    "Variação(ões) Denominativa(s)" : "Glândula anal, Esfíncter anal, Esfíncter",
    "Variante(s) Popular(es)" : "Cu, Fiofó, Toba",
    "Definição" : "Extremidade terminal do intestino grosso, por onde as fezes são expelidas."
}

junta_do_osso = {
    "Termo" : "Junta do Osso",
    "Categoria" : "Termo Popular Informal/Anatomia",
    "Termo(s) técnico(s)" : "Articulação",
    "Variação(ões) Denominativa(s)" : "Junta, Juntas, Juntura",
    "Variante(s) Popular(es)" :  "-",
    "Definição" : "Junção ou articulação óssea, joelho."
}

barriga_agua = {
    "Termo" : "Barriga d'água",
    "Categoria" : "Termo Popular Informal/Doença",
    "Termo(s) Técnico(s)" : "Ascite",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "-",
    "Definição" : "Acúmulo de de líquido em região próxima ao estômago."
}

beico = {
    "Termo" : "Beiço",
    "Categoria" : "Termo Popular Informal/Anatomia",
    "Termo Técnico" : "Boca",
    "Variação(ões) Denominativa(s)" : "Cavidade Oral, Cavidade Bucal",
    "Variante(s) Popular(es)" :  "-",
    "Definição" : "Contorno ovalado da parte externa da cavidade oral, boca."
}

macela = {
    "Termo" : "Macela",
    "Categoria" : "Termo Popular Informal/Medicina alternativa",
    "Termo Técnico" : "Camomila",
    "Variação(ões) Denominativa(s)" : "Macela-Fétida",
    "Variante(s) Popular(es)" : "-",
    "Definição" : "Planta amarga com propriedade medicinal, utilizada para infecções gástricas e intestinais."
}

dordoi = {
    "Termo" : "Dordói",
    "Categoria" : "Termo Popular Informal/Doença",
    "Termo Técnico" : "Conjuntivite",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "-",
    "Definição" : "Doença similar a conjuntivite, inflamação nos olhos."
}

mocorongo = {
    "Termo" : "Mocorongo",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Consternação",
    "Variação(ões) Denominativa(s)" : "Lamentação, Tristeza",
    "Variante(s) Popular(es)" :  "Mocorongo",
    "Definição" : "Diz-se de quem apresenta tristeza e desânimo como sintoma de depressão."
}

vento_igauzado = {
    "Termo" : "Vento Igauzado",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo" : "Constipação Instestinal",
    "Variação(ões) Denominativa(s)" : "Obstipação, Prisão de Ventre",
    "Variante(s) Popular(es)" :  "-",
    "Definição" : "Sintoma de prisão de ventre, retenção de gases."
}

perrengue = {
    "Termo" : "Perrengue",
    "Categoria" : "Termo Popular Informal/Doença",
    "Termo Técnico" : "Debilidade Muscular",
    "Variação(ões) Denominativa(s)" : "Fraqueza Muscular",
    "Variante(s) Popular(es)" :  "-",
    "Definição" : "Estado debilitado por adoecimento ou mal-estar em função de alterações climáticas extremas ou do organismo humano."
}

pano = {
    "Termo" : "Pano",
    "Categoria" : "Termo médico/Sintoma",
    "Termo Técnico" : "Dermatopatia",
    "Variação(ões) Denominativa(s)" : "Dermatose, Doenças de pele, Doença Cutânea, Doença Dermatológica",
    "Variante(s) Popular(es)" : "-",
    "Definição" : "Sintoma de dermatite, manchas esbranquiçadas que aparecem na parte superficial da pele em função de inflamação ou de fungos; dermatose."
}

geratacao = {
    "Termo" : "Geratação",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Desidratação",
    "Variação(ões) Denominativa(s)" : "Stress hídrico, Estresse hídrico",
    "Variante(s) Popular(es)" :  "-",
    "Definição" : "Perda de água pelo organismo."
}

colerina = {
    "Termo" : "Colerina",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Diarréia",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "Disandar, Obradera",
    "Definição" : "Expulsão líquida e contínua de fezes."
}

disandar = {
    "Termo" : "Disandar",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Diarréia",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "Colerina, Obradera",
    "Definição" : "Expulsão líquida e contínua de fezes."
}

obradera = {
    "Termo" : "Obradera",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Diarréia",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "Colerina, Disandar",
    "Definição" : "Expulsão líquida e contínua de fezes."
}

azanga = {
    "Termo" : "Azangá",
    "Categoria" : "Termo Popular Informal/Doença",
    "Termo Técnico" : "Doença",
    "Variação(ões) Denominativa(s)" : "Enfermidade, Moléstia",
    "Variante(s) Popular(es)" :  "Zangá, Enfermagem",
    "Definição" : "Adoecimento decorrente de alteração das condições biológicas normais do organismo humano."
}

zanga = {
    "Termo" : "Zangá",
    "Categoria" : "Termo Popular Informal/Doença",
    "Termo Técnico" : "Doença",
    "Variação(ões) Denominativa(s)" : "Enfermidade, Moléstia",
    "Variante(s) Popular(es)" :  "Zangá, Enfermagem",
    "Definição" : "Adoecimento decorrente de alteração das condições biológicas normais do organismo humano."
}

enfermagem = {
    "Termo" : "Enfermagem",
    "Categoria" : "Termo Popular Informal/Doença",
    "Termo Técnico" : "Doença",
    "Variação(ões) Denominativa(s)" : "Enfermidade, Moléstia",
    "Variante(s) Popular(es)" :  "Azangá, Zangá",
    "Definição" : "Adoecimento decorrente de alteração das condições biológicas normais do organismo humano."
}

ismuricido = { 
    "Termo" : "Ismuricido",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Doente Terminal",
    "Variação(ões) Denominativa(s)" : "Paciente Terminal",
    "Variante(s) Popular(es)" :  "Dismilinguido",
    "Definição" : "Diz-se de pessoa ou animal em estado de agonia, relaciona-se à ausência de sinais vitais."
}

dismiliguindo = { 
    "Termo" : "Dismiliguindo",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Doente Terminal",
    "Variação(ões) Denominativa(s)" : "Paciente Terminal",
    "Variante(s) Popular(es)" :  "Ismuricido",
    "Definição" : "Diz-se de pessoa ou animal em estado de agonia, relaciona-se à ausência de sinais vitais."
}

cacunda = {
    "Termo" : "Cacunda",
    "Categoria" : "Termo Popular Informal/Anatomia",
    "Termo Técnico" : "Dorso",
    "Variação(ões) Denominativa(s)" : "Costas",
    "Variante(s) Popular(es)" : "Carcunda, Corcunda",
    "Definição" : "Parte posterior do corpo que integra a coluna vertebral, do pescoço até a pelve; costas." 
}

carcunda = {
    "Termo" : "Carcunda",
    "Categoria" : "Termo Popular Informal/Anatomia",
    "Termo Técnico" : "Dorso",
    "Variação(ões) Denominativa(s)" : "Costas",
    "Variante(s) Popular(es)" : "Cacunda, Corcunda",
    "Definição" : "Parte posterior do corpo que integra a coluna vertebral, do pescoço até a pelve; costas." 
}

corcunda = {
    "Termo" : "Corcunda",
    "Categoria" : "Termo Popular Informal/Anatomia",
    "Termo Técnico" : "Dorso",
    "Variação(ões) Denominativa(s)" : "Costas",
    "Variante(s) Popular(es)" : "Cacunda, Carcunda",
    "Definição" : "Parte posterior do corpo que integra a coluna vertebral, do pescoço até a pelve; costas." 
}

sinapismo = {
    "Termo" : "Sinapismo",
    "Categoria" : "Termo Popular Informal/Medicina alternativa",
    "Termo Técnico" : "Emplastro",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" : "Pacho, Matutagem, Fumentação, Emprasto",
    "Definição" : "Loção fitoterápica que se fixa à pele conforme sua umidade e ao calor para amenizar dores."
}

pacho = {
    "Termo" : "Pacho",
    "Categoria" : "Termo Popular Informal/Medicina alternativa",
    "Termo Técnico" : "Emplastro",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" : "Sinapismo, Matutagem, Fumentação, Emprasto",
    "Definição" : "Loção fitoterápica que se fixa à pele conforme sua umidade e ao calor para amenizar dores."
}

matutagem = {
    "Termo" : "Matutagem",
    "Categoria" : "Termo Popular Informal/Medicina alternativa",
    "Termo Técnico" : "Emplastro",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" : "Sinapismo, Pacho, Fumentação, Emprasto",
    "Definição" : "Loção fitoterápica que se fixa à pele conforme sua umidade e ao calor para amenizar dores."
}

fumentacao = {
    "Termo" : "Fumentação",
    "Categoria" : "Termo Popular Informal/Medicina alternativa",
    "Termo Técnico" : "Emplastro",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" : "Sinapismo, Matutagem, Pacho, Emprasto",
    "Definição" : "Loção fitoterápica que se fixa à pele conforme sua umidade e ao calor para amenizar dores."
}

emprasto = {
    "Termo" : "Emprasto",
    "Categoria" : "Termo Popular Informal/Medicina alternativa",
    "Termo Técnico" : "Emplastro",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" : "Sinapismo, Matutagem, Fumentação, Pacho",
    "Definição" : "Loção fitoterápica que se fixa à pele conforme sua umidade e ao calor para amenizar dores."
}

perrenguice = {
    "Termo" : "Perrenguice",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Enfermo",
    "Variação(ões) Denominativa(s)" : "Paciente, Doente, Cliente",
    "Variante(s) Popular(es)" : "Pitimbado, Passando Mal",
    "Definição" : "Desânimo decorrente de problema de saúde; ausência de vigor físico."
}

pitimbado = {
    "Termo" : "Pitimbado",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Enfermo",
    "Variação(ões) Denominativa(s)" : "Paciente, Doente, Cliente",
    "Variante(s) Popular(es)" : "Perrenguice, Passando Mal",
    "Definição" : "Desânimo decorrente de problema de saúde; ausência de vigor físico."
}

passando_mal = {
    "Termo" : "Passando Mal",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Enfermo",
    "Variação(ões) Denominativa(s)" : "Paciente, Doente, Cliente",
    "Variante(s) Popular(es)" : "Perrenguice, Pitimbado",
    "Definição" : "Desânimo decorrente de problema de saúde; ausência de vigor físico."
}

catita = {
    "Termo" : "Catita",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Escabiose",
    "Variação(ões) Denominativa(s)" : "Sarna Sarcóptica, Sarna",
    "Variante(s) Popular(es)" :  "Pereba",
    "Definição" : "Sintoma de lesão cutânea de origem infecciosa."
}

pereba = {
    "Termo" : "Pereba",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Escabiose",
    "Variação(ões) Denominativa(s)" : "Sarna Sarcóptica, Sarna",
    "Variante(s) Popular(es)" :  "Pereba",
    "Definição" : "Sintoma de lesão cutânea de origem infecciosa."
}

bucho = {
    "Termo" : "Bucho",
    "Categoria" : "Termo Popular Informal/Anatomia",
    "Termo Técnico" : "Estômago",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "Estambo, Pandu",
    "Definição" : "Órgão do aparelho digestivo, estômago."
}

estambo = {
    "Termo" : "Estambo",
    "Categoria" : "Termo Popular Informal/Anatomia",
    "Termo Técnico" : "Estômago",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "Bucho, Pandu",
    "Definição" : "Órgão do aparelho digestivo, estômago."
}

pandu = {
    "Termo" : "pandu",
    "Categoria" : "Termo Popular Informal/Anatomia",
    "Termo Técnico" : "Estômago",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "Estambo, Pandu",
    "Definição" : "Órgão do aparelho digestivo, estômago."
}

zaroia = {
    "Termo" : "Zaroia",
    "Categoria" : "Termo Popular Informal/Doença",
    "Termo Técnico" : "Estrabismo",
    "Variação(ões) Denominativa(s)" : "Forias, Vergo Estrabismo, Hipertropia",
    "Variante(s) Popular(es)" : "Vesgo(a)",
    "Definição" : "Alteração ou desvio ocular; desvio de um dos por ausência de paralelismo; estrábico."
}

vesgo = {
    "Termo" : "Vesgo",
    "Categoria" : "Termo Popular Informal/Doença",
    "Termo Técnico" : "Estrabismo",
    "Variação(ões) Denominativa(s)" : "Forias, Vergo Estrabismo, Hipertropia",
    "Variante(s) Popular(es)" : "Zaroia",
    "Definição" : "Alteração ou desvio ocular; desvio de um dos por ausência de paralelismo; estrábico."
}

cara = {
    "Termo" : "Cara",
    "Categoria" : "Termo Popular Informal/Anatomia",
    "Termo Técnico" : "Face",
    "Variação(ões) Denominativa(s)" : "Rosto",
    "Variante(s) Popular(es)" : "Fuça",
    "Definição" : "Região completa da face."
}

iscornado = {
    "Termo" : "Iscornado",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Fadiga",
    "Variação(ões) Denominativa(s)" : "Lassitude",
    "Variante(s) Popular(es)" :  "-",
    "Definição" : "Sintoma de fadiga, ausência de ânimo."
}

guela = {
    "Termo" : "Guela",
    "Categoria" : "Termo Popular Informal/Anatomia",
    "Termo Técnico" : "Faringe",
    "Variação(ões) Denominativa(s)" : "Garganta",
    "Variante(s) Popular(es)" :  "-",
    "Definição" : "Região ligada ao esôfago, garganta."
}

osso_ringido = {
    "Termo" : "Osso Ringido",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Fratura Óssea",
    "Variação(ões) Denominativa(s)" : "Fratura",
    "Variante(s) Popular(es)" :  "Osso ringido",
    "Definição" : "Presença de trinca na formação óssea."
}

carnegao = {
    "Termo" : "Carnegão",
    "Categoria" : "Termo Popular Informal/Doença",
    "Termo Técnico" : "Furunculose",
    "Variação(ões) Denominativa(s)" : "Furúnculo",
    "Variante(s) Popular(es)" : "Furunco, Nascida",
    "Definição" : "Inflamação formada por bactérias na pele como uma grande espinha com formação de pus."
}

furunco = {
    "Termo" : "Furunco",
    "Categoria" : "Termo Popular Informal/Doença",
    "Termo Técnico" : "Furunculose",
    "Variação(ões) Denominativa(s)" : "Furúnculo",
    "Variante(s) Popular(es)" : "Carnegão, Nascida",
    "Definição" : "Inflamação formada por bactérias na pele como uma grande espinha com formação de pus."
}

nascida = {
    "Termo" : "Nascida",
    "Categoria" : "Termo Popular Informal/Doença",
    "Termo Técnico" : "Furunculose",
    "Variação(ões) Denominativa(s)" : "Furúnculo",
    "Variante(s) Popular(es)" : "Furunco, Carnegão",
    "Definição" : "Inflamação formada por bactérias na pele como uma grande espinha com formação de pus."
}

bicha = {
    "Termo" : "Bicha",
    "Categoria" : "Termo Popular Informal/Doença",
    "Termo Técnico" : "Helmintíase",
    "Variação(ões) Denominativa(s)" : "Verminose",
    "Variante(s) Popular(es)" :  "Lombriga, Lumbriga",
    "Definição" : "Parasita causador de verminose."
}

lombriga = {
    "Termo" : "Lombriga",
    "Categoria" : "Termo Popular Informal/Doença",
    "Termo Técnico" : "Helmintíase",
    "Variação(ões) Denominativa(s)" : "Verminose",
    "Variante(s) Popular(es)" :  "Bicha, Lumbriga",
    "Definição" : "Parasita causador de verminose."
}

lumbriga = {
    "Termo" : "Lumbriga",
    "Categoria" : "Termo Popular Informal/Doença",
    "Termo Técnico" : "Helmintíase",
    "Variação(ões) Denominativa(s)" : "Verminose",
    "Variante(s) Popular(es)" :  "Bicha, Lombriga",
    "Definição" : "Parasita causador de verminose."
}

istrupiado = {
    "Termo" : "Istrupiado",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Invalidez",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "-",
    "Definição" : "Dificuldade em locomover-se sem apoio por má postura, acidente ou doença."
}

intuxicar = {
    "Termo" : "Intuxicar",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Intoxicação",
    "Variação(ões) Denominativa(s)" : "Envenenamento",
    "Variante(s) Popular(es)" :  "-",
    "Definição" : "Sintoma de envenenamento por alguma substância."
}

passagem = {
    "Termo" : "Passagem",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Menopausa",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "-",
    "Definição" : "Sintoma de menopausa, cessação fisiológica do ciclo menstrual."
}

bichera = {
    "Termo" : "Bichera",
    "Categoria" : "Termo Popular Informal/Doença",
    "Termo Técnico" : "Míiase",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "-",
    "Definição" : "Doença parasitária ocasionada pela penetração na pele da larva da varejeira, mosca da família Dermatobia homini."
}

bertueja = {
    "Termo" : "Bertueja",
    "Categoria" : "Termo Popular Informal/Doença",
    "Termo Técnico" : "Miliária",
    "Variação(ões) Denominativa(s)" : "Brotoeja, Miliária Rubra",
    "Variante(s) Popular(es)" :  "-",
    "Definição" : "Dermatite inflamatória responsável pela erupção cutânea devido à obstrução dos canais ou ductos que levam o suor das glândulas sudoríparas até a pele."
}

fuca = {
    "Termo" : "Fuça ou Face",
    "Categoria" : "Termo Popular Informal/Anatomia",
    "Termo(s) Técnico(s)" : "Nariz ou Face",
    "Variação(ões) Denominativa(s)[Nariz]" : "-",
    "Variante(s) Popular(es) [Nariz]" :  "-",
    "Definição [Nariz]" : "Região nasal.",
    "Categoria [Face]" : "\nTermo Popular Informal/Anatomia",
    "Variação(ões) Denominativa(s) [Face]" : "Rosto",
    "Variante(s) Popular(es) [Face]" : "Fuça",
    "Definição [Face]" : "Região completa da face."
}

entojo = {
    "Termo" : "Entojo",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Náusea",
    "Variação(ões) Denominativa(s)" : "Enjoo, Ânsia de Vômito",
    "Variante(s) Popular(es)" :  "Embulia",
    "Definição" : "Náusea é uma sensação de desconforto que afeta a porção superior do abdômen, mais ou menos na região da boca do estômago. Na náusea, o paciente apresenta sensibilidade local, como se de fato fosse vomitar."
}

embulia = {
    "Termo" : "Embulia",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Náusea",
    "Variação(ões) Denominativa(s)" : "Enjoo, Ânsia de Vômito",
    "Variante(s) Popular(es)" :  "Entojo",
    "Definição" : "Náusea é uma sensação de desconforto que afeta a porção superior do abdômen, mais ou menos na região da boca do estômago. Na náusea, o paciente apresenta sensibilidade local, como se de fato fosse vomitar."
}

opilado = {
    "Termo" : "Opilado",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Palidez",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "-",
    "Definição" : "Palidez é a perda de coloração da pele. 'Opilado' se refere ao sintoma de verminose em função da palidez e tonalidade amarelada da pele."
}

bofe = {
    "Termo" : "Bofe",
    "Categoria" : "Termo Popular Informal/Anatomia",
    "Termo Técnico" : "Pulmão",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "-",
    "Definição" : "Órgão responsável pela respiração e fornecimento de oxigênio ao corpo humano, pulmão."
}
difruco = {
    "Termo" : "Difruço",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Resfriado",
    "Variação(ões) Denominativa(s)" : "Constipação, Coriza Aguda",
    "Variante(s) Popular(es)" :  "Infruenza",
    "Definição" : "Sintoma de doença viral, infecciosa e contagiosa que afeta as vias respiratórias, gripe."
}

infruenza = {
    "Termo" : "Infruenza",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Resfriado",
    "Variação(ões) Denominativa(s)" : "Constipação, Coriza Aguda",
    "Variante(s) Popular(es)" :  "Difruço",
    "Definição" : "Sintoma de doença viral, infecciosa e contagiosa que afeta as vias respiratórias, gripe."
}

remela = {
    "Termo" : "Remela",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Secreção",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "-",
    "Definição" : "Produção e descarga de substâncias específicas no meio externo pelas células de um organismo.'Remela' se refere a secreção matinal da região das pálpebras."
}

doraida = {
    "Termo" : "Doraiada",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Sofrimento Físico",
    "Variação(ões) Denominativa(s)" : "Dor generalizada",
    "Variante(s) Popular(es)" :  "-",
    "Definição" : "Sintoma de doença que traz sofrimento físico excessivo."
}

imbigo = {
    "Termo" : "Imbigo",
    "Categoria" : "Termo Popular Informal/Anatomia",
    "Termo Técnico" : "Umbigo",
    "Variação(ões) Denominativa(s)" : "-",
    "Variante(s) Popular(es)" :  "-",
    "Definição" : "Região da cicatriz umbilical, umbigo."
}

incanjicada = {
    "Termo" : "Incanjicada",
    "Categoria" : "Termo Popular Informal/Doença",
    "Termo Técnico" : "Urticária",
    "Variação(ões) Denominativa(s)" : "Ardência",
    "Variante(s) Popular(es)" :  "-",
    "Definição" : "Sintoma de reação alérgica em que se espalham crostas pela pele."
}

lanca = {
    "Termo" : "Lançá",
    "Categoria" : "Termo Popular Informal/Sintoma",
    "Termo Técnico" : "Vomitar",
    "Variação(ões) Denominativa(s)" : "Êmese",
    "Variante(s) Popular(es)" :  "-",
    "Definição" : "Expelir, pela boca, com esforço e em golfadas, o alimento ingerido."
}

dicionario_popular = {
    "amarelao" : amarelao,
    "marelao" : marelao,
    "doenca do jeca tatu": doenca_do_jeca_tatu,
    "cu" : cu,
    "fiofo" : fiofo,
    "boga" : boga,
    "toba" : toba,
    "junta do osso" : junta_do_osso,
    "barriga d'agua" : barriga_agua,
    "barriga de agua" : barriga_agua,
    "barriga d agua" : barriga_agua,
    "beico" : beico,
    "macela" : macela,
    "dordoi" : dordoi,
    "mocorongo" : mocorongo,
    "perrengue" : perrengue,
    "pano" : pano,
    "geratacao" : geratacao,
    "colerina" : colerina,
    "disandar" : disandar,
    "obradera" : obradera,
    "azanga" : azanga,
    "zanga" : zanga,
    "enfermagem" : enfermagem,
    "ismuricido" : ismuricido, 
    "dismilinguido" : dismiliguindo,
    "cacunda" : cacunda,
    "carcunda" : carcunda,
    "corcunda" : corcunda,
    "sinapismo" : sinapismo,
    "pacho" : pacho,
    "matutagem" : matutagem,
    "fumentacao" : fumentacao,
    "emprasto" : emprasto,
    "perrenguice" : perrenguice,
    "pitimbado" : pitimbado,
    "passando_mal" : passando_mal,
    "catita" :  catita,
    "pereba" : pereba,
    "bucho" : estomago,
    "estambo" : estomago,
    "pandu" : estomago,
    "zaroia" : zaroia,
    "vesgo" : vesgo,
    "cara" : cara,
    "iscornado" : fadiga,
    "guela" : faringe,
    "osso ringido" : fratura_ossea,
    "carnegao" : carnegao, 
    "furunco" : furunco, 
    "nascida" : nascida,
    "bicha" : bicha, 
    "lombriga": lombriga, 
    "lumbriga" : lumbriga,
    "istrupiado" : istrupiado,
    "intuxicar" : intuxicar,
    "passagem" : passagem,
    "bichera" : bichera,
    "bertueja" : bertueja,
    "fuca" : fuca, 
    "embulia" : embulia,
    "entojo" : entojo,
    "opilado" : opilado,
    "bofe" : bofe,
    "difruco" : difruco,
    "infruenza" : infruenza,
    "remela" : remela,
    "doraiada" : doraida,
    "imbigo" : imbigo,
    "incanjicada" : incanjicada,
    "lanca" : lanca,
}

def formatString(string):
    try:
        string = unicode(string, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3 
        pass
    string = unicodedata.normalize('NFD', string)
    string = string.encode('ascii', 'ignore')
    string = string.decode("utf-8")
    return str(string)

if __name__ == "__main__":
    print("******************************LEXICO-MORFOLOGICO*********************************")

    while True:
        found = 0
        print("\n1)Verificar termos disponíveis no dicionário;")
        print("2)Buscar palavra, seu significado e seu(s) termo(s) alternativo(s);")
        print("3)Sair;")
        words = 0
        op = int(input())
        init(convert=True)
        if op == 1:
            print(Fore.LIGHTGREEN_EX + "Termos médicos:")
            for x in dicionario_tecnico:
                print(Fore.LIGHTYELLOW_EX + f"{x}")
            print(Fore.LIGHTGREEN_EX + "\nTermos populares:")
            for x in dicionario_popular:
                print(Fore.LIGHTYELLOW_EX + f"{x}")
            print(Style.RESET_ALL) 

        elif op == 2:
            print("Insira o termo a ser buscado:")
            termo = input()
            termo = formatString(termo.lower())
            tempo = time.time()

            for x in dicionario_tecnico:
                if termo == x:
                    print(Fore.LIGHTGREEN_EX + "\nTermo Técnico")
                    for y in dicionario_tecnico[x]:
                        print(Fore.LIGHTBLUE_EX + f"{y} : " + Fore.LIGHTMAGENTA_EX + f"{dicionario_tecnico[x][y]}")
                        found = 1
            print(Style.RESET_ALL)

            for x in dicionario_popular:
                if termo == x:
                    print(Fore.LIGHTGREEN_EX + "\nTermo Popular")
                    for y in dicionario_popular[x]:
                        print(Fore.LIGHTBLUE_EX + f"{y} : " + Fore.LIGHTMAGENTA_EX + f"{dicionario_popular[x][y]}")
                        found = 1
            print(Style.RESET_ALL)
            
            if found == 0:
                print(Back.RED + "Palavra inserida não está disponível no dicionário")
                print(Style.RESET_ALL)

            print("Tempo de busca:", (time.time() - tempo)*1000, "ms")
        elif op == 3:
            exit(0)

        else:
            print(Back.RED + "Operação não reconhecida. Por favor, selecione uma das funções citadas.")
            print(Style.RESET_ALL)