from flask import request, render_template
from flask import Flask
from math import gcd
import random

# 1 dia em minutos de cada planeta
mercurio = (58  * 24) * 60 
venus = (243 * 24) * 60
marte = 25 * 60
jupiter = 10 * 60
saturno = 11 * 60
urano = 17 * 60
netuno = 16 * 60
terra = 24 * 60

# 1 dia em horas de cada planeta
dMer = 1408.03 / 24
dVen = 5832.03 / 24
dMar = 25
dJup = 10
dSat = 11
dUra = 17
dNet = 16

# distancia média em rel a Terra
dist_Mer = 77300000
dist_Ven = 41400000
dist_Mar = 78300000
dist_Jup = 62873000
dist_Sat = 1275000000
dist_Ura = 2723950000
dist_Net = 4351400000

def tempoEnvio(distancia_sonda):
    vel_luz = 299792  # km/s
    tempo_segundos = distancia_sonda / vel_luz
    return tempo_segundos

def mmc(a, b):
    return abs(a * b) / gcd(int(a), int(b))

app = Flask(__name__)

tema = 'static/bg-tema.png'
@app.route('/')
@app.route('/index.html')
def homepage():
    
    return render_template('index.html', tema = tema)

@app.route('/', methods=['GET', 'POST'])
def resultado():
    tema = 'static/bg-tema.png'
    valor = request.form['planeta']
    if valor == 'mercurio':
        valor = "Mercúrio"
        minutos = tempoEnvio(dist_Mer)
        minutos = minutos/60
        tempo = f'{minutos:.2f} minutos'        

        sol = '58.000.000'
        orbita = '88 dias'
        superficie = '74.800.000'
        dia = f'{dMer:.0f} dias.'
        temperatura = 'Varia entre -180 e 460'
        moons = 'Não possui.'
        gravidade = 3.7
        link = 'https://g.co/kgs/jTtfZ6A'

        sondas = ['Mariner 10','MESSENGER', 'BepiColombo']
        sonda = random.choice(sondas)
        if sonda == 'Mariner 10':
            img_sonda = 'sondas/mariner10.png'
            info = 'A Mariner 10 foi a primeira nave espacial enviada ao planeta Mercúrio; a primeira missão a explorar dois planetas (Mercúrio e Vênus) durante uma única missão; a primeira a usar assistência gravitacional para alterar sua trajetória de voo; a primeira a retornar ao seu alvo após um encontro inicial; e a primeira a usar o vento solar como um meio importante de orientação da nave espacial durante o voo.'
            fonte = 'https://science.nasa.gov/mission/mariner-10/'
            dados_coletados = ['Superfície: ',
                                '- A Mariner 10 revelou uma superfície coberta de crateras, muito semelhante à da Lua. Essa semelhança indica que Mercúrio é geologicamente inativo há bilhões de anos.',
                                '- Descobriu grandes bacias de impacto, como a bacia Caloris, com 1.550 km de diâmetro, uma das maiores estruturas de impacto do Sistema Solar.',
                                '- Observou escarpas e falhas de contração (chamadas rupes), sugerindo que o planeta encolheu ao longo de sua história.',
                            'Campo Magnético:',
                                '- A sonda detectou que Mercúrio possui um campo magnético fraco, com cerca de 1% da força do campo magnético da Terra.',
                            'Atmosfera (Exosfera):',
                                '- Mercúrio tem uma exosfera extremamente tênue composta principalmente de hidrogênio, hélio, oxigênio, sódio, cálcio e potássio. Esta atmosfera é continuamente renovada pelo vento solar e pela sublimação de elementos da superfície.',
                            'Limitações da Missão:',
                                '- A Mariner 10 mapeou apenas cerca de 45% da superfície de Mercúrio, deixando o restante para missões posteriores, como a Messenger e a BepiColombo.']

        elif sonda == 'MESSENGER':
            img_sonda = 'sondas/messenger.jpg'
            info = 'MESSENGER (Mercury Surface, Space Environment, Geochemistry and Ranging) foi a sétima missão da classe Discovery e a primeira nave espacial a orbitar Mercúrio. Seu objetivo principal era estudar a geologia, o campo magnético e a composição química do planeta. Foi a primeira missão a Mercúrio depois da Mariner 10, mais de 30 anos antes.'
            fonte = 'https://science.nasa.gov/mission/messenger/'
            dados_coletados = ['Superfície:',
                                    '- Mapeamento completo da superfície em alta resolução.',
                                    '- Descoberta de depósitos brilhantes em crateras polares, confirmados como gelo de água protegido por material orgânico.',
                                    '- Evidência de vulcanismo antigo, com fluxos de lava cobrindo grandes áreas.',
                                    '- Identificação de hollows, depressões brilhantes que se formam pela sublimação de materiais voláteis.',
                                'Composição química:',
                                    '- Medições de elementos como sódio, potássio, magnésio e cálcio na exosfera de Mercúrio (uma camada extremamente fina de gases ao redor do planeta).',
                                    '- Superfície rica em enxofre, indicando um passado geológico diferente do de outros planetas rochosos, como a Terra e Marte.',
                                    '- Evidência de materiais voláteis que sobrevivem em um ambiente tão próximo do Sol.',
                                'Campo Magnético:',
                                    '- Mapeamento detalhado do campo magnético, mostrando que ele é gerado por um núcleo externo líquido, semelhante ao da Terra.',
                                    '- Identificação de assimetrias no campo magnético, com a região norte sendo mais fortemente protegida que a sul.',
                                'Núcleo e Interior:',
                                '   - Revelou que o núcleo de Mercúrio ocupa cerca de 85% do raio do planeta, tornando-o proporcionalmente maior do que o núcleo de qualquer outro planeta do Sistema Solar.',
                                    '- O núcleo é parcialmente líquido, com uma camada externa rica em ferro-sulfeto, uma característica única.',
                                'Exosfera:',
                                    '- Confirmou a presença de átomos como hidrogênio, hélio, oxigênio, sódio e potássio na exosfera.',
                                    '- Observou que essa exosfera é formada principalmente pela interação do vento solar com a superfície de Mercúrio.',
                                'Gravidade e Rotação:',
                                    '- Confirmação da ressonância 3:2, onde Mercúrio gira três vezes em seu eixo para cada duas órbitas ao redor do Sol.']
        else:
            img_sonda = 'sondas/bepicolombo.png'
            info = 'BepiColombo é uma missão internacional composta por duas espaçonaves viajando juntas para Mercúrio para orbitar e estudar o planeta de pontos de vista únicos. A Agência Espacial Europeia (ESA) forneceu um orbitador. A Agência de Exploração Aeroespacial do Japão (JAXA) forneceu o segundo orbitador.'
            fonte = 'https://science.nasa.gov/mission/bepicolombo/'
            dados_coletados = ['Sonda enviada em 2018, ainda não coletou dados suficientes.']

        planet = 'planetas/mercurio.jpg'

        resultado = mmc(mercurio, terra)
        resultado = int(resultado/60)

        if resultado >= 24:
            resultado /= 24

        return render_template('index.html', resultado = int(resultado), valor = valor, sonda = sonda, temperatura = temperatura, planet = planet, gravidade = gravidade, img_sonda = img_sonda, moons = moons, tema = tema, dia = dia, info = info, fonte = fonte, dados_coletados = dados_coletados, sol = sol, orbita = orbita, superficie = superficie, link = link, tempo = tempo)

    elif valor == 'venus':
        valor = "Vênus"
        minutos = tempoEnvio(dist_Ven)
        minutos = minutos/60
        tempo = f'{minutos:.2f} minutos'  

        sol = '108.200.000'
        orbita = '225 dias'
        superficie = '460.200.000'
        dia = f'{dVen:.0f} dias.'
        link = 'https://g.co/kgs/4r3z8hf'

        sondas = ['Magellan','Venus Express', 'Akatsuki']
        sonda = random.choice(sondas)
        if sonda == 'Magellan':
            img_sonda = 'sondas/magellan.png'
            info = 'Uma das missões de espaço profundo mais bem-sucedidas, a Magellan foi a primeira nave espacial a obter imagens de toda a superfície de Vênus e fez várias descobertas sobre o planeta. Mesmo quando mergulhou na atmosfera venusiana e queimou, ela ainda estava coletando dados. A missão Magellan da NASA para Vênus foi uma das missões de espaço profundo mais bem-sucedidas. Foi a primeira nave espacial a obter imagens de toda a superfície de Vênus e fez várias descobertas sobre o planeta. A Magellan queimou cerca de 10 horas após receber o comando para mergulhar na atmosfera venusiana.'
            fonte = 'https://science.nasa.gov/mission/magellan/'
            dados_coletados = ['Mapeamento da superfície: Utilizando radar de abertura sintética (SAR), a Magellan criou mapas detalhados de mais de 98% da superfície de Vênus, revelando:',
                                    '- Vastas planícies vulcânicas e estruturas geológicas, como domos de lava e vales tectônicos.',
                                    '- Vulcões gigantes (como o Monte Maat) e evidências de atividade vulcânica passada.',
                                    '- Crateras de impacto bem preservadas, indicando uma superfície relativamente jovem (cerca de 300-500 milhões de anos).',
                                    '- Identificou que cerca de 85% da superfície é composta de planícies vulcânicas.',
                               'Topografia e gravidade:',
                                    '- Mapeamento tridimensional da topografia.',
                                    '- Mapas de gravidade indicaram que Vênus possui uma litosfera mais espessa do que a da Terra.',
                                    '- Identificação de anomalias gravitacionais, sugerindo dinâmicas internas do planeta.']

        elif sonda == 'Venus Express':
            img_sonda = 'sondas/venus.png'
            info = 'Venus Express foi a primeira nave espacial europeia a orbitar Vênus. A missão original deveria durar não mais que 500 dias terrestres, mas a missão foi estendida cinco vezes. A sonda Venus Express da ESA foi projetada para estudar a atmosfera de Vênus, seu ambiente de plasma e as características da superfície a partir de uma órbita elíptica quase polar de 24 horas.'
            fonte = 'https://science.nasa.gov/mission/venus-express/'
            dados_coletados = ['Estudo atmosférico:',
                                    '- Detectou vórtices polares dinâmicos nos polos.',
                                    '- Observou a super-rotação da atmosfera, onde os ventos circulam mais rápido que o próprio planeta.',
                                    '- Identificou a presença de camadas de nuvens ácidas, compostas de ácido sulfúrico, além de rastrear mudanças sazonais e temporais.',
                                    '- Confirmou a existência de uma perda atmosférica para o espaço, devido à interação com o vento solar (Vênus não tem campo magnético global).',
                                'Composição química:',
                                    '- Detectou indícios de relâmpagos atmosféricos.',
                                    '- Observou variações no dióxido de enxofre, potencialmente relacionadas à atividade vulcânica.',
                                'Temperatura e clima:',
                                    '- Medições precisas das temperaturas da atmosfera e da superfície.']

        else:
            img_sonda = 'sondas/akatsuki.png'
            info = '''Akatsuki está estudando a atmosfera de Vênus a partir da órbita. Recuperando-se de uma inserção orbital perdida em 2010 e entrando na órbita de Vênus em 2015, Akatsuki é a primeira missão bem-sucedida do Japão a explorar outro planeta.
             Akatsuki, que significa amanhecer em japonês, está estudando a circulação atmosférica de Vênus. Informações meteorológicas são obtidas mapeando globalmente nuvens e constituintes menores sucessivamente com quatro câmeras em comprimentos de onda ultravioleta e infravermelho, detectando raios com um gerador de imagens de alta velocidade e observando a estrutura vertical da atmosfera com técnicas de radiociência.'''
            fonte = 'https://science.nasa.gov/mission/akatsuki/'
            dados_coletados = ['Estudo climático:',
                                    '- Monitora os padrões dinâmicos das nuvens usando câmeras infravermelhas e ultravioletas.',
                                    '- Observou ondas estacionárias atmosféricas (como ondas de gravidade) que podem estar relacionadas à interação da atmosfera com a topografia.',
                                'Super-rotação atmosférica:',
                                    '- Detalhamento dos processos que causam os ventos ultra-rápidos.',
                                'Clima e composição:',
                                    '- Imagens detalhadas das camadas de nuvens e da dinâmica das tempestades.',
                                    '- Dados sobre o papel do dióxido de enxofre e outras partículas nas mudanças atmosféricas.']

        temperatura = 'Média de 465'
        moons = 'Não possui.'
        gravidade = 8.87

        planet = 'planetas/venus.jpg'

        resultado = mmc(venus, terra)
        resultado = int(resultado/60)

        if resultado >= 24:
            resultado /= 24

        return render_template('index.html', resultado = int(resultado), valor = valor, sonda = sonda, temperatura = temperatura, planet = planet, gravidade = gravidade, img_sonda = img_sonda, moons = moons, tema = tema, dia = dia, info = info, fonte = fonte, dados_coletados = dados_coletados, sol = sol, orbita = orbita, superficie = superficie, link = link, tempo = tempo)
    
    elif valor == 'marte':
        valor = "Marte"
        minutos = tempoEnvio(dist_Mar)
        minutos = minutos/60
        tempo = f'{minutos:.2f} minutos'  

        sol = '227.900.000'
        orbita = '687 dias'
        superficie = '144.400.000'
        dia = f'{dMar} horas'
        link = 'https://g.co/kgs/8UDpYkp'

        sondas = ['Mariner 4','Mariner 9']
        sonda = random.choice(sondas)
        if sonda == 'Mariner 4':
            img_sonda = 'sondas/mariner4.png'
            info = '''A Mariner 4 foi a quarta de uma série de naves espaciais usadas para a exploração planetária em modo de aproximação em voo, tendo feito a primeira aproximação bem-sucedida ao planeta Marte, enviando as primeiras fotografias da superfície marciana.
            Foi a missão responsável por capturar as primeiras imagens de um outro planeta enviadas do espaço. A Mariner 4 foi projetada para conduzir observações científicas detalhadas de Marte e transmitir estas observações à Terra.'''
            fonte = 'https://pt.wikipedia.org/wiki/Mariner_4'
            dados_coletados = ['Atmosfera:',
                                    '- Detectou que a atmosfera marciana era extremamente fina, composta majoritariamente de dióxido de carbono (CO₂), com uma pressão superficial cerca de 0,6% da terrestre.',
                                'Temperatura:',
                                    '- As medições sugeriram que a temperatura em Marte era extremamente baixa, chegando a aproximadamente -100°C.',
                                'Campo Magnético:',
                                    '- Não foi detectado um campo magnético global significativo, sugerindo que Marte não possuía um núcleo dinâmico ativo como o da Terra.',
                                'Radiação:',
                                    '- Detectou níveis de radiação espacial, importantes para futuras missões tripuladas, mostrando que os astronautas precisariam de proteção significativa.']

        else:
            img_sonda = 'sondas/mariner9.png'
            info = 'A Mariner 9 da NASA venceu a soviética Mars 2 — que teve uma vantagem de 11 dias — para Marte, tornando-se a primeira espaçonave a orbitar outro planeta. A sonda mapeou 85% da superfície marciana e enviou mais de 7.000 fotos, incluindo imagens de Olympus Mons, Valles Marineris e Phobos e Deimos.'
            fonte = 'https://science.nasa.gov/mission/mariner-9/'
            dados_coletados = ['Exploração de características geológicas:',
                                    '- Canais de escoamento: Evidências de erosão sugeriram a possível presença de água no passado marciano.',
                                    '- Vulcões: Descobriu o Monte Olimpo, o maior vulcão do sistema solar.',
                                    '- Valles Marineris: Um sistema de cânions gigantes, com 4.000 km de comprimento e até 7 km de profundidade.',
                                    '- Calotas polares: Confirmou que as calotas polares continham dióxido de carbono congelado e provavelmente gelo de água.',
                               'Tempestades de poeira:',
                                    '- A Mariner 9 chegou durante uma tempestade global de poeira, oferecendo a primeira observação direta de fenômenos meteorológicos marcianos em grande escala.',
                                'Atmosfera:',
                                    '- Detalhou melhor a composição atmosférica, confirmando a predominância de dióxido de carbono e traços de outros gases.',
                                'Mapeamento extensivo:',
                                    '- Criou um mapa detalhado de 85% da superfície marciana, revelando muito mais diversidade geológica do que a Mariner 4 sugeria.']

        nomes = ['Fobos','Deimos']
        luas = ['luas/marte/fobos.jpg', 'luas/marte/deimos.jpg']
        luas_e_nomes = zip(nomes, luas)

        temperatura = 'Varia entre -123 e 36'
        moons = 'Fobos e Deimos'
        gravidade = 3.73
        
        planet = 'planetas/marte.jpg'

        resultado = mmc(marte, terra)
        resultado = int(resultado/60)

        if resultado >= 24:
            resultado /= 24
        return render_template('index.html', resultado = int(resultado), valor = valor, sonda = sonda, temperatura = temperatura, planet = planet, gravidade = gravidade, img_sonda = img_sonda, moons = moons, luas_e_nomes = luas_e_nomes, tema = tema, dia = dia, info = info, fonte = fonte, dados_coletados = dados_coletados, sol = sol, orbita = orbita, superficie = superficie, link = link, tempo = tempo)

    elif valor == 'jupiter':
        valor = "Júpiter"
        minutos = tempoEnvio(dist_Jup)
        minutos = minutos/60
        tempo = f'{minutos:.2f} minutos'  

        sol = '778.500.000'
        orbita = '12 anos'
        superficie = '6,142 × 10^10'
        dia = f'{dJup} horas.'
        link = 'https://g.co/kgs/v1LzMtj'

        sondas = ['Galileo','Juno']
        sonda = random.choice(sondas)
        if sonda == 'Galileo':
            img_sonda = 'sondas/galileo.png'
            info = 'Galileu orbitou Júpiter por quase oito anos e fez passagens próximas por todas as principais luas do planeta. Sua câmera e nove outros instrumentos enviaram relatórios que permitiram aos cientistas determinar, entre outras coisas, que a lua gelada de Júpiter, Europa, provavelmente tem um oceano subterrâneo com mais água do que a quantidade total encontrada no oceano da Terra. Ele descobriu que os vulcões da lua Io repetidamente e rapidamente ressurgem o pequeno mundo. A espaçonave enviou dados indicando que a lua gigante de Júpiter, Ganimedes, possui seu próprio campo magnético. Galileu até carregou uma pequena sonda que implantou e enviou para o fundo da atmosfera de Júpiter. A sonda fez leituras por quase uma hora antes de ser esmagada por uma pressão avassaladora.'
            fonte = 'https://science.nasa.gov/mission/galileo/'
            dados_coletados = ['Atmosfera de Júpiter:',
                                    '- A Galileo forneceu informações detalhadas sobre a composição atmosférica de Júpiter, detectando complexos padrões de nuvens, vórtices e tempestades. A famosa Grande Mancha Vermelha de Júpiter foi observada de perto, e a sonda revelou detalhes sobre os ventos e as temperaturas nas diferentes camadas da atmosfera.',
                               'Luas de Júpiter:',
                                    '- Io: A sonda encontrou evidências de vulcões ativos, como o vulcão Pele, e uma atmosfera fina, composta principalmente de enxofre e dióxido de enxofre. Isso confirmou que Io é o corpo mais geologicamente ativo do Sistema Solar.',
                                    '- Europa: A Galileo forneceu dados sobre uma superfície de gelo muito suave e homogênea, sugerindo a presença de um oceano de água líquida sob a crosta de gelo, o que aumentou as especulações sobre a possibilidade de vida ali.',
                                    '- Ganimedes: A sonda detectou um campo magnético ao redor de Ganimedes, o que é único entre as luas do Sistema Solar, indicando que a lua tem um núcleo metálico e um campo magnético próprio.',
                                    '- Calisto: Os dados indicaram que Calisto pode ter uma crosta de gelo profunda e uma superfície antiga e altamente craterada.',
                                'Anéis de Júpiter:',
                                    '- Descobriu que Júpiter tem anéis finos compostos principalmente de partículas pequenas e escuras.']
            
        else:
            img_sonda = 'sondas/juno.png'
            info = 'Desde que chegou a Júpiter em 2016, a sonda espacial Juno da NASA tem sondado abaixo das nuvens densas e proibitivas que circundam o planeta gigante – o primeiro orbitador a olhar tão de perto. Ela busca respostas para perguntas sobre a origem e evolução de Júpiter, nosso sistema solar e planetas gigantes em todo o cosmos.'
            fonte = 'https://science.nasa.gov/mission/juno/'
            dados_coletados = ['Composição e Atmosfera:',
                                    '- Forneceu informações sobre a composição interna de Júpiter, sugerindo que o planeta pode ter uma camada interna de hidrogênio metálico e um núcleo que pode ser maior do que o esperado.',
                                    '- Investigou as camadas mais profundas da atmosfera de Júpiter, revelando as dinâmicas complexas das nuvens e os padrões de tempestades, incluindo novos detalhes sobre a Grande Mancha Vermelha, que se mostrou muito mais dinâmica do que se imaginava.',
                                'Campo Magnético:',
                                    '- Revelou que o campo magnético de Júpiter é mais forte e mais complexo do que os cientistas haviam previsto, com áreas de campo magnético extremamente poderosas perto dos polos.',
                                'Auroras:',
                                    '- A sonda detectou auroras intensas nos polos de Júpiter, muito mais energéticas do que as da Terra, causadas pela interação com as partículas carregadas que formam o intenso cinturão de radiação do planeta.',
                                'Anéis e Luas:',
                                    '- Enquanto a Juno não tem foco principal nas luas, ela passou por algumas delas, e os dados ajudaram a confirmar a presença de anéis finos e fracos ao redor de Júpiter, observados pela Galileo.']

        nomes = ['Europa','Ganímedes','Io']
        luas = ['luas/jupiter/europa.jpg', 'luas/jupiter/Ganímedes.jpg', 'luas/jupiter/Io.jpg']
        luas_e_nomes = zip(nomes, luas)
        
        temperatura = 'Média de -153'
        moons = 'Jupiter possui 95 luas dentre elas são: Europa, Ganímedes, Io, Calicore, Amalteia, Lisiteia, Euporia, Carme, Adrasteia, Himalia, S/2003 J 19, Esponde, Calique, Ortósia, Tebe, Erinome, Elara, Júpiter LII, Megaclite, Telxinoi, Harpalique, Euquelade, Caldene, Cilene, Helique, Aitne, Hermipe, Júpiter LI, Pasite, Euante, Autonoe, Ananke, Sinope, Iocasta, Tione, Coré, Mneme, Métis, Praxidique, Isonoe, Euridome, Temisto, Carpo, Caliroe, Pasife, Arque, Dia, Herse.'
        gravidade = 24.79

        planet = 'planetas/jupiter.jpg'

        resultado = mmc(jupiter, terra)
        resultado = int(resultado/60)

        if resultado >= 24:
            resultado /= 24

        return render_template('index.html', resultado = int(resultado), valor = valor, sonda = sonda, temperatura = temperatura, planet = planet, gravidade = gravidade, img_sonda = img_sonda, moons = moons, luas_e_nomes = luas_e_nomes, tema = tema, dia = dia, info = info, fonte = fonte, dados_coletados = dados_coletados, sol = sol, orbita = orbita, superficie = superficie, link = link, tempo = tempo)

    elif valor == 'saturno':
        valor = "Saturno"
        minutos = tempoEnvio(dist_Sat)
        minutos = minutos/60
        tempo = f'{minutos:.2f} minutos'  

        sol = '1,434 × 10^9'
        orbita = 'aproximadamente 30 anos'
        superficie = '4,27 × 10^10'
        dia = f'{dSat} horas.'
        link = 'https://g.co/kgs/6CdpoGB'

        sondas = ['Voyager 1', 'Voyager 2']
        sonda = random.choice(sondas)
        if sonda == 'Voyager 1':
            img_sonda = 'sondas/voyager1.png'
            info = '''Nenhuma nave espacial foi mais longe que a Voyager 1 da NASA. Lançada em 1977 para voar por Júpiter e Saturno, a Voyager 1 cruzou o espaço interestelar em agosto de 2012 e continua coletando dados. 
            A Voyager 1 vem explorando nosso sistema solar desde 1977. A sonda está agora no espaço interestelar, a região fora da heliopausa, ou a bolha de partículas energéticas e campos magnéticos do Sol. A Voyager 1 foi lançada depois da Voyager 2, mas por causa de uma rota mais rápida, ela saiu do cinturão de asteroides antes de sua gêmea, e ultrapassou a Voyager 2 em 15 de dezembro de 1977.'''
            fonte = 'https://science.nasa.gov/mission/voyager/voyager-1/'
            dados_coletados = ['Anéis de Saturno: Voyager 1 revelou detalhes sobre os anéis de Saturno, mostrando a estrutura complexa dos anéis A, B e C, além de detectar as lacunas entre eles, como a famosa lacuna de Cassini. A sonda também detectou a composição e as partículas presentes nos anéis, que variam de pó fino a rochas maiores.',
                               'Atividade atmosférica: A sonda observou tempestades intensas na atmosfera de Saturno, incluindo a Grande Mancha Branca, uma enorme tempestade de longa duração, e o comportamento das nuvens nas latitudes mais altas.',
                               'Composição da atmosfera: A Voyager 1 mediu a composição da atmosfera de Saturno, encontrando uma mistura de hidrogênio e hélio, com pequenas quantidades de metano, amônia e outros compostos.',
                               'Luvas de Saturno: A sonda passou perto de várias luas, incluindo Titã, a maior lua de Saturno, que foi observada com uma densa atmosfera, composta principalmente de nitrogênio. A sonda também captou dados de outras luas, como Mimas, Encélado, Tétis, Dione, Rhea, entre outras.']

        else:
            img_sonda = 'sondas/voyager2.png'
            info = '''A Voyager 2 é a única nave espacial a visitar Urano e Netuno. A sonda está agora no espaço interestelar, a região fora da heliopausa, ou a bolha de partículas energéticas e campos magnéticos do Sol.
            A Voyager 2 da NASA é a segunda nave espacial a entrar no espaço interestelar. Em 10 de dezembro de 2018, a nave espacial se juntou à sua gêmea – Voyager 1 – como os únicos objetos feitos pelo homem a entrar no espaço entre as estrelas.'''
            fonte = 'https://science.nasa.gov/mission/voyager/voyager-2/'
            dados_coletados = ['Mais detalhes sobre os anéis: Voyager 2 também investigou os anéis de Saturno e fez observações complementares sobre suas características e composição. A sonda foi capaz de estudar a estrutura dos anéis e fornecer imagens de alta resolução.',
                               'Interações com Titã: A Voyager 2 passou a uma distância um pouco maior de Titã, mas ainda assim foi capaz de enviar dados valiosos sobre a lua e sua espessa atmosfera. Ela não pode penetrar na densa atmosfera de Titã, mas ajudou a identificar que a lua tinha uma atmosfera rica em nitrogênio e compostos orgânicos.',
                               'Estudos de satélites e luas: Durante o seu sobrevoo, a Voyager 2 também estudou luas menores de Saturno, com imagens e dados que ajudaram a entender as formas e a evolução dessas luas.']

        nomes = ['Titã','Encélado','Mimas','Dione','Jápeto','Tétis']
        luas = ['luas/saturno/titã.jpg', 'luas/saturno/Encélado.png', 'luas/saturno/Mimas.jpg', 'luas/saturno/Dione.jpg', 'luas/saturno/Jápeto.jpg', 'luas/saturno/Tétis.jpg']
        luas_e_nomes = zip(nomes, luas)

        temperatura = 'Média de -184'
        moons = 'Saturno Possui 146 luas dentre elas são: Titã, Encélado, Mimas, Dione, Jápeto, Tétis, Hipérion, Epimeteu, Telesto, Febe, Dafne, Reia, Paaliaq, Erriapo, Ijiraq, Kiviuq, Narvi, Albiorix, Mundilfari, Skathi, Tarvos, Siarnaq, Thrymr, Suttungr, Ymir, Metone, Palene, Aegir, Anteia, Aegaeon, Bestla, Fornjot, Hyrrokkin, Járnsaxa, Farbauti, Fenrir, Loge, Bergelmir, Greip, Bebhionn, Polideuces, Skoll, Tarqeq, Surtur, S/2007 S3, S/2007 S2, S/2004 S12, S/2004 S17, S/2006 S3, S/2006 S1.'
        gravidade = 10.44

        planet = 'planetas/saturno.jpg'

        resultado = mmc(saturno, terra)
        resultado = int(resultado/60)

        if resultado >= 24:
            resultado /= 24

        return render_template('index.html', resultado = int(resultado), valor = valor, sonda = sonda, temperatura = temperatura, planet = planet, gravidade = gravidade, img_sonda = img_sonda, moons = moons, luas_e_nomes = luas_e_nomes, tema = tema, dia = dia, info = info, fonte = fonte, dados_coletados = dados_coletados, sol = sol, orbita = orbita, superficie = superficie, link = link, tempo = tempo)

    elif valor == 'urano':
        valor = "Urano"
        minutos = tempoEnvio(dist_Ura)
        minutos = minutos/60
        tempo = f'{minutos:.2f} minutos'
        
        sol = '2,871 × 10^9'
        orbita = 'aproximadamente 84 anos'
        superficie = '8,083 × 10^9'
        dia = f'{dUra} horas.'
        link = 'https://www.google.com/search?kgmid=%2Fm%2F0c3ss&hl=pt-BR&q=Urano&shndl=0&source=sh%2Fx%2Fkp%2Fosrp%2Fm5%2F1&kgs=14281723cd9ad04a'

        sonda = 'Voyager 2'
        img_sonda = 'sondas/voyager2.png'
        info = '''A Voyager 2 é a única nave espacial a visitar Urano e Netuno. A sonda está agora no espaço interestelar, a região fora da heliopausa, ou a bolha de partículas energéticas e campos magnéticos do Sol.
        A Voyager 2 da NASA é a segunda nave espacial a entrar no espaço interestelar. Em 10 de dezembro de 2018, a nave espacial se juntou à sua gêmea – Voyager 1 – como os únicos objetos feitos pelo homem a entrar no espaço entre as estrelas.'''
        fonte = 'https://science.nasa.gov/mission/voyager/voyager-2/'

        dados_coletados = ['Atmosfera de Urano:',
                                '- Composição: A atmosfera de Urano é composta principalmente por hidrogênio (83%), hélio (15%) e metano (2%). O metano, que absorve luz vermelha, é responsável pela coloração azul esverdeada do planeta.',
                                '- Temperatura: Urano tem uma temperatura média de cerca de -224°C, tornando-o um dos planetas mais frios do Sistema Solar.',
                                '- Ventos: A sonda detectou ventos em Urano com velocidades de até 900 km/h, soprando em direção ao oeste.',
                                '- Camadas atmosféricas: A atmosfera de Urano possui camadas distintas, com nuvens de metano nas altitudes mais altas e nuvens de amônia em profundidades maiores.',
                                'Campo magnético:',
                                '- Campo Magnético Descentralizado: O campo magnético de Urano é bastante peculiar e descentrado, com um ângulo de inclinação de cerca de 59° em relação ao eixo de rotação do planeta, ao contrário da Terra, que tem um campo magnético mais alinhado.',
                                '- Intensidade do Campo Magnético: A sonda revelou que o campo magnético de Urano é mais forte do que o esperado, com uma intensidade muito maior nas proximidades dos polos.',
                           'Anéis:',
                                '- Anéis de Urano: A Voyager 2 detectou 11 anéis em torno de Urano, sendo eles mais tênues e menos visíveis do que os anéis de Saturno. Estes anéis são compostos principalmente por partículas escuras, com tamanhos que variam de micrômetros a metros.',
                                '- Estrutura do Anel: Os anéis estão agrupados em três principais zonas: anéis internos mais estreitos e mais escuros, e anéis externos mais brilhantes e mais dispersos.',
                            'Luas de Urano:',
                                '- Descoberta de luas adicionais: A Voyager 2 confirmou a existência de 10 luas, além das 5 já conhecidas, durante sua passagem por Urano.',
                                '- Características das luas: As luas de Urano variam em tamanho e características geológicas. A maior lua, Titânia, tem uma superfície cheia de vales e falhas, enquanto Miranda apresenta grandes descontinuidades geológicas e grandes falhas.',
                                '- Géiseres em Miranda: A Voyager observou evidências de atividade geotérmica em Miranda, incluindo geisers ou atividades que poderiam ser devidas a interação gravitacional com Urano.',
                                'Inclinação do eixo: Urano tem uma rotação extrema, com o eixo de rotação inclinado em cerca de 98°, o que faz com que o planeta tenha uma forma quase "deitada", em comparação com outros planetas do Sistema Solar.']
        
        nomes = ['Titânia','Miranda','Umbriel','Ariel','Oberon']
        luas = ['luas/urano/Titânia.jpg', 'luas/urano/Miranda.png', 'luas/urano/Umbriel.jpg', 'luas/urano/Ariel.jpg', 'luas/urano/Oberon.jpg']
        luas_e_nomes = zip(nomes, luas)

        temperatura = 'Média de -184'
        moons = 'Urano Possui 27 luas dentre elas são: Titânia, Miranda, Umbriel, Ariel, Oberon, Setebos, Puck, Desdémona, Cordélia, Sicorax, Trínculo, Bianca, Perdita, Ferdinando, Cupido, Calibã, Próspero, Pórcia, Estefano, Créssida, Rosalinda, Julieta, Mab, Francisco, Ofélia, Margarida.'
        gravidade = 8.87

        planet = 'planetas/urano.png'

        resultado = mmc(urano, terra)
        resultado = int(resultado/60)

        if resultado >= 24:
            resultado /= 24

        return render_template('index.html', resultado = int(resultado), valor = valor, sonda = sonda, temperatura = temperatura, planet = planet, gravidade = gravidade, img_sonda = img_sonda, moons = moons, luas_e_nomes = luas_e_nomes, tema = tema, dia = dia, info = info, fonte = fonte, dados_coletados = dados_coletados, sol = sol, orbita = orbita, superficie = superficie, link = link, tempo = tempo)

    elif valor == 'netuno':
        valor = "Netuno"
        minutos = tempoEnvio(dist_Net)
        minutos = minutos/60
        tempo = f'{minutos:.2f} minutos'

        sol = '4,495 × 10^9'
        orbita = 'aproximadamente 165 anos'
        superficie = '7,618 × 10^9'
        dia = f'{dNet} horas.'
        link = 'https://g.co/kgs/MFrB8gu'

        sonda = 'Voyager 2'
        img_sonda = 'sondas/voyager2.png'
        info = '''A Voyager 2 é a única nave espacial a visitar Urano e Netuno. A sonda está agora no espaço interestelar, a região fora da heliopausa, ou a bolha de partículas energéticas e campos magnéticos do Sol.
        A Voyager 2 da NASA é a segunda nave espacial a entrar no espaço interestelar. Em 10 de dezembro de 2018, a nave espacial se juntou à sua gêmea – Voyager 1 – como os únicos objetos feitos pelo homem a entrar no espaço entre as estrelas.'''
        fonte = 'https://science.nasa.gov/mission/voyager/voyager-2/'

        dados_coletados = ['Atmosfera:',
                                '- Composição atmosférica: Netuno tem uma atmosfera composta principalmente de hidrogênio (83%), hélio (15%) e metano (2-3%). O metano é o que dá a Netuno sua coloração azul característica, pois absorve a luz vermelha e reflete a azul.',
                                '- Nuvens e tempestades: A Voyager 2 observou tempestades intensas, incluindo a famosa Grande Mancha Escura, que era uma grande tempestade atmosférica semelhante à Grande Mancha Vermelha de Júpiter, mas muito menor. Essa mancha escura foi mais tarde observada se dissipando.',
                                '- Ventos supersônicos: Netuno possui ventos extremamente fortes, que podem atingir até 2.400 km/h, mais rápidos do que os ventos mais fortes registrados em Júpiter e Saturno.',
                            'Anéis de Netuno:',
                                '- A Voyager 2 confirmou a presença de anéis ao redor de Netuno, que antes eram apenas sugeridos por observações telescópicas. Netuno tem um sistema de anéis bastante complexo, composto por anéis principais, finos e escuros.',
                                '- Anéis principais: Existem cinco anéis conhecidos, sendo eles muito mais tênues e escuros do que os anéis de Saturno.',
                                '- Estruturas em arco: Um dos anéis de Netuno, o anel Adams, possui características peculiares, como arcos brilhantes e densos, que são incomuns no Sistema Solar.',
                            'Luas de Netuno:',
                                '- Tritão: A lua mais notável de Netuno, Tritão, foi observada em detalhes. A Voyager 2 descobriu que Tritão é uma lua retrógrada (ou seja, ela gira na direção oposta à de Netuno). Isso sugere que Tritão pode ter sido um objeto capturado, possivelmente de uma órbita exterior.',
                                '- A sonda encontrou evidências de gêiseres ativos na superfície de Tritão, que expeliam nitrogênio líquido e vapor de água.',
                                '- Superfície de Tritão: A superfície de Tritão é coberta por gelo, principalmente de nitrogênio, e apresenta vastas planícies congeladas, montanhas e regiões geológicas de aparência jovem.',
                            'Campos Magnéticos:',
                                '- A sonda mediu o campo magnético de Netuno, que é inclinado em relação ao seu eixo de rotação, o que sugere que o planeta possui um campo magnético complexo e assimétrico. Ele também é mais intenso que o de Urano.',
                            'Temperatura e Clima:',
                                '- Netuno é extremamente frio, com temperaturas que atingem cerca de -218°C. Mesmo com essa temperatura extremamente baixa, o planeta ainda apresenta atividade atmosférica significativa, com ventos e tempestades fortes.']
        
        nomes = ['Tritão']
        luas = ['luas/netuno/tritao.jpg']
        luas_e_nomes = zip(nomes, luas)

        temperatura = 'Média de -223'

        gravidade = 11.15
        moons = 'Netuno Possui 14 luas dentre elas são: Tritão, Talassa, Hipocampo, Nereida, Galateia, Despina, Neso, Náiade, Halimede, Psámata, Laomedeia, Proteu, Larissa.'
        planet = 'planetas/netuno.jpg'

        resultado = mmc(netuno, terra)
        resultado = int(resultado/60)

        if resultado >= 24:
            resultado /= 24

        return render_template('index.html', resultado = int(resultado), valor = valor, sonda = sonda, temperatura = temperatura, planet = planet, gravidade = gravidade, img_sonda = img_sonda, moons = moons, luas_e_nomes = luas_e_nomes, tema = tema, dia = dia, info = info, fonte = fonte, dados_coletados = dados_coletados, sol = sol, orbita = orbita, superficie = superficie, link = link, tempo = tempo)

if __name__ == "__main__":
    app.run(debug=True)