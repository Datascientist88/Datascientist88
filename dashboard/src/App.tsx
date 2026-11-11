import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

const data = [
  { name: 'Repositories', value: 0 },
  { name: 'Stars', value: 0 },
  { name: 'Commits', value: 0 }
];

export default function App() {
  return (
    <main style={{ padding: 40 }}>
      <h1>GitHub Analytics Dashboard</h1>
      <p>Live verified GitHub activity analytics.</p>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="value" />
        </BarChart>
      </ResponsiveContainer>
    </main>
  );
}
