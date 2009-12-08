import FWCore.ParameterSet.Config as cms

process = cms.Process("TriggerSampleSkim")
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)
#number of Events to be skimmed.
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

#replace fileNames  with the file you want to skim
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    #    '/store/relval/CMSSW_3_3_0/RelValZMM/GEN-SIM-RECO/STARTUP31X_V8-v1/0009/BE1D1CF5-2FB7-DE11-915E-001D09F290CE.root',
    #    '/store/relval/CMSSW_3_3_0/RelValInclusiveppMuX/GEN-SIM-RECO/MC_31X_V9-v1/0002/BA1B9439-C4B7-DE11-93E3-001A92971B0C.root',
    #    '/store/relval/CMSSW_3_3_0/RelValJpsiMM_Pt_0_20/GEN-SIM-RECO/STARTUP31X_V8-v1/0002/FE7BCA5A-73B7-DE11-8BFE-001A92810ADE.root',
    #'/store/relval/CMSSW_3_3_4/RelValJpsiMM/GEN-SIM-RECO/STARTUP3X_V8A-v1/0001/7C7FE2F1-65D5-DE11-A7DD-00261894396F.root',
    #'/store/relval/CMSSW_3_3_4/RelValZEE/GEN-SIM-RECO/MC_31X_V9-v1/0001/AAF8E775-3FD5-DE11-B625-001731AF6B77.root',
    #'/store/relval/CMSSW_3_3_4/RelValZMM/GEN-SIM-RECO/STARTUP3X_V8A-v1/0001/C6364ABD-68D5-DE11-AC70-0018F3D0961E.root',
    #'/store/relval/CMSSW_3_3_4/RelValTTbar/GEN-SIM-RECO/STARTUP3X_V8A-v1/0001/4C6D127D-B0D5-DE11-A6C9-002618943939.root',
    #    '/store/relval/CMSSW_3_3_0/RelValZEE/GEN-SIM-RECO/MC_31X_V9-v2/0002/AA25E184-4ABD-DE11-AC55-0017312B5E1D.root',
    #'/store/relval/CMSSW_3_3_4/RelValMinBias/GEN-SIM-RECO/STARTUP3X_V8A-v1/0001/F24C0338-6BD5-DE11-A9D4-001A9281170A.root',
    #'/store/relval/CMSSW_3_3_4/RelValMinBias/GEN-SIM-RECO/STARTUP3X_V8A-v1/0000/A0425179-3DD5-DE11-A4F9-001731A2832D.root'
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/FE60E1B0-3CE2-DE11-A3CC-000423D9517C.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/FCD3942D-41E2-DE11-96F1-001D09F23944.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/FC8F2EAF-3CE2-DE11-AF67-000423D99E46.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/FC239CE9-4BE2-DE11-8751-003048678098.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/FA02D52F-45E2-DE11-BECA-001617C3B65A.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/F84759D3-43E2-DE11-A96F-001D09F29533.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/F6A63C33-35E2-DE11-8B75-000423D99658.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/F25F0802-4FE2-DE11-B5C7-001D09F27003.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/F07DC625-38E2-DE11-B0D7-000423D99CEE.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/F07CB938-42E2-DE11-830B-000423D9890C.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/F057CB0D-3FE2-DE11-B49F-001617C3B76A.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/EEFA40AB-3AE2-DE11-9346-000423D986C4.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/EED21668-57E2-DE11-8B4A-001D09F251FE.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/EEC00EAB-4CE2-DE11-A544-001D09F25208.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/ECD6F9C4-33E2-DE11-983F-000423D99658.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/ECA0B06B-48E2-DE11-A3BF-000423D99660.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/E6CADC83-53E2-DE11-90EE-001D09F24D67.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/E647C156-56E2-DE11-94AA-0030487A18A4.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/E4A573ED-3DE2-DE11-B902-001617C3B6FE.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/E49FEF0C-3FE2-DE11-A417-000423D99614.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/E45A446B-58E2-DE11-BA05-001D09F24D8A.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/E2A63B3E-3AE2-DE11-8333-001D09F2906A.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/E27C17F0-4EE2-DE11-B3DD-000423D992DC.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/E0D88AC7-31E2-DE11-810D-001D09F252F3.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/DCAEB140-42E2-DE11-AF0D-001D09F282F5.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/DA902E08-37E2-DE11-8E49-000423D98804.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/DA0B566E-47E2-DE11-AFF3-000423D985B0.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/D838A120-33E2-DE11-A28B-001D09F24024.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/D4E98B32-43E2-DE11-A978-000423D9863C.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/D2FF3EA6-3AE2-DE11-ACAF-001D09F25456.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/D29CF78B-3BE2-DE11-AB8B-000423D999CA.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/CAECC3E5-54E2-DE11-B6BF-000423D99AAE.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/CACBE0AE-3AE2-DE11-9A37-001617DBD224.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/C84BF8F0-3FE2-DE11-9C6D-000423D8FA38.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/C44A8A65-57E2-DE11-A032-003048D373AE.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/C29A0C0D-3FE2-DE11-B462-000423D99996.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/C08DB957-42E2-DE11-9130-001D09F24E39.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/BEB552C0-42E2-DE11-BD86-001617E30CC8.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/BE5E668D-3BE2-DE11-8C78-001D09F282F5.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/BCAF7CF3-47E2-DE11-93CC-003048D2BE08.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/BC32BD66-57E2-DE11-B375-001D09F252E9.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/BA3FE3E7-54E2-DE11-8D7C-000423D98BE8.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/B89D92C6-33E2-DE11-BBA4-001D09F25456.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/B640ED6C-32E2-DE11-8066-001D09F2932B.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/B48F37AD-3CE2-DE11-935F-000423D98EA8.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/B2E32FF3-47E2-DE11-84FD-000423D94908.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/AE17F938-40E2-DE11-BBB8-001617DBD224.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/AC458D83-53E2-DE11-959D-0019B9F70468.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/AC3C5724-38E2-DE11-A88D-001617C3B654.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/AAFB91AC-3AE2-DE11-BAD3-001D09F28F0C.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/A2C478AD-3CE2-DE11-9588-000423D98634.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/A0CD8ECB-42E2-DE11-9D19-000423D99BF2.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/A0901568-57E2-DE11-98A7-0019B9F707D8.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/9EDF0330-45E2-DE11-9D77-000423D9870C.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/98EF6459-56E2-DE11-B107-001D09F29533.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/96CE6CEC-3DE2-DE11-AB3B-001617DBD224.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/965A0494-36E2-DE11-9ABF-0019B9F709A4.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/90B7B8EB-4BE2-DE11-B825-003048D2C108.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/9033FF77-5CE2-DE11-A358-001D09F232B9.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/8E87F3AA-4CE2-DE11-9A7E-001D09F252F3.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/8CD2F7D4-43E2-DE11-A30F-0019B9F7312C.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/884A57AB-3AE2-DE11-8208-000423D6CA72.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/88383132-46E2-DE11-8FF5-001D09F29114.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/86AF60CD-42E2-DE11-81F8-000423D99394.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/8610CA75-48E2-DE11-9701-001D09F2915A.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/8231AF07-37E2-DE11-9CA1-000423D6CA42.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/7AC35E3E-3AE2-DE11-A43D-001D09F282F5.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/7A0519E6-54E2-DE11-BD14-000423D94A20.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/78F54733-45E2-DE11-81A3-0030487A18F2.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/78F47AEB-4BE2-DE11-AD00-003048D2BE08.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/780C476F-48E2-DE11-9937-001D09F27067.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/7215E336-5AE2-DE11-BB72-000423D9A2AE.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/70738895-36E2-DE11-ADC0-001D09F29597.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/6CDCB3A8-4CE2-DE11-A5B1-001D09F282F5.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/6C13286A-58E2-DE11-A033-001D09F24682.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/6AB63708-37E2-DE11-83D5-000423D6A6F4.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/6A0449D3-43E2-DE11-BDE9-001D09F24489.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/6868D691-36E2-DE11-A840-0016177CA778.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/68303D95-36E2-DE11-898F-001D09F295A1.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/66C9443E-3AE2-DE11-956D-001D09F232B9.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/665109EE-3DE2-DE11-938D-001617DBD556.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/661A5E31-46E2-DE11-88C5-001D09F28D4A.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/64CC1FC8-33E2-DE11-AA58-001D09F2437B.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/647F7B23-38E2-DE11-90FC-000423D6006E.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/647B3CF8-5AE2-DE11-B88F-001D09F290BF.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/62ED4B20-45E2-DE11-A1A8-000423D98BC4.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/623B3DC7-31E2-DE11-9C28-001D09F2B2CF.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/5CC0B00D-3FE2-DE11-A84F-000423D6006E.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/5C32A5C6-33E2-DE11-86BA-001D09F2932B.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/58BE2E34-5AE2-DE11-8D52-0019B9F72CE5.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/58B40D59-56E2-DE11-8AE7-001D09F231C9.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/56464DF0-3FE2-DE11-89A4-001D09F24489.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/54FBD996-36E2-DE11-BA3C-001D09F2932B.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/54227092-55E2-DE11-BBBE-001617C3B65A.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/5406BBC6-33E2-DE11-B984-0019B9F704D6.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/522E8AAF-3CE2-DE11-A7A6-001D09F29114.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/522C9431-35E2-DE11-A21C-000423D99EEE.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/5071268D-3BE2-DE11-ADAE-000423D98F98.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/4CFF2436-5AE2-DE11-80C9-001D09F28E80.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/4CD63A30-46E2-DE11-BAAC-001617C3B6CC.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/4807E332-41E2-DE11-9FF2-001617C3B65A.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/46E8196A-58E2-DE11-A65C-001D09F2905B.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/42D989E8-54E2-DE11-8E97-001617DBD556.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/407DCA26-43E2-DE11-803C-001617DC1F70.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/4034FCF2-47E2-DE11-A723-000423D98BE8.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/3E8796C5-39E2-DE11-982B-000423D98930.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/3C722A8D-3BE2-DE11-AD0C-001D09F2527B.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/3AFE62F8-3FE2-DE11-B3AF-000423D98BE8.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/3AFB84AF-3CE2-DE11-98A5-001D09F28EA3.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/3AE3CBE5-54E2-DE11-8438-003048D37514.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/3ABD83BC-4BE2-DE11-A9BB-000423D987E0.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/36C0F280-55E2-DE11-9A4C-000423D987FC.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/365C7833-54E2-DE11-8B07-003048D37514.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/343887ED-3DE2-DE11-B557-000423D9989E.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/32B30833-35E2-DE11-A4C1-003048D3756A.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/309101CD-39E2-DE11-A817-003048D373AE.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/307E47BA-4BE2-DE11-B36D-000423D987FC.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/2C8FF376-53E2-DE11-B626-003048D37456.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/2C7C14F0-4EE2-DE11-BEF7-000423D94534.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/2C15506A-32E2-DE11-A2DD-0030486730C6.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/2ACE8122-46E2-DE11-B97D-001617E30D12.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/2A34B7EE-3DE2-DE11-A4BD-00304879FA4A.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/281E7A4A-5AE2-DE11-9824-0030487D0D3A.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/2237806B-48E2-DE11-A87E-001D09F2512C.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/1E7A09CC-42E2-DE11-BEB9-000423D94C68.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/1E50FE73-57E2-DE11-ABB5-001617C3B6E2.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/1E47EDD7-49E2-DE11-B7E2-003048D2C1C4.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/1E2B66CD-42E2-DE11-AAF1-000423DD2F34.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/1C243E8D-3BE2-DE11-9917-001D09F24353.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/189EB1AB-4CE2-DE11-968F-001D09F24934.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/16EA3C34-35E2-DE11-A674-0030487A18F2.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/146D9B6F-47E2-DE11-BB59-0030487A18F2.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/10C5CCF1-3FE2-DE11-A4B6-000423D999CA.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/102E572A-41E2-DE11-BD6B-000423D99658.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/0CF61965-57E2-DE11-AF2C-003048D2C108.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/0C84E124-38E2-DE11-BF58-003048D3750A.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/08762134-5AE2-DE11-93B0-000423D99614.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/0816F593-36E2-DE11-B4DB-0019B9F70468.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/063F1306-39E2-DE11-BFC7-003048D37538.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/02C42DDD-43E2-DE11-9760-000423D98BC4.root',
    '/store/express/BeamCommissioning09/OfflineMonitor/FEVTHLTALL/v2/000/123/596/02C28F6F-47E2-DE11-940A-0030487A1FEC.root'
    )
                            )

