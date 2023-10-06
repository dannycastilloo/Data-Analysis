frecuencia <- c(84, 50, 100, 26, 15)
sectores <- c("x1", "x2", "x3", "x4", "x5")

barplot(frecuencia, names.arg = sectores, horiz = TRUE, col = "blue", main = "Gráfico Horizontal de Barras", xlab = "Frecuencia")