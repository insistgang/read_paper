#!/usr/bin/env python3
"""安全补齐论文笔记 frontmatter 的空元数据字段。

只更新 authors/year/venue 的空值, 不改正文、不改阅读状态、不覆盖已有值。
信息来源优先使用 `.paper-cache/extracts/*.txt` 中已经提取的 PDF 首页文本。
"""
import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Optional


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from validate_library import (  # noqa: E402
    frontmatter_scalar,
    is_blank_frontmatter_value,
    parse_frontmatter,
)


ROOT = SCRIPT_DIR.parent
DEFAULT_NOTES = ROOT / "02-Notes" / "Papers"
DEFAULT_CACHE = ROOT / ".paper-cache" / "extracts"
FIELDS = ("authors", "year", "venue")

VENUE_PATTERNS = (
    ("中国图象图形学报", re.compile(r"\bJournal of Image and Graphics\b|中国图象图形学报", re.I)),
    ("Medical Image Analysis", re.compile(r"\bMedical Image Analysis\s+\d{2,4}\b|\bMedical Image Analysis\s+\d+\s*\(", re.I)),
    ("Pattern Recognition", re.compile(r"\bPattern Recognition(?: Letters)?\s+\d{2,4}\b|\bPattern Recognition\s+\d+\s*\(", re.I)),
    ("Information Sciences", re.compile(r"\bInformation Sciences\s+\d{2,4}\b|\bInformation Sciences\s+\d+\s*\(", re.I)),
    ("Knowledge-Based Systems", re.compile(r"\bKnowledge-Based Systems\s+\d{2,4}\b|\bKnowledge-Based Systems\s+\d+\s*\(", re.I)),
    ("Computers in Biology and Medicine", re.compile(r"\bComputers in Biology and Medicine\s+\d{2,4}\b|\bComputers in Biology and Medicine\s+\d+\s*\(", re.I)),
    ("IEEE TMI", re.compile(r"\bIEEE Transactions on Medical Imaging\b|\bIEEE TRANSACTIONS ON MEDICAL IMAGING\b", re.I)),
    ("IEEE JSTARS", re.compile(r"\bIEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing\b|\bIEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH", re.I)),
    ("European Control Conference (ECC)", re.compile(r"\bEuropean Control Conference\s*\(ECC\)", re.I)),
    ("UKACC Control", re.compile(r"\bUKACC\b.*\bConference on Control\b|\bConference on Control\s*\(CONTROL\)", re.I)),
    ("Remote Sensing", re.compile(r"\bRemote Sensing\s+\d{4}\b|\bRemote Sensing\s+\d+\s*[,)]|mdpi\.com/journal/remotesensing", re.I)),
    ("Scientific Reports", re.compile(r"\bScientific Reports\b", re.I)),
    ("Sensors", re.compile(r"\bSensors\s+\d{4}\b|\bSensors\s+\d+\s*[,)]|mdpi\.com/journal/sensors", re.I)),
    ("Applied Sciences", re.compile(r"\bApplied Sciences\b", re.I)),
    ("Electronics", re.compile(r"\bElectronics\s+\d{4}\b|\bElectronics\s+\d+\s*[,)]|mdpi\.com/journal/electronics", re.I)),
    ("Machines", re.compile(r"\bMachines\s+\d{4}\b|\bMachines\s+\d+\s*[,)]|mdpi\.com/journal/machines", re.I)),
    ("iScience", re.compile(r"\biScience\b", re.I)),
    ("ISPRS Archives", re.compile(r"\bISPRS\b.*\bArchives\b|\bInternational Archives of the Photogrammetry", re.I)),
    ("IEEE TPAMI", re.compile(r"\bTPAMI\b|IEEE Transactions on Pattern Analysis", re.I)),
    ("IEEE TIP", re.compile(r"\bTIP\b|IEEE Transactions on Image Processing", re.I)),
    ("IEEE TGRS", re.compile(r"\bTGRS\b|IEEE Transactions on Geoscience", re.I)),
    ("CVPR", re.compile(r"\bCVPR\b|Computer Vision and Pattern Recognition", re.I)),
    ("ICCV", re.compile(r"\bICCV\b|International Conference on Computer Vision", re.I)),
    ("ECCV", re.compile(r"\bECCV\b|European Conference on Computer Vision", re.I)),
    ("NeurIPS", re.compile(r"\bNeurIPS\b|\bNIPS\b", re.I)),
    ("ICML", re.compile(r"\bICML\b|International Conference on Machine Learning", re.I)),
    ("ICLR", re.compile(r"\bICLR\b|International Conference on Learning Representations", re.I)),
    ("AAAI", re.compile(r"\bAAAI\b", re.I)),
    ("MICCAI", re.compile(r"\bMICCAI\b", re.I)),
)

FILENAME_VENUE_HINTS = (
    ("medical-image-an", "Medical Image Analysis"),
    ("medical-ima", "Medical Image Analysis"),
    ("pattern-r", "Pattern Recognition"),
    ("informati", "Information Sciences"),
    ("knowledge", "Knowledge-Based Systems"),
    ("computers-in-biolog", "Computers in Biology and Medicine"),
    ("scientific_reports", "Scientific Reports"),
    ("scientific-reports", "Scientific Reports"),
    ("cjig", "中国图象图形学报"),
    ("remote_sensing", "Remote Sensing"),
    ("remote-sensing", "Remote Sensing"),
    ("sensors", "Sensors"),
    ("applsci", "Applied Sciences"),
    ("electronics", "Electronics"),
    ("machines", "Machines"),
    ("isprs", "ISPRS Archives"),
    ("tpami", "IEEE TPAMI"),
    ("ieee-tip", "IEEE TIP"),
    ("arxiv", "arXiv"),
)

