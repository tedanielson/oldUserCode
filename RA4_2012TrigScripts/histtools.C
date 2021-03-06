namespace hist {

   //Add all histograms whose names match one of ten possible regular expression
   //patterns or begin with one of ten possible given prefixes.  Feel free to
   //mix and match regular expression patterns and prefixes.  If the final hist-
   //ogram named outHistName does not exist it is created.

   void add(const char* outHistName, const char* patORpfx0, const char* patORpfx1, const char* patORpfx2 = 0, const char* patORpfx3 = 0, const char* patORpfx4 = 0, const char* patORpfx5 = 0, const char* patORpfx6 = 0, const char* patORpfx7 = 0, const char* patORpfx8 = 0, const char* patORpfx9 = 0)
   {
      add(outHistName, patORpfx0);
      add(outHistName, patORpfx1);
      if (patORpfx2) add(outHistName, patORpfx2);
      if (patORpfx3) add(outHistName, patORpfx3);
      if (patORpfx4) add(outHistName, patORpfx4);
      if (patORpfx5) add(outHistName, patORpfx5);
      if (patORpfx6) add(outHistName, patORpfx6);
      if (patORpfx7) add(outHistName, patORpfx7);
      if (patORpfx8) add(outHistName, patORpfx8);
      if (patORpfx9) add(outHistName, patORpfx9);
   }

  // Sumw2 all your bleep if you're a muppet (like Tom) and forgot to do it in
  // your analysis code
  void sumw2Everything() {
    TList* list = gDirectory->GetList();
    TIterator* iter = list->MakeIterator();

    TObject* obj = 0;
    while (obj = iter->Next()) {
      if (! obj->InheritsFrom(TH1::Class())) continue;

      ((TH1F*)obj)->Sumw2();
    }
  }

  // Multiply everything by a scale factor
  void normalize_all_by_single_SF(double factor) {
    TList* list = gDirectory->GetList();
    TIterator* iter = list->MakeIterator();

    TObject* obj = 0;
    while (obj = iter->Next()) {
      if (! obj->InheritsFrom(TH1::Class())) continue;

      ((TH1F*)obj)->Scale(factor);
    }
  }
  

  // normalize all your bleep to 1
  void normalizeAllToUnity() {
     TList* list = gDirectory->GetList();
    TIterator* iter = list->MakeIterator();

    TObject* obj = 0;
    while (obj = iter->Next()) {
      if (! obj->InheritsFrom(TH1::Class())) continue;
      int nBins = ((TH1F*)obj)->GetNbinsX();
      Float_t integral = ((TH1F*)obj)->Integral(1, nBins+1);
      if (integral > 0) ((TH1F*)obj)->Scale(1/integral);
    }
  }
  
  //Add all histograms whose names match the given regular expression pattern
  //or begin with the given prefix.  If the final histogram named outHistName
  //does not exist it is created.
  
  void add(const char* outHistName, const char* patORpfx) {
    TRegexp reg(patORpfx, kFALSE);
    
    TList* list = gDirectory->GetList() ;
    TIterator* iter = list->MakeIterator();
    
      TObject* obj = 0;
      TObject* hist = 0;
      Bool_t makeOutHist = false;

      hist = gDirectory->Get(outHistName);
      //If out hist does not exist, remember to create it
      if (! hist) makeOutHist = true;

      while (obj = iter->Next()) {
         if (! obj->InheritsFrom(TH1::Class())) continue;

         TString name = obj->GetName();
         //Don't add out hist
         if (name == TString(outHistName)) continue;

         if (TString(patORpfx).MaybeRegexp()) {
            if (TString(obj->GetName()).Index(reg) < 0 ) continue;
         } else if (! name.BeginsWith(patORpfx)) continue;

         if (makeOutHist) {
            hist = obj->Clone(outHistName);

            if (hist->InheritsFrom(TH2::Class()))
               ((TH2*)hist)->Reset();
            else
               ((TH1*)hist)->Reset();

            ((TH1*)hist)->SetTitle(outHistName);
            ((TH1*)hist)->Sumw2();
            makeOutHist = false;
         }

         ((TH1*)hist)->Add((TH1*)obj);
      }
   }

   //For all histograms whose names match the given regular expression pattern
   //or begin with the given prefix, set the fill, line and marker colors to the
   //given value.
   
   void color(const char* patORpfx, Color_t color) {
     //     cout << "color = " << color << endl;
     //     if (color == 1) color+=20;
      TRegexp reg(patORpfx, kFALSE);

      TList* list = gDirectory->GetList() ;
      TIterator* iter = list->MakeIterator();

      TObject* obj = 0;

      while (obj = iter->Next()) {
         if (! obj->InheritsFrom(TH1::Class())) continue;

         TString name = obj->GetName();

         if (TString(patORpfx).MaybeRegexp()) {
            if (TString(obj->GetName()).Index(reg) < 0 ) continue;
         } else if (! name.BeginsWith(patORpfx)) continue;

	 //	 ((TH1*)obj)->SetFillColor(color);
         ((TH1*)obj)->SetLineColor(color);
         ((TH1*)obj)->SetMarkerColor(color);
      }
   }

   //For all histograms drawn on a given TCanvas, set the fill, line and marker
   //colors in ascending order starting from the given color.

   void colors(TCanvas* canvas, Color_t color = 1) {
      if(! canvas) return 0;

      TList* list = canvas->GetListOfPrimitives();
      TIterator* iter = list->MakeIterator();

      TObject* obj = 0;

      //Hist color iterator
      Int_t colorIt = color;

      while (obj = iter->Next()) {
         if (! obj->InheritsFrom(TH1::Class())) continue;

         //yellow
         if (colorIt == 5)
            ++colorIt;

         hist::color(obj->GetName(), colorIt);
         if (colorIt == 40)
            colorIt = 1;
         else 
            ++colorIt;
      }
   }

   //For all histograms added to a given THStack, set the fill, line and marker
   //colors in ascending order starting from the given color.

   void colors(THStack* stack, Color_t color = 1) {
      if(! stack) return 0;

      //      cout << "Time for some bullbleep debugging." << endl;

      TList* list = stack->GetHists();
      TIterator* iter = list->MakeIterator();

      TObject* obj = 0;

      //Hist color iterator
      Int_t colorIt = color;

      //      cout << "colorIt = " << colorIt << endl;

      while (obj = iter->Next()) {
	//	cout << "in the while loop" << endl;
         if (! obj->InheritsFrom(TH1::Class())) continue;
	 //	 cout << "colorIt = " << colorIt << endl;
	 //         hist::color(obj->GetName(), colorIt);
	 ((TH1F*)obj)->SetFillColor(colorIt);
	 ((TH1F*)obj)->SetMarkerColor(colorIt);

         int markerNumber = colorIt + 19;
         ((TH1F*)obj)->SetMarkerStyle(markerNumber);
         ((TH1F*)obj)->SetFillColor(colorIt);
         ((TH1F*)obj)->SetMarkerColor(colorIt);

	 if (markerNumber >= 30) markerNumber = 1;

         if (colorIt == 50) colorIt = 1;
	 
	 else if (colorIt >= 9 && colorIt < 20) colorIt += 30;

         else ++colorIt;
      }
   }

   //Create a canvas and Draw("same") all histograms whose names match the given
   //regular expression pattern or begin with the given prefix.  If the TCanvas
   //named canvasName does not exist it is created.  Optionally apply colors and
   //styles to all histograms.

   void drawsame(const char* canvasName, const char* patORpfx,Option_t* drawOption = "") {
     //     cout << "testing this method" << endl;
     TRegexp reg(patORpfx, kFALSE);
     TList* list = gDirectory->GetList() ;
     //     cout << "this bleeping directory has " << gDirectory->GetNkeys() << "things in it" << endl;
     TIterator* iter = list->MakeIterator();
     
     TObject* obj = 0;
     TObject* canvas = 0;
     Bool_t makeCanvas = false;
     
     canvas = gROOT->GetListOfCanvases()->FindObject(canvasName);
     //If canvas does not exist, remember to create it
     //     cout << "found our canvas" << endl;
     if (! canvas) makeCanvas = true;
     
     while (obj = iter->Next()) {
       //       cout << "We have an object" << endl;
       if (! obj->InheritsFrom(TH1::Class())) continue;
       
       TString name = obj->GetName();
       //       cout << "Testing object of name " << name << endl;
       
       //       if (TString(patORpfx).MaybeRegexp()) { THIS BASICALLY ADDS IT IF IT HAS A BLEEPING PULSE
       if (TString(name).Contains(patORpfx)) {
	 //	 cout << "possible match" << endl;
	 if (TString(obj->GetName()).Index(reg) < 0 ) {
	   //	   cout << "not a match here" << endl;
	   continue;
	 } 
	 else if (! name.BeginsWith(patORpfx)) {
	   //	   cout << "mismatched beginning" << endl;
	   continue;
	 }
       
	 
	 if (makeCanvas) {
	   canvas = new TCanvas(canvasName, canvasName);
	   makeCanvas = false;
	 }
	 
	 ((TH1*)obj)->UseCurrentStyle();
	 ((TCanvas*)canvas)->cd();
	 if (!((TCanvas*)canvas)->GetListOfPrimitives()->GetEntries()) {
	   //	   cout << "Drawing with non-same option" << endl;
	   ((TH1*)obj)->Draw(Form("%s", drawOption));
	 }
	 else {
	   //	   cout << "Drawing with the same option" << endl;
	   ((TH1*)obj)->Draw(Form("SAME%s", drawOption));
	 }
       }
     }
     
     hist::colors((TCanvas*)canvas);

   }
   
   //Return a pointer to a TLegend with an entry for each histogram drawn on a
   //given TCanvas.  Display either the line, point or fill values.  Optionally
   //apply colors to all histograms.  By default, entry labels are the names of
   //their respective histograms.  Optionally, if histogram names are of the
   //form XX_YY_ZZ_WW, entry labels can be XX (token=0), YY (token=1), etc.
   
   TLegend* legend(TCanvas* canvas, Option_t* option = "lpf", Bool_t addColor = kFALSE, Int_t token = -1,
                   Float_t xmin = 0.75, Float_t ymin = 0.75, Float_t xmax = 0.99, Float_t ymax = 0.99) {
     if(! canvas) return 0;
     
     TLegend* leg = new TLegend(xmin, ymin, xmax, ymax);
     TList* list = canvas->GetListOfPrimitives();
     TIterator* iter = list->MakeIterator();
     
     TObject* obj = 0;

     //Hist color iterator
     Int_t colorIt = 1;
     
     while (obj = iter->Next()) {
       
       if (! obj->InheritsFrom(TH1::Class())) continue;
       
       if (addColor) {
	 hist::color(obj->GetName(), colorIt);
	 ++colorIt;
       }
       
       if (token == -1) {
	 //	 cout << "Adding to TLegend  " << obj->GetName() << endl; 
	 leg->AddEntry(obj, obj->GetName());
       }
       else {
	 TString name(obj->GetName());
	 TObjArray* a = name.Tokenize("_");
	 if (a->GetEntries() <= token)
	   leg->AddEntry(obj, obj->GetName(), option);
	 else
	   leg->AddEntry(obj, a->At(token)->GetName(), option);
       }
     }
     
     return leg;
   }
   
   //Return a pointer to a TLegend with an entry for each histogram added to a
   //given THStack.  Display either the line, point or fill values.  Optionally
   //apply colors to all histograms.  By default, entry labels are the names of
   //their respective histograms.  Optionally, if histogram names are of the
   //form XX_YY_ZZ_WW, entry labels can be XX (token=0), YY (token=1), etc.

   TLegend* legend(THStack* stack, Option_t* option = "lp", Bool_t addColor = kFALSE, Int_t token = -1,
                   Float_t xmin = 0.50, Float_t ymin = 0.51, Float_t xmax = 0.85, Float_t ymax = 0.92) {
      if(! stack) return 0;

      TLegend* leg = new TLegend(xmin, ymin, xmax, ymax);
      TList* list = stack->GetHists();
      TIterator* iter = list->MakeIterator();

      TObject* obj = 0;

      //Hist color iterator
      Int_t colorIt = 1;

      while (obj = iter->Next()) {
         if (! obj->InheritsFrom(TH1::Class())) continue;

         if (addColor) {
            hist::color(obj->GetName(), colorIt);
            ++colorIt;
         }

         if (token == -1)
            leg->AddEntry(obj, obj->GetTitle(), option);
         else {
            TString name(obj->GetName());
            TObjArray* a = name.Tokenize("_");
            if (a->GetEntries() <= token)
               leg->AddEntry(obj, obj->GetName(), option);
            else
               leg->AddEntry(obj, a->At(token)->GetName(), option);
         }
      }

      return leg;
   }

   //Normalize to one all histograms whose names match the given regular exp-
   //ression pattern or begin with the given prefix.

   void normalize(const char* patORpfx) {
      TRegexp reg(patORpfx, kFALSE);

      TList* list = gDirectory->GetList() ;
      TIterator* iter = list->MakeIterator();

      TObject* obj = 0;

      while (obj = iter->Next()) {
         if (! obj->InheritsFrom(TH1::Class())) continue;

         TString name = obj->GetName();

         if (TString(patORpfx).MaybeRegexp()) {
            if (TString(obj->GetName()).Index(reg) < 0 ) continue;
         } else if (! name.BeginsWith(patORpfx)) continue;

         Double_t integral = 0;

         if (obj->InheritsFrom(TH2::Class()))
            integral = ((TH2*)obj)->Integral();
         else
            integral = ((TH1*)obj)->Integral();

         if (integral) {
            ((TH1*)obj)->Sumw2();
            ((TH1*)obj)->Scale(1./integral);
         }
      }
   }

   //Scale by the given value all histograms whose names match the given regular
   //expression pattern or begin with the given prefix.

   void scale(const char* patORpfx, Double_t scale,Option_t* drawOption = "") {
      TRegexp reg(patORpfx, kFALSE);

      TList* list = gDirectory->GetList() ;
      TIterator* iter = list->MakeIterator();

      TObject* obj = 0;

      while (obj = iter->Next()) {
         if (! obj->InheritsFrom(TH1::Class())) continue;

         TString name = obj->GetName();

         if (TString(patORpfx).MaybeRegexp()) {
            if (TString(obj->GetName()).Index(reg) < 0 ) continue;
         } else if (! name.BeginsWith(patORpfx)) continue;

         ((TH1*)obj)->Sumw2();
         ((TH1*)obj)->Scale(scale);
      }
   }

   //Scale bins to given value of x-axis units for all histograms whose names
   //match the given regular expression pattern or begin with the given prefix.

   void scalebins(const char* patORpfx, Double_t scale) {
      TRegexp reg(patORpfx, kFALSE);

      TList* list = gDirectory->GetList() ;
      TIterator* iter = list->MakeIterator();

      TObject* obj = 0;

      while (obj = iter->Next()) {
         if (! obj->InheritsFrom(TH1::Class())) continue;

         TString name = obj->GetName();

         if (TString(patORpfx).MaybeRegexp()) {
            if (TString(obj->GetName()).Index(reg) < 0 ) continue;
         } else if (! name.BeginsWith(patORpfx)) continue;

         Double_t binWidth, binContent, binError, newBinContent, newBinError;
         for (Int_t i = 1; i <= ((TH1*)obj)->GetNbinsX(); ++i) {
            binWidth = ((TH1*)obj)->GetBinWidth(i);
            binContent = ((TH1*)obj)->GetBinContent(i);
            binError = ((TH1*)obj)->GetBinError(i);
            newBinContent = (binContent*scale)/binWidth;
            newBinError = (binError*scale)/binWidth;

            ((TH1*)obj)->SetBinContent(i, newBinContent);
            ((TH1*)obj)->SetBinError(i, newBinContent);
            // Rename y axis with scale
         }
      }
   }

   //Don't you hate it when you draw multiple histograms on the same canvas only
   //to find that the bottom histogram's range does not encompass those of the
   //histograms drawn on top?  This method determines the maximum and minimum y
   //range of all the histograms drawn on a given TCanvas and appropriately re-
   //sizes the bottom histogram.

   void setrangey(TCanvas* canvas, Double_t maxy = -999999, Double_t miny = 999999) {
      if(! canvas) return 0;

      TList* list = canvas->GetListOfPrimitives();
      TIterator* iter = list->MakeIterator();

      TObject* obj = 0;
      TObject* top = 0;

      while (obj = iter->Next()) {
	//	cout << "iterating over objects, should be 2 in this case" << endl;
	if (! obj->InheritsFrom(TH1::Class())) {
	  //	  cout << "bleep, stacks present a problem" << endl;
	  continue;
	}

         if (! top) top = obj;

	 //	 cout << "Make sure we are looking at different objects\n";
	 //	 cout << "max for this object: " << ((TH1*)obj)->GetMaximum() << endl;

         if (((TH1*)obj)->GetMaximum() > maxy) maxy = ((TH1*)obj)->GetMaximum();

         // JAKE Set to log scale if max/min > 10

         if (canvas->GetLogy()) {
            //protect against user supplied argument
            if (miny == 0) miny = 999999;

            for(Int_t bin = 1; bin <= ((TH1*)obj)->GetNbinsX(); ++bin) {
               Double_t binContent = ((TH1*)obj)->GetBinContent(bin);
               if (binContent != 0 && binContent < miny)
                  miny = binContent;
            }
         } else if (((TH1*)obj)->GetMinimum() < miny) miny = ((TH1*)obj)->GetMinimum();
      }

      cout << "miny, maxy = " << miny <<" "<<maxy << endl;

      ((TH1*)top)->SetMaximum(maxy*1.3);
      ((TH1*)top)->SetMinimum(miny*0.7);
   }

   //Create a stacked histogram consisting of all histograms whose names match
   //the given regular expression pattern or begin with the given prefix.  If
   //the THStack named stackHistName does not exist it is created.  Optionally
   //apply colors to all histograms.  Set drawOption to "nostack" if you do not
   //want to stack, to "hist" to display histograms without errors, to "histe"
   //to display histograms with errors, etc.

  void stack(const char* stackHistName, const char* patORpfx, Bool_t addColor = kFALSE, Option_t* drawOption = "") {
     //     cout << "bleep1" << endl;
     TRegexp reg(patORpfx, kFALSE);
     
      TList* list = gDirectory->GetList() ;
      TIterator* iter = list->MakeIterator();

      TObject* obj = 0;
      TObject* stack = 0;
      Bool_t makeStackHist = false;

      stack = gDirectory->Get(stackHistName);
      //If stack hist does not exist, remember to create it
      if (! stack) makeStackHist = true;

      //Hist color iterator
      Int_t colorIt = 1;

      while (obj = iter->Next()) {
         if (! obj->InheritsFrom(TH1::Class())) continue;

         TString name = obj->GetName();

         if (TString(patORpfx).MaybeRegexp()) {
            if (TString(obj->GetName()).Index(reg) < 0 ) continue;
         } else if (! name.BeginsWith(patORpfx)) continue;

         if (makeStackHist) {
            stack = new THStack(stackHistName, stackHistName);
            makeStackHist = false;
         }

         if (addColor) {
	   cout << "calling the color method" << endl;
            hist::color(obj->GetName(), colorIt);
            ++colorIt;
         }

         ((THStack*)stack)->Add((TH1*)obj, drawOption);
      }

      // Currently breaks .ls
      gDirectory->Append(stack);
   }

   //For all histograms drawn on a given TCanvas, set the marker styles in
   //ascending order starting from the given style.

   void styles(TCanvas* canvas, Style_t style = 20) {
      if(! canvas) return 0;

      TList* list = canvas->GetListOfPrimitives();
      TIterator* iter = list->MakeIterator();

      TObject* obj = 0;

      //Hist style iterator
      Int_t styleIt = style;

      while (obj = iter->Next()) {
         if (! obj->InheritsFrom(TH1::Class())) continue;

         ((TH1*)obj)->SetMarkerStyle(styleIt);
         ++styleIt;
      }
   }

   //For all histograms drawn on a given THStack, set the marker styles in
   //ascending order starting from the given style.

   void styles(THStack* stack, Style_t style = 20) {
      if(! stack) return 0;

      TList* list = stack->GetHists();
      TIterator* iter = list->MakeIterator();

      TObject* obj = 0;

      //Hist style iterator
      Int_t styleIt = style;

      while (obj = iter->Next()) {
         if (! obj->InheritsFrom(TH1::Class())) continue;

         ((TH1*)obj)->SetMarkerStyle(styleIt);
         ++styleIt;
      }
   }

   //Set the x-axis title of all histograms whose names match the given regular
   //expression pattern or begin with the given prefix.

   void xaxis(const char* patORpfx, const char* title) {
      TRegexp reg(patORpfx, kFALSE);

      TList* list = gDirectory->GetList() ;
      TIterator* iter = list->MakeIterator();

      TObject* obj = 0;

      while (obj = iter->Next()) {
         if (! (obj->InheritsFrom(TH1::Class()) || obj->InheritsFrom(THStack::Class()))) continue;

         TString name = obj->GetName();

         if (TString(patORpfx).MaybeRegexp()) {
            if (TString(obj->GetName()).Index(reg) < 0 ) continue;
         } else if (! name.BeginsWith(patORpfx)) continue;

         if (obj->InheritsFrom(TH1::Class()))
            ((TH1*)obj)->GetXaxis()->SetTitle(title);
         if (obj->InheritsFrom(THStack::Class())) {
            ((THStack*)obj)->Draw();
            ((THStack*)obj)->GetXaxis()->SetTitle(title);
         }
      }
   }

   //Set the y-axis title of all histograms whose names match the given regular
   //expression pattern or begin with the given prefix.

   void yaxis(const char* patORpfx, const char* title) {
      TRegexp reg(patORpfx, kFALSE);

      TList* list = gDirectory->GetList() ;
      TIterator* iter = list->MakeIterator();

      TObject* obj = 0;

      while (obj = iter->Next()) {
         if (! (obj->InheritsFrom(TH1::Class()) || obj->InheritsFrom(THStack::Class()))) continue;

         TString name = obj->GetName();

         if (TString(patORpfx).MaybeRegexp()) {
            if (TString(obj->GetName()).Index(reg) < 0 ) continue;
         } else if (! name.BeginsWith(patORpfx)) continue;

         if (obj->InheritsFrom(TH1::Class()))
            ((TH1*)obj)->GetYaxis()->SetTitle(title);
         if (obj->InheritsFrom(THStack::Class())) {
            ((THStack*)obj)->Draw();
            ((THStack*)obj)->GetYaxis()->SetTitle(title);
         }
      }
   }
}

