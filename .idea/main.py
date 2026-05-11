from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import DataAnalyser, GpaAnalyser, CountryAnalyser

fm = FileManager('students.csv')
fm.check_file()
fm.create_output_folder()

dl = DataLoader('students.csv')
dl.load()
dl.preview()

base = DataAnalyser(dl.students)
print(base)
base.analyse()

gpa_analyser = GpaAnalyser(dl.students)
print(gpa_analyser)
gpa_analyser.analyse()
gpa_analyser.print_results()

sample_10 = dl.students[:10]
analysers = [GpaAnalyser(dl.students), CountryAnalyser(sample_10)]

print("-" * 30)
print("Running all analysers:")
print("-" * 30)

for a in analysers:
    print(a)
    a.analyse()
    a.print_results()


saver = ResultSaver(analysers[0].result, 'output/result.json')
report = Report(analysers[0], saver)
report.generate()