CURATED_VENUE_OVERRIDES = {
    "26211-41200-1-SM": "AMMS 2018",
    "2023_Limpets_Computer_Vision_Frontiers": "Frontiers in Marine Science",
    "AFF": "CVPR",
    "ASSA&FRFN": "CVPR",
    "Attention": "ECCV",
    "Dysample(上采样)": "ICCV",
    "EBSCO-FullText-09_12_2025": "Social Behavior and Personality",
    "FMM": "ICCV",
    "FSAS&DFFN": "CVPR",
    "GraphLayer": "ECCV",
    "PCBAM&SWA": "PLOS ONE",
    "Parallel ViT": "ECCV",
    "RAMiT&HRAMi": "CVPR Workshops",
    "SGFN&ASSA&ACSA": "ICCV",
    "Three-ways-ChatGPT-helps-me-in-my-academic-writing": "Nature",
    "SwiftFormerEncoder&ConvEncoder": "ICCV",
    "cjig_paper_5": "中国图象图形学报",
    "cjig_图像处理_深度伪造及其取证技术综述": "中国图象图形学报",
    "s10462-025-11212-y": "Artificial Intelligence Review",
    "一种针对多分类的网络入侵检测系统模型_杨启成": "哈尔滨工业大学学报",
    "基于双向时序窗口Transformer的网络入侵检测方法_王长浩": "计算机应用研究",
    "基于深度学习的有向目标检测研究进展_基于深度学习的有向目标检测研究进展": "图像与信号处理",
    "基于知识蒸馏的轻量化恶意流量检测方法_孙剑文": "信息网络安全",
    "科学数据与科学文献关联信息存在状态与整合模式设计研究_卫军朝": "情报科学",
    "红外与可见光图像分组融合的视觉Transformer": "中国图象图形学报",
    "融合CNN-GRU和Transformer的网络入侵检测方法_黄迎春": "火力与指挥控制",
    "融合Transformer和Inception的网络入侵检测研究_张万琪": "电信科学",
    "融合数据映射和知识蒸馏的恶意软件轻量化检测方法_罗养霞": "武汉大学学报(理学版)",
    "论托马斯·库恩科学哲学的创...学革命的结构》出版60周年_崔伟奇": "自然辩证法研究",
    "ssrn-5357895": "G-CARED 2025",
    "2010_Detecting_Botnets_Th": "未明确",
    "2019_Spectrum_Prediction": "未明确",
    "2022_SODA_Site_Object_De": "未明确",
    "生物孔隙分割 Bio-Pores": "Preprint submitted to Elsevier",
    "直肠分割放疗 Deep Rectum": "未明确",
    "2024_三维人脸成像及重建技术综述": "中国图象图形学报",
    "2024_融合场景先验的船名文本检测方法": "中国图象图形学报",
    "2024_融合非局部特征表示的模糊图像复原": "中国图象图形学报",
    "2024_面向三维人体坐标及旋转角估计的注意力融合网络": "中国图象图形学报",
    "图像重定向质量评价的研究进展": "中国图象图形学报",
    "无人机视角下的目标检测研究进展": "中国图象图形学报",
    "注意力引导局部特征联合学习的人脸表情识别": "中国图象图形学报",
    "深度学习的跨视角地理定位方法综述": "中国图象图形学报",
    "深度学习背景下的图像语义分割方法综述": "中国图象图形学报",
    "面向图像复原的非因果选择性状态空间模型": "中国图象图形学报",
    "面向深度学习的三维点云补全算法综述": "中国图象图形学报",
    "高斯_维纳表示下的稠密焦栈图生成方法": "中国图象图形学报",
}

CURATED_YEAR_OVERRIDES = {
    "AFF": "2024",
    "ASSA&FRFN": "2024",
    "Attention": "2022",
    "Dysample(上采样)": "2023",
    "FMM": "2023",
    "FSAS&DFFN": "2023",
    "GraphLayer": "2022",
    "Parallel ViT": "2022",
    "RAMiT&HRAMi": "2024",
    "SGFN&ASSA&ACSA": "2023",
    "SwiftFormerEncoder&ConvEncoder": "2023",
}

