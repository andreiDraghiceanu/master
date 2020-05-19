import sys
from prettytable import PrettyTable
from optparse import OptionParser
import pymysql


def return_testcases():
    connection = pymysql.connect(host='127.0.0.1', user="root", passwd="123456", db='Performance_Tests')
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    column = "SELECT `Test_Name` FROM testcases"
    cursor.execute(column)
    row = cursor.fetchall()
    testcases = []
    for key in row:
        testcases.append(key['Test_Name'])
    return testcases

test_names = return_testcases()


def parse_options():
    global options
    parser = OptionParser()
    if len(sys.argv[1:]) == 0:
        print("Warning! No argument given!")
        parser.print_help()
        sys.exit(1)
    parser.add_option("--device_one", dest="device_one", action="store", help="First chassis", default=None)
    parser.add_option("--device_two", dest="device_two", action="store", help="Second chassis", default=None)
    parser.add_option("--build_one", dest="build_one", action="store", help="Build for chassis one", default=None)
    parser.add_option("--build_two", dest="build_two", action="store", help="Build for chassis two", default=None)
    parser.add_option("--email_address", dest="email_address", action="store", help="Results e-mail", default=None)
    parser.add_option("--email_name", dest="email_name", action="store", help="Name of regression file", default=None)
    parser.add_option("--email_server", dest="email_server", action="store", help="E-mail server", default=None)
    (options, args) = parser.parse_args()
    return (options.device_one, options.device_two, options.build_one, options.build_two,
            options.email_address, options.email_name, options.email_server)


def return_values(chassis, build):
    unexecuted_tests = []
    all_executed_tests = []
    connection = pymysql.connect(host='127.0.0.1', user="root", passwd="123456", db='Performance_Tests')
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    column = "SELECT `Test Name`, Result FROM" + chassis + "WHERE `Build` = " + build
    cursor.execute(column)
    row = cursor.fetchall()
    test_names = return_testcases()
    for key in row:
        all_executed_tests.append(key['Test Name'])
    for counter in range(len(test_names)):
        if test_names[counter] not in all_executed_tests:
            unexecuted_tests.append(test_names[counter])
            key = {'Test Name': test_names[counter], 'Result': None}
            row.append(dict(key))
            counter += 1
    connection.close()
    return row




def create_table(device_one, device_two, build_one, build_two):

    first_chassis = return_values(device_one, build_one)
    second_chassis = return_values(device_two, build_two)
    dict_result_one = {}
    dict_result_two = {}
    test_cases = []
    list_result_one = []
    list_result_two = []
    list_percent = []

    for value in first_chassis:
        if value['Test Name'] in test_names:
            dict_result_one[value['Test Name']] = value['Result']
    for value in second_chassis:
        if value['Test Name'] in test_names:
            dict_result_two[value['Test Name']] = value['Result']

    for test in test_names:

        if test in dict_result_one:
            test_cases.append(test)
            list_result_one.append(dict_result_one[test])
        if test in dict_result_two:
            list_result_two.append(dict_result_two[test])
        if dict_result_one[test] is not None and dict_result_two[test] is not None:
            list_percent.append(round((100 - (dict_result_two[test] * 100) / dict_result_one[test]), 2))
        else:
            list_percent.append(None)


    table = PrettyTable()
    table.column_names = ['Test Name', 'Chassis I Results', 'Chassis II Results', 'Difference in Percents']
    table.add_column(table.column_names[0], test_cases)
    table.add_column(table.column_names[1], list_result_one)
    table.add_column(table.column_names[2], list_result_two)
    table.add_column(table.column_names[3], list_percent)
    table.align["Test Name"] = 'l'
    print(table)
    return




def send_mail():
    pass


if __name__ == '__main__':

    parse_options()
    device_one = '`%s`' % options.device_one
    device_two = '`%s`' % options.device_two
    build_one = '"%s"' % options.build_one
    build_two = '"%s"' % options.build_two
    if device_two is None:
        device_two = device_one
    if build_two is None:
        build_two = build_one
    email_address = options.email_address
    email_server_name = options.email_server
    email_name = options.email_name
    create_table(device_one, device_two, build_one, build_two)