// Input:  2 histogram
// Output: one histogram which is the efficiency:
// h1 :  TOTAL NUMBER OF EVENTS
// h2 :  NUMBER OF EVENTS THAT PASS

#include "TH1.h"

// Method by pointer
TH1F* eff(TH1F* h1, TH1F* h2, const char* name="eff"){

  // first, verify that all histograms have same binning
  // nx is the number of visible bins
  // nxtot = nx+2 includes underflow and overflow
  Int_t nx = h1->GetNbinsX();
  if (h2->GetNbinsX() != nx) {
    //    cout << "Histograms must have same number of bins" << endl;
    return 0;
  }

  // get the new histogram
  TH1F* temp = (TH1F*) h1->Clone(name);
  temp->SetTitle(name);
  temp->Reset();
  temp->Sumw2();

  // Do the calculation
  temp->Divide(h2,h1,1.,1.,"B");

  // Done
  return temp;
}


// Method by name
TH1F* eff(const char* name1, const char* name2, const char* name="eff"){

  // Get a list of object and their iterator
  TList* list = gDirectory->GetList() ;
  TIterator* iter = list->MakeIterator();

  // Loop over objects, set the pointers
  TObject* obj;
  TH1F* h1=0;
  TH1F* h2=0;
  TString str1 = Form("%s",name1);
  TString str2 = Form("%s",name2);
  while(obj=iter->Next()) {
    TString objName = obj->GetName();
    if (objName == str1) h1 = (TH1F*) obj;
    if (objName == str2) h2 = (TH1F*) obj;
  }

  // quit if not found
  if (h1 == 0) {
    //    cout << "Histogram " << name1 << " not found" << endl;
    return 0;
  }
  if (h2 == 0) {
    //    cout << "Histogram " << name2 << " not found" << endl;
    return 0;
  }

  // Call the method by pointer
  TH1F* temp = eff(h1, h2, name);
  return temp;
}
// Input:  4 histogram
// Output: one histogram which is the BG subtracted efficiency:
// h1 :  TOTAL NUMBER OF EVENTS, SIGNAL REGION
// h2 :  NUMBER OF EVENTS THAT PASS, SIGNAL REGION
// h3 :  TOTAL NUMBER OF EVENTS, SIDE BAND
// h4 :  NUMBER OF EVENTS THAT PASS, SIDE BAND

