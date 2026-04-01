-- 1. Criação da tabela proponentes (Tabela Principal)
CREATE TABLE proponentes (
    id_proposta INTEGER PRIMARY KEY,
    uf_proponente TEXT,
    municip_proponente TEXT,
    cod_munic_ibge TEXT,
    cod_orgao_sup TEXT,
    desc_orgao_sup TEXT,
    natureza_juridica TEXT,
    nr_proposta TEXT,
    dia_prop INTEGER,
    mes_prop INTEGER,
    ano_prop INTEGER,
    dia_proposta DATE,
    cod_orgao TEXT,
    desc_orgao TEXT,
    modalidade TEXT,
    identif_proponente TEXT,
    nm_proponente TEXT,
    cep_proponente TEXT,
    endereco_proponente TEXT,
    bairro_proponente TEXT,
    nm_banco TEXT,
    situacao_conta TEXT,
    situacao_projeto_basico TEXT,
    sit_proposta TEXT,
    dia_inic_vigencia_proposta DATE,
    dia_fim_vigencia_proposta DATE,
    objeto_proposta TEXT,
    item_investimento TEXT,
    enviada_mandataria TEXT,
    nome_subtipo_proposta TEXT,
    descricao_subtipo_proposta TEXT,
    vl_global_prop NUMERIC(18,2),
    vl_repasse_prop NUMERIC(18,2),
    vl_contrapartida_prop NUMERIC(18,2),
    cd_agencia TEXT,
    cd_conta TEXT
);

-- 2. Criação da tabela convenios

CREATE TABLE convenios (
    nr_convenio INTEGER ,
    id_proposta INTEGER PRIMARY KEY, 
    dia INTEGER,
    mes INTEGER,
    ano INTEGER,
    dia_assin_conv DATE,
    sit_convenio TEXT,
    subsituacao_conv TEXT,
    situacao_publicacao TEXT,
    instrumento_ativo TEXT,
    ind_opera_obtv TEXT,
    nr_processo TEXT,
    ug_emitente TEXT,
    dia_publ_conv DATE,
    dia_inic_vigenc_conv DATE,
    dia_fim_vigenc_conv DATE,
    dia_fim_vigenc_original_conv DATE,
    dias_prest_contas INTEGER,
    dia_limite_prest_contas DATE,
    data_suspensiva DATE,
    data_retirada_suspensiva DATE,
    dias_clausula_suspensiva INTEGER,
    situacao_contratacao TEXT,
    ind_assinado TEXT,
    motivo_suspensao TEXT,
    ind_foto TEXT,
    qtde_convenios INTEGER,
    qtd_ta INTEGER,
    qtd_prorroga INTEGER,
    vl_global_conv NUMERIC(18,2),
    vl_repasse_conv NUMERIC(18,2),
    vl_contrapartida_conv NUMERIC(18,2),
    vl_empenhado_conv NUMERIC(18,2),
    vl_desembolsado_conv NUMERIC(18,2),
    vl_saldo_reman_tesouro NUMERIC(18,2),
    vl_saldo_reman_convenente NUMERIC(18,2),
    vl_rendimento_aplicacao NUMERIC(18,2),
    vl_ingresso_contrapartida NUMERIC(18,2),
    vl_saldo_conta NUMERIC(18,2),
    valor_global_original_conv NUMERIC(18,2),
    
);

-- 3. Criação da tabela situacao

CREATE TABLE situacao (
    id_proposta INTEGER,
    nr_convenio INTEGER,
    dia_historico_sit DATE,
    historico_sit TEXT,
    dias_historico_sit INTEGER,
    cod_historico_sit INTEGER,

    FOREIGN KEY (id_proposta) REFERENCES proponentes (id_proposta),
    FOREIGN KEY (id_proposta) REFERENCES convenios (id_proposta)
);

-- 4. Criação da tabela execucao_financeira
-- Chave estrangeira para proponentes
CREATE TABLE execucao_financeira (
    id_proposta INTEGER PRIMARY KEY,
    valor_total_resumo_fisico_financeiro NUMERIC(18,2),
    valor_realizado_resumo_fisico_financeiro NUMERIC(18,2),
    percentual_execucao_resumo_fisico_financeiro NUMERIC(5,2),
    FOREIGN KEY (id_proposta) REFERENCES proponentes (id_proposta)
);


-- Criando tabela de localidades a partir da tabela de proponentes
CREATE TABLE localidades AS
SELECT 
	bairro_proponente,
	cep_proponente,
	cod_munic_ibge,
	endereco_proponente,
	munic_proponente,
	uf_proponente
FROM
	proponentes
FOREIGN KEY (id_proposta) REFERENCES proponentes (id_proposta)
;

-- Criando indíces pós-carga

-- Localidades
CREATE INDEX idx_localidades_cod_munic ON localidades(cod_munic_ibge);
CREATE INDEX idx_uf ON localidades(uf_proponente);

-- Convenios
CREATE INDEX idx_convenios_nr_convenio ON convenios (nr_convenio);

-- Situacao
CREATE INDEX idx_situacao_nr_convenio ON situacao (nr_convenio);
CREATE INDEX idx_situacao_id_proposta ON situacao (id_proposta);