CURATED_AUTHOR_OVERRIDES = {
    "ASSA&FRFN": ["Shihao Zhou", "Duosheng Chen", "Jinshan Pan", "Jinglei Shi", "Jufeng Yang"],
    "Attention": ["Ardian Umam", "Cheng-Kun Yang", "Yung-Yu Chuang", "Jen-Hui Chuang", "Yen-Yu Lin"],
    "2010_Detecting_Botnets_Th": ["Yousof Al-Hammadi", "Uwe Aickelin"],
    "2010_Implications_of_the": ["N. Haghighipour", "S. Rastegar"],
    "2017_A_Comprehensive_Surv": ["John E. Ball", "Derek T. Anderson", "Chee Seng Chan"],
    "2017_Real-Time_Illegal_Pa": ["Xuemei Xie", "Chenye Wang", "Shu Chen", "Guangming Shi", "Zhifu Zhao"],
    "2018_Automatic_Pixelwise": ["Andrew Khalel", "Motaz El-Saban"],
    "2018_Deep_learning_based": ["Zhiwei Li", "Huanfeng Shen", "Qing Cheng", "Yuhao Liu", "Shucheng You", "Zongyi He"],
    "2019_Anticipating_Illegal": ["James R. Watson", "A. John Woodill"],
    "2019_Building_change_dete": ["Bi Qi", "Kun Qin", "Han Zhang", "Wenjun Han", "Zhili Li", "Kai Xu"],
    "2019_Spectrum_Prediction": ["Lissy Pellaco", "Nirankar Singh", "Joakim Jaldén"],
    "2020_Predicting_Illegal_F": ["A. John Woodill", "Maria Kavanaugh", "Michael Harte", "James R. Watson"],
    "2023_Learning_Efficient_U": ["Yiyun Zhang", "Zijian Wang", "Yadan Luo", "Xin Yu", "Zi Huang"],
    "2024_Correlation_of_Objec": ["Matthias Bartolo", "Dylan Seychell"],
    "2024_YOLOv5-Based_Object": ["Sindhu Boddu", "Arindam Mukherjee"],
    "2025_2510.09893_HIPPD_Brain-Inspired_Personality_Detection": [
        "Guanming Chen",
        "Lingzhi Shen",
        "Xiaohao Cai",
        "Shoaib Jameel",
        "Imran Razzak",
    ],
    "3D树木分割图 3D Tree Segmentation": [
        "Jonathan Williams",
        "Carola-Bibiane Schönlieb",
        "Tom Swinfield",
        "Juheon Lee",
        "Xiaohao Cai",
        "Lan Qie",
        "David A. Coomes",
    ],
    "CasDyFBlock&RMB&LFB": ["Yinglong Wang", "Bin He"],
    "CornerPoint3D 3D检测新尺度 CornerPoint3D": [
        "Ruixiao Zhang",
        "Runwei Guan",
        "Xiangyu Chen",
        "Adam Prugel-Bennett",
        "Xiaohao Cai",
    ],
    "DA_Block": [
        "Guanqun Sun",
        "Yizhi Pan",
        "Weikun Kong",
        "Zichang Xu",
        "Jianhua Ma",
        "Teeradaj Racharak",
        "Le-Minh Nguyen",
        "Junyi Xin",
    ],
    "DWConv": ["François Chollet"],
    "FECAttention(时序预测)": ["Maowei Jiang", "Pengyu Zeng", "Kai Wang", "Huan Liu", "Wenbo Chen", "Haoran Liu"],
    "LAE&MSFM&RFAConv": ["Zhongwen Yu", "Qiu Guan", "Jianmin Yang", "Zhiqiang Yang", "Qianwei Zhou", "Yang Chen", "Feng Chen"],
    "Mask_to_Height_YOLOv11_2510.27224": ["Mahmoud El Hussieni", "Bahadır K. Güntürk", "Hasan F. Ateş", "Oğuz Hanoğlu"],
    "RSSG": ["Hang Guo", "Jinmin Li", "Tao Dai", "Zhihao Ouyang", "Xudong Ren", "Shu-Tao Xia"],
    "平衡神经网络搜索I Balanced NAS I": ["Mingyang Du", "Ping Zhong", "Xiaohao Cai", "Daping Bi", "Zhifei Li"],
    "深度学习架构综述 CNNs RNNs Transformers": ["Khaled Alomar", "Halil Ibrahim Aysel", "Xiaohao Cai"],
    "船舶匹配遥感 Ship Matching": ["Leyang Li", "Guixing Cao", "Jun Liu", "Xiaohao Cai"],
}

AFFILIATION_WORDS = re.compile(
    r"\b(University|Institute|School|Department|College|Laboratory|Lab|Academy|"
    r"Faculty|Hospital|Center|Centre|Dept\.?|Corporation|Inc\.|Ltd\.|China|USA|"
    r"United States|UK|Australia|Switzerland|Spain|Russia|India|Germany|France|"
    r"Campus|Directorate|Corp\.?|Consulting|LLC|Beijing|Shanghai|Guangzhou|"
    r"Hong Kong|Email|Corresponding|Abstract|Keywords|Index Terms|Preprint|"
    r"Submitted|Accepted|Published)\b",
    re.I,
)
BAD_AUTHOR_WORDS = re.compile(
    r"\b(Student|Member|Senior|Lead|Author|Research|Building|Construction|"
    r"Satellite|Imagery|Information|System|Systems|Concepts|General|Current|"
    r"Progress|Future|Trends|Programmable|Gradients|Citation|Early|Access|"
    r"IEEE|TRANSACTIONS|Medical|Imaging|Journal|Volume|VOL|NO|Abstract|"
    r"Keywords|Editor|Chief|Commission|Working|Group|WG|Appendix|Filter|"
    r"Pascal|VOC|Context|Notably|Processing|Speed|Target|Object|Article|"
    r"Info|Revised|December|Fig|Table|Result|Results|Dataset|Engineering|"
    r"Technology|Technologies|Science|Sciences|Tech|Fund|Institute|College|"
    r"Intelligent|Intelligence|Communication|Communications|Environmental|"
    r"Received|Publishing|Operations|Hoes|Lane|Enhancement|Speech|Automatic|"
    r"Play|Haidian|District|Monaural|Components)\b",
    re.I,
)
AUTHOR_ROLE_WORDS = re.compile(
    r"\b(Student\s+Member|Senior\s+Member|Member|Fellow|IEEE|ACM|Dr\.?|Mr\.?|Ms\.?|Mrs\.?)\b",
    re.I,
)
BAD_AUTHOR_SUBSTRINGS = (
    "university", "institute", "department", "laboratory", "academy", "sensetime",
    "researchgate", "preprint", "copyright", "all rights reserved",
    "machine intelligence", "electronic engineering", "software engineering",
    "review copy", "do not distribute", "article info",
)
VENUE_AFFILIATION_RE = re.compile(
    r"\b(University|Institute|Department|School|Faculty|College|Laboratory|"
    r"Lab|Center|Centre|Hospital|Ministry|Academy|Corporation|"
    r"Research\s+Laborator(?:y|ies)|Foundation|Funding|Grant|"
    r"Authorized\s+licensed\s+use|Downloaded\s+on|Abstract|Keywords|"
    r"Corresponding|Email|e-mail)\b",
    re.I,
)
BAD_CHINESE_AUTHOR_VALUES = {
    "完整版", "现状及展望", "方法综述", "研究进展", "性能", "未来", "建议", "目前",
    "因此", "为了避免", "随机噪声", "降低成本", "色彩分明", "突破", "本文在",
    "在高斯", "深入探讨", "高精度和", "研究方向", "展望",
}
COMMON_CHINESE_SURNAMES = set(
    "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜"
    "戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐"
    "费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余元卜顾孟平"
    "黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴宋庞熊纪舒屈项祝董梁"
    "杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田胡凌霍"
    "虞万支柯昝管卢莫经房裘缪干解应宗丁宣邓郁单杭洪包诸左石崔吉龚程"
    "邢裴陆荣翁荀羊於惠甄曲家封芮羿储靳汲邴糜松井段富巫乌焦巴弓牧隗"
    "武"
)
TITLE_WORDS = re.compile(
    r"\b(Detection|Segmentation|Classification|Recognition|Network|Networks|"
    r"Model|Models|Learning|Survey|Review|Method|Methods|Approach|Image|Images|"
    r"Remote|Sensing|Transformer|Mamba|Diffusion|Dataset|Benchmark|Based|Using|"
    r"via|for|with|of|and|the)\b",
    re.I,
)


