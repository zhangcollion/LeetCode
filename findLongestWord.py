from typing import List
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda k: (-len(k), k))
        l = []
        def in_str(sub_str):
            index = -1
            for a in sub_str:
                if a in s[index+1:]:
                    index = s.index(a, index+1)
                else:
                    return False
            return True

        for i in d:
            if in_str(i):
                return i
        return ""



if __name__ == "__main__":
    s = "wsmzffsupzgauxwokahurhhikapmqitytvcgrfpavbxbmmzdhnrazartkzrnsmoovmiofmilihynvqlmwcihkfskwozyjlnpkgdkayioieztjswgwckmuqnhbvsfoevdynyejihombjppgdgjbqtlauoapqldkuhfbynopisrjsdelsfspzcknfwuwdcgnaxpevwodoegzeisyrlrfqqavfziermslnlclbaejzqglzjzmuprpksjpqgnohjjrpdlofruutojzfmianxsbzfeuabhgeflyhjnyugcnhteicsvjajludwizklkkosrpvhhrgkzctzwcghpxnbsmkxfydkvfevyewqnzniofhsriadsoxjmsswgpiabcbpdjjuffnbvoiwotrbvylmnryckpnyemzkiofwdnpnbhkapsktrkkkakxetvdpfkdlwqhfjyhvlxgywavtmezbgpobhikrnebmevthlzgajyrmnbougmrirsxi"
    d = ["jpthiudqzzeugzwwsngebdeai","nbmxgkduynigvzuyblwjepn"]
    print(Solution().findLongestWord(s, d))