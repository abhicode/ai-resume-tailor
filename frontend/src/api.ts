import axios  from "axios";

const API = axios.create({
    baseURL: "/api"
});

export interface IngestResponse {
    job_description: string;
    resume_text: string;
    target_role?: string;
}

export interface TailorRequest {
    job_description: string;
    resume_text: string;
    target_role?: string;
}

export interface TailorResponse {
    score: number;
    matched_keywords: string[];
    missing_keywords: string[];
    title_suggestion: string;
    summary_suggestion: string;
    bullet_suggestions: {
        text: string;
        rationale: string;
        mapped_requirement: string;
    }[];
    changes: {
        section: string;
        before: string;
        after: string;
    }[];
    tailored_resume_markdown: string;
}

export const ingestResume = async (file: File, job_description: string, target_role?: string): Promise<IngestResponse> => {
    const formData = new FormData();
    formData.append("file", file);
    formData.append("job_description", job_description);
    if (target_role) formData.append("target_role", target_role);

    const res = await API.post<IngestResponse>("/ingest", formData, {
        headers: { "Content-Type": "multipart/form-data" },
    });
    return res.data;
}

export const tailorResume = async (data: TailorRequest): Promise<TailorResponse> => {
    const res = await API.post<TailorResponse>("/tailor", data);
    return res.data;
}