#include "TH1.h"


TH1F* eff_bg(TH1F* h1, TH1F* h2, TH1F* h3, TH1F* h4, const char* name="eff"){

  // first, verify that all histograms have same binning
  // nx is the number of visible bins
  // nxtot = nx+2 includes underflow and overflow
  Int_t nx = h1->GetNbinsX();
  Int_t nxtot = nx + 2;
  if (h2->GetNbinsX() != nx) {
    //    cout << "Histograms must have same number of bins" << endl;
    return 0;
  }
  if (h3->GetNbinsX() != nx) {
    //    cout << "Histograms must have same number of bins" << endl;
    return 0;
  }
  if (h3->GetNbinsX() != nx) {
    //    cout << "Histograms must have same number of bins" << endl;
    return 0;
  }

  // get the new histogram
  TH1F* temp = (TH1F*) h1->Clone(name);
  temp->SetTitle(name);
  temp->Reset();
  temp->Sumw2();

  // Loop over bins, calculate efficiency and error, put it in histogram
  for (Int_t i=0; i<nxtot; i++) {
    Double_t x1 = h1->GetBinContent(i);
    Double_t x2 = h2->GetBinContent(i);
    Double_t x3 = h3->GetBinContent(i);
    Double_t x4 = h4->GetBinContent(i);
    Double_t denom = x1 - x3;
    Double_t eff;
    if (denom == 0.) {
      eff = 0;
    } else {
      eff   = (x2-x4)/denom;
    }
    Double_t failSig = x1 - x2;
    Double_t failBg  = x3 - x4;
    Double_t blah    = (1-eff)*(1-eff)*(x2+x4) + eff*eff*(failSig+failBg);
    if (blah <= 0.) blah=0.0;
    Double_t err;
    if (denom == 0) {
      err = 0.;
    } else {
      err = sqrt(blah)/denom;
    }
    temp->SetBinContent(i,eff);
    temp->SetBinError(i,err);
  }

  // Done
  return temp;
}

