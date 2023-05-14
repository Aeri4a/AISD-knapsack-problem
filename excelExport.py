import xlsxwriter


def excelExport(wbName, sheetNames, templates, moveX=0, moveY=0):
    workbook = xlsxwriter.Workbook(f'{wbName}.xlsx')

    for i in range(len(sheetNames)):
        worksheet = workbook.add_worksheet(sheetNames[i])
        for idx, t in enumerate(templates[i]):
            worksheet.write(0, idx, t["name"])
            for i in range(len(t["data"])):
                worksheet.write(i+1, idx, t["data"][i])

    workbook.close()
