from PyQt6.QtCore import QDateTime
from PyQt6.QtCharts import QChartView, QChart, QSplineSeries, QDateTimeAxis, QValueAxis
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget


class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        chart = QChart()

        chart.setTitle("Preisverlauf")

        self.__temperature_nft1 = QSplineSeries()
        self.__temperature_nft1.setName("NFT1")

        self.__temperature_nft2 = QSplineSeries()
        self.__temperature_nft2.setName("NFT2")


        axis_datetime = QDateTimeAxis()
        axis_datetime.setFormat("hh:mm:ss")
        axis_datetime.setTitleText("Uhrzeit")

        self.__temperature_nft1.append(QDateTime(2025, 1, 20, 2, 0, 0).toMSecsSinceEpoch(), 5.0)
        self.__temperature_nft1.append(QDateTime(2025, 1, 20, 2, 45, 0).toMSecsSinceEpoch(), 3.5)
        self.__temperature_nft1.append(QDateTime(2025, 1, 20, 3, 30, 0).toMSecsSinceEpoch(), 6.0)
        self.__temperature_nft1.append(QDateTime(2025, 1, 20, 4, 15, 0).toMSecsSinceEpoch(), 9.0)
        self.__temperature_nft1.append(QDateTime(2025, 1, 20, 5, 0, 0).toMSecsSinceEpoch(), 7.5)

        # Datenpunkte für NFT2 (grüne Linie)
        self.__temperature_nft2.append(QDateTime(2025, 1, 20, 2, 0, 0).toMSecsSinceEpoch(), 5.0)
        self.__temperature_nft2.append(QDateTime(2025, 1, 20, 2, 45, 0).toMSecsSinceEpoch(), 3.5)
        self.__temperature_nft2.append(QDateTime(2025, 1, 20, 3, 30, 0).toMSecsSinceEpoch(), 2.0)
        self.__temperature_nft2.append(QDateTime(2025, 1, 20, 4, 15, 0).toMSecsSinceEpoch(), 8.0)
        self.__temperature_nft2.append(QDateTime(2025, 1, 20, 5, 0, 0).toMSecsSinceEpoch(), 9.0)

        start_datetime = QDateTime(2025, 1, 20, 2, 0, 0)
        end_datetime = QDateTime.fromString("2025-01-20_05:00:00", "yyyy-MM-dd_hh:mm:ss")

        axis_datetime.setRange(start_datetime, end_datetime)


        axis_temperature = QValueAxis()
        axis_temperature.setRange(0.0, 10.0)
        axis_temperature.setTitleText("Preis in Euro")


        chart.addSeries(self.__temperature_nft1)
        chart.addSeries(self.__temperature_nft2)


        chart.addAxis(axis_datetime, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(axis_temperature, Qt.AlignmentFlag.AlignLeft)

        self.__temperature_nft1.attachAxis(axis_datetime)
        self.__temperature_nft2.attachAxis(axis_datetime)

        self.__temperature_nft1.attachAxis(axis_temperature)
        self.__temperature_nft2.attachAxis(axis_temperature)

        self.setChart(chart)
