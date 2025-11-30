larg = float (input('largura da parede em m'))
alt = float ( input('altura da parede em m1')) 
area = larg * alt
print ('Sua parede tem dimensao de {}x{} e sua área é de {}m^2'.format(larg, alt, area))
tinta = area / 2
# a cada 2m^2 precisso de 1L de tinta
print (' para pintar essa parede voce precisa de {}L de tinta'.format(tinta))