#load the EventContent and Skim cff/i files for EXOMu sub-skim.
process.load('Workspace.data_skim.singleMuonSkim_EventContent_cfi')
process.load('Workspace.data_skim.singleMuonSkim_cff')
process.load('Workspace.data_skim.singleElectronSkim_EventContent_cfi')
process.load('Workspace.data_skim.singleElectronSkim_cff')
process.load('Workspace.data_skim.muonTagProbe_EventContent_cfi')
process.load('Workspace.data_skim.muonTagProbeFilters_cff')
process.load('Workspace.data_skim.electronTagProbe_EventContent_cfi')
process.load('Workspace.data_skim.electronTagProbeFilters_cff')
process.load('Workspace.data_skim.singlePhotonSkim_EventContent_cfi')
process.load('Workspace.data_skim.singlePhotonSkim_cff')
process.load('Workspace.data_skim.jetSkim_EventContent_cfi')
process.load('Workspace.data_skim.jetSkim_cff')
process.load('Workspace.data_skim.METSkim_EventContent_cfi')
process.load('Workspace.data_skim.METSkim_cff')

#possible trigger modification by user, defualt HLT_Mu9 in EXOMuOct09_cff.py
#process.exoticaMuHLT.HLTPaths = ['HLT_Mu3']


#define output file name. 
#process.exoticaMuOutputModule.fileNames = cms.untracked.vstring('EXOMuOct09.root')#possible EventContent  modification by user

