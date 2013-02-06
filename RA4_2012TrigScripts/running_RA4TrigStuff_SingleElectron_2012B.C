{

  TChain *chainB_SingleElectron = new TChain("eventB");
  TChain *chainA_SingleElectron = new TChain("eventA");

  chainB_SingleElectron->Add(Form("output/SingleElectron_PD/SingleElectron_2012B.root/eventB"));
  chainA_SingleElectron->Add(Form("output/SingleElectron_PD/SingleElectron_2012B.root/eventA"));

  gROOT->ProcessLine(".L RA4_leptonTriggerStudies.C++");
  
  tree1r(chainB_SingleElectron,chainA_SingleElectron,"SingleElectron_HT_MET_effs_2012BOnly",2.90);  
  
}
