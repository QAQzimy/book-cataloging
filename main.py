#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Word 英文字母→空格  最终修复版
支持：正文 / 页眉 / 页脚 / 嵌套表格 / 文本框
修复：_Header / _Footer 无 header_part / footer_part 属性
"""
import re
import sys
from pathlib import Path
from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import Table, _Cell
from docx.section import _Header, _Footer
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.oxml.shape import CT_Inline, CT_Anchor

# 图形界面
import tkinter as tk
from tkinter import filedialog, messagebox

def ask_docx() -> Path:
    """弹出文件选择框，返回用户选中的 Word 文件路径；取消则退出程序"""
    tk.Tk().withdraw()
    file = filedialog.askopenfilename(title="请选择 Word 文件", filetypes=[("Word 文件", "*.docx")])
    if not file:
        sys.exit(0)
    return Path(file)

# ---------- 核心处理 ----------
def eng2space(text: str) -> str:
    """把英文字母全部替换成半角空格"""
    return re.sub(r'[A-Za-z]', ' ', text)

def process_paragraph(p: Paragraph):
    """逐 Run 修改：把英文字母换成空格"""
    for run in p.runs:
        if run.text:
            run.text = eng2space(run.text)

def process_table(table: Table):
    """递归处理表格：遍历每一行→每一格→再调统一容器处理"""
    for row in table.rows:
        for cell in row.cells:
            process_block_item_container(cell)

def process_textbox(block):
    """处理文本框（w:txbxContent）里的段落与表格"""
    for child in block.xpath('.//w:txbxContent//w:p | .//w:txbxContent//w:tbl'):
        if child.tag.endswith('p'):
            process_paragraph(Paragraph(child, block))
        elif child.tag.endswith('tbl'):
            process_table(Table(child, block))

def process_block_item_container(container):
    """
    统一入口：Document / _Cell / _Header / _Footer
    彻底修复属性错误
    """
    # ① 取“能遍历子节点”的 lxml 元素
    if isinstance(container, _Cell):
        parent_elem = container._tc                       # <w:tc>
    elif isinstance(container, (_Header, _Footer)):
        parent_elem = container._element                  # <w:hdr> 或 <w:ftr>
    else:                                                 # Document
        parent_elem = container.element.body              # <w:body>

    # ② 统一遍历段落、表格、文本框
    for child in parent_elem:
        if isinstance(child, CT_P):
            process_paragraph(Paragraph(child, container))
        elif isinstance(child, CT_Tbl):
            process_table(Table(child, container))
        elif isinstance(child, (CT_Inline, CT_Anchor)):
            for txbx in child.xpath('.//w:txbxContent'):
                process_textbox(txbx)

# ---------- 主流程 ----------
def main(docx_path: Path):
    """总控：打开文档→处理→保存新文件"""
    doc = Document(docx_path)          # ① 磁盘 → 内存（解压+XML解析）

    # 正文
    process_block_item_container(doc)
    # 页眉 / 页脚
    for sect in doc.sections:
        for hdr in (sect.header, sect.first_page_header, sect.even_page_header):
            if hdr is not None:
                process_block_item_container(hdr)
        for ftr in (sect.footer, sect.first_page_footer, sect.even_page_footer):
            if ftr is not None:
                process_block_item_container(ftr)

    out_path = docx_path.with_name(f"{docx_path.stem}_english_to_spaces.docx")
    doc.save(out_path)                 # ② 内存 → 磁盘（重新打包为 ZIP）
    messagebox.showinfo("完成", f"已生成：\n{out_path}")

# ---------- 程序入口 ----------
if __name__ == "__main__":
    main(ask_docx())                   # ③ 双击后先弹窗选文件