#include <TList.h>
#include <TIterator.h>

void deleteHistos() {
   // Delete all existing histograms in memory
   TObject* obj;
   TList* list = gDirectory->GetList() ;
   TIterator* iter = list->MakeIterator();
   while (obj=iter->Next()) {
     if (obj->IsA()->InheritsFrom(TH1::Class()) ||
         obj->IsA()->InheritsFrom(TH2::Class()) ) {delete obj;}
   }
}
histio()
{
}

saveHist(const char* filename, const char* pat="*")
{
   TList* list = gDirectory->GetList() ;
   TIterator* iter = list->MakeIterator();

   TRegexp re(pat,kTRUE) ;

   TFile outf(filename,"RECREATE") ;
   while(obj=iter->Next()) {
      if (TString(obj->GetName()).Index(re)>=0) {
         obj->Write() ;
         cout << "." ;
         cout.flush() ;
      }
   }
   cout << endl ;
   outf.Close() ;

   delete iter ;
}


loadHist(const char* filename, const char* pfx=0, const char* pat="*", Bool_t doAdd=kFALSE)
{
   TFile inf(filename) ;
   //inf.ReadAll() ;
   TList* list = inf.GetListOfKeys() ;
   TIterator* iter = list->MakeIterator();

   TRegexp re(pat,kTRUE) ;
   cout << "pat = " << pat << endl ;

   gDirectory->cd("Rint:") ;

   TObject* obj ;
   TKey* key ;
   cout << "doAdd = " << (doAdd?"T":"F") << endl ;
   cout << "loadHist: reading." ;
   while(key=(TKey*)iter->Next()) {

      Int_t ridx = TString(key->GetName()).Index(re) ;
      if (ridx==-1) {
         continue ;
      }

      obj = inf->Get(key->GetName()) ;
      TObject* clone ;
      if (pfx) {

         // Find existing TH1-derived objects
         TObject* oldObj = 0 ;
         if (doAdd){
            oldObj = gDirectory->Get(Form("%s_%s",pfx,obj->GetName())) ;
            if (oldObj && !oldObj->IsA()->InheritsFrom(TH1::Class())) {
               oldObj = 0 ;
            }
         }
         if (oldObj) {
            clone = oldObj ;
            ((TH1*)clone)->Add((TH1*)obj) ;
         } else {
            clone = obj->Clone(Form("%s_%s",pfx,obj->GetName())) ;
         }


      } else {

         // Find existing TH1-derived objects
         TObject* oldObj = 0 ;
         if (doAdd){
            oldObj = gDirectory->Get(key->GetName()) ;
            if (oldObj && !oldObj->IsA()->InheritsFrom(TH1::Class())) {
               oldObj = 0 ;
            }
         }

         if (oldObj) {
            clone = oldObj ;
            ((TH1*)clone)->Add((TH1*)obj) ;
         } else {
            clone = obj->Clone() ;
         }
      }
      if (!gDirectory->GetList()->FindObject(clone)) {
         gDirectory->Append(clone) ;
      }
      cout << "." ;
      cout.flush() ;
   }
   cout << endl;
   inf.Close() ;
   delete iter ;
}
