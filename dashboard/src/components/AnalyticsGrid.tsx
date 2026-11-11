import KPICard from './KPICard';

export default function AnalyticsGrid() {
  const metrics = [
    ['Repositories', 0],
    ['Stars', 0],
    ['Forks', 0],
    ['Commits', 0],
    ['Contributors', 0],
    ['Languages', 0],
  ];

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      {metrics.map(([title, value]) => (
        <KPICard key={String(title)} title={String(title)} value={Number(value)} />
      ))}
    </div>
  );
}
