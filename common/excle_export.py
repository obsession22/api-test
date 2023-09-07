import openpyxl


def excle_read(excle_url, sheet_name):
    # 加载工作薄
    wb = openpyxl.load_workbook(excle_url)
    # 获取sheet对象
    sheet = wb[sheet_name]
    # 获取最大行和最大列
    all_list = []
    for row in range(2, sheet.max_row+1):
        row_list = []
        for column in range(1, sheet.max_column+1):
            row_list.append(sheet.cell(row, column).value)
        all_list.append(row_list)
    return all_list


def read_all_excel_data(excel_url):
    data = {}
    # 加载工作簿
    workbook = openpyxl.load_workbook(excel_url, data_only=True)

    for sheet_name in workbook.sheetnames:
        sheet_data = excle_read(excel_url, sheet_name)
        data[sheet_name] = sheet_data
    return data


if __name__ == '__main__':
    # print(excle_read("../data/ele.xlsx", "Sheet1"))
    print(read_all_excel_data('../data/api_test.xlsx'))

