#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速调整publication排序的工具脚本
使用方法：
  1. 编辑 publication_order.txt 文件调整顺序
  2. 运行此脚本: python3 update_publication_order.py
"""

import os
import re

def read_order_from_file():
    """从publication_order.txt读取排序"""
    order_file = "publication_order.txt"
    
    if not os.path.exists(order_file):
        print(f"⚠️  找不到配置文件: {order_file}")
        return {}
    
    publication_order = {}
    weight = 1
    
    with open(order_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # 跳过空行和注释
            if not line or line.startswith('#'):
                continue
            
            # 这一行是论文文件夹名
            publication_order[line] = weight
            weight += 1
    
    return publication_order

def update_publication_weight(folder_path, weight):
    """更新单个publication的weight字段"""
    index_file = os.path.join(folder_path, "index.md")
    
    if not os.path.exists(index_file):
        return False
    
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已有weight字段
    if re.search(r'^weight:\s*\d+', content, re.MULTILINE):
        # 更新现有weight
        content = re.sub(
            r'^weight:\s*\d+',
            f'weight: {weight}',
            content,
            flags=re.MULTILINE
        )
    else:
        # 在title后面添加weight字段
        content = re.sub(
            r'(title:.*?\n\n)',
            f'\\1# 排序权重：数字越小越靠前\nweight: {weight}\n\n',
            content,
            flags=re.DOTALL
        )
    
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """主函数"""
    base_dir = "./"
    
    if not os.path.exists(base_dir):
        print(f"❌ 找不到目录: {base_dir}")
        return
    
    # 从文件读取排序配置
    publication_order = read_order_from_file()
    
    if not publication_order:
        print("❌ 没有找到有效的排序配置")
        return
    
    print("🚀 开始更新publication排序...\n")
    
    updated_count = 0
    for folder_name, weight in publication_order.items():
        folder_path = os.path.join(base_dir, folder_name)
        
        if os.path.exists(folder_path):
            if update_publication_weight(folder_path, weight):
                print(f"✅ 已更新: {folder_name} → weight: {weight}")
                updated_count += 1
            else:
                print(f"⚠️  跳过: {folder_name} (没有index.md)")
        else:
            print(f"⚠️  找不到: {folder_name}")
    
    print(f"\n🎉 完成！共更新了 {updated_count} 个publication的排序")
    print("\n💡 提示：")
    print("   - 数字越小的论文会显示在越前面")
    print("   - 相同weight的论文按日期排序")
    print("   - 编辑 publication_order.txt 可以调整任意论文的顺序")

if __name__ == "__main__":
    main()
