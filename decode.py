# Enter your code here. Read input from STDIN. Print output to STDOUT
def sortlist(seq, idfun=None): 
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       # in old Python versions:
       # if seen.has_key(marker)
       # but in new ones:
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result

def build_decode(dic, eword, dword):
    for i, ec in enumerate(eword):
        dc = dic.setdefault(ec, dword[i])
        if dc != dword[i]:
            return {}
    return dic

def is_possible(eword, dword):
    return True if build_decode({}, eword, dword) else False

def skip_word(dic, eword):
    for c in eword:
        if c not in dic:
            return False
    return True
    
def main(text):
    enc_words = text.split()
    enc_words = list(set(enc_words))
    enc_words.sort(key = len, reverse=True)
    
    dic = None
    len_list = {}
    dic_list = {}
    with open('dictionary.lst') as d:
        for word in d:
            word = word.strip().lower()
            l = len(word)
            len_words = len_list.setdefault(l, [])
            len_words.append(word)
            len_list[l] = len_words
    
    for e in enc_words:
        len_words = len_list[len(e)]
        lwords = len_words[:]
        for lw in len_words:
            if not is_possible(e, lw):
                lwords.remove(lw)
        dic_list[e] = lwords

    decoder = {}
    decoder[' '] = ' '
    for e, d in dic_list.iteritems():
        if len(d) == 1:
            decoder = build_decode(decoder.copy(), e, d[0])
            enc_words.remove(e)
        # if len(d) > 31:
        #     enc_words.remove(e)
    
    print "####### {} \n".format(enc_words)
    enc_words.sort(key = lambda x: len(dic_list[x]))
    print "####### {} \n".format(enc_words)
    print "####### {}".format([len(dic_list[x]) for x in enc_words])

    i = 0
    decoder_dic = {}
    ij = {}
    temp_decoder = decoder.copy()
    decoder_dic[i] = temp_decoder
    
    while i < len(enc_words):
        e = enc_words[i]
        d_words =  dic_list[e]
        #print "decode list: {}".format(d_words)
        fail = True
        j = ij.setdefault(i, 0)
        if skip_word(temp_decoder, e):
            i += 1
            decoder_dic[i] = temp_decoder.copy()
            continue
        while j < len(d_words):
            #print "temp decoder: {}".format(temp_decoder)
            d = d_words[j]
            temp_decoder = build_decode(temp_decoder.copy(), e, d)
            j += 1
            #print "encoded word: {}".format(e)
            #print "decode word: {}".format(d)
            #print "new temp: {}".format(temp_decoder)
            if not temp_decoder:
                temp_decoder = decoder_dic[i]    
            else:
                fail = False
                break
        if fail:
            #print "failed go back one"
            i -= 1
            if i <= 0:
                #print "... start over from first word"
                temp_decoder = decoder.copy()
                i = 0
            else:
                #print "... back to i - {} with decoder - {}".format(i, temp_decoder)
                temp_decoder = decoder_dic[i]
                
        else:
            #print "next encoded word"
            ij[i] = j
            #print "setting ij[{}] to {}".format(i, j)
            i += 1
            decoder_dic[i] = temp_decoder.copy()
            #print "decoder_dic: {}".format(decoder_dic)
    
    decoder = decoder_dic[i]
    
    print decoder
    print ''.join([decoder[c] for c in text])    

# my_input = "lhpohes gvjhe ztytwojmmtel lgsfcgver segpsltjyl vftstelc djfl rml catrroel jscvjqjyfo mjlesl lcjmmfqe egvj gsfyhtyq sjfgver csfaotyq lfxtyq gjywplesl lxljm dxcel mpyctyq"
#my_input = "lhpohes gvjhe ztytwojmmtel lgsfcgver segpsltjyl vftstelc djfl rml catrroel jscvjqjyfo mjlesl lcjmmfqe egvj gsfyhtyq sjfgver csfaotyq lfxtyq gjywplesl lxljm dxcel mpyctyq ztytwojmmtelel mfcgv spres mjm psgvty bfml ofle mjlc dtc tygfycfctjy dfsyl zpygvel csfao yealqsjpml atyl lgsjql qyfsotelc fseyf ojllel gjzmselltyq wpyhtelc zpltgl weygel afyher rstnesl aefleo rtyhes mvflel yphe rstnes qojder dtwwer lojml mfcgvel reocfl djzder djpygtyq gstmmoeafsel reg cpdel qspyqe mflctel csflvtyq vfcl avfghtyq vftsdfool mzer rsjye wjjol psol mplvtyq catrroe mvfqe lgseey leqzeycer wjseqsjpyrer lmjtoes msjwtoel docl djpyger cjpstlcl goefy gojddesl mjrl qjddoe gjy gpdtyql lyftotyq rjayojfr swgl vjle atrqec gjzmfgces frfl qotcgver gspzd zftodjzdl lyfsh"

my_input = "btnpufhz esxfh vyhvefz ufhez xsgfnafcfz umabtfz qz kmhmgsjfg ghndf tiufhzumbfz ahneez ydsdafhfzasdw uhnanbne pmdwefz lmeeumufhz oymgz tnuz kmdz vncfz pmdwfgz dmsxf ltmbq wmz zdmsez zmiz pszkfmayhf aydf zyd zumdwef vvzfz wnvvefz khfflmhf tmpzafhz bndz sdksdsasfz mpnfvmz athmztfz tmppfh tfcfz bivfhuydq gnldfg ghsxfh pmdwefh zuskki zlmv zunnksdw gfmgfh ahsxsme dyqfg kemw pmhwsdme byvsdwfg enzfhz uzfygn bhsuueflmhf bmebyemanhz gnldsdw pydwz uyzt xmc uydafg zbhffd gsf enzfh difalnhq kenlbtmhaz venbqfg ayvf vmhkz zbmw jfhnfz ggfg kemxnh vhnqf vmhkfg kemxnhz pyaafhfg tmppfhsdw byvfz befmdfg hnvyzafh kenngsdw vhfmqz zunsefhz knzzsez bhmindz yhe ufzzspmefg bhfasdz hmdgnpdfzz bhfmasndszpz zsenz jnhbtsdw bnnqsf bendf oyfzfz meaz zpnqf zuffgnpfafh ztmhflmhf"

main(my_input)
        