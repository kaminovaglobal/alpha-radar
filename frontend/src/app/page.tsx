// 1. All imports belong at the very top of the file
import DashboardLayout from "@/components/layout/DashboardLayout";
import OpportunityFeed from "@/components/Opportunities/OpportunityFeed";

// 2. Data structures sit outside the component function
const opportunities = [
  {
    title: "Monad Testnet",
    category: "AIRDROP",
    score: 92
  }
];

// 3. Your main page component function
export default function Home() {
  return (
    <DashboardLayout>
      <h1 className="text-3xl font-bold mb-6">
        Alpha Radar Dashboard
      </h1>
      
      {/* This renders your data using the imported component mechanics */}
      <OpportunityFeed opportunities={opportunities} />
    </DashboardLayout>
  );
}