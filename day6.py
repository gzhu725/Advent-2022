with open('elf6.txt') as reader:
  lines = reader.readlines()

lines = 'lrgrvgvttzmtmtgglmgmccpclppvdvtvvllvggvrggbwwlzlmzzbppnvpnvppcjjzhjhthnhjnhhhndhnnnsbnnhzzvhhplplzlrzzgpzpwzpwwsvsjvjfvvphpspwswrswscwscwsscffspsbbjjcjwjrwwtgwwgswswwzbzddqnnpqnpnqppwzwszsnsjjpddhvvcbbhhpzzlpzlzppfpvvmcmvvflfttrltrlldlglbgblltqtffrtrwrzwwzmzwmwwlzzhttwzzwnnmrrcdrdjrjqjvqvvjzzgccrllhmhzzfnfwwtzwzwpwhhdjhhmzzbbvggzdzccbzbbpcpqccjbcbppsttdjdnjnppjjnmmszmzgzddtctvctcvttgtbbzqqggnmmdllvdvmvzzhfffzvfvtfvtvwwcnwnvwwbccggjcjqcqcbcrrppdqppdzpzqppttjhjdjqjppzgzjjpllwrrbttrvvzzbhzzqppndppwqppnrpnnttfwttsrrgprggmtmhmzhzczwzmwzwrwqwrrrdqrrvssnlngnppfqqgbgjjcttbgtbtmtctmcmcmgmsgsffhghqhbbvtbbtltmltlnlpnngcnggbngbnnzgzccgcpgcpcjppnnzjzdjdggzjzljjhnncgcjcscfctcvttvqtqmqjjsqjqpqfqhqmmlvvmppfrfjjngnnfllrlhhppcjcbjcctgcgtcgcvgvffqfcfpcpdpffrbrvbvnnphpqpfqqtnttmtgtlgtgzttnvvpwvwvcwcfwcwmccwlclqlflpflplwpllndlltlqtlqqmqnqmnqnvqvrrtddqndnrdnnpzprrqnnggvqvhvpvptvvvzwzrwwscsqqmcmttbgtgpptzptzzvszvzdvvtsscbbrpptssltssztszttlvlqljlgljlhhwvhwvvqhvqhqrhqqcnqccnbcbppbffzqfqsfspsqsjjrhjjchcmhmnhmmzjmjmfjmmsbsvvgcggtdgghchrrpnnrttnthtdtmmhmdmppmgpgllrwlrwlwvvlmlglppzttsvsbsnbncnjnffddzcddbzzbzgbghhhtltwtggljjggsdswwpmmfhfsfvfrrgmrgrfggvzzbnbttwqqdcdppqcqpcpqpjqpjpbbgjbgjjfwfwpfpgpzgzmzgzdzzpwzwqqjqfqllgrgjjfvvqnvncntngnhgnhgnnzvvbsbmbqmqwmqwwhbwhhsccvhcclncnqccnvnzvvdgvgnvnttmbbhccwgwttlwtwqttqcqmcqcdcmmjpmmjsjhhprrnnqddjwdjjvvhvgvssthhnfhnnntfthhtggthhbrbrjbbjfbjjrgrsrjrqqqfwflfclflnnnnvggfqgqzzbbvttfcfvcvsswvssnzndndvnvqqznnrjnnsmmptmppncpchcctwtbbgbqqjqtqsqfsfvfvnvmvzzpgzppdzdvdqdjdnjnttvvjbbzrzqrqwrqrbqrqsqpspjssnqnpqqnjndjjzmmvbbrqrccrffhwhggbttpnpphwhhmrrndrnddzqzzfbfwbwnwtwjjwjmjsjcjgcjjfcftcffvpvwwbffgzgnnlfffnddtdbdlbbcjbjmmfpfzfbbwbdwwfmfpmmfjfffvzvdvvhrvrcvcscjjpfjjnfnzzrtrpphtppzrppwhhphthltlllttghgwwvlwlflhldlzzmbzzjppnwppvlplqqbtbwwccswccqzzjhjbbhbnhnshnsslmmlqqjfjrjjmvvhpjqhzqffhsdsbwpjvgpvmbfqltrmpnwfcptpfmtjcpbzfldbhcmzchshrlbjgggrfjcqhzqqvbzsczmbgqmzqmltlrtlbnsfvmlhbbcqbbltjpdrpznrglshvgdnqwlhthghvtbffddcjwgdzfswzbppjtdhstcqqmvzmjrvfjbhmrznwqczdjjclnhbmtdvvzwttwnrlfqwpglpcppdwdcvfqpqfnmbvzvmqlmnlgnrsqdjvtsftgnlrtzsrcqhltmhzhpmzqqfqrjwhqfnqdtnshwgfhcpjrlplnqczdlntnhsczrgfhflsfbmftsbptflqbpwblrfnfzvqtpblftmscpzgdhhsbdbjhqclnptwtmhbbfglmvwnbqgvqhmmswwjpfwqjbvznmcpdzcvbzjmfqnwstvvtdnlvnpznnblfqzjjrjgnsbtmmbjzsvmgwddtnzcvhvtdrmjgtcrjzznrssscrzcfbfpgpnpppsqcqpccnbdjnwrbvhrcwgqncjrzbdhzqpfhqbnvbfrzmlfbfvtpggrtdswnvlsvpjsmfchhpbbszbnqqfrmhpqzdjhmhmnnmplbtrpgphvvqdfbcfnrfrbfbtshlmlfltjnbmggqntvhdnlvtcvlhmlrlfzfrqmlwqzrdghvdvtsqvmpdjrjclmlmgjqwzzldnzvfmwmrrnfghsvpcwjdtlnrhpjczwpgfbhpnmcbpthsndfflbjhnlwdbbmlttfqcmswvppslptgzbvfgppvpnhjccrpgrpwtngmmccjghhcwddmnglschnpjwqtrtsvggnpzvsqshfvcnhptphtlmqmpznfzwvbnhwpsfwvpflsdjcjgfzjprbbfzgdbmrjgwrgfdphghrhnpvfncrdzcwtthmqtdwlhjsdthqpzhbjpgggndtrmwvcsqhzrzwbhtqsqthvqncprvnpsrlpvlvcjrcflhbdhrfthlfnqbzbmvlvhmbjnbbjhpjwlfflfhpfwcwnnsljthvzwprqjmgpldlzjnjtjfjrgnrpzpvzfcsrprbjhwnmccwhppjrlnndjdjzqwpcwnvqwgmnwbrjqqvbplvsncnmdfrbhrrhghfllhrghzmlnltgdsqlgbvnlchgcbqlpqptdwmsjpqrprlhqmstzjfnzgbgvlfshwpcrgzcqmmfwvhwlsdvplmdgrtfrjwpfvhnjqdbwsfcqhchstlzfpdljgvcqsfcnqccnpmvsqbmwjtzwhpglhbjwzmvgqwjhvwfhnlbtsgljzmlldcpjwdcfppmnmphdmhpmdqwwtjtrdhlrjlvzgpbcgvwcmtclgpqwhtpbdtdbdscfzbrzmgjlbppcnvphphfnvzdzzlvfsvsgbgqcnlqwmtcrpwzcvnmnvtmcdsstvqpqzdpvtdsbvtwhdvgzqmzvwlspgbwmlnsrqdqnjwrllncflqsrzdqtjqvpnpjlqfwqtlqfqwlltszcwtpmjtldjgvmvptpmzqhwmlvjgnntpvcslmhlhdbjtjjnvsbnzwtdclwbzrvlqzjljtbdjvwgbwcltvnbhfvtgqrbmzbbfvldhmdvfvtlqglnblfmmpjqmzlnfjltsqdrgmlhbhngrrmhnjndggsdcfmtssmmtmzvhzrmwjsqjcvbsgqgtvdmvqlvlrvglrtlshfdmfrmljjggwjbcsztsjmjftcbbjwrmgqvssrvtgzcgthtlgsjspfmdgwptjdrbswqlpfsbtjlnhllmjpbfhgpfcprpdnqqvqdmcbqhbcqtstvnjdzwzwvhhwmcvcfbdwczpwpdhvnstjnbblbprzsccmwrzgfhmrpvzfztvsrtncdhzhptpfqtnqwvqtwdpvcqztgjgrcbdnvqftphtfbtqdhrffdrdmwsbpvhshzvjbvsrljnzddmmfgcnfdssvzdbsfwmfjsdnslbrqsqfwfqbqszjwvgcjbhrfjcnlfhzvhcbbbpmhhvjdtgrqlcchqtvnhlrgtssllvgcdjrlzlzfbrrrvwvvcgfjdlpscsqljmmwmvwnvrgdmgcbvmwmgprbfrbgptlfjbhrmczwrzwbdhdvtgvldnzfgcngdfhbgqsfzlrbwbvdflrrsrcwthjzvgmdtndgtsjtswfbdqvcjtsdvrvqpmmdlghsdbzplgpfnstplpjdvttgzmnhssftqcqjvdvvdrmltbrpsjvqwbljrqrtqldzbwzznsdstvmdzbrvvtgrrphmbrzwnjbmqvfhljcdlbzqtcbjsfqdqcr'



'''for i in range(len(lines)-3):
  four = lines[i: i+4]
  if len(set(four)) == len(four):
    print(i+4)
    break'''


for i in range(len(lines)-13):
  fourteen = lines[i: i+14]
  if len(set(fourteen)) == len(fourteen):
    print(i+14)
    break



