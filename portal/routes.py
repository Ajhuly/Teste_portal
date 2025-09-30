# rotas de links
from flask import render_template, url_for, flash, redirect
from portal import app
from portal.forms import ContatoForm

@app.route('/')
def home():
    return render_template('index.html')

# Rotas para a seção 'Sobre'
@app.route('/sobre/quem-somos')
def quem_somos():
    return render_template('sobre/quem_somos.html')

@app.route('/sobre/espaco')
def sobre_espaco():
    return render_template('sobre/espaco.html')

@app.route('/sobre/contato', methods=['GET', 'POST'])
def sobre_contato():
    form = ContatoForm()
    if form.validate_on_submit():
        # Aqui, você poderia adicionar a lógica para enviar o e-mail
        # ou salvar os dados em um banco de dados.
        # Por enquanto, vamos apenas exibir uma mensagem de sucesso.
        flash('Sua mensagem foi enviada com sucesso!', 'success')
        return redirect(url_for('sobre_contato'))
    return render_template('sobre/contato.html', form=form)

# Rotas para a seção 'Acervo & Publicações'
@app.route('/acervo/busca')
def acervo_busca():
    return render_template('acervo_publicacoes/busca.html')

@app.route('/publicacoes/teses')
def publicacoes_teses():
    return render_template('acervo_publicacoes/teses.html')

@app.route('/publicacoes/instituicao')
def publicacoes_instituicao():
    return render_template('acervo_publicacoes/instituicao.html')

# Rotas para a seção 'História & Cultura'
@app.route('/historia/memoria-imagem')
def historia_memoria_imagem():
    return render_template('historia_cultura/memoria_imagem.html')

@app.route('/historia/calendario-ciencia')
def historia_calendario_ciencia():
    return render_template('historia_cultura/calendario_ciencia.html')

@app.route('/historia/artigos/einstein')
def historia_artigos_einstein():
    return render_template('historia_cultura/artigos_einstein.html')

@app.route('/historia/artigos/feynman')
def historia_artigos_feynman():
    return render_template('historia_cultura/artigos_feynman.html')

@app.route('/historia/filmes')
def historia_filmes():
    return render_template('historia_cultura/filmes.html')

@app.route('/historia/eventos')
def historia_eventos():
    return render_template('historia_cultura/eventos.html')

# Rotas para a seção 'Ciência Aberta'
@app.route('/ciencia-aberta/apresentacao')
def ciencia_aberta_apresentacao():
    return render_template('ciencia_aberta/apresentacao.html')

@app.route('/ciencia-aberta/dataverse')
def ciencia_aberta_dataverse():
    return render_template('ciencia_aberta/dataverse.html')

@app.route('/ciencia-aberta/iniciativas')
def ciencia_aberta_iniciativas():
    return render_template('ciencia_aberta/iniciativas.html')

@app.route('/ciencia-aberta/documentacao')
def ciencia_aberta_documentacao():
    return render_template('ciencia_aberta/documentacao.html')

# Rotas para a seção 'NRI'
@app.route('/nri/atividades')
def nri_atividades():
    return render_template('nri/atividades.html')

@app.route('/nri/tcg')
def nri_tcg():
    return render_template('nri/tcg.html')

@app.route('/nri/dados-comprobatorios')
def nri_dados_comprobatorios():
    return render_template('nri/dados_comprobatorios.html')

# Rotas para a seção 'LAB3I'
@app.route('/lab3i/laboratorio')
def lab3i_laboratorio():
    return render_template('lab3i/laboratorio.html')

@app.route('/lab3i/participacao-eventos')
def lab3i_participacao_eventos():
    return render_template('lab3i/participacao_eventos.html')

@app.route('/lab3i/monitoramento-iot')
def lab3i_monitoramento_iot():
    return render_template('lab3i/monitoramento_iot.html')

@app.route('/lab3i/maddar')
def lab3i_maddar():
    return render_template('lab3i/maddar.html')

@app.route('/lab3i/integracoes-migracao')
def lab3i_integracoes_migracao():
    return render_template('lab3i/integracoes_migracao.html')

@app.route('/lab3i/formacao-cientifica')
def lab3i_formacao_cientifica():
    return render_template('lab3i/formacao_cientifica.html')

@app.route('/lab3i/visita-virtual')
def lab3i_visita_virtual():
    return render_template('lab3i/visita_virtual.html')