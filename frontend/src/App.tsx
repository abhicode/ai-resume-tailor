import { useState } from "react";
import {tailorResume, ingestResume } from "./api";
import type { TailorResponse } from "./api";

function App() {
    const [file, setFile] = useState<File | null>(null);
    const [jobDescription, setJobDescription] = useState("");
    const [targetRole, setTargetRole] = useState("");
    const [result, setResult] = useState<TailorResponse | null>(null);
    const [loading, setLoading] = useState(false);

    const handleUploadAndTailor = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!file || !jobDescription) {
            alert("Please select a resume file and enter a job description.");
            return;
        }
        setLoading(true);
        try {
            const ingestRes = await ingestResume(file, jobDescription, targetRole);

            const tailored = await tailorResume({
                job_description: jobDescription,
                resume_text: ingestRes.resume_text,
                target_role: targetRole,
            });

            setResult(tailored);
        } catch (err) {
            console.error(err);
            alert("Error processing resume");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="max-w-3xl mx-auto p-6">
        <h1 className="text-3xl font-bold mb-6">AI Resume Tailor</h1>

        <form onSubmit={handleUploadAndTailor} className="space-y-4">
            <input
                type="file"
                accept=".pdf,.docx,.txt"
                onChange={(e) => setFile(e.target.files?.[0] || null)}
                className="block w-full border p-2 rounded"
            />
            <textarea
                placeholder="Paste Job Description"
                value={jobDescription}
                onChange={(e) => setJobDescription(e.target.value)}
                rows={6}
                className="w-full border p-3 rounded"
            />
            <input
                type="text"
                placeholder="Target Role (optional)"
                value={targetRole}
                onChange={(e) => setTargetRole(e.target.value)}
                className="w-full border p-3 rounded"
            />
            <button
                type="submit"
                disabled={loading}
                className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 disabled:bg-gray-400"
            >
            {loading ? "Processing..." : "Upload & Tailor Resume"}
            </button>
        </form>

        {result && (
            <div className="mt-8 space-y-4">
                <h2 className="text-2xl font-semibold">Tailoring Results</h2>
                <p><strong>Score:</strong> {result.score}</p>
                <p><strong>Title Suggestion:</strong> {result.title_suggestion}</p>
                <p><strong>Summary Suggestion:</strong> {result.summary_suggestion}</p>

                <h3 className="text-xl font-semibold mt-4">Matched Keywords</h3>
                <ul className="list-disc pl-6">
                    {result.matched_keywords.map((kw, i) => (
                    <li key={i}>{kw}</li>
                    ))}
                </ul>

                <h3 className="text-xl font-semibold mt-4">Missing Keywords</h3>
                <ul className="list-disc pl-6">
                    {result.missing_keywords.map((kw, i) => (
                    <li key={i}>{kw}</li>
                    ))}
                </ul>

                <h3 className="text-xl font-semibold mt-4">Tailored Resume</h3>
                <pre className="bg-gray-100 p-4 rounded whitespace-pre-wrap">
                    {result.tailored_resume_markdown}
                </pre>
            </div>
        )}
        </div>
    );
}

export default App;
