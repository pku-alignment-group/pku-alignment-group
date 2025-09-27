#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量生成publication页面的脚本
"""

import json
import os
import shutil
from datetime import datetime

# JSON数据
publications_data = {
    "publications": [
        {
            "year": 2025,
            "mediaType": "image",
            "title": "Revolutionizing health care: The transformative impact of large language models in medicine",
            "authors": [
                "Kuo Zhang",
                "Xiangbin Meng",
                "Xiangyu Yan",
                "Jiaming Ji",
                "Jingqian Liu",
                "Hua Xu",
                "Heng Zhang",
                "Da Liu",
                "Jingjia Wang",
                "Xuliang Wang",
                "Jun Gao",
                "Yuan-geng-shuo Wang",
                "Chunli Shao",
                "Wenyao Wang",
                "Jiarong Li",
                "Ming-Qi Zheng",
                "Yaodong Yang",
                "Yi-Da Tang"
            ],
            "venue": "Journal of Medical Internet Research.",
            "link": "https://www.jmir.org/2025/1/e59069",
            "thumbnail": "./assets/figures/publications/2025-01-Revolutionizing.png",
            "topic": [
                "AI Alignment"
            ],
            "type": "Article",
            "selected": 0,
            "Github": "#",
            "Data": "#",
            "LeaderBoard": "#",
            "Talks": "#",
            "MachineHeart": "#"
        },
        {
            "year": 2025,
            "title": "Stream Aligner: Efficient Sentence-Level Alignment via Distribution Induction",
            "authors": [
                "Hantao Lou", 
                "Jiaming Ji", 
                "Kaile Wang", 
                "Yaodong Yang"
            ],
            "venue": "AAAI 2025",
            "link": "https://arxiv.org/abs/2501.05336",
            "thumbnail": "./assets/figures/publications/2024-12-stream-aligner.png",
            "topic": [
                "AI Alignment"
            ]
        },
        {
            "year": 2025,
            "title": "Sequence to Sequence Reward Modeling: Improving RLHF by Language Feedback",
            "authors": [
                "Jiayi Zhou*", 
                "Jiaming Ji*", 
                "Juntao Dai", 
                "Yaodong Yang"
            ],
            "venue": "AAAI 2025 Oral.",
            "link": "https://arxiv.org/abs/2409.00162",
            "thumbnail": "./assets/figures/publications/2024-12-seq-to-seq-RM.png",
            "topic": [
                "AI Alignment"
            ],
            "selected": 1,
            "Github": "#",
            "Data": "#"
        },
        {
            "year": 2024,
            "title": "SafeSora: Towards Safety Alignment of Text2Video Generation via a Human Preference Dataset",
            "authors": [
                "Juntao Dai",
                "Tianle Chen",
                "Xuyao Wang",
                "Ziran Yang",
                "Taiye Chen",
                "Jiaming Ji",
                "Yaodong Yang"
            ],
            "venue": "NeurIPS 2024.",
            "link": "https://proceedings.neurips.cc/paper_files/paper/2024/hash/1eb543faf7c69e8a7eb8b85f70be818f-Abstract-Datasets_and_Benchmarks_Track.html",
            "thumbnail": "./assets/figures/publications/2024-06-safe-sora.png",
            "topic": [
                "AI Safety",
                "Safety Alignment"
            ]
        },
        {
            "year": 2024,
            "title": "Language Models Resist Alignment: Evidence From Data Compression",
            "authors": [
                "Jiaming Ji*",
                "Kaile Wang*",
                "Tianyi Qiu*",
                "Boyuan Chen*",
                "Jiayi Zhou",
                "Changye Li",
                "Hantao Lou",
                "Yaodong Yang"
            ],
            "venue": "Arxiv 2024.",
            "link": "https://arxiv.org/abs/2406.06144",
            "thumbnail": "./assets/figures/publications/2024-06-resist-alignment.png",
            "topic": [
                "Large Language Models",
                "Safety Alignment",
                "AI Safety"
            ],
            "selected": 1
        },
        {
            "year": 2024,
            "title": "ProgressGym: Alignment with a Millennium of Moral Progress",
            "authors": [
                "Tianyi Qiu*", 
                "Yang Zhang*", 
                "Xuchuan Huang", 
                "Jasmine Xinze Li", 
                "Jiaming Ji", 
                "Yaodong Yang"
            ],
            "venue": "NeurIPS 2024.",
            "link": "https://proceedings.neurips.cc/paper_files/paper/2024/file/1a6d49c1a298ebb799d005b7b90ab31d-Paper-Datasets_and_Benchmarks_Track.pdf",
            "thumbnail": "./assets/figures/publications/2024-06-progress-gym.png",
            "topic": [
                "Large Language Models",
                "AI Alignment"
            ],
            "selected": 1
        },
        {
            "year": 2024,
            "title": "PKU-SafeRLHF: Towards Multi-Level Safety Alignment for LLMs with Human Preference",
            "authors": [
                "Jiaming Ji*", 
                "Donghai Hong*", 
                "Borong Zhang*", 
                "Boyuan Chen*",
                "Josef Dai",
                "Boren Zheng",
                "Tianyi Qiu",
                "Boxun Li",
                "Yaodong Yang"
            ],
            "venue": "Arxiv 2024.",
            "link": "https://arxiv.org/abs/2406.15513",
            "thumbnail": "./assets/figures/publications/2024-06-pku-saferlhf.png",
            "topic": [
                "Large Language Models",
                "Safety Alignment",
                "Reinforcement Learning from Human Feedback"
            ],
            "selected": 1,
            "Data": "https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF"
        },
        {
            "year": 2024,
            "title": "The application of large language models in medicine: A scoping review",
            "authors": [
                "Xiangbin Meng", 
                "Xiangyu Yan", 
                "Kuo Zhang", 
                "Da Liu"
            ],
            "venue": "iScience, Cell Press, 2024.",
            "link": "https://www.cell.com/iscience/fulltext/S2589-0042(24)00935-0",
            "thumbnail": "./assets/figures/publications/2024-05-scope-review.png",
            "topic": [
                "AI for Medicine"
            ]
        },
        {
            "year": 2024,
            "title": "Safe RLHF: Safe Reinforcement Learning from Human Feedback",
            "authors": [
                "Josef Dai*", 
                "Xuehai Pan*", 
                "Ruiyang Sun*", 
                "Jiaming Ji*", 
                "Xinbo Xu", 
                "Mickel Liu", 
                "Yizhou Wang", 
                "Yaodong Yang"
            ],
            "venue": "ICLR 2024.",
            "link": "https://openreview.net/forum?id=TyFrPOKYXw",
            "thumbnail": "./assets/figures/publications/2024-01-saferlhf.png",
            "topic": [
                "Safety Alignment",
                "Reinforcement Learning from Human Feedback"
            ],
            "selected": 1,
            "Github": "https://github.com/PKU-Alignment/safe-rlhf"
        },
        {
            "year": 2024,
            "title": "SafeDreamer: Safe Reinforcement Learning with World Models",
            "authors": [
                "Weidong Huang*",
                "Jiaming Ji*",
                "Borong Zhang",
                "Chunhe Xia",
                "Yaodong Yang"
            ],
            "venue": "ICLR 2024.",
            "link": "https://arxiv.org/abs/2307.07176",
            "thumbnail": "./assets/figures/publications/2024-01-safedreamer.mp4",
            "topic": [
                "Reinforcement Learning",
                "Robotics"
            ],
            "selected": 1,
            "Github": "https://github.com/PKU-Alignment/SafeDreamer"
        },
        {
            "year": 2023,
            "title": "Safety-Gymnasium: A Unified Safe Reinforcement Learning Benchmark",
            "authors": [
                "Jiaming Ji*",
                "Borong Zhang*",
                "Jiayi Zhou*",
                "Xuehai Pan",
                "Weidong Huang",
                "Ruiyang Sun",
                "Yiran Geng",
                "Yifan Zhong",
                "Juntao Dai",
                "Yaodong Yang"
            ],
            "venue": "NeurIPS 2023.",
            "link": "https://proceedings.neurips.cc/paper_files/paper/2023/file/3c557a3d6a48cc99444f85e924c66753-Paper-Datasets_and_Benchmarks.pdf",
            "thumbnail": "./assets/figures/publications/2023-09-safety-gymnasium.png",
            "topic": [
                "Safe Reinforcement Learning",
                "Robotics"
            ],
            "selected": 1,
            "Github": "https://github.com/PKU-Alignment/safety-gymnasium"
        },
        {
            "year": 2023,
            "title": "BeaverTails: Towards Improved Safety Alignment of LLM via a Human-Preference Dataset",
            "authors": [
                "Jiaming Ji*",
                "Mickel Liu*",
                "Juntao Dai*",
                "Xuehai Pan",
                "Chi Zhang",
                "Ce Bian",
                "Chi Zhang",
                "Ruiyang Sun",
                "Yizhou Wang",
                "Yaodong Yang"
            ],
            "venue": "NeurIPS 2023.",
            "link": "https://arxiv.org/abs/2307.04657",
            "thumbnail": "./assets/figures/publications/2023-09-beavertails.png",
            "topic": [
                "Large Language Models",
                "Safety Alignment",
                "Reinforcement Learning from Human Feedback"
            ],
            "selected": 1,
            "Github": "https://github.com/PKU-Alignment/safe-rlhf",
            "Data": "https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF"
        }
    ]
}

def sanitize_filename(title):
    """将标题转换为合适的文件名"""
    # 移除特殊字符并用短横线替换空格
    import re
    filename = re.sub(r'[^\w\s-]', '', title)
    filename = re.sub(r'[-\s]+', '-', filename).strip('-').lower()
    return filename[:50]  # 限制长度

def get_publication_type(venue):
    """根据venue确定publication类型"""
    if 'arxiv' in venue.lower():
        return ["article"]
    elif any(conf in venue.lower() for conf in ['neurips', 'iclr', 'aaai', 'icml', 'nips']):
        return ["paper-conference"]
    elif any(journal in venue.lower() for journal in ['jmlr', 'journal', 'tipami']):
        return ["article-journal"]
    else:
        return ["article"]

def extract_thumbnail_filename(thumbnail_path):
    """从thumbnail路径提取文件名"""
    if thumbnail_path:
        return os.path.basename(thumbnail_path)
    return ""

def generate_publication_md(pub_data, folder_name):
    """生成单个publication的markdown文件"""
    
    # 基本信息提取
    title = pub_data['title']
    authors = pub_data.get('authors', [])
    venue = pub_data.get('venue', '')
    link = pub_data.get('link', '')
    year = pub_data.get('year', 2024)
    topics = pub_data.get('topic', [])
    thumbnail = extract_thumbnail_filename(pub_data.get('thumbnail', ''))
    
    # 可选链接
    github = pub_data.get('Github', '')
    data = pub_data.get('Data', '')
    
    # 生成作者列表
    authors_yaml = '\n'.join([f'- "{author}"' for author in authors])
    
    # 生成标签
    tags_yaml = '\n'.join([f'- {topic}' for topic in topics])
    
    # 确定是否featured
    is_featured = pub_data.get('selected', 0) == 1
    
    # 生成markdown内容
    md_content = f"""---
