type Props = {
  title: string;
  value: string | number;
  trend?: string;
};

export default function KPICard({ title, value, trend }: Props) {
  return (
    <div className="rounded-xl border p-5 shadow-sm">
      <p className="text-sm opacity-70">{title}</p>
      <h2 className="text-3xl font-bold mt-2">{value}</h2>
      {trend && <p className="text-sm mt-2">{trend}</p>}
    </div>
  );
}
