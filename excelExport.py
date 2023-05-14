import xlsxwriter


def excelExport(wbName, sheetName, template, moveX=0, moveY=0):
    workbook = xlsxwriter.workbook(f'{wbName}.xlsx')

    worksheet = workbook.add_worksheet(sheetName)
    for idx, t in enumerate(template):
        worksheet.write(0, idx, t["name"])
        for i in range(len(t["data"])):
            worksheet.write(i+1, idx, t["data"][i])

    workbook.close()