#AODSIMEventContent/AODEventContent/RECOSIMEventContent/RECOEventContent
#by uncommenting next lines.
#from Configuration.EventContent.EventContent_cff import *
#from SUSYBSMAnalysis.Skimming.EXOMuOct09_EventContent_cfi import *
#SpecifiedEvenetContent=cms.PSet(
#    outputCommands = cms.untracked.vstring(
#      "keep *_exoticaHLTMuonFilter_*_*",
#	  "keep *_exoticaRecoMuonFilter_*_*",
#      )
#    )
#process.exoticaMuOutputModule.outputCommands.extend(RECOSIMEventContent.outputCommands)
#process.exoticaMuOutputModule.outputCommands.extend(SpecifiedEvenetContent.outputCommands)

#possible cut modification by user
#process.exoticaHLTMuonFilter.cut=  cms.string('pt > 5.0')
#process.exoticaHLTMuonFilter.minN=   cms.int32(2) 
#process.exoticaRecoMuonFilter.cut=  cms.string('pt > 15.0')

#Possible exoticaMuHLTQualitySeq or exoticaMuRecoQualitySeq selection by user
#process.exoticaMuSkimPath=cms.Path(process.exoticaMuHLTQualitySeq)
process.singleMuPt5SkimPath=cms.Path(process.singleMuPt5RecoQualitySeq)
process.superClusterPt5SkimPath=cms.Path(process.singleElectronSCRecoQualitySeq)
process.singlePhotonPt5SkimPath=cms.Path(process.singlePhotonPt5QualitySeq)
process.muonJPsiMMSkimPath=cms.Path(process.muonJPsiMMRecoQualitySeq)
process.jetSkimPath=cms.Path(process.jetRecoQualitySeq)
process.METSkimPath=cms.Path(process.METQualitySeq)

process.endPath = cms.EndPath(process.singleMuPt5OutputModule+
                              process.superClusterPt5OutputModule+
                              process.singlePhotonPt5OutputModule+                              
                              process.muonJPsiMMOutputModule+
                              process.jetOutputModule+process.METOutputModule)
#process.endPath = cms.EndPath(process.singleMuOutputModule+process.singlePhotonOutputModule+process.muonZMMOutputModule+process.jetOutputModule+process.METOutputModule)
