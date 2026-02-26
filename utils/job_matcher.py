import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from utils.embeddings import embed_text_list

def match_jobs(resume_text, jobs_path="data/jobs.csv"):
    jobs = pd.read_csv(jobs_path, sep="\t")

    # normalize columns
    jobs.columns = jobs.columns.str.strip().str.lower()

    if "description" not in jobs.columns:
        return pd.DataFrame({"ERROR_columns_found": [str(jobs.columns.tolist())]})

    job_desc = jobs["description"].astype(str).tolist()

    job_vectors = embed_text_list(job_desc)
    resume_vector = embed_text_list([resume_text])

    scores = cosine_similarity(resume_vector, job_vectors)[0]

    jobs["score"] = scores

    return jobs.sort_values("score", ascending=False).head(3)