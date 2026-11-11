import React from 'react';

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-neutral-950 text-white p-6">
      <header className="mb-8">
        <h1 className="text-3xl font-bold">GitHub Analytics Dashboard</h1>
        <p className="text-neutral-400">Real-time developer activity and repository intelligence</p>
      </header>
      {children}
    </div>
  );
}
