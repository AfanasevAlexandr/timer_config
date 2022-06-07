# рабочая версия конфигуратора. убраны секунды.
from PyQt5 import QtWidgets, uic
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
from datetime import datetime

app = QtWidgets.QApplication([])
ui = uic.loadUi("timerConfigGui.ui")  # ссылка не файл интерфейса

serial = QSerialPort()
serial.setBaudRate(115200)

portList = []
data = []
settingsReadKey = 0
minutes = 0
hours = 0
date = 0
month = 0
year = 0
day = ''

for port in QSerialPortInfo().availablePorts():  # ищем СОМ порты
    portList.append(port.portName())  # создаем массив с портами
ui.comPortBox.addItems(portList)  # заполняем комбобокс с портами


def comOpen():  # открытие порта
    serial.setPortName(ui.comPortBox.currentText())
    serial.open(QIODevice.ReadWrite)


def comClose():  # закрытие порта
    serial.close()


def comSend(key=999, param=999):  # отправка пакетав в порт в виде КЛЮЧ,ПАРАМЕТР;
    sendData = ''
    sendData = str(key) + ',' + str(param) + ';'
    print(f'Отправлено {sendData}')
    serial.write(sendData.encode())


def comRead():
    global settingsReadKey
    com_received_data = ''
    if settingsReadKey == 0:  # автоматическое получение настроек с плк при подключении
        settingsReadKey = 1
        #com_send(key=200)  # автоматическое получение настроек с плк при подключении
    try:
        com_received_data = str(serial.readLine(), 'utf-8').strip().split(',')
        for element in range(len(com_received_data)):
            com_received_data[element] = int(com_received_data[element])
    except:
        print('Ошибка данных порта')
        ui.statusbar.showMessage('Внимаие! Ошибка данных СОМ-порта.')
    print(f'Принято: {com_received_data}')

    try:
        if com_received_data[0] < 150:  # передача настроек с компа в плк. получает от плк номер нужного параметра и отдает его ГОТОВО!!!
            if com_received_data[0] == -1:  # формирование массива с параметрами
                global data
                data = [0] * 120  # очищаем массив с параметрами перед генерацией
                # out1 ponedelnik
                if ui.out1ponC.isChecked(): data[0] = 10000
                data[0] += ui.out1ponOnHoursS.value() * 60 + ui.out1ponOnMinsS.value()
                data[1] = ui.out1ponOffHoursS.value() * 60 + ui.out1ponOffMinsS.value()

                # out1 vtornik
                if ui.out1vtorC.isChecked(): data[2] = 10000
                data[2] += ui.out1vtorOnHoursS.value() * 60 + ui.out1vtorOnMinsS.value()
                data[3] = ui.out1vtorOffHoursS.value() * 60 + ui.out1vtorOffMinsS.value()

                # ou1 sreda
                if ui.out1sredC.isChecked(): data[4] = 10000
                data[4] += ui.out1sredOnHoursS.value() * 60 + ui.out1sredOnMinsS.value()
                data[5] = ui.out1sredOffHoursS.value() * 60 + ui.out1sredOffMinsS.value()

                # out1 chetverg
                if ui.out1chetC.isChecked(): data[6] = 10000
                data[6] += ui.out1chetOnHoursS.value() * 60 + ui.out1chetOnMinsS.value()
                data[7] = ui.out1chetOffHoursS.value() * 60 + ui.out1chetOffMinsS.value()

                # out1 pyatnitsa
                if ui.out1pyatC.isChecked(): data[8] = 10000
                data[8] += ui.out1pyatOnHoursS.value() * 60 + ui.out1pyatOnMinsS.value()
                data[9] = ui.out1pyatOffHoursS.value() * 60 + ui.out1pyatOffMinsS.value()

                # out1 subbota
                if ui.out1subC.isChecked(): data[10] = 10000
                data[10] += ui.out1subOnHoursS.value() * 60 + ui.out1subOnMinsS.value()
                data[11] = ui.out1subOffHoursS.value() * 60 + ui.out1subOffMinsS.value()

                # out1 voskresene
                if ui.out1voskC.isChecked(): data[12] = 10000
                data[12] += ui.out1voskOnHoursS.value() * 60 + ui.out1voskOnMinsS.value()
                data[13] = ui.out1voskOffHoursS.value() * 60 + ui.out1voskOffMinsS.value()

                # OUT2 PON
                if ui.out2ponC.isChecked(): data[14] = 10000
                data[14] += ui.out2ponOnHoursS.value() * 60 + ui.out2ponOnMinsS.value()
                data[15] = ui.out2ponOffHoursS.value() * 60 + ui.out2ponOffMinsS.value()
                # out2 vtornik
                if ui.out2vtorC.isChecked(): data[16] = 10000
                data[16] += ui.out2vtorOnHoursS.value() * 60 + ui.out2vtorOnMinsS.value()
                data[17] = ui.out2vtorOffHoursS.value() * 60 + ui.out2vtorOffMinsS.value()

                # out2 sreda
                if ui.out2sredC.isChecked(): data[18] = 10000
                data[18] += ui.out2sredOnHoursS.value() * 60 + ui.out2sredOnMinsS.value()
                data[19] = ui.out2sredOffHoursS.value() * 60 + ui.out2sredOffMinsS.value()

                # out2 chetverg
                if ui.out2chetC.isChecked(): data[20] = 10000
                data[20] += ui.out2chetOnHoursS.value() * 60 + ui.out2chetOnMinsS.value()
                data[21] = ui.out2chetOffHoursS.value() * 60 + ui.out2chetOffMinsS.value()

                # out2 pyatnitsa
                if ui.out2pyatC.isChecked(): data[22] = 10000
                data[22] += ui.out2pyatOnHoursS.value() * 60 + ui.out2pyatOnMinsS.value()
                data[23] = ui.out2pyatOffHoursS.value() * 60 + ui.out2pyatOffMinsS.value()

                # out2 subbota
                if ui.out2subC.isChecked(): data[24] = 10000
                data[24] += ui.out2subOnHoursS.value() * 60 + ui.out2subOnMinsS.value()
                data[25] = ui.out2subOffHoursS.value() * 60 + ui.out2subOffMinsS.value()

                # out2 voskresene
                if ui.out2voskC.isChecked(): data[26] = 10000
                data[26] += ui.out2voskOnHoursS.value() * 60 + ui.out2voskOnMinsS.value()
                data[27] = ui.out2voskOffHoursS.value() * 60 + ui.out2voskOffMinsS.value()

                # out3 pon
                if ui.out3ponC.isChecked(): data[28] = 10000
                data[28] += ui.out3ponOnHoursS.value() * 60 + ui.out3ponOnMinsS.value()
                data[29] = ui.out3ponOffHoursS.value() * 60 + ui.out3ponOffMinsS.value()

                # out3 vtornik
                if ui.out3vtorC.isChecked(): data[30] = 10000
                data[30] += ui.out3vtorOnHoursS.value() * 60 + ui.out3vtorOnMinsS.value()
                data[31] = ui.out3vtorOffHoursS.value() * 60 + ui.out3vtorOffMinsS.value()

                # ou1 sreda
                if ui.out3sredC.isChecked(): data[32] = 10000
                data[32] += ui.out3sredOnHoursS.value() * 60 + ui.out3sredOnMinsS.value()
                data[33] = ui.out3sredOffHoursS.value() * 60 + ui.out3sredOffMinsS.value()

                # out3 chetverg
                if ui.out3chetC.isChecked(): data[34] = 10000
                data[34] += ui.out3chetOnHoursS.value() * 60 + ui.out3chetOnMinsS.value()
                data[35] = ui.out3chetOffHoursS.value() * 60 + ui.out3chetOffMinsS.value()

                # out3 pyatnitsa
                if ui.out3pyatC.isChecked(): data[36] = 10000
                data[36] += ui.out3pyatOnHoursS.value() * 60 + ui.out3pyatOnMinsS.value()
                data[37] = ui.out3pyatOffHoursS.value() * 60 + ui.out3pyatOffMinsS.value()
                # out3 subbota
                if ui.out3subC.isChecked(): data[38] = 10000
                data[38] += ui.out3subOnHoursS.value() * 60 + ui.out3subOnMinsS.value()
                data[39] = ui.out3subOffHoursS.value() * 60 + ui.out3subOffMinsS.value()

                # out3 voskresene
                if ui.out3voskC.isChecked(): data[40] = 10000
                data[40] += ui.out3voskOnHoursS.value() * 60 + ui.out3voskOnMinsS.value()
                data[41] = ui.out3voskOffHoursS.value() * 60 + ui.out3voskOffMinsS.value()

                # out4 pon
                if ui.out4ponC.isChecked(): data[42] = 10000
                data[42] += ui.out4ponOnHoursS.value() * 60 + ui.out4ponOnMinsS.value()
                data[43] = ui.out4ponOffHoursS.value() * 60 + ui.out4ponOffMinsS.value()

                # out4 vtornik
                if ui.out4vtorC.isChecked(): data[44] = 10000
                data[44] += ui.out4vtorOnHoursS.value() * 60 + ui.out4vtorOnMinsS.value()
                data[45] = ui.out4vtorOffHoursS.value() * 60 + ui.out4vtorOffMinsS.value()

                # ou1 sreda
                if ui.out4sredC.isChecked(): data[46] = 10000
                data[46] += ui.out4sredOnHoursS.value() * 60 + ui.out4sredOnMinsS.value()
                data[47] = ui.out4sredOffHoursS.value() * 60 + ui.out4sredOffMinsS.value()

                # out4 chetverg
                if ui.out4chetC.isChecked(): data[48] = 10000
                data[48] += ui.out4chetOnHoursS.value() * 60 + ui.out4chetOnMinsS.value()
                data[49] = ui.out4chetOffHoursS.value() * 60 + ui.out4chetOffMinsS.value()
                # out4 pyatnitsa
                if ui.out4pyatC.isChecked(): data[50] = 10000
                data[50] += ui.out4pyatOnHoursS.value() * 60 + ui.out4pyatOnMinsS.value()
                data[51] = ui.out4pyatOffHoursS.value() * 60 + ui.out4pyatOffMinsS.value()

                # out4 subbota
                if ui.out4subC.isChecked(): data[52] = 10000
                data[52] += ui.out4subOnHoursS.value() * 60 + ui.out4subOnMinsS.value()
                data[53] = ui.out4subOffHoursS.value() * 60 + ui.out4subOffMinsS.value()

                # out4 voskresene
                if ui.out4voskC.isChecked(): data[54] = 10000
                data[54] += ui.out4voskOnHoursS.value() * 60 + ui.out4voskOnMinsS.value()
                data[55] = ui.out4voskOffHoursS.value() * 60 + ui.out4voskOffMinsS.value()

                # out5 pon
                if ui.out5ponC.isChecked(): data[56] = 10000
                data[56] += ui.out5ponOnHoursS.value() * 60 + ui.out5ponOnMinsS.value()
                data[57] = ui.out5ponOffHoursS.value() * 60 + ui.out5ponOffMinsS.value()

                # out5 vtornik
                if ui.out5vtorC.isChecked(): data[58] = 10000
                data[58] += ui.out5vtorOnHoursS.value() * 60 + ui.out5vtorOnMinsS.value()
                data[59] = ui.out5vtorOffHoursS.value() * 60 + ui.out5vtorOffMinsS.value()

                # ou1 sreda
                if ui.out5sredC.isChecked(): data[60] = 10000
                data[60] += ui.out5sredOnHoursS.value() * 60 + ui.out5sredOnMinsS.value()
                data[61] = ui.out5sredOffHoursS.value() * 60 + ui.out5sredOffMinsS.value()

                # out5 chetverg
                if ui.out5chetC.isChecked(): data[62] = 10000
                data[62] += ui.out5chetOnHoursS.value() * 60 + ui.out5chetOnMinsS.value()
                data[63] = ui.out5chetOffHoursS.value() * 60 + ui.out5chetOffMinsS.value()

                # out5 pyatnitsa
                if ui.out5pyatC.isChecked(): data[64] = 10000
                data[64] += ui.out5pyatOnHoursS.value() * 60 + ui.out5pyatOnMinsS.value()
                data[65] = ui.out5pyatOffHoursS.value() * 60 + ui.out5pyatOffMinsS.value()

                # out5 subbota
                if ui.out5subC.isChecked(): data[66] = 10000
                data[66] += ui.out5subOnHoursS.value() * 60 + ui.out5subOnMinsS.value()
                data[67] = ui.out5subOffHoursS.value() * 60 + ui.out5subOffMinsS.value()

                # out5 voskresene
                if ui.out5voskC.isChecked(): data[68] = 10000
                data[68] += ui.out5voskOnHoursS.value() * 60 + ui.out5voskOnMinsS.value()
                data[69] = ui.out5voskOffHoursS.value() * 60 + ui.out5voskOffMinsS.value()

                # out6 pon
                if ui.out6ponC.isChecked(): data[70] = 10000
                data[70] += ui.out6ponOnHoursS.value() * 60 + ui.out6ponOnMinsS.value()
                data[71] = ui.out6ponOffHoursS.value() * 60 + ui.out6ponOffMinsS.value()

                # out6 vtornik
                if ui.out6vtorC.isChecked(): data[72] = 10000
                data[72] += ui.out6vtorOnHoursS.value() * 60 + ui.out6vtorOnMinsS.value()
                data[73] = ui.out6vtorOffHoursS.value() * 60 + ui.out6vtorOffMinsS.value()

                # out6 sreda
                if ui.out6sredC.isChecked(): data[74] = 10000
                data[74] += ui.out6sredOnHoursS.value() * 60 + ui.out6sredOnMinsS.value()
                data[75] = ui.out6sredOffHoursS.value() * 60 + ui.out6sredOffMinsS.value()

                # out6 chetverg
                if ui.out6chetC.isChecked(): data[76] = 10000
                data[76] += ui.out6chetOnHoursS.value() * 60 + ui.out6chetOnMinsS.value()
                data[77] = ui.out6chetOffHoursS.value() * 60 + ui.out6chetOffMinsS.value()

                # out6 pyatnitsa
                if ui.out6pyatC.isChecked(): data[78] = 10000
                data[78] += ui.out6pyatOnHoursS.value() * 60 + ui.out6pyatOnMinsS.value()
                data[79] = ui.out6pyatOffHoursS.value() * 60 + ui.out6pyatOffMinsS.value()

                # out6 subbota
                if ui.out6subC.isChecked(): data[80] = 10000
                data[80] += ui.out6subOnHoursS.value() * 60 + ui.out6subOnMinsS.value()
                data[81] = ui.out6subOffHoursS.value() * 60 + ui.out6subOffMinsS.value()

                # out6 voskresene
                if ui.out6voskC.isChecked(): data[82] = 10000
                data[82] += ui.out6voskOnHoursS.value() * 60 + ui.out6voskOnMinsS.value()
                data[83] = ui.out6voskOffHoursS.value() * 60 + ui.out6voskOffMinsS.value()
                # комбобоксы выбора датчиков для выходов 7-12
                data[84] = ui.out7BolDatBox.currentIndex()
                data[85] = ui.out7MenDatBox.currentIndex()
                data[86] = ui.out8BolDatBox.currentIndex()
                data[87] = ui.out8MenDatBox.currentIndex()
                data[88] = ui.out9BolDatBox.currentIndex()
                data[89] = ui.out9MenDatBox.currentIndex()
                data[90] = ui.out10BolDatBox.currentIndex()
                data[91] = ui.out10MenDatBox.currentIndex()
                data[92] = ui.out11BolDatBox.currentIndex()
                data[93] = ui.out11MenDatBox.currentIndex()
                data[94] = ui.out12BolDatBox.currentIndex()
                data[95] = ui.out12MenDatBox.currentIndex()
                # значения для датчиков
                data[96] = ui.out7BolDatValS.value()
                data[97] = ui.out7MenDatValS.value()
                data[98] = ui.out8BolDatValS.value()
                data[99] = ui.out8MenDatValS.value()
                data[100] = ui.out9BolDatValS.value()
                data[101] = ui.out9MenDatValS.value()
                data[102] = ui.out10BolDatValS.value()
                data[103] = ui.out10MenDatValS.value()
                data[104] = ui.out11BolDatValS.value()
                data[105] = ui.out11MenDatValS.value()
                data[106] = ui.out12BolDatValS.value()
                data[107] = ui.out12MenDatValS.value()
                # радиоконопки выбора действия вкл/выкл
                data[108] = int(ui.out7BolOnR.isChecked())
                data[109] = int(ui.out7MenOnR.isChecked())
                data[110] = int(ui.out8BolOnR.isChecked())
                data[111] = int(ui.out8MenOnR.isChecked())
                data[112] = int(ui.out9BolOnR.isChecked())
                data[113] = int(ui.out9MenOnR.isChecked())
                data[114] = int(ui.out10BolOnR.isChecked())
                data[115] = int(ui.out10MenOnR.isChecked())
                data[116] = int(ui.out11BolOnR.isChecked())
                data[117] = int(ui.out11MenOnR.isChecked())
                data[118] = int(ui.out12BolOnR.isChecked())
                data[119] = int(ui.out12MenOnR.isChecked())

                comSend(key=-1)  # отправка ответа что массив с параметрами сформирован
            elif com_received_data[0] == 120:
                comSend(
                    key=149)  ##когда были отправлены все 120 параметров (1-119) и получен запрос =120, то посылаем команду записи настроек в память плк
            else:
                comSend(key=com_received_data[0], param=data[com_received_data[0]])  # отправка параметров в ПЛК
            ui.statusbar.showMessage(f'Передача настроек в контроллер {str(com_received_data[0] - 1)}/119')

        elif 150 <= com_received_data[0] < 199:  # данные телеметрии ГОТОВО
            # прогрессбары состояния каналов
            if com_received_data[0] == 151:
                ui.out1bar.setValue(com_received_data[1])  # 0
            elif com_received_data[0] == 152:
                ui.out2bar.setValue(com_received_data[1])  # 1
            elif com_received_data[0] == 153:
                ui.out3bar.setValue(com_received_data[1])  # 2
            elif com_received_data[0] == 154:
                ui.out4bar.setValue(com_received_data[1])  # 3
            elif com_received_data[0] == 155:
                ui.out5bar.setValue(com_received_data[1])  # 4
            elif com_received_data[0] == 156:
                ui.out6bar.setValue(com_received_data[1])  # 5
            elif com_received_data[0] == 157:
                ui.out7bar.setValue(com_received_data[1])  # 6
            elif com_received_data[0] == 158:
                ui.out8bar.setValue(com_received_data[1])  # 7
            elif com_received_data[0] == 159:
                ui.out9bar.setValue(com_received_data[1])  # 8
            elif com_received_data[0] == 160:
                ui.out10bar.setValue(com_received_data[1])  # 9
            elif com_received_data[0] == 161:
                ui.out11bar.setValue(com_received_data[1])  # 10
            elif com_received_data[0] == 162:
                ui.out12bar.setValue(com_received_data[1])  # 11
            # значения датчиков в лейблы
            elif com_received_data[0] == 163:
                ui.temp1L.setText(str(com_received_data[1]))  # 12
            elif com_received_data[0] == 164:
                ui.temp2L.setText(str(com_received_data[1]))  # 13
            elif com_received_data[0] == 165:
                ui.analog1L.setText(str(com_received_data[1]))  # 14
            elif com_received_data[0] == 166:
                ui.analog2L.setText(str(com_received_data[1]))  # 15
            elif com_received_data[0] == 167:
                ui.analog3L.setText(str(com_received_data[1]))  # 16
            elif com_received_data[0] == 168:
                ui.analog4L.setText(str(com_received_data[1]))  # 17
            # время и дата
            elif com_received_data[0] == 169:  # 18
                global minutes
                minutes = com_received_data[1]
                if minutes < 10: minutes = '0' + str(minutes)
            elif com_received_data[0] == 170:  # 19
                global hours
                hours = com_received_data[1]
                if hours < 10: hours = '0' + str(hours)
            elif com_received_data[0] == 171:  # 20
                global date
                date = com_received_data[1]
                if date < 10: date = '0' + str(date)
            elif com_received_data[0] == 172:  # 21
                global month
                month = com_received_data[1]
                if month < 10: month = '0' + str(month)
            elif com_received_data[0] == 173:  # 22
                global year
                year = com_received_data[1]
            # определение дня недели
            elif com_received_data[0] == 174:  # 23
                global day
                if com_received_data[1] == 7:
                    day = 'Воскресенье'
                elif com_received_data[1] == 1:
                    day = 'Понедельник'
                elif com_received_data[1] == 2:
                    day = 'Вторник'
                elif com_received_data[1] == 3:
                    day = 'Среда'
                elif com_received_data[1] == 4:
                    day = 'Четверг'
                elif com_received_data[1] == 5:
                    day = 'Пятница'
                elif com_received_data[1] == 6:
                    day = 'Суббота'
            # вывод строки с датой-временем в лейбл
            ui.currentTimeL.setText(f'{hours}:{minutes},  {date}.{month}.{year},  {day}')
            # отправка запроса на получение следующего парамета телеметрии
            if com_received_data[0] <= 173: comSend(key=com_received_data[0] + 1)

        elif 200 <= com_received_data[0] < 400:  # чтение настроек из ПЛК. ГОТОВО!!
            ui.statusbar.showMessage(f'Чтение настроек контроллера {str(com_received_data[0] - 200)}/119')
            # настройки канала 1 понедельник
            if com_received_data[0] == 200:
                if com_received_data[1] >= 10000:
                    ui.out1ponC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out1ponC.setCheckState(False)
                ui.out1ponOnHoursS.setValue(com_received_data[1] // 60)
                ui.out1ponOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 201:
                ui.out1ponOffHoursS.setValue(com_received_data[1] // 60)
                ui.out1ponOffMinsS.setValue(com_received_data[1] % 60)

            # out 1 vtornik
            elif com_received_data[0] == 202:
                if (com_received_data[1]) >= 10000:
                    ui.out1vtorC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out1vtorC.setCheckState(False)
                ui.out1vtorOnHoursS.setValue(com_received_data[1] // 60)
                ui.out1vtorOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 203:
                ui.out1vtorOffHoursS.setValue(com_received_data[1] // 60)
                ui.out1vtorOffMinsS.setValue(com_received_data[1] % 60)

            # out1 sreda
            elif com_received_data[0] == 204:
                if (com_received_data[1]) >= 10000:
                    ui.out1sredC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out1sredC.setCheckState(False)
                ui.out1sredOnHoursS.setValue(com_received_data[1] // 60)
                ui.out1sredOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 205:
                ui.out1sredOffHoursS.setValue(com_received_data[1] // 60)
                ui.out1sredOffMinsS.setValue(com_received_data[1] % 60)

            # out1 chetvaerg
            elif com_received_data[0] == 206:
                if (com_received_data[1]) >= 10000:
                    ui.out1chetC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out1chetC.setCheckState(False)
                ui.out1chetOnHoursS.setValue(com_received_data[1] // 60)
                ui.out1chetOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 207:
                ui.out1chetOffHoursS.setValue(com_received_data[1] // 60)
                ui.out1chetOffMinsS.setValue(com_received_data[1] % 60)

            # out1 pyatn
            elif com_received_data[0] == 208:
                if (com_received_data[1]) >= 10000:
                    ui.out1pyatC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out1pyatC.setCheckState(False)
                ui.out1pyatOnHoursS.setValue(com_received_data[1] // 60)
                ui.out1pyatOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 209:
                ui.out1pyatOffHoursS.setValue(com_received_data[1] // 60)
                ui.out1pyatOffMinsS.setValue(com_received_data[1] % 60)

            # out1 subbota
            elif com_received_data[0] == 210:
                if (com_received_data[1]) >= 10000:
                    ui.out1subC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out1subC.setCheckState(False)
                ui.out1subOnHoursS.setValue(com_received_data[1] // 60)
                ui.out1subOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 211:
                ui.out1subOffHoursS.setValue(com_received_data[1] // 60)
                ui.out1subOffMinsS.setValue(com_received_data[1] % 60)

            # out1 voskr
            elif com_received_data[0] == 212:
                if (com_received_data[1]) >= 10000:
                    ui.out1voskC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out1voskC.setCheckState(False)
                ui.out1voskOnHoursS.setValue(com_received_data[1] // 60)
                ui.out1voskOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 213:
                ui.out1voskOffHoursS.setValue(com_received_data[1] // 60)
                ui.out1voskOffMinsS.setValue(com_received_data[1] % 60)

            # out2 pon
            elif com_received_data[0] == 214:
                if (com_received_data[1]) >= 10000:
                    ui.out2ponC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out2ponC.setCheckState(False)
                ui.out2ponOnHoursS.setValue(com_received_data[1] // 60)
                ui.out2ponOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 215:
                ui.out2ponOffHoursS.setValue(com_received_data[1] // 60)
                ui.out2ponOffMinsS.setValue(com_received_data[1] % 60)

            # out2 vtornik
            elif com_received_data[0] == 216:
                if (com_received_data[1]) >= 10000:
                    ui.out2vtorC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out2vtorC.setCheckState(False)
                ui.out2vtorOnHoursS.setValue(com_received_data[1] // 60)
                ui.out2vtorOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 217:
                ui.out2vtorOffHoursS.setValue(com_received_data[1] // 60)
                ui.out2vtorOffMinsS.setValue(com_received_data[1] % 60)

            # out2 sreda
            elif com_received_data[0] == 218:
                if (com_received_data[1]) >= 10000:
                    ui.out2sredC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out2sredC.setCheckState(False)
                ui.out2sredOnHoursS.setValue(com_received_data[1] // 60)
                ui.out2sredOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 219:
                ui.out2sredOffHoursS.setValue(com_received_data[1] // 60)
                ui.out2sredOffMinsS.setValue(com_received_data[1] % 60)

            # out2 chetverg
            elif com_received_data[0] == 220:
                if (com_received_data[1]) >= 10000:
                    ui.out2chetC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out2chetC.setCheckState(False)
                ui.out2chetOnHoursS.setValue(com_received_data[1] // 60)
                ui.out2chetOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 221:
                ui.out2chetOffHoursS.setValue(com_received_data[1] // 60)
                ui.out2chetOffMinsS.setValue(com_received_data[1] % 60)

            # out2 pyatn
            elif com_received_data[0] == 222:
                if (com_received_data[1]) >= 10000:
                    ui.out2pyatC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out2pyatC.setCheckState(False)
                ui.out2pyatOnHoursS.setValue(com_received_data[1] // 60)
                ui.out2pyatOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 223:
                ui.out2pyatOffHoursS.setValue(com_received_data[1] // 60)
                ui.out2pyatOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 224:
                if (com_received_data[1]) >= 10000:
                    ui.out2subC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out2subC.setCheckState(False)
                ui.out2subOnHoursS.setValue(com_received_data[1] // 60)
                ui.out2subOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 225:
                ui.out2subOffHoursS.setValue(com_received_data[1] // 60)
                ui.out2subOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 226:
                if (com_received_data[1]) >= 10000:
                    ui.out2voskC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out2voskC.setCheckState(False)
                ui.out2voskOnHoursS.setValue(com_received_data[1] // 60)
                ui.out2voskOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 227:
                ui.out2voskOffHoursS.setValue(com_received_data[1] // 60)
                ui.out2voskOffMinsS.setValue(com_received_data[1] % 60)

            ######### out3
            elif com_received_data[0] == 228:
                if (com_received_data[1]) >= 10000:
                    ui.out3ponC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out3ponC.setCheckState(False)
                ui.out3ponOnHoursS.setValue(com_received_data[1] // 60)
                ui.out3ponOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 229:
                ui.out3ponOffHoursS.setValue(com_received_data[1] // 60)
                ui.out3ponOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 230:
                if (com_received_data[1]) >= 10000:
                    ui.out3vtorC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out3vtorC.setCheckState(False)
                ui.out3vtorOnHoursS.setValue(com_received_data[1] // 60)
                ui.out3vtorOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 231:
                ui.out3vtorOffHoursS.setValue(com_received_data[1] // 60)
                ui.out3vtorOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 232:
                if (com_received_data[1]) >= 10000:
                    ui.out3sredC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out3sredC.setCheckState(False)
                ui.out3sredOnHoursS.setValue(com_received_data[1] // 60)
                ui.out3sredOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 233:
                ui.out3sredOffHoursS.setValue(com_received_data[1] // 60)
                ui.out3sredOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 234:
                if (com_received_data[1]) >= 10000:
                    ui.out3chetC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out3chetC.setCheckState(False)
                ui.out3chetOnHoursS.setValue(com_received_data[1] // 60)
                ui.out3chetOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 235:
                ui.out3chetOffHoursS.setValue(com_received_data[1] // 60)
                ui.out3chetOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 236:
                if (com_received_data[1]) >= 10000:
                    ui.out3pyatC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out3pyatC.setCheckState(False)
                ui.out3pyatOnHoursS.setValue(com_received_data[1] // 60)
                ui.out3pyatOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 237:
                ui.out3pyatOffHoursS.setValue(com_received_data[1] // 60)
                ui.out3pyatOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 238:
                if (com_received_data[1]) >= 10000:
                    ui.out3subC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out3subC.setCheckState(False)
                ui.out3subOnHoursS.setValue(com_received_data[1] // 60)
                ui.out3subOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 239:
                ui.out3subOffHoursS.setValue(com_received_data[1] // 60)
                ui.out3subOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 240:
                if (com_received_data[1]) >= 10000:
                    ui.out3voskC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out3voskC.setCheckState(False)
                ui.out3voskOnHoursS.setValue(com_received_data[1] // 60)
                ui.out3voskOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 241:
                ui.out3voskOffHoursS.setValue(com_received_data[1] // 60)
                ui.out3voskOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 242:
                if (com_received_data[1]) >= 10000:
                    ui.out4ponC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out4ponC.setCheckState(False)
                ui.out4ponOnHoursS.setValue(com_received_data[1] // 60)
                ui.out4ponOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 243:
                ui.out4ponOffHoursS.setValue(com_received_data[1] // 60)
                ui.out4ponOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 244:
                if (com_received_data[1]) >= 10000:
                    ui.out4vtorC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out4vtorC.setCheckState(False)
                ui.out4vtorOnHoursS.setValue(com_received_data[1] // 60)
                ui.out4vtorOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 245:
                ui.out4vtorOffHoursS.setValue(com_received_data[1] // 60)
                ui.out4vtorOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 246:
                if (com_received_data[1]) >= 10000:
                    ui.out4sredC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out4sredC.setCheckState(False)
                ui.out4sredOnHoursS.setValue(com_received_data[1] // 60)
                ui.out4sredOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 247:
                ui.out4sredOffHoursS.setValue(com_received_data[1] // 60)
                ui.out4sredOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 248:
                if (com_received_data[1]) >= 10000:
                    ui.out4chetC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out4chetC.setCheckState(False)
                ui.out4chetOnHoursS.setValue(com_received_data[1] // 60)
                ui.out4chetOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 249:
                ui.out4chetOffHoursS.setValue(com_received_data[1] // 60)
                ui.out4chetOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 250:
                if (com_received_data[1]) >= 10000:
                    ui.out4pyatC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out4pyatC.setCheckState(False)
                ui.out4pyatOnHoursS.setValue(com_received_data[1] // 60)
                ui.out4pyatOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 251:
                ui.out4pyatOffHoursS.setValue(com_received_data[1] // 60)
                ui.out4pyatOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 252:
                if (com_received_data[1]) >= 10000:
                    ui.out4subC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out4subC.setCheckState(False)
                ui.out4subOnHoursS.setValue(com_received_data[1] // 60)
                ui.out4subOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 253:
                ui.out4subOffHoursS.setValue(com_received_data[1] // 60)
                ui.out4subOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 254:
                if (com_received_data[1]) >= 10000:
                    ui.out4voskC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out4voskC.setCheckState(False)
                ui.out4voskOnHoursS.setValue(com_received_data[1] // 60)
                ui.out4voskOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 255:
                ui.out4voskOffHoursS.setValue(com_received_data[1] // 60)
                ui.out4voskOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 256:
                if (com_received_data[1]) >= 10000:
                    ui.out5ponC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out5ponC.setCheckState(False)
                ui.out5ponOnHoursS.setValue(com_received_data[1] // 60)
                ui.out5ponOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 257:
                ui.out5ponOffHoursS.setValue(com_received_data[1] // 60)
                ui.out5ponOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 258:
                if (com_received_data[1]) >= 10000:
                    ui.out5vtorC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out5vtorC.setCheckState(False)
                ui.out5vtorOnHoursS.setValue(com_received_data[1] // 60)
                ui.out5vtorOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 259:
                ui.out5vtorOffHoursS.setValue(com_received_data[1] // 60)
                ui.out5vtorOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 260:
                if (com_received_data[1]) >= 10000:
                    ui.out5sredC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out5sredC.setCheckState(False)
                ui.out5sredOnHoursS.setValue(com_received_data[1] // 60)
                ui.out5sredOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 261:
                ui.out5sredOffHoursS.setValue(com_received_data[1] // 60)
                ui.out5sredOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 262:
                if (com_received_data[1]) >= 10000:
                    ui.out5chetC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out5chetC.setCheckState(False)
                ui.out5chetOnHoursS.setValue(com_received_data[1] // 60)
                ui.out5chetOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 263:
                ui.out5chetOffHoursS.setValue(com_received_data[1] // 60)
                ui.out5chetOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 264:
                if (com_received_data[1]) >= 10000:
                    ui.out5pyatC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out5pyatC.setCheckState(False)
                ui.out5pyatOnHoursS.setValue(com_received_data[1] // 60)
                ui.out5pyatOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 265:
                ui.out5pyatOffHoursS.setValue(com_received_data[1] // 60)
                ui.out5pyatOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 266:
                if (com_received_data[1]) >= 10000:
                    ui.out5subC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out5subC.setCheckState(False)
                ui.out5subOnHoursS.setValue(com_received_data[1] // 60)
                ui.out5subOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 267:
                ui.out5subOffHoursS.setValue(com_received_data[1] // 60)
                ui.out5subOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 268:
                if (com_received_data[1]) >= 10000:
                    ui.out5voskC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out5voskC.setCheckState(False)
                ui.out5voskOnHoursS.setValue(com_received_data[1] // 60)
                ui.out5voskOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 269:
                ui.out5voskOffHoursS.setValue(com_received_data[1] // 60)
                ui.out5voskOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 270:
                if (com_received_data[1]) >= 10000:
                    ui.out6ponC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out6ponC.setCheckState(False)
                ui.out6ponOnHoursS.setValue(com_received_data[1] // 60)
                ui.out6ponOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 271:
                ui.out6ponOffHoursS.setValue(com_received_data[1] // 60)
                ui.out6ponOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 272:
                if (com_received_data[1]) >= 10000:
                    ui.out6vtorC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out6vtorC.setCheckState(False)
                ui.out6vtorOnHoursS.setValue(com_received_data[1] // 60)
                ui.out6vtorOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 273:
                ui.out6vtorOffHoursS.setValue(com_received_data[1] // 60)
                ui.out6vtorOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 274:
                if (com_received_data[1]) >= 10000:
                    ui.out6sredC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out6sredC.setCheckState(False)
                ui.out6sredOnHoursS.setValue(com_received_data[1] // 60)
                ui.out6sredOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 275:
                ui.out6sredOffHoursS.setValue(com_received_data[1] // 60)
                ui.out6sredOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 276:
                if (com_received_data[1]) >= 10000:
                    ui.out6chetC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out6chetC.setCheckState(False)
                ui.out6chetOnHoursS.setValue(com_received_data[1] // 60)
                ui.out6chetOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 277:
                ui.out6chetOffHoursS.setValue(com_received_data[1] // 60)
                ui.out6chetOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 278:
                if (com_received_data[1]) >= 10000:
                    ui.out6pyatC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out6pyatC.setCheckState(False)
                ui.out6pyatOnHoursS.setValue(com_received_data[1] // 60)
                ui.out6pyatOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 279:
                ui.out6pyatOffHoursS.setValue(com_received_data[1] // 60)
                ui.out6pyatOffMinsS.setValue(com_received_data[1] % 60)


            elif com_received_data[0] == 280:
                if (com_received_data[1]) >= 10000:
                    ui.out6subC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out6subC.setCheckState(False)
                ui.out6subOnHoursS.setValue(com_received_data[1] // 60)
                ui.out6subOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 281:
                ui.out6subOffHoursS.setValue(com_received_data[1] // 60)
                ui.out6subOffMinsS.setValue(com_received_data[1] % 60)

            # out6 voskr
            elif com_received_data[0] == 282:
                if (com_received_data[1]) >= 10000:
                    ui.out6voskC.setCheckState(True)
                    com_received_data[1] -= 10000
                else:
                    ui.out6voskC.setCheckState(False)
                ui.out6voskOnHoursS.setValue(com_received_data[1] // 60)
                ui.out6voskOnMinsS.setValue(com_received_data[1] % 60)

            elif com_received_data[0] == 283:
                ui.out6voskOffHoursS.setValue(com_received_data[1] // 60)
                ui.out6voskOffMinsS.setValue(com_received_data[1] % 60)
                # out7 set config
            elif com_received_data[0] == 284:
                ui.out7BolDatBox.setCurrentIndex(com_received_data[1])
            elif com_received_data[0] == 296:
                ui.out7BolDatValS.setValue(com_received_data[1])
            elif com_received_data[0] == 308:
                if com_received_data[1] == 0:
                    ui.out7BolOnR.setChecked(False)
                    ui.out7BolOffR.setChecked(True)
                else:
                    ui.out7BolOnR.setChecked(True)
                    ui.out7BolOffR.setChecked(False)
            elif com_received_data[0] == 285:
                ui.out7MenDatBox.setCurrentIndex(com_received_data[1])
            elif com_received_data[0] == 297:
                ui.out7MenDatValS.setValue(com_received_data[1])
            elif com_received_data[0] == 309:
                if com_received_data[1] == 0:
                    ui.out7MenOnR.setChecked(False)
                    ui.out7MenOffR.setChecked(True)
                else:
                    ui.out7MenOnR.setChecked(True)
                    ui.out7MenOffR.setChecked(False)
                    # out 8
            elif com_received_data[0] == 286:
                ui.out8BolDatBox.setCurrentIndex(com_received_data[1])
            elif com_received_data[0] == 298:
                ui.out8BolDatValS.setValue(com_received_data[1])
            elif com_received_data[0] == 310:
                if com_received_data[1] == 0:
                    ui.out8BolOnR.setChecked(False)
                    ui.out8BolOffR.setChecked(True)
                else:
                    ui.out8BolOnR.setChecked(True)
                    ui.out8BolOffR.setChecked(False)
            elif com_received_data[0] == 287:
                ui.out8MenDatBox.setCurrentIndex(com_received_data[1])
            elif com_received_data[0] == 299:
                ui.out8MenDatValS.setValue(com_received_data[1])
            elif com_received_data[0] == 311:
                if com_received_data[1] == 0:
                    ui.out8MenOnR.setChecked(False)
                    ui.out8MenOffR.setChecked(True)
                else:
                    ui.out8MenOnR.setChecked(True)
                    ui.out8MenOffR.setChecked(False)
                    # out9
            elif com_received_data[0] == 288:
                ui.out9BolDatBox.setCurrentIndex(com_received_data[1])
            elif com_received_data[0] == 300:
                ui.out9BolDatValS.setValue(com_received_data[1])
            elif com_received_data[0] == 312:
                if com_received_data[1] == 0:
                    ui.out9BolOnR.setChecked(False)
                    ui.out9BolOffR.setChecked(True)
                else:
                    ui.out9BolOnR.setChecked(True)
                    ui.out9BolOffR.setChecked(False)
            elif com_received_data[0] == 289:
                ui.out9MenDatBox.setCurrentIndex(com_received_data[1])
            elif com_received_data[0] == 301:
                ui.out9MenDatValS.setValue(com_received_data[1])
            elif com_received_data[0] == 313:
                if com_received_data[1] == 0:
                    ui.out9MenOnR.setChecked(False)
                    ui.out9MenOffR.setChecked(True)
                else:
                    ui.out9MenOnR.setChecked(True)
                    ui.out9MenOffR.setChecked(False)
                    # out10
            elif com_received_data[0] == 290:
                ui.out10BolDatBox.setCurrentIndex(com_received_data[1])
            elif com_received_data[0] == 302:
                ui.out10BolDatValS.setValue(com_received_data[1])
            elif com_received_data[0] == 314:
                if com_received_data[1] == 0:
                    ui.out10BolOnR.setChecked(False)
                    ui.out10BolOffR.setChecked(True)
                else:
                    ui.out10BolOnR.setChecked(True)
                    ui.out10BolOffR.setChecked(False)
            elif com_received_data[0] == 291:
                ui.out10MenDatBox.setCurrentIndex(com_received_data[1])
            elif com_received_data[0] == 303:
                ui.out10MenDatValS.setValue(com_received_data[1])
            elif com_received_data[0] == 315:
                if com_received_data[1] == 0:
                    ui.out10MenOnR.setChecked(False)
                    ui.out10MenOffR.setChecked(True)
                else:
                    ui.out10MenOnR.setChecked(True)
                    ui.out10MenOffR.setChecked(False)
                    # OUT11
            elif com_received_data[0] == 292:
                ui.out11BolDatBox.setCurrentIndex(com_received_data[1])
            elif com_received_data[0] == 304:
                ui.out11BolDatValS.setValue(com_received_data[1])
            elif com_received_data[0] == 316:
                if com_received_data[1] == 0:
                    ui.out11BolOnR.setChecked(False)
                    ui.out11BolOffR.setChecked(True)
                else:
                    ui.out11BolOnR.setChecked(True)
                    ui.out11BolOffR.setChecked(False)
            elif com_received_data[0] == 293:
                ui.out11MenDatBox.setCurrentIndex(com_received_data[1])
            elif com_received_data[0] == 305:
                ui.out11MenDatValS.setValue(com_received_data[1])
            elif com_received_data[0] == 317:
                if com_received_data[1] == 0:
                    ui.out11MenOnR.setChecked(False)
                    ui.out11MenOffR.setChecked(True)
                else:
                    ui.out11MenOnR.setChecked(True)
                    ui.out11MenOffR.setChecked(False)
                    # out12
            elif com_received_data[0] == 294:
                ui.out12BolDatBox.setCurrentIndex(com_received_data[1])
            elif com_received_data[0] == 306:
                ui.out12BolDatValS.setValue(com_received_data[1])
            elif com_received_data[0] == 318:
                if com_received_data[1] == 0:
                    ui.out12BolOnR.setChecked(False)
                    ui.out12BolOffR.setChecked(True)
                else:
                    ui.out12BolOnR.setChecked(True)
                    ui.out12BolOffR.setChecked(False)
            elif com_received_data[0] == 295:
                ui.out12MenDatBox.setCurrentIndex(com_received_data[1])
            elif com_received_data[0] == 307:
                ui.out12MenDatValS.setValue(com_received_data[1])
            elif com_received_data[0] == 319:
                if com_received_data[1] == 0:
                    ui.out12MenOnR.setChecked(False)
                    ui.out12MenOffR.setChecked(True)
                else:
                    ui.out12MenOnR.setChecked(True)
                    ui.out12MenOffR.setChecked(False)
            # отправка запроса на следующий параметр
            if com_received_data[0] < 319: comSend(key=com_received_data[0] + 1)

        elif 400 <= com_received_data[0] < 450:  # диапазон не используется
            print('пустой диапазон 400-449')

        elif 450 <= com_received_data[0] < 460:  # синхронизация времени
            current_datetime = datetime.now()
            if com_received_data[0] == 451:
                comSend(key=451, param=current_datetime.second)
            elif com_received_data[0] == 452:
                comSend(key=452, param=current_datetime.minute)
            elif com_received_data[0] == 453:
                comSend(key=453, param=current_datetime.hour)
            elif com_received_data[0] == 454:
                comSend(key=454, param=current_datetime.day)
            elif com_received_data[0] == 455:
                comSend(key=455, param=current_datetime.month)
            elif com_received_data[0] == 456:
                comSend(key=456, param=current_datetime.year - 2000)  # ПЛК требуется год в диапазоне 0-99
            elif com_received_data[0] == 457:
                comSend(key=457, param=current_datetime.isoweekday())

    except:
        print('Ошибка парсинга')
        ui.statusbar.showMessage('Внимание! Ошибка парсинга данных!')


serial.readyRead.connect(comRead)  # если в порту что-то есть, то читаем +

ui.comOpenB.clicked.connect(comOpen)  # кнопка открытия порта +
ui.comCloseB.clicked.connect(comClose)  # кнопка закрытия порта +
ui.readSettingsB.clicked.connect(lambda: comSend(key=200))  # кнопка чтения настроек
ui.writeSettingsB.clicked.connect(lambda: comSend(key=-2))  # кнопка записи настроек
ui.timeSyncB.clicked.connect(lambda: comSend(key=450))  # синхронизация времени. посылвет в плк код 450, на который должен получить в ответ 451 чтобы начать синх
# кнопки проверки выходов
ui.out1checkB.pressed.connect(lambda: comSend(key=460))
ui.out1checkB.released.connect(lambda: comSend(key=461))
ui.out2checkB.pressed.connect(lambda: comSend(key=462))
ui.out2checkB.released.connect(lambda: comSend(key=463))
ui.out3checkB.pressed.connect(lambda: comSend(key=464))
ui.out3checkB.released.connect(lambda: comSend(key=465))
ui.out4checkB.pressed.connect(lambda: comSend(key=466))
ui.out4checkB.released.connect(lambda: comSend(key=467))
ui.out5checkB.pressed.connect(lambda: comSend(key=468))
ui.out5checkB.released.connect(lambda: comSend(key=469))
ui.out6checkB.pressed.connect(lambda: comSend(key=470))
ui.out6checkB.released.connect(lambda: comSend(key=471))
ui.out7checkB.pressed.connect(lambda: comSend(key=472))
ui.out7checkB.released.connect(lambda: comSend(key=473))
ui.out8checkB.pressed.connect(lambda: comSend(key=474))
ui.out8checkB.released.connect(lambda: comSend(key=475))
ui.out9checkB.pressed.connect(lambda: comSend(key=476))
ui.out9checkB.released.connect(lambda: comSend(key=477))
ui.out10checkB.pressed.connect(lambda: comSend(key=478))
ui.out10checkB.released.connect(lambda: comSend(key=479))
ui.out11checkB.pressed.connect(lambda: comSend(key=480))
ui.out11checkB.released.connect(lambda: comSend(key=481))
ui.out12checkB.pressed.connect(lambda: comSend(key=482))
ui.out12checkB.released.connect(lambda: comSend(key=483))

ui.show()  # показать интерфейс
app.exec()  #
