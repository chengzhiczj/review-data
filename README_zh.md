# 论文配套材料使用说明

本文件夹对应论文 Data availability 中承诺提供的逐篇提取记录、编码数据、发表信息和绘图代码，包含当前定稿的31篇研究。材料以英文数据字段为主，本说明用于快速使用。

## 检索与筛选材料的范围

`docs/search_and_screening.md`和`data/search_protocol.json`整理了论文中记载的检索来源、概念词块、检索字段、纳入与排除标准、筛选流程和汇总数量。这些是方法协议说明，不是历史检索日志。当前材料包不包含原始数据库导出文件、逐条去重记录或逐篇筛选决定，也不使用补写的脚本替代研究者的历史判断。筛选由研究者人工完成，无需将其表述为自动筛选程序。

复现代码的范围是最终31篇研究的编码、综合分析、统计和图件，不是重新执行2026年6月的数据库检索。`study_extraction.csv`中的`query`字段描述的是各原始系统如何检索证据，不是本综述如何检索论文。

## 从哪里开始

直接用 Excel 或其他表格软件打开以下文件即可查看数据：

- `data/study_extraction.csv`：31篇的查询、知识单元与索引、筛选与重排序、提示与证据集成、模型、基线、评估协议、数据集、实验对象和指标。
- `data/study_coding.csv`：生命周期主贡献、多标签阶段覆盖、任务族、知识来源、检索组件、集成路线、重复条件化和推理模式。
- `data/publication_metadata.csv`：截至检索截止时的年份和发表类型，以及当前参考文献版本、DOI和来源链接。
- `data/evaluation_decisions.csv`：31篇×6个评估维度，共186条判定，含判定理由和对应原文证据编号。

`docs/codebook.md`解释分类定义和计数规则，`docs/data_dictionary.md`解释字段。`data/studies.json`是程序读取的主数据，CSV是与其一致的便于阅读的导出版本。

`evidence/excerpts.jsonl`保存433处去重的原文摘录，可通过证据编号关联到提取记录和评估判定。`results/study_records.md`和`results/evaluation_audit.md`提供逐篇阅读版本。

## 运行代码

使用 Python 3.12 或以上版本。在本文件夹打开终端后执行：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python reproduce.py
```

如 PowerShell 的脚本策略限制环境激活，可以直接使用虚拟环境的 Python：

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe reproduce.py
```

仅检查数据、编码、证据链接、汇总统计和文件校验和：

```powershell
python reproduce.py --check-only
```

结果默认写入 `results/`，图件在 `results/figures/`。也可以通过 `--output ./my_results`指定其他输出目录。依赖安装完成后，分析不访问网络，不需要API，不依赖原电脑路径。

## 统计口径

发表年份和类型遵守论文的2026年6月截止口径：截止前已正式发表的研究采用正式发表年份，期刊包括early access；否则采用首次arXiv提交年份。当前参考文献中的年份和渠道另外保存，避免后续正式发表改变原统计。

主要贡献为发现20篇、分析7篇、缓解4篇。阶段覆盖允许重叠，为22、20、9篇。稠密检索计入22篇。六维评估计数依次为6、1、1、1、1、4篇；功能正确性和修复后安全性同时报告全体31篇和5篇Patch研究两种分母。

`not_reported`表示所审查原文未报告满足定义的评估，不等于系统没有该能力。相似度代理、人工或参考依据、静态工具、执行测试和模型验证采用不同状态保存。

## 图件

程序从逐篇数据生成六张统计图，另绘制RAG框架图和筛选流程图，复制原作者的生命周期矢量图，共输出9个PDF及对应PNG。材料包提供生命周期矢量素材和筛选流程的TikZ片段，复现使用Python代码，无需论文LaTeX工程。原有文件名 `pie_distribution`被保留，其内容实际为条形图。

材料包不包含论文全文、主LaTeX文件或论文工程，运行也不依赖这些文件。提取记录在整理时已与正文对齐，运行时检查数据内部一致性与预期汇总值。

质量评估部分保存论文已报告的检查表、协议和汇总值，不从汇总值反推逐篇评分、109篇筛选决定或κ的原始输入。

完整英文说明见 `README.md`。`MANIFEST.sha256`用于验证输入和代码完整性，`docs/reproduction_check.json`记录本次独立运行检查。
