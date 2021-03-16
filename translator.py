en = open("yoshimitsu_en.json", "r")
ko = open("yoshimitsu_ko.json", "w", encoding="UTF-8")

for line in en:
    if '"Command":' in line:
        new_text = (
            line[19:]
            .replace("in rage ", "레이지 도중 ")
            .replace("(Opponent in front)", "(전방에 상대가 있을 때)")
            .replace("(Opponent behind)", "(후방에 상대가 있을 때)")
            .replace("(Second hit miss)", "(후속타가 헛쳤을 때)")
            .replace("(SSL)", "(시계방향 횡이동)")
            .replace("(SSR)", "(반시계방향 횡이동)")
            .replace("(After on step)", "(한 걸음 걸은 후)")
            .replace("(After two step)", "(두 걸음 걸은 후)")
            .replace("(After three step)", "(세 걸음 걸은 후)")
            .replace("(Four steps)", "(네 걸음 걸은 후)")
            .replace("(Five steps)", "(다섯 걸음 걸은 후)")
            .replace("(Six steps)", "(여섯 걸음 걸은 후)")
            .replace("(one spin)", "(한 바퀴)")
            .replace("(two spins)", "(두 바퀴)")
            .replace("(three spins)", "(세 바퀴)")
            .replace("(four spins)", "(네 바퀴)")
            .replace("(five spins)", "(다섯 바퀴)")
            .replace("(two to five hits)", "(두 번째부터 다섯번째까지)")
            .replace("1", "LP")
            .replace("2", "RP")
            .replace("3", "LK")
            .replace("4", "RK")
            .replace("d/b", "1")
            .replace("d/f", "3")
            .replace("u/b", "7")
            .replace("u/f", "9")
            .replace("qcf", "6N23")
            .replace("d", "2")
            .replace("b", "4")
            .replace("f", "6")
            .replace("u", "8")
            .replace("*", "N")
            .replace("j", "홀드")
            .replace("+", "")
            .replace(", ", " ")
            .replace("or", "또는")
            .replace("(to NSS)", "(납도로 전환)")
            .replace("NSS", "납도 중")
            .replace("(to KIN)", "(금타 자세 이행)")
            .replace("KIN", "금타 자세에서")
            .replace("(to MED)", "(무상 자세 이행)")
            .replace("MED", "무상 자세")
            .replace("(to FLE)", "(지뢰인 자세 이행)")
            .replace("FLE", "지뢰인 자세 중")
            .replace("(to WFL)", "(지뢰맹마 이행)")
            .replace("WFL", "지뢰맹마 중")
            .replace("(to IND)", "(만자앉기 자세 이행)")
            .replace("IND", "만자앉기 중")
            .replace("(to INS)", "(만자앉기 자세 이행)")
            .replace("INS", "만자앉기 중")
            .replace("(to DGF)", "(만잠자리 자세 이행)")
            .replace("DGF", "만잠자리 자세 중")
            .replace("(to PDP)", "(독무 자세 이행)")
            .replace("PDP", "독무 자세 중")
            .replace("WS", "일어나며 ")
            .replace("BT", "뒤자세")
            .replace("SS", "횡이동 중 ")
            .replace("FC", "앉은 자세에서 ")
            .replace("(Cancel)", "(취소)")
            .replace("D/B", "1")
            .replace("D/F", "3")
            .replace("U/B", "7")
            .replace("U/F", "9")
            .replace("D", "2")
            .replace("B", "4")
            .replace("F", "6")
            .replace("U", "8")
        )
        ko.write(f"{line[:19]}{new_text}")
    elif '"Hit level":' in line:
        new_text = (
            line[21:]
            .replace("Attack returned", "반격")
            .replace("(throw)", "(잡기)")
            .replace("(Special)", "(특수)")
            .replace("(KIN)", "(금타)")
            .replace("(DGF)", "(만잠자리)")
            .replace("(IND)", "(만자앉기)")
            .replace("(FLE)", "(지뢰인)")
            .replace("TC", "앉은 자세")
            .replace("TJ", "점프")
            .replace("h", "상")
            .replace("m", "중")
            .replace("l", "하")
            .replace(", ", " ")
            .replace("!", "가불기")
        )
        ko.write(f"{line[:21]}{new_text}")
    else:
        ko.write(line)

en.close()
ko.close()
