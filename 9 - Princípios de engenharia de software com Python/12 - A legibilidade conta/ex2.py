from statistics import mean

'''
Opções de nome para a primeira variável:
d, diameter, pupil_diameter, ou pupil_diameter_in_millimeters
'''

# Sample measurements of pupil diameter in mm
pupil_diameter = [3.3, 6.8, 7.0, 5.4, 2.7]

'''
Opções de nome para a segunda variável:
m, mean, mean_diameter, ou mean_pupil_diameter_in_millimeters.
'''

# Average pupil diameter from sample
mean_diameter = mean(pupil_diameter)

print(mean_diameter)

'''
O código acima demonstra o valor da legibilidade ao nomear variáveis de forma clara e descritiva. As variáveis 'pupil_diameter' e 'mean_diameter' são escolhidas entre várias opções, como 'd', 'diameter', 'm', 'mean', etc. Isso facilita a compreensão do código, tornando-o mais acessível para outros desenvolvedores e para futuras manutenções. A escolha de nomes descritivos para variáveis é uma prática recomendada em programação, pois ajuda a evitar confusões e torna o código mais intuitivo. Neste caso, 'pupil_diameter' indica claramente que se trata do diâmetro da pupila, enquanto 'mean_diameter' deixa evidente que é a média desse diâmetro. Isso melhora a legibilidade e a manutenção do código ao longo do tempo.
'''

