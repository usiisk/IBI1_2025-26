import sys


try:
    import matplotlib.pyplot as plt
    plt.switch_backend('Agg')          
except ImportError as e:
    print("错误：无法导入 matplotlib。请安装 matplotlib 库：")
    print("  pip install matplotlib")
    print("如果已经安装，请检查你的 Python 环境是否正确。")
    sys.exit(1)
except Exception as e:
    print(f"导入 matplotlib 时出错: {e}")
    print("请尝试使用 Miniconda 环境中的 Python 运行此脚本。")
    sys.exit(1)

valid_stops = ['TAA', 'TAG', 'TGA']

while True:
    target_stop = input(f"请输入终止密码子 ({', '.join(valid_stops)}): ").upper().strip()
    if target_stop in valid_stops:
        break
    print(f"无效输入，请从 {valid_stops} 中选择一个。")

fasta_file = input("请输入 FASTA 文件名（默认: Saccharomyces_cerevisiae.cdna.all.fa）: ").strip()
if not fasta_file:
    fasta_file = "Saccharomyces_cerevisiae.cdna.all.fa"

genes = {}
current_id = None
current_seq_parts = []

try:
    with open(fasta_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith('>'):
                if current_id is not None:
                    genes[current_id] = ''.join(current_seq_parts)
                
                header = line[1:]
                current_id = header.split()[0]
                current_seq_parts = []
            else:
                current_seq_parts.append(line)
        if current_id is not None:
            genes[current_id] = ''.join(current_seq_parts)
except FileNotFoundError:
    print(f"错误：文件 '{fasta_file}' 不存在。")
    sys.exit(1)

print(f"共读取 {len(genes)} 条基因序列。")


all_codon_counts = {}
genes_with_valid_orf = 0

for gene_name, seq in genes.items():
    seq = seq.upper()          
    longest_orf_seq = ""      
    max_orf_len = 0

   
    for frame in range(3):
        i = frame
        while i + 3 <= len(seq):
            if seq[i:i+3] == 'ATG':               
                start = i
    
                last_stop_pos = -1
                pos = start + 3
                while pos + 3 <= len(seq):
                    codon = seq[pos:pos+3]
                    if codon == target_stop:
                        last_stop_pos = pos        
                    elif codon in valid_stops:     
                        break
                    pos += 3
                if last_stop_pos != -1:
                    orf_len = last_stop_pos + 3 - start
                    if orf_len > max_orf_len:
                        max_orf_len = orf_len
                        longest_orf_seq = seq[start:last_stop_pos+3]
            i += 3

    if longest_orf_seq:
        genes_with_valid_orf += 1
    
        for k in range(0, len(longest_orf_seq) - 3, 3):
            codon = longest_orf_seq[k:k+3]
            if len(codon) == 3:
                all_codon_counts[codon] = all_codon_counts.get(codon, 0) + 1

if not all_codon_counts:
    print(f"没有找到任何以 {target_stop} 结束的 ORF。")
    sys.exit(0)

print(f"\n在 {len(genes)} 条基因中，有 {genes_with_valid_orf} 条包含以 {target_stop} 结束的 ORF。")
total_codons = sum(all_codon_counts.values())
print(f"共统计到 {total_codons} 个密码子。")


sorted_items = sorted(all_codon_counts.items(), key=lambda x: x[1], reverse=True)

top_n = 10
top_items = sorted_items[:top_n]
others_count = sum(count for _, count in sorted_items[top_n:])

labels = [codon for codon, _ in top_items]
sizes = [count for _, count in top_items]
if others_count > 0:
    labels.append('Other')
    sizes.append(others_count)

plt.figure(figsize=(12, 8))
wedges, texts, autotexts = plt.pie(sizes, labels=labels, autopct='%1.1f%%',
                                   startangle=140, textprops={'fontsize': 10})
plt.title(f"终止密码子 {target_stop} 上游同框密码子分布\n"
          f"(基于 {genes_with_valid_orf} 个基因的 {total_codons} 个密码子)")


for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

plt.axis('equal')
plt.tight_layout()

output_file = f"codon_usage_{target_stop}.png"
plt.savefig(output_file, dpi=300)
print(f"\n饼图已保存为: {output_file}")

