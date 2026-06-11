import DashboardLayout from "@/components/layout/DashboardLayout";
import OpportunityFeed from "@/components/opportunities/OpportunityFeed";

const opportunities = [
  {
    title: "Monad Testnet",
    category: "AIRDROP",
    score: 92
  }
];

export default function Home() {
  return (
    <DashboardLayout>
      <h1 className="text-3xl font-bold">
        Alpha Radar Dashboard
      </h1>
      {/* If you plan to render the feed here, you can now use <OpportunityFeed /> */}
    </DashboardLayout>
  );
}