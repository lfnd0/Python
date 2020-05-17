is_raining = True

print('Hoje estou com roupas ' + ('secas', 'molhadas')[is_raining])

print('Hoje estou com roupas ' + ('molhadas' if is_raining else 'secas'))
