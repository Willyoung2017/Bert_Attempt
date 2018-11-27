import requests
import json
import nltk
import time
def post_allen(sentence):
    headers = {"Content-Type": "application/json"}
    url='http://demo.allennlp.org/predict/semantic-role-labeling'
    data={"sentence":sentence}
    NETWORK_STATUS = True # 判断状态变量
    try:
        response=requests.post(url,json.dumps(data),headers = headers, timeout=30)
        if response.status_code == 200:
            return json.loads(response.text)
    except requests.exceptions.Timeout:
        NETWORK_STATUS = False # 请求超时改变状态
        if NETWORK_STATUS == False:
            for i in range(1, 10):
                print("请求超时，第%s次重复请求" % i)
                response = requests.post(url, json.dumps(data), headers=headers, timeout=30)
                if response.status_code == 200:
                    return json.loads(response.text)
    return -1

def parse_squad_data(source):
    srl_output_file = open("srl_squad","w",encoding="utf-8")
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    with open(source, 'r') as f:
        source_data = json.load(f)
    data_files = source_data['data']
    for article_ix, article in enumerate(data_files):
        article_ix = "%s-%d" % (source, article_ix)
        print(article_ix)
        srl_output_file.write("========start========article========"+str(article_ix)+"========"+article["title"]+"\n")
        for para_ix, para in enumerate(article['paragraphs']):
            srl_output_file.write("========start========paragraphs========" + str(article_ix) + "========" + article["title"]+"\n")
            print("para:"+str(para_ix))
            para_json = []
            context = para['context']
            sentences = tokenizer.tokenize(context)
            for sent_ix,sentence in enumerate(sentences):
                print("sent_ix:" + str(para_ix))
                sentence_json = {}
                response = post_allen(sentence)
                time.sleep(5)
                sentence_json["num"] = sent_ix
                sentence_json["raw"] = sentence
                sentence_json["srl"] = response
                para_json.append(sentence_json)
                
            srl_output_file.write(json.dumps(para_json) + "\n")
            srl_output_file.write("========end========paragraphs========" + str(para_ix)+"\n")
            #srl_output_file.write(json.dumps(paragraphs) + "\n")
        srl_output_file.write("========end========article========" + str(article_ix)+"========"+article["title"]+"\n")
    srl_output_file.close()
parse_squad_data("squad_data/dev-v1.1.json")
# sentence = "Super Bowl 50 was an American football game to determine the champion of the National Football League (NFL) for the 2015 season."
# response = post_allen(sentence)