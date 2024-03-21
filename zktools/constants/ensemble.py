

# Human (homo_sapiens) and Mouse (mus_musculus) genomes respectively
GRCh = "https://ftp.ensembl.org/pub/release-{release}/fasta/homo_sapiens/dna/Homo_sapiens.GRCh{build}.dna.chromosome.{chr}.fa.gz"
GRCm = "https://ftp.ensembl.org/pub/release-{release}/fasta/mus_musculus/dna/Mus_musculus.GRCm{build}.dna.chromosome.{chr}.fa.gz"

# available only mouse and human
available = ['human','homo_sapiens','mouse','mus_musculus']
human = ['human','homo_sapiens']
mouse = ['mouse','mus_musculus']

human_all_chr: list[int|str] = list(range(1,23))+['X','Y'] # list of human chromosomes
mouse_all_chr: list[int|str] = list(range(1,19))+['X','Y'] # list of mouse chromosomes