title: "{title}"

external_link: "{link}"

authors:
{authors_yaml}

date: "{year}-01-01T00:00:00Z"
publication_types: {get_publication_type(venue)}
publication: "{venue}"
publication_short: "{venue.split()[0] if venue else ''}"

summary: "{title}"

tags:
{tags_yaml}

featured: {str(is_featured).lower()}

url_pdf: '{link}'"""

    # 添加可选链接
    if github and github != '#':
        md_content += f"\nurl_code: '{github}'"
    if data and data != '#':
        md_content += f"\nurl_dataset: '{data}'"
    
    md_content += f"""

image:
  filename: "{thumbnail}"
  focal_point: ""
  preview_only: false

projects: []
slides: ""
---"""

    return md_content

def main():
    """主函数：批量生成所有publication"""
    base_dir = "content/publication"
    
    # 确保基础目录存在
    os.makedirs(base_dir, exist_ok=True)
    
    # 已经存在的publication（跳过）
    existing_pubs = {
        "2025-safevla", "2025-sae-v", "2025-align-anything", 
        "2024-aligner", "2024-omnisafe", "2023-ai-alignment-survey"
    }
    
    print("开始批量生成publication...")
    
    for pub in publications_data['publications']:
        # 生成文件夹名
        year = pub.get('year', 2024)
        title = pub['title']
        folder_name = f"{year}-{sanitize_filename(title)}"
        
        # 跳过已存在的
        if folder_name in existing_pubs:
            print(f"跳过已存在的: {folder_name}")
            continue
        
        # 创建目录
        pub_dir = os.path.join(base_dir, folder_name)
        os.makedirs(pub_dir, exist_ok=True)
        
        # 生成markdown文件
        md_content = generate_publication_md(pub, folder_name)
        md_file = os.path.join(pub_dir, "index.md")
        
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        # 复制图片文件
        thumbnail = extract_thumbnail_filename(pub.get('thumbnail', ''))
        if thumbnail:
            src_image = f"static/media/publications/{thumbnail}"
            dst_image = os.path.join(pub_dir, "featured.png")
            
            if os.path.exists(src_image):
                shutil.copy2(src_image, dst_image)
                print(f"✅ 已创建: {folder_name}")
            else:
                print(f"⚠️  图片不存在: {src_image} for {folder_name}")
        else:
            print(f"✅ 已创建: {folder_name} (无图片)")
    
    print("\n🎉 批量生成完成！")

if __name__ == "__main__":
    main()
