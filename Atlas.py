import PySimpleGUI as sg


class menu:
    def __init__(self):
        self.janela = sg.Window('Infome Seus Investimento', layout= [
            [sg.Text('Informe o valor investido todo mês: ', s=30), sg.Input(s=10, k= 'investido')],
            [sg.Text ('Informe o valor da ação: ', s=30), sg.Input(s=10, k='valor_acao')],
            [sg.Text('Informe o rendimento mensal da ação: ',  s=30), sg.Input(s=10, k= 'mensal')],
            [sg.Text('Informe o quantos meses quer investir: ', s=30), sg.Input(s=10, k= 'meses')],
            [sg.Button('Enviar'), sg.Button ('Sair')]
            ])
        
        
        
        while True:
            event, values = self.janela.read()
            
            if event == 'Sair' or event == sg.WINDOW_CLOSED:
                break
            
            elif event == 'Enviar':
                
                nova_aba = sg.Window('Seus investimentos', layout=[
                    [sg.Text('Calculo')],
                    [sg.Text(' Numero de ações: '), sg.Text(self.calculo_compra_acao(values['investido'], values['valor_acao']))],
                    [sg.Text(' valor investido nas ações: '), sg.Text(self.valor_investido(self.calculo_compra_acao(values['investido'], values['valor_acao']), values['valor_acao']))],
                    [sg.Text('Valor restante do Investimento'), sg.Text(self.sobra(self.valor_investido(self.calculo_compra_acao(values['investido'], values['valor_acao']), values['valor_acao']), values ['investido']))],
                    [sg.Text(' Valor sobre juros: '), sg.Text(self.calculo_juros_sobre_juros(self.valor_investido(self.calculo_compra_acao(values['investido'], values['valor_acao']), values['valor_acao']), values['mensal']))],
                    [sg.Text('Valor investido em meses: '), sg.Text(self.cacul0_meses_investido(self.valor_investido(self.calculo_compra_acao(values['investido'], values['valor_acao']),values ['valor_acao']), values ['mensal'], values ['meses']))]
                ])
                
                event, values = nova_aba.read() 
                
                   
        self.janela.close()
    
    def calculo_compra_acao(self, investido, valor_acao):
        
        total_acoes = float(investido) // float(valor_acao)
        return total_acoes
    
    def calculo_juros_sobre_juros(self, total_investido, mensal):
        
        calculo_total_juros = float(total_investido) + (float(total_investido) * float(mensal) / 100)
        return calculo_total_juros
    
    def valor_investido(self,total_acoes, valor_acao):
        
        total_investido = float(total_acoes) * float(valor_acao)
        return total_investido 
    
    def sobra(self,x_investido, investido):
        
        sobra = float(investido) - float(x_investido)
        return sobra

    def cacul0_meses_investido (self, total_investido, mensal, meses):
        
        total_meses = float(total_investido) * (1 + (float(mensal) / 100)) ** float(meses)
        return total_meses
menu()
