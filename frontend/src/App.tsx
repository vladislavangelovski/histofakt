import {JSX, useState} from 'react'


export default function App() {
  const [query, setQuery] = useState('');
  const [answer, setAnswer] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(false);

  const ask = async () => {
      setLoading(true);
      try {
          const res = await fetch("http://localhost:8000/ask", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ query, language:"en" })
          });
          const data = await res.json();
          setAnswer(data.answer);
      } finally {
          setLoading(false);
      }
  };

  let display: JSX.Element | null = null;
  if (loading) {
      display = <p>Loading...</p>;
  }
  else if (answer) {
      display = (
          <p>
              <strong>Answer:</strong> {answer}
          </p>
      )
  }

  return (
    <main style={{ padding: "2rem", fontFamily: "sans-serif" }}>
        <h1>HistoFakt Tutor (stub)</h1>

        <form
        onSubmit={e => {
            e.preventDefault();
            ask();
        }}>
            <input
                value={query}
                onChange={e => setQuery(e.target.value)}
                placeholder="Ask a historical claim…"
                style={{width: "300px", marginRight: "8px"}}
            />
            <button type="submit">Ask</button>
        </form>

        {display}
    </main>
  )
}
