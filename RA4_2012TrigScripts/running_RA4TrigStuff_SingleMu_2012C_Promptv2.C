{

  TChain *chainB_SingleMu = new TChain("eventB");
  TChain *chainA_SingleMu = new TChain("eventA");

  chainB_SingleMu->Add(Form("output/SingleMu_PD/SingleMuon_2012C_Promptv2.root/eventB"));
  chainA_SingleMu->Add(Form("output/SingleMu_PD/SingleMuon_2012C_Promptv2.root/eventA"));

  gROOT->ProcessLine(".L RA4_leptonTriggerStudies.C++");
  
  tree1r(chainB_SingleMu,chainA_SingleMu,"SingleMu_HT_MET_effs_2012C_Promptv2",2.90);  
  
}
