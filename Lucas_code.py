# Importiert Klassen für Zeitverarbeitung
from PyQt6.QtCore import QDateTime, Qt

# Importiert Qt-Charts-Komponenten: Chart-Ansicht, Chart selbst, Kurvenserien, Achsen
from PyQt6.QtCharts import QChartView, QChart, QSplineSeries, QDateTimeAxis, QValueAxis

# Importiert grundlegendes Widget (für Elternklasse)
from PyQt6.QtWidgets import QWidget


# Zentrale Anzeige der GUI: ein ChartView-Widget, das ein Diagramm anzeigt
class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        # Erzeuge das Diagramm
        chart = QChart()
        chart.setTitle("Preisverlauf")  # Titel setzen

        # Erstellt die erste Spline-Serie (geglättete Linie) für NFT1
        self.__temperature_nft1 = QSplineSeries()
        self.__temperature_nft1.setName("NFT1")

        # Erstellt die zweite Spline-Serie für NFT2
        self.__temperature_nft2 = QSplineSeries()
        self.__temperature_nft2.setName("NFT2")

        # Erstellt eine Zeitachse (unten)
        axis_datetime = QDateTimeAxis()
        axis_datetime.setFormat("hh:mm:ss")  # Format der Zeitachse (nur Uhrzeit)
        axis_datetime.setTitleText("Uhrzeit")  # Titel der X-Achse

        # Fügt Datenpunkte für NFT1 hinzu (X = Zeit in Millisekunden, Y = Preis)
        self.__temperature_nft1.append(QDateTime(2025, 1, 20, 2, 0, 0).toMSecsSinceEpoch(), 5.0)
        self.__temperature_nft1.append(QDateTime(2025, 1, 20, 2, 45, 0).toMSecsSinceEpoch(), 3.5)
        self.__temperature_nft1.append(QDateTime(2025, 1, 20, 3, 30, 0).toMSecsSinceEpoch(), 6.0)
        self.__temperature_nft1.append(QDateTime(2025, 1, 20, 4, 15, 0).toMSecsSinceEpoch(), 9.0)
        self.__temperature_nft1.append(QDateTime(2025, 1, 20, 5, 0, 0).toMSecsSinceEpoch(), 7.5)

        # Fügt Datenpunkte für NFT2 hinzu
        self.__temperature_nft2.append(QDateTime(2025, 1, 20, 2, 0, 0).toMSecsSinceEpoch(), 5.0)
        self.__temperature_nft2.append(QDateTime(2025, 1, 20, 2, 45, 0).toMSecsSinceEpoch(), 3.5)
        self.__temperature_nft2.append(QDateTime(2025, 1, 20, 3, 30, 0).toMSecsSinceEpoch(), 2.0)
        self.__temperature_nft2.append(QDateTime(2025, 1, 20, 4, 15, 0).toMSecsSinceEpoch(), 8.0)
        self.__temperature_nft2.append(QDateTime(2025, 1, 20, 5, 0, 0).toMSecsSinceEpoch(), 9.0)

        # Start- und Endzeit für die X-Achse definieren
        start_datetime = QDateTime(2025, 1, 20, 2, 0, 0)
        end_datetime = QDateTime.fromString("2025-01-20_05:00:00", "yyyy-MM-dd_hh:mm:ss")
        axis_datetime.setRange(start_datetime, end_datetime)

        # Erstellt die Y-Achse (Preis in Euro)
        axis_temperature = QValueAxis()
        axis_temperature.setRange(0.0, 10.0)  # Y-Achse von 0 bis 10
        axis_temperature.setTitleText("Preis in Euro")  # Titel der Y-Achse

        # Serien dem Diagramm hinzufügen
        chart.addSeries(self.__temperature_nft1)
        chart.addSeries(self.__temperature_nft2)

        # Achsen zum Diagramm hinzufügen und ausrichten
        chart.addAxis(axis_datetime, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(axis_temperature, Qt.AlignmentFlag.AlignLeft)

        # Serien mit Achsen verbinden
        self.__temperature_nft1.attachAxis(axis_datetime)
        self.__temperature_nft2.attachAxis(axis_datetime)
        self.__temperature_nft1.attachAxis(axis_temperature)
        self.__temperature_nft2.attachAxis(axis_temperature)

        # Das konfigurierte Chart in der Ansicht anzeigen
        self.setChart(chart)