@dataclass
class InferredValue:
    value: Any
    source: str


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---", 4)
    if end < 0:
        return "", text
    return text[4:end], text[end + 4 :]


def quote_yaml(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def clean_text_line(line: str) -> str:
    line = line.replace("\x00", " ").replace("\uf0a7", " ")
    line = re.sub(r"[\u0001-\u001f\u007f]+", " ", line)
    line = re.sub(r"\s+", " ", line)
    return line.strip()


def useful_lines(text: str, limit: int = 80) -> list[str]:
    lines = []
    for raw in text.splitlines():
        line = clean_text_line(raw)
        if not line or line.startswith("# "):
            continue
        lines.append(line)
        if len(lines) >= limit:
            break
    return lines


def infer_year_from_arxiv(stem: str, text: str) -> Optional[str]:
    match = re.match(r"^(\d{2})(\d{2})\.\d{4,5}(?:v\d+)?$", stem)
    if not match:
        match = re.search(r"(?:^|[_-])(\d{2})(\d{2})\.\d{4,5}(?:v\d+)?(?:$|[_-])", stem)
    if not match:
        match = re.search(r"arxiv:(\d{2})(\d{2})\.\d{4,5}(?:v\d+)?\b", text, re.I)
    if not match:
        return None
    yy = int(match.group(1))
    year = 2000 + yy if yy <= 30 else 1900 + yy
    return str(year)


def infer_year(stem: str, text: str) -> Optional[InferredValue]:
    curated = CURATED_YEAR_OVERRIDES.get(stem)
    if curated:
        return InferredValue(curated, "curated-cache-year")

    arxiv_year = infer_year_from_arxiv(stem, text)
    if arxiv_year:
        return InferredValue(arxiv_year, "arxiv-id")

    explicit = re.search(r"\b(19|20)\d{2}\b", stem)
    if explicit:
        return InferredValue(explicit.group(0), "filename-year")

    for match in re.finditer(r"\b(19|20)\d{2}\b", text[:6000]):
        year = int(match.group(0))
        if 1990 <= year <= 2030:
            return InferredValue(str(year), "cache-text-year")
    return None


def infer_venue(stem: str, text: str) -> Optional[InferredValue]:
    curated = CURATED_VENUE_OVERRIDES.get(stem)
    if curated:
        return InferredValue(curated, "curated-cache-venue")

    stem_lower = stem.lower()
    if (
        re.search(r"arxiv:\d{4}\.\d{4,5}", text, re.I)
        or re.match(r"^\d{4}\.\d{4,5}v?\d*$", stem)
        or re.search(r"(?:^|[_-])\d{4}\.\d{4,5}(?:v\d+)?(?:$|[_-])", stem)
    ):
        return InferredValue("arXiv", "arxiv-id")

    for hint, venue in FILENAME_VENUE_HINTS:
        if hint in stem_lower:
            return InferredValue(venue, f"filename-hint:{hint}")

    lines = useful_lines(text, limit=120)
    for line in lines:
        if len(line) > 220:
            continue
        for venue, pattern in VENUE_PATTERNS:
            if pattern.search(line):
                return InferredValue(venue, "cache-text-venue")
    return None


def strip_author_marker(name: str, strip_affiliation_suffix: bool = False) -> str:
    name = re.sub(r"[\*†‡§¶#]+", "", name)
    name = AUTHOR_ROLE_WORDS.sub("", name)
    name = re.sub(r"\s+", " ", name).strip(" ,;")
    words = name.split()
    if words:
        last = words[-1]
        # PDF extraction often glues affiliation letters: `Fenga`, `Qiaob`, `Xic`.
        if strip_affiliation_suffix and len(last) > 2 and re.search(r"[A-Za-z]+[a-f]$", last):
            words[-1] = last[:-1]
    return " ".join(words)


def normalize_author_case(name: str) -> str:
    """Turn all-caps PDF names into readable title case without touching initials."""
    if not name or not name.isupper():
        return name
    parts = []
    for word in name.split():
        if "." in word:
            parts.append(word)
        else:
            parts.append(word[:1] + word[1:].lower())
    return " ".join(parts)


def fix_broken_name_spaces(text: str) -> str:
    """Repair common PDF extraction splits inside a single name token."""
    text = re.sub(r"\b([A-Z][a-z]{1,4})\s+([a-z]{3,})\b", r"\1\2", text)
    text = re.sub(r"\b([A-Za-z]+-[a-z]{2,})\s+([a-z]{2,})\b", r"\1\2", text)
    return text


def normalize_author_part(
    part: str,
    strip_affiliation_suffix: bool = False,
    allow_chinese_name: bool = False,
) -> Optional[str]:
    part = clean_text_line(part)
    part = re.sub(r"\([^)]*\)", "", part)
    part = AUTHOR_ROLE_WORDS.sub("", part)
    part = re.sub(r"(?<=[A-Za-z\u4e00-\u9fff])\d+(?:,\d+)*", "", part)
    part = re.sub(r"\b\d+(?:,\d+)*\b", "", part)
    part = re.sub(r"^(?:USA|US|UK|OH|DC|NY|CA|TX|VA|NC)(?=[A-Z])", "", part)
    part = re.sub(r"^(?:and|&)\s+", "", part, flags=re.I)
    part = re.sub(r"^[a-z]\s*", "", part)
    part = strip_author_marker(part, strip_affiliation_suffix=strip_affiliation_suffix)
    part = fix_broken_name_spaces(part)
    part = re.sub(r"[^A-Za-zÀ-ÖØ-öø-ÿ\u4e00-\u9fff\.\-'\s]", "", part)
    part = re.sub(r"\s+", " ", part).strip(" .,-")
    if not part:
        return None
    if re.fullmatch(r"[\u4e00-\u9fff]{2,5}", part):
        if (
            allow_chinese_name
            and part not in BAD_CHINESE_AUTHOR_VALUES
            and part[0] in COMMON_CHINESE_SURNAMES
        ):
            return part
        return None
    lowered = part.lower()
    if any(token in lowered for token in BAD_AUTHOR_SUBSTRINGS):
        return None
    if re.search(r"[a-z][A-Z]", part):
        return None
    if AFFILIATION_WORDS.search(part) or BAD_AUTHOR_WORDS.search(part) or TITLE_WORDS.search(part):
        return None
    words = part.split()
    if not (2 <= len(words) <= 5):
        return None
    for word in words:
        cleaned = word.strip(".-'")
        if len(cleaned) == 1 and "." not in word:
            return None
    if len(words) >= 3 and part.isupper():
        return None
    if not all(re.search(r"[A-ZÀ-ÖØ-Þ]", word[:1]) for word in words if word):
        return None
    return normalize_author_case(part)


def parse_author_line(line: str, allow_single: bool = False) -> list[str]:
    line = clean_text_line(line)
    if not line or len(line) > 220:
        return []
    affiliation_line = re.sub(
        r"^[a-z](?=(School|Department|Institute|College|Faculty|Lab|Laboratory|Center|Centre))",
        "",
        line,
    )
    if AFFILIATION_WORDS.search(affiliation_line):
        return []
    if re.search(r"@|https?://|doi\.org|arXiv", line, re.I):
        return []
    if re.search(r"\b(via|using|based|survey|review|dataset|benchmark)\b", line, re.I):
        return []

    line = re.sub(r"(?<=[0-9])(?=[A-ZÀ-ÖØ-Þ])", ", ", line)
    line = AUTHOR_ROLE_WORDS.sub("", line)
    if line.count(". ") and len(line.split()) > 18:
        line = line.rsplit(". ", 1)[1]
    if re.search(r"[,;]|\band\b|[\u4e00-\u9fff].*[，、]|&", line, re.I):
        parts = re.split(r"\s*(?:,|;|\band\b|&|、|，)\s*", line, flags=re.I)
    else:
        parts = [line]
    marked_parts = [
        part for part in parts
        if re.search(r"[A-Za-z]{2,}[a-f](?:[\*†‡§¶#\d\s]*)$", part.strip())
    ]
    strip_affiliation_suffix = len(parts) >= 2 and len(marked_parts) >= max(2, len(parts) // 2)
    allow_chinese_name = bool(re.search(r"[、，,;]", line))

    authors = []
    for part in parts:
        author = normalize_author_part(
            part,
            strip_affiliation_suffix=strip_affiliation_suffix,
            allow_chinese_name=allow_chinese_name,
        )
        if author and author not in authors:
            authors.append(author)
    if len(authors) == 1 and TITLE_WORDS.search(authors[0]):
        return []
    if len(authors) == 1 and not allow_single:
        return []
    return authors[:12]


def line_is_affiliation_like(line: str) -> bool:
    affiliation_line = re.sub(
        r"^[a-z](?=(School|Department|Institute|College|Faculty|Lab|Laboratory|Center|Centre))",
        "",
        clean_text_line(line),
    )
    return bool(
        AFFILIATION_WORDS.search(affiliation_line)
        or re.search(r"@|University|Department|Institute|School|Tech|Fund", affiliation_line, re.I)
    )


def author_line_prefix_before_affiliation(line: str) -> str:
    parts = re.split(
        r",\s*(?:The\s+)?(?:University|Institute|School|Department|College|Faculty|"
        r"Laboratory|Lab|Center|Centre|Academy|Old Dominion|Idiap|Stanford|"
        r"Cornell|Duke|Texas|Worcester|Innopolis|Australian|Energy Initiative)",
        line,
        maxsplit=1,
        flags=re.I,
    )
    return parts[0]


def same_authorish(a: str, b: str) -> bool:
    clean_a = re.sub(r"[^A-Za-z\u4e00-\u9fff]", "", a).lower()
    clean_b = re.sub(r"[^A-Za-z\u4e00-\u9fff]", "", b).lower()
    if not clean_a or not clean_b:
        return False
    shorter, longer = sorted((clean_a, clean_b), key=len)
    return len(shorter) >= 6 and longer.startswith(shorter)


def append_author(authors: list[str], author: str) -> None:
    for idx, existing in enumerate(authors):
        if same_authorish(existing, author):
            if len(author) > len(existing):
                authors[idx] = author
            return
    if author not in authors:
        authors.append(author)


def clean_author_list(authors: list[str]) -> list[str]:
    cleaned: list[str] = []
    has_chinese = any(re.search(r"[\u4e00-\u9fff]", author) for author in authors)
    for author in authors:
        if has_chinese and not re.search(r"[\u4e00-\u9fff]", author):
            # Chinese journals often repeat an English transliteration after the Chinese author line.
            continue
        if BAD_AUTHOR_WORDS.search(author) or AFFILIATION_WORDS.search(author):
            continue
        if any(token in author.lower() for token in BAD_AUTHOR_SUBSTRINGS):
            continue
        append_author(cleaned, author)
    return cleaned


def glued_country_author(line: str) -> Optional[str]:
    match = re.search(
        r"(?:USA|US|UK|University|Institute|Corp\.?|Lab|Fund)"
        r"([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z.\-]+){1,4})$",
        line,
    )
    if not match:
        return None
    return normalize_author_part(match.group(1), allow_chinese_name=False)


def parse_author_block(lines: list[str], title: str) -> Optional[list[str]]:
    """Handle first-page layouts where one author appears per affiliation line."""
    if not lines:
        return None

    abstract_idx = next(
        (i for i, line in enumerate(lines) if re.match(r"^(Abstract|ABSTRACT|摘要)\b", line, re.I)),
        min(len(lines), 40),
    )
    search_limit = min(len(lines), max(abstract_idx, 12))
    authors: list[str] = []
    title_seen = False

    for idx, line in enumerate(lines[:search_limit]):
        prefix_candidate = parse_author_line(author_line_prefix_before_affiliation(line), allow_single=True)
        if title_overlap(line, title) or (
            idx > 0
            and title_overlap(f"{lines[idx - 1]} {line}", title)
            and not prefix_candidate
        ):
            title_seen = True
            continue
        if not title_seen and idx > 8:
            continue
        if re.match(r"^(Abstract|ABSTRACT|摘要)\b", line, re.I):
            break

        glued = glued_country_author(line)
        if glued:
            append_author(authors, glued)
            continue

        before_affiliation = author_line_prefix_before_affiliation(line)
        candidates = prefix_candidate
        next_line_continues_author = (
            idx + 1 < len(lines)
            and re.match(r"^[\*∗†‡§¶#,\s]+[A-ZÀ-ÖØ-Þ]", lines[idx + 1])
        )
        if len(candidates) == 1 and (
            "," in line
            or next_line_continues_author
            or (idx + 1 < len(lines) and line_is_affiliation_like(lines[idx + 1]))
            or (idx + 2 < len(lines) and line_is_affiliation_like(lines[idx + 2]))
        ):
            append_author(authors, candidates[0])
            continue
        if line_is_affiliation_like(line):
            continue

        candidates = parse_author_line(line)
        if candidates:
            for author in candidates:
                append_author(authors, author)
            continue
        if len(authors) >= 2 and title_seen:
            break

    authors = clean_author_list(authors)
    return authors[:12] if len(authors) >= 2 else None


def extend_with_author_continuations(authors: list[str], lines: list[str], start_idx: int) -> list[str]:
    extended = list(authors)
    for line in lines[start_idx + 1 : start_idx + 3]:
        if not re.match(r"^[\*∗†‡§¶#,\s]*(?:and\s+)?[A-ZÀ-ÖØ-Þ]", line):
            break
        for author in parse_author_line(line, allow_single=True):
            append_author(extended, author)
    return clean_author_list(extended)


def title_overlap(line: str, title: str) -> bool:
    if not title or title.endswith(".pdf"):
        return False
    line_words = {w.lower() for w in re.findall(r"[A-Za-z]{4,}", line)}
    title_words = {w.lower() for w in re.findall(r"[A-Za-z]{4,}", title)}
    if not line_words or not title_words:
        return False
    return len(line_words & title_words) >= max(2, min(4, len(title_words) // 2))


def infer_chinese_author_from_stem(stem: str) -> Optional[InferredValue]:
    if "_" not in stem:
        return None
    suffix = stem.rsplit("_", 1)[1].strip()
    if (
        re.fullmatch(r"[\u4e00-\u9fff]{2,5}", suffix)
        and suffix not in BAD_CHINESE_AUTHOR_VALUES
        and suffix[0] in COMMON_CHINESE_SURNAMES
    ):
        return InferredValue([suffix], "filename-author-suffix")
    return None


def infer_authors(stem: str, title: str, text: str) -> Optional[InferredValue]:
    curated = CURATED_AUTHOR_OVERRIDES.get(stem)
    if curated:
        return InferredValue(curated, "curated-cache-authors")

    from_stem = infer_chinese_author_from_stem(stem)
    if from_stem:
        return from_stem

    lines = useful_lines(text, limit=120)
    from_block = parse_author_block(lines, title)
    if from_block:
        return InferredValue(from_block, "cache-text-author-block")

    abstract_idx = next(
        (i for i, line in enumerate(lines) if re.match(r"^(Abstract|摘要)\b", line, re.I)),
        min(len(lines), 20),
    )
    search_lines = lines[:abstract_idx]

    for idx, line in enumerate(search_lines):
        if title_overlap(line, title):
            continue
        authors = parse_author_line(line)
        if authors:
            return InferredValue(extend_with_author_continuations(authors, search_lines, idx), "cache-text-author-line")

        allow_single = bool(
            idx > 0
            and (title_overlap(search_lines[idx - 1], title) or (idx > 1 and title_overlap(search_lines[idx - 2], title)))
            and (idx + 1 >= len(search_lines) or line_is_affiliation_like(search_lines[idx + 1]))
        )
        if allow_single:
            authors = parse_author_line(line, allow_single=True)
            if authors:
                authors = clean_author_list(authors)
                if authors:
                    return InferredValue(authors, "cache-text-single-author-line")

    # Some IEEE PDFs extract the abstract column before the title and author line.
    for idx, line in enumerate(lines[:120]):
        if title_overlap(line, title):
            continue
        authors = parse_author_line(line)
        if authors:
            return InferredValue(extend_with_author_continuations(authors, lines, idx), "cache-text-late-author-line")
    return None


def infer_metadata(stem: str, title: str, cache_text: str) -> dict[str, InferredValue]:
    out: dict[str, InferredValue] = {}
    authors = infer_authors(stem, title, cache_text)
    year = infer_year(stem, cache_text)
    venue = infer_venue(stem, cache_text)
    if authors:
        out["authors"] = authors
    if year:
        out["year"] = year
    if venue:
        out["venue"] = venue
    return out


def field_block_bounds(lines: list[str], key: str) -> Optional[tuple[int, int]]:
    start = None
    key_re = re.compile(rf"^{re.escape(key)}\s*:")
    next_key_re = re.compile(r"^[A-Za-z_][\w-]*\s*:")
    for idx, line in enumerate(lines):
        if key_re.match(line):
            start = idx
            break
    if start is None:
        return None
    end = start + 1
    while end < len(lines) and not next_key_re.match(lines[end]):
        end += 1
    return start, end


def insert_index_for_field(lines: list[str]) -> int:
    for preferred in ("pdf", "primary_topic", "status"):
        bounds = field_block_bounds(lines, preferred)
        if bounds:
            return bounds[0]
    return len(lines)


def replace_field(lines: list[str], key: str, new_lines: list[str]) -> list[str]:
    bounds = field_block_bounds(lines, key)
    if bounds:
        start, end = bounds
        return lines[:start] + new_lines + lines[end:]
    idx = insert_index_for_field(lines)
    return lines[:idx] + new_lines + lines[idx:]


def frontmatter_field_is_blank(fm_text: str, key: str) -> bool:
    parsed = parse_frontmatter("---\n" + fm_text + "\n---\n")
    return key not in parsed or is_blank_frontmatter_value(parsed[key])


def yaml_list_values(value: str) -> list[str]:
    normalized = frontmatter_scalar(value)
    if is_blank_frontmatter_value(normalized):
        return []
    if normalized.startswith("[") and normalized.endswith("]"):
        inner = normalized[1:-1].strip()
        if not inner:
            return []
        return [
            item.strip().strip('"').strip("'").strip()
            for item in inner.split(",")
            if item.strip().strip('"').strip("'").strip()
        ]
    return [normalized]


def authors_value_is_suspicious(value: str) -> bool:
    authors = yaml_list_values(value)
    if not authors:
        return False
    for author in authors:
        if (
            "@" in author
            or re.search(r"\b(?:Corp|Corporation|Google|Inc|Ltd|LLC)\.?\b", author, re.I)
            or AFFILIATION_WORDS.search(author)
            or BAD_AUTHOR_WORDS.search(author)
            or any(token in author.lower() for token in BAD_AUTHOR_SUBSTRINGS)
        ):
            return True
    return False


def venue_value_is_suspicious(value: str) -> bool:
    normalized = frontmatter_scalar(value)
    if is_blank_frontmatter_value(normalized):
        return False
    if VENUE_AFFILIATION_RE.search(normalized):
        return True
    if re.search(r"\b(?:Senior\s+Member|Member|Fellow)\s*,\s*IEEE\b", normalized, re.I):
        return True
    if len(normalized) > 120 and normalized.count(",") >= 4:
        return True
    return False


def frontmatter_field_should_update(
    fm_text: str,
    key: str,
    replace_suspicious: bool = False,
) -> bool:
    parsed = parse_frontmatter("---\n" + fm_text + "\n---\n")
    if key not in parsed or is_blank_frontmatter_value(parsed[key]):
        return True
    return bool(
        replace_suspicious
        and (
            (key == "authors" and authors_value_is_suspicious(parsed[key]))
            or (key == "venue" and venue_value_is_suspicious(parsed[key]))
        )
    )


def update_note_frontmatter(
    text: str,
    updates: dict[str, InferredValue],
    replace_suspicious: bool = False,
) -> tuple[str, list[str]]:
    fm_text, body = split_frontmatter(text)
    if not fm_text:
        return text, []

    lines = fm_text.splitlines()
    changed = []

    authors = updates.get("authors")
    if authors and frontmatter_field_should_update("\n".join(lines), "authors", replace_suspicious):
        author_lines = ["authors:"] + [f"  - {quote_yaml(author)}" for author in authors.value]
        lines = replace_field(lines, "authors", author_lines)
        changed.append("authors")

    year = updates.get("year")
    if year and frontmatter_field_should_update("\n".join(lines), "year", replace_suspicious):
        lines = replace_field(lines, "year", [f"year: {year.value}"])
        changed.append("year")

    venue = updates.get("venue")
    if venue and frontmatter_field_should_update("\n".join(lines), "venue", replace_suspicious):
        lines = replace_field(lines, "venue", [f"venue: {quote_yaml(venue.value)}"])
        changed.append("venue")

    if not changed:
        return text, []
    return "---\n" + "\n".join(lines) + "\n---" + body, changed


def cache_path_for_note(note_path: Path, fm: dict[str, str], cache_dir: Path) -> Path:
    cache = frontmatter_scalar(fm.get("extract_cache", ""))
    if cache:
        path = ROOT / cache
        if path.is_file():
            return path
    return cache_dir / f"{note_path.stem}.txt"


def process_note(
    note_path: Path,
    cache_dir: Path,
    dry_run: bool,
    selected_fields: set[str],
    selected_sources: set[str],
    replace_suspicious: bool = False,
) -> tuple[list[str], dict[str, InferredValue]]:
    text = note_path.read_text(encoding="utf-8", errors="replace")
    fm = parse_frontmatter(text)
    if not fm:
        return [], {}
    document_type = frontmatter_scalar(fm.get("document_type", "paper")) or "paper"
    if document_type == "supplementary":
        return [], {}

    missing = [
        field for field in FIELDS
        if field in selected_fields
        and (
            field not in fm
            or is_blank_frontmatter_value(fm[field])
            or (replace_suspicious and field == "authors" and authors_value_is_suspicious(fm[field]))
            or (replace_suspicious and field == "venue" and venue_value_is_suspicious(fm[field]))
        )
    ]
    if not missing:
        return [], {}

    cache_path = cache_path_for_note(note_path, fm, cache_dir)
    cache_text = cache_path.read_text(encoding="utf-8", errors="replace") if cache_path.is_file() else ""
    title = frontmatter_scalar(fm.get("title", note_path.stem))
    inferred = infer_metadata(note_path.stem, title, cache_text)
    updates = {field: inferred[field] for field in missing if field in inferred}
    if selected_sources:
        updates = {
            field: value for field, value in updates.items()
            if value.source in selected_sources
        }
    if not updates:
        return [], inferred

    updated, changed = update_note_frontmatter(text, updates, replace_suspicious=replace_suspicious)
    if changed and not dry_run:
        note_path.write_text(updated, encoding="utf-8")
    return changed, updates


def main() -> int:
    parser = argparse.ArgumentParser(description="安全补齐 authors/year/venue 空字段")
    parser.add_argument("--notes-dir", type=Path, default=DEFAULT_NOTES)
    parser.add_argument("--cache-dir", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--only", nargs="*", default=[])
    parser.add_argument("--fields", nargs="+", choices=FIELDS, default=list(FIELDS))
    parser.add_argument(
        "--sources",
        nargs="*",
        default=[],
        help="只接受指定推断来源, 如 filename-author-suffix arxiv-id cache-text-venue",
    )
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument(
        "--replace-suspicious",
        action="store_true",
        help="允许替换明显误填的 authors 字段；默认仍只补空字段",
    )
    args = parser.parse_args()
    selected_fields = set(args.fields)
    selected_sources = set(args.sources)

    notes = sorted(args.notes_dir.glob("*.md"))
    if args.only:
        wanted = set(args.only)
        notes = [p for p in notes if p.stem in wanted]

    changed_notes = 0
    changed_fields: Counter[str] = Counter()
    inferred_sources: Counter[str] = Counter()
    unresolved = 0

    for note_path in notes:
        if args.limit and changed_notes >= args.limit:
            break
        changed, updates = process_note(
            note_path,
            args.cache_dir,
            args.dry_run,
            selected_fields,
            selected_sources,
            args.replace_suspicious,
        )

        if changed:
            changed_notes += 1
            changed_fields.update(changed)
            for field in changed:
                inferred_sources[f"{field}:{updates[field].source}"] += 1
            if args.verbose:
                details = ", ".join(
                    f"{field}={updates[field].value!r} ({updates[field].source})" for field in changed
                )
                action = "would update" if args.dry_run else "updated"
                print(f"{action} {note_path.name}: {details}")
        elif updates:
            unresolved += 1

    mode = "DRY RUN" if args.dry_run else "WRITE"
    print(f"metadata fill {mode} {date.today().isoformat()}")
    print(f"changed_notes: {changed_notes}")
    print(f"changed_fields: {dict(changed_fields)}")
    print(f"sources: {dict(inferred_sources)}")
    if unresolved:
        print(f"inferred_but_unchanged: {unresolved}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
