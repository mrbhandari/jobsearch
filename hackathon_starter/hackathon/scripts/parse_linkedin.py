from bs4 import BeautifulSoup
import glob
import re
#i_path_join = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "static", "data", i)
#filepath = '/Users/PEM-Mac/br/jobsearch/hackathon_starter/hackathon/static/data/Download/044f631e1864388ef06fc819364e86a9.html'

def parse_skills(filepath):
    print filepath
    skill_list = []
    skill_count = []


    with open(filepath, 'r') as f:
        soup = BeautifulSoup(f.read())
    try:
        ss = soup.find("h1").get_text()
        input_skill = ss
        print input_skill

        try:
            ss = soup.find("ul", {"class": "buckets-container"}).find_all("p", {"class": "title bucket-label"})
            for i in ss:
                skill_list.append(i.get_text())

            ss = soup.find("ul", {"class": "buckets-container"}).find_all("p", {"class": "subtitle bucket-label"})
            for i in ss:
                skill_count.append(i.get_text().strip().replace(',', ''))
        except AttributeError:
            print "Type 2"
            try:
                ss = soup.find("div", {"class": "set"}).find_all("label", {"class": "stat-label"})
                for i in ss:
                    #print i.get_text()
                    skill = re.findall(r'^.+\(', i.get_text())[0].replace('(' , '').strip()
                    #print skill
                    skill_list.append(skill)

                    #print i.get_text()
                    count = re.findall(r'\([0-9,]+', i.get_text())[0].replace('(', '').replace(',', '').strip()
                    #print count
                    skill_count.append(count)
            except AttributeError:
                print "No skills found"
                print filepath
    except AttributeError:
        print "Empty file did not find h1 for"
        print filepath
    except:
        print "Unkonwn error for"
        print filepath


    output_text =''

    if len(skill_list) == len(skill_count):
        #checks that there are atleast as many skills as counts before writing
        for i in range(0,len(skill_list)):
            output_text += ('\t').join([input_skill, skill_list[i], skill_count[i]])+ '\n'
    #print output_text
    return output_text

def write_to_file():
    mypath = "/Users/PEM-Mac/br/jobsearch/hackathon_starter/hackathon/static/data/download/"
    list_of_files = glob.glob(mypath+ "*.html")
    
    for i in list_of_files:
        output_text = parse_skills(i)
        filepath = '/Users/PEM-Mac/br/jobsearch/hackathon_starter/hackathon/static/data/'
        filename = 'coviewed_skills.tsv'
        try:
            with open(filepath + filename, 'a') as f:
                f.write(output_text)
        except UnicodeEncodeError:
            print "Invalid character -probably univeristy for "
            print filepath

if __name__ == '__main__':
    write_to_file()


#print re.findall(r'\([0-9,]+', i.get_text())[0].replace('(', '').replace(',', '').strip()
#parse_skills('/Users/PEM-Mac/br/jobsearch/hackathon_starter/hackathon/static/data/Download/0ee0cf93f585454deedb6e2e32393c91.html')

