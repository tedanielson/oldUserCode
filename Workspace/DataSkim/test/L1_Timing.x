
{

TFile f("l1Plots.root");

gStyle->SetPadLeftMargin(0.4);
gStyle->SetPadRightMargin(0.18);

gStyle->SetOptStat(0);
gStyle->SetPalette (1);



TCanvas* c1 = new TCanvas("c1","c1");

  TPaveLabel* title = new TPaveLabel(0.1,0.96,0.9,0.99,"Run ");
  title->Draw();
  TPad* graphPad = new TPad("Graphs","Graphs",0.01,0.05,0.95,0.95);
  graphPad->Draw();
  graphPad->cd();
  graphPad->Divide(2,2);

graphPad->cd(1);
  Timing_L1A_1 -> Draw("colz");

graphPad->cd(2);
  Timing_L1A_2 -> Draw("colz");

graphPad->cd(3);
  Timing_L1A_3 -> Draw("colz");

graphPad->cd(4);
  Timing_L1A_4 -> Draw("colz");


c1->SaveAs("L1_timing.gif");

TCanvas* c2 = new TCanvas("c2","c2");

  TPaveLabel* title2 = new TPaveLabel(0.1,0.96,0.9,0.99,"Run ");
  title2->Draw();
  TPad* graphPad2 = new TPad("Graphs","Graphs",0.01,0.05,0.95,0.95);
  graphPad2->Draw();
  graphPad2->cd();
  graphPad2->Divide(2);


graphPad2 -> cd(1);
   Timing_L1T_1 -> Draw("colz");

graphPad2 -> cd(2);
   Timing_L1T_2 -> Draw("colz");

c2->SaveAs("Tech_timing.gif");


}

