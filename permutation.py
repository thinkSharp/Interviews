import collections
def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    lns1, lns2, start = len(s1), len(s2), - 1

    counter = collections.Counter(s1)
    tracker = collections.Counter()

    for i, s in enumerate(s2):
        tracker[s] += 1
        if i >= lns1:
            if tracker[s2[i-lns1]] == 1:
                del tracker[s2[i-lns1]]
            else:
                tracker[s2[i-lns1]] -=1
        if tracker == counter:
            return True

    return False
def test_p():
    res = checkInclusion('adc','dca')
    print(res)
    res = checkInclusion('adc','dcda')
    print(res)
    res = checkInclusion('abc','cccbbbaaa')
    print(res)
    res = checkInclusion('ab','eidbaooo')
    print(res)
    res = checkInclusion('adc','dcda')
    print(res)

    res = checkInclusion("vxqakfyaqahufxfizupjrkkifjlbfqfeprqrfjvxnubntdtlvz",
                         "oumgfmlrbivgnrvsfslnheghnbhhicbvaddqadwicekguhjairhpqtebqvzyxdfodntxmoqtffgmsomnhndbrffxmuyjvqazwfvugyvmshxignfenmkihorjkshwyuxxkxidpkalqmdnxxmnovhangcwggjwjrletxhelehcipflvqyueptgjxugyipegamjbweqdfeswrjepjjlviuhfikfaojbhrujdfpnenrvajrdplwaevpbzkcdkyhidbgizwofjoxfvnkzhmwvegnfipgmnikljmmcrleffceqsxrxgsjmjmaflnxtigfoeaafsrjaxaqumhatpdeueridyxfjajsjkcrfwkwguclqtrefwevwalmcvoiragprwwnxpwgqoyulsadfhstduevikkkwmofklomdvpdcnxxsotudmkjgakbzopzengbfrvhiikzrsmmurewnnquydhntpqprtyvouatjevvoerbnzunwtdiigohcctulnvpgfbtdjmjsvszphulflmolunohifxsycaiifkngpuycnlihebmhaapureljxlqozydijsbcitfrdjhbdppvhpfjfuxujwfkcezyvhbityajxcccbuyvoluzndgjsyvrbluvagqtuujpsxjcgdtkbhaxsatmellmotdeoxsxjsywuavjqpzjkcpsrowqgogovcouosjhblhdmbkeidafpimjaiypownlcilpahbszmmcwbqmztpdmbqeuizjwdifruojquahdtdukydxgehpourjytveajjvtpiphihkmgqpmnuukpqtjyyqhfsiezugszdbjsseaxxdxomhouvetgcvfeuvwszmhgpkkorubvahxoufpfcukgchdubddpijsolrkvgiizhqefdhvpzvpmuxnwpcaepnpuicgvoxdqfcaabhsxgnorbpkboueplrpztqehrufldndxuenmvynranzqontfihfwvtxmiadbogsawlpmyycaztkyrqxwoxocbtngrmaiyafqqornrknnsmulglzyjnydvwpfefbuwhcocvyczklwywgwergmboqagcsngavorldbpsefoaynkmfqrjzdtbylibwwhhuhfqkoorihjewpcpuxhjnbeiegpplsyrzzyxsnnslvbkslzhwqjzrijdyucnnoshkxbagqdzxwnarwbzivhjpzgvaqrtywqwdetcqtsxviebsnpeflvegyjgxaskwuesfaqdjfdvuklayyekvumbuciranyvymtwshowdxyxbtpuchskraonnwvvvbdehhjdqiluauesssredqoeypadjsahxjqrgxmguppwrydbsiuvhjxyvsseeisbymztpaxclvxsvypdnabnhcnlzelogrfcvvzpwrujkdvwvzlgdbdqgiruxygolkamiluvmfuoaslakmsaehubjxlcfvonmcnqenxwjgypqfedszrisegdtlwhxdsqeyhkynmtdyrjwwslwwtucbtuxxlkymelgqumhgyjnnjtqvaatmcfpbupfszdcuwgbyudffdpxszrqskmnpdqeauilbwnojibjfqwaalwnmevjbbzvptawuemsvlqfmonxycnfnzmgfmwpmjcyvhjfjpyhywjqbtjwhxudqhuclhyfbiuazzvnklkjfiupntduclftpddhfkioqkptklhynubibyjwllgexbjafcgubnelxzdapnxsqtmnqcdscrgpawigubbugtnxvebnrlujkxranwzbiemsvykjlmnyyfkrplutmpohohtqntxmkdfmlwvspedxlgylwbqfbhtolkfbfjfmvbhxafbwmlolagckjeffnwsiesgkhpyeupuyvcmfhlxygrmkkvuarjviqxfgkwturzkzwquefcyelduecwqrachowsxbdcgrvtkmlkyloqjjlyctuzsztafqearzuiogjrfqbseqibzddpabbfhbkeiorgslhecyicrvxvlzynxctnydzpgghjocuqimuxlvwymkhvbaqyljurieblfffxplmfwszrhvqiyzaqruihxvabytqvhmauzmrgcxtiotlkhtqcrugthgerkvixykexnlyxntpgagigdepzchsplujazcqabzvjcvutxriirzeydvffvzhhhihlfwewusmuzeecuytcwermdxpcffsewvyfearxirlmdwqfxsaljqnyvfiibqgxpfgkuoqadxcbdgcrhhrhvrdluzlefeerwhwinuqzuwuvairwqraajnifdihhzuqtciqmkrxafiuixbqacmgxfybmdghunmgwbidvanucokddovmznczycruztcayuwafcvjnqxhzarfvdqfounjciebxngwfwjknqmrappyuiewzdjshsbespzfcrwswtpayqaldwdvwiyoullwxshgzdluqbwecxkiyrqrguyepbcqzgafvjfxkzvglnghbmogenghozxncfenobraxqrhybxcoyovwreawnxiurnggbecnybohhicmvxlexizgvskafbxabzkzuvbrksbanikuewjgbkwcxoqibcpissudhljplgqifaebgxueiukmqxfcjwkysjjyuamlcatwqfhltyrwjdutbqoclvpcyhczybrmsatuwaswlziqqasyedtoxhmhktrjfwytfhxhncwiovjbpimtjpkwmxkalmxdjkwqhtakjraqiykrrmgncirghthsyfuhubmkhduibikgkorispskluycaepxdgxsodeqstbreyfuxtwksqqyqlvzvqtnoirjujqeltakrbiubuoqzyorkgcdkormvctirrowpemxtfgiqpzkadbpxaghodshuxorilbjxfigpcixuhcbaoulyxaoweiaojcbmbptwcfzgvylwcfyvmhoepvexcmkqvlrbknbhvctplytkqjjvmfadhksevedhfhmbhhqzgooudgxuazdskajgvuejhpvgngpfsayyyvupptpjvveuwrsrdwewhwivpmojlvvhnahpqwvrspjpradwkylbsketjriqqpvhhedbhkkvswcvwadunencyxtxmindabykaqoaoeifqdwihohbueikhixdfumrldazczdlorgtcwrrylwjxyxzgmdujwiapwpzrikupdeijmqrarvwhfcgzrkysnwsjeqhqtembrwkcjxtvjwwwkarolvbeczwinodvtgvbbqdwipckezgxwdizrnaxfexnjoafnrqxgywruytmfktkoygmbdwogjfjdvohglnxngnijysafyrlzofdovuslmcnhxfjjitvbdvwbluorpwtmtynrmzjrbiaqvzcqrxppojxnqfebtwpmfvuhigbahvjraidtmmceaxctnbtolhuiqcforksdbypcvjagrvsqguhgbyqgqiruvvqszezfmlntffbdrlcwyjcgriqycabijkokoqzntelifjxzyvytnbfflkoiipilzafyicgniewbuapmfzqcaximlfjhvuurfscozgpgghvsuvpqqtsojdphbumqrluvgnbhlymulcmqziytcampdpdrqvfwxygwbysofektetfrwedzklwgtjytibpdzakxjfvczcfxtdjpbngqzrmvyudslvlqsezwkqkkcbxoipifopzynllvbuujssspdsycqbyvdlgoauisrkvahwipcwukmvllgsaijkdrpuxlzyzsjabsatdgzmbebovnlydvqgjphwxqgfzaqyxadgfdmtbbqlpvciucjdrhlluumnqubughdaauyhkvdekpoamoliyttnyondnmphcesvowghyktattrxhvlbdlrsfjssflnvtyltawmuqoofhvvobkistzasjhmbkessjtditkmxpzlskojwokiatbwhdzjbzbsqkzmnzvdpyaxygrehqgfqqaxnnerizmarbooohufcdhwpvsulsstmcoivxapufjqtnaviffihkpyrbrzfjenqtxlxfqkfjvazubkrdqluffwaluvqilsfrqrdmnhdhrjkbpkgtkznoqnvpswoyndtqqckqqtcubtutrbxrforaitavuazzugvgczvsyfvqnuakykuwczsithogunmpejpmrxcjjvvzbxzyrltihlsirevhjohihonylwsekburnndcwxkybjifubalefhmiiitpqqzjjazsbfgtxopdjvbdgdmcfrfiebeopggbukfxxxcjotbiltihiddnuwrlzvrzsfmgkrulvcwbeqnkkhgobokkkspdzomfgvodqvzrvajlanwbyeioxtxbyfrapsjtgqvqzdoerwkfvzmsbzhumuotznpiozkvodscfaffpgiapftqlrthudvgvenfzyaxaummpmyhyuswvegysoppwnysdpqyzzrubdrenplyiqmmvthtfreynmltqbizpycniwwnunqynfyeigduomqqulemmdjqpndhuxvmizutfzxztrbavfopefglqyvrqwggjnrpnkcyghelmcnmtmtzsepopwzoirjcdjenpuqpvutueinapitkhsmmraytgftzpjlekyhcwdltjjxsycydcvfmzwgbcxcoboqcbxzkszwlhxgpnpynjjhaqucnwhxhoyhqrkeeqgggqliogjuqyxgzcfvhmtkevipopxmowjotswevzmsxngshovradrjxihwbnqqpuhobnmlfassydwmlcgirrhrlxhkchzwrokrllbibjecgqfpttvuerckuegvooxssxvdcemgbuuirzfckxnxwsszrpcuogfuusrplrielkgvhvygnjkfzfzxsqhifoxctfhuipqxctdlvgdkewprxfuxsgfvfqtclxgzsadtvhuvpqrxjjjjrrxqgovoyuipqnhosvoufbqvugpplwzrphrjrnrllxpoxtuwlwkzotpebuamennaapntnneyvhahgxdbhtbqplduxaodhsskkpqynrzonhagrwxcoeagawjvcucsvbotsaelkywjoyeehsbfdwgoqnyyaunvhqdjvtsbxbbbpgfxnngxmikrrgsdbsokwdpyevqoplxqudieqpisrsbfxugybymbjwzoyevpigikboxhdntktxmzvjzywtbvcjrhuhwosrijcqmkfjcqxbitntabzbroolnxjllqfnznkaystntwegkkofkxsyxuamsxpubavzwfoixtjlluujjwifajginhtcywidlmkkhysmulzvzldxwyopdodzryxpkqrdukecragplzfysuwqcqaoqqfjuyfqliwkmvwvfubcklvdhzutgtgumayojpvovumxemspycidbnnmcxyarkxttcvqqhomkilqaqoovnrqlvubeeofiwxjqyayzcycgoiircgxgzhnqrbcgkrofcotpkqouabcqbdrouxxageejbjlfuzmbmfckrqbbyyhzvjrrpzbefamvoufqogovzaokciuzmevfyuaaypyjqggwipkgzkbmlbafbzlljsfmhscsodcrbbfylkfyqxokfgolmosuxpdsjspfciammxqirioodfxngosyzlkltpmsxpafmabupevthayfxdbiovsqxkrenmfkoctidrdqinrqojnelptkuzrcebddkboyxkhrfwrgvikyrvjihcfitdhdtexfnxtcsgmxkntaimhvdrndqprsddtqctysmzounvmsvxxhwgoxegqjqtouwapoxuvbkmpriuanvqoxorjcpprofqdspoosgmmlnztpaubosqqknbbqnhpyyubonpkwmlowfjgpmtgzlqujxljdadtosbhnmngepkjlmvuescozvzclobocahnkyplhqstopknrhufneybwebebhgxvwyydolesgbojzvvndmsgbhxhoybgakgdesrsmvrzhmijyjytdmpdxehxrhgsyiedfrxlgvxpxwyjaxjowwnuujnabjqcylypgduzrwituqvwckkworwlkcluicfwgydzothrmcisvfrhgpnpecbhxisfzchndxftawqybqnfuxetoupeplgxatqxytnfmokteeqmxjemgwrufklkwaxazzgelzfgglhirzjffkoqxmbtwkhhbodamujvwljmlivdbbirtubccsgrvkylyfmppilsxezcdozjpbdfjtnuwgfsreodmpafkzclgtzrgvbewdbaoephgkmwwidfcvzjkvrcafkzfdxxxdpgbqrybzejaaezxrwpxbeziscdwfbfahiefzokbnhgfqxkbcuixenmmnvolepkzkpeasrygpyoummmsoticswegyqyxkaqscmrtsnoblraczloiqcznabchbatdicakdpulzkddhcagdeogibasyddubcezmztaukusexmsjymljapvllrqfhpgkfudyedlcbhwpfimlplclrcxpttnxamzucpfagisbajnyrzvxxlzjolxxisexrojzwcratimkamjliplucbdejtcgwryaweatwbkqardkbmrdbdseggojlslcjhmcumhxikgdzxjuyyjcyyvkvseyvqjewdlrrpnwxltnnedjupeclekzyvoormnowjkrpuwfavricrvjoqqbjqijpqlmsnwmonmbjxvbpokumfvdfnxbhxxsfzxcozwhzmgrwkdczrcigxbuvlnyyuvsraobwuznkxdizyqifjwgtwnmxunhukoeqpxafupdxwzfymwsblpvyyktdspctcxmwsxfqgsgedimmhcqjztpmrbavhogwuhzbngycbggsoakrvuceiditgcwxaopcirtivcibqpxbqdstcokmypyuzlaowongknpzitpdhjkoszoqvdgrtqvckyjmduketumefixobawbekqfrnwebsijgvihedwmegkssznkwgwqgavcakfhdwesqyjvotcevhgltzcknzqrindzbywgiibjsnvsttugwizaxayngnmfsmjopzqygphvxdhdwnrnksdqwnahecbzpxeetihclinvbxmrpoiynuxsyabdmhtaqnjtsiearotujspwgmnjoqgeqbcrbrmssjtbuqciflfjjfxkiapfttwymziapbxjenhwrzcdrjtjudhcztpwqungqidwzjhsgwlxlujrpeepubglthkbnhbdqwwlbjbnndfjupllxyluagyieeurajyhdqcinkmosympawgreeihdjcfggtomoeooqbklqfxoavtpcdhrlcsezabwufygrghnmtdvisfrzfjmmgnqwnxdyvidbxizsunzosikevlwzgrybbidzyytsaspbgbgzrmgimcmmulodqbqljxeusveynagjkphulpqnqkfrbjcvtntzmjwsfifmhsphicrtchdydlklhrdghmtacbjfktgvphhlhhkkcqkytcfgjuoblfdjpkuocherhufixafdbgotxrxrcuohgpxpogfggvkdrkixzfkahtnwhvbntqbrpqxvutbldhrfirzxfupybrvolteycfjkdcaubwtqomzfepcevmpecqpteevaubtbchlaakgqpzvjwqxzbcneektiwhvyoexdufbirqhukdmtlfqtjhboncqciumvxccncrjpecyuctxfdsekblmnpmjkotsfopoeakeetsvagoayijofejkjixevcvopuymjxdpgrjupgbpjpqacdbbcpzuqwaztmxfriypcfdybjamjxflzinuxcszriqnsokpegxzfzgidrjsbfftnzxgcxtbrordopldbrtxqeeeeiixdnedgoaohbadmrnstciefemzhepbfwccdulrgduxhebifzivhzgiueajetcrwqvmeailiyyjclgfeizotkkjiaedwsqsngsoqrpekysgzlmtijsxdrcpjchecchkxhjuyevtdlohohbgrkyfsmygplztmvrgeuqjuenepnsarcopkadsbvvpzmcacliqagsfvsfylfoinibat")
    print(res)
test_p()
