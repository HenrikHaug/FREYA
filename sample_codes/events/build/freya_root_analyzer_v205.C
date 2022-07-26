#include <TH1.h>
#include <TH2.h>
#include <TTree.h>
#include <TROOT.h>
#include <iostream>
#include <cstdio>
#include "TFile.h"
#include "TChain.h"
#include <algorithm>
#include <fstream>
#include <sstream>
#include <string>

// root -l freya_root_analyzer_v205.C


TFile *vetsex = new TFile("test3.dat.root", "READ");
TTree *mytree = (TTree *) gROOT->FindObject("FreyaTree");


/*
List of meanings:

iAf1: fission fragment 1, mass number
iAf2: fission fragment 2, mass number
iAp1: product fission fragment 1, mass number (after n emission)
iAp2: product fission fragment 2, mass number (after n emission)
E1kin: kinetic energy of 1 product
E2kin: kinetic energy of second product
n0: neutrons from compound nuclei
n1: neutrons from first fission fragment
n2: neutrons from second fission fragment
m0: # pre-fission photons
m1: # photons from fragment 1
m2: # photons from fragment 2
P0: energy of neutrons emmited pre-fission (?)
P1: energy of neutrons emmited by F1
P2: energy of neutrons emitted by F2
Q0: energy of gammas emitted pre-fission
Q1: energy of gammas emitted by F1
Q2: energy of gamma emitted by F2

m_first: # photons from first chance fission
m_second: # photons from second chance fission
m_second: # photons from third chance fission

Q_first: energy from PFG's from first chance
Q_second: energy from PFG's from second chance
Q_third: energy from PFG's from third chance
*/

//Fragment mass yields
TH1D *hframe_iAf1;
TH1D *hframe_iAf2;

TH1D *hframe_m0;
TH1D *hframe_m1;
TH1D *hframe_m2;

TH1D *hframe_Q1;
TH1D *hframe_Q2;
TH1D *hframe_Qtot;


void create_frames();


void freya_root_analyzer_v205() {

	create_frames();


	//////////////////////////////////////
	//  Fission fragment mass distribution
	/////////////////////////////////////

	TCanvas *A_yield = new TCanvas("A_yield","Fragment Yield",150,10,990,660);
	mytree->Draw("iAf1>>hframe_iAf1");
	mytree->Draw("iAf2>>hframe_iAf2");
	hframe_iAf1->SetLineColor(2);
	hframe_iAf1->GetXaxis()->SetTitle("Mass [A]");
	hframe_iAf1->GetYaxis()->SetTitle("Counts");
	hframe_iAf1->SetTitle("Fission fragment mass distribution");
	hframe_iAf1->Draw();
	hframe_iAf2->Draw("same");

	auto legend_A_yield = new TLegend(0.7,0.75,0.9,0.9);
	legend_A_yield->SetTextSize(0.03);
	legend_A_yield->AddEntry(hframe_iAf1,     "FF1, light,","l");
	legend_A_yield->AddEntry(hframe_iAf2,     "FF2, heavy","l");
	legend_A_yield->Draw();

	std::cout << "\n" << std::endl;
	std::cout << "Avg. initial mass FF1 [A]: " << hframe_iAf1->GetMean() << " Avg. initial mass FF2 [A]: " << hframe_iAf2->GetMean() << std::endl;
	std::cout << "\n" << std::endl;


	///////////////////////////////////////
	// Number of fissions
	///////////////////////////////////////

	int F = 0;
	for(int i=0;i<300;i++){
  		F += hframe_iAf1->GetBinContent(i);
	}
	std::cout << "Number of fissions: " << F << std::endl;
	std::cout << "\n" << std::endl;

	////////////////////////////////////////
	/// Gamma properties
	///////////////////////////////////////

	//Gamma multiplicity distribution
	TCanvas *photon_mult = new TCanvas("gamma_mult","gamma multiplicity",150,10,990,660);
	mytree->Draw("m1>>hframe_m1");
	mytree->Draw("m2>>hframe_m2");
	hframe_m1->SetLineColor(2);
	hframe_m1->GetXaxis()->SetTitle("Multiplicity");
	hframe_m1->GetYaxis()->SetTitle("Counts");
	hframe_m1->SetTitle("Gamma multiplicity");
	hframe_m1->Draw();
	hframe_m2->Draw("same");

	//Gamma energy spectrum (individual fragments) -> Needs to be normalized to counts/(MeV*F)
	TCanvas *gamma_spectrum = new TCanvas("gamma_spectrum","Gamma Energy Spectrum ",150,10,990,660);
	gamma_spectrum->SetLogy();
	mytree->Draw("Q1>>hframe_Q1");
	mytree->Draw("Q2>>hframe_Q2");
	hframe_Q1->SetLineColor(2);
	hframe_Q1->GetXaxis()->SetTitle("Energy [MeV]");
	hframe_Q1->GetYaxis()->SetTitle("Counts");
	hframe_Q1->SetTitle("Gamma spectrum, Per Fragment");
	hframe_Q1->Draw();
	hframe_Q2->Draw("same");

	//Gamma energy spectrum (total) -> Needs to be normalized to counts/(MeV*F)
	TCanvas *gamma_spectrum_total = new TCanvas("gamma_spectrum_total","Gamma Energy Spectrum Total ",150,10,990,660);
	gamma_spectrum_total->SetLogy();
	hframe_Qtot->Add(hframe_Q1,1.0);
	hframe_Qtot->Add(hframe_Q2,1.0);
	hframe_Qtot->GetXaxis()->SetTitle("Energy [MeV]");
	hframe_Qtot->GetYaxis()->SetTitle("Counts");
	hframe_Qtot->SetTitle("Total Gamma Spectrum, F1+F2");
	hframe_Qtot->Draw();

	//Calculate average PFG multiplicity and energy
	int nbins_Qtot= hframe_Qtot->GetNbinsX();
	double avg_gamma_multiplicity = 0;

	for (int i=1; i<nbins_Qtot;i++){
		avg_gamma_multiplicity += hframe_Qtot->GetBinContent(i)/F;
	}

	std::cout << "Average gamma multiplicity per fission: " << avg_gamma_multiplicity << std::endl;
	//cout << "\n" << endl;
}


void create_frames() {

	gStyle->SetOptStat(0);
	int nbins;
	int maxbin;

	hframe_iAf1 = new TH1D("hframe_iAf1","",250,0,249);
	hframe_iAf2 = new TH1D("hframe_iAf2","",250,0,249);

	hframe_m1 = new TH1D("hframe_m1","",21,0,20);
	hframe_m2 = new TH1D("hframe_m2","",21,0,20);

	hframe_Q1 = new TH1D("hframe_Q1", "", 1000,0.001,10);
	hframe_Q2 = new TH1D("hframe_Q2", "", 1000,0.001,10);
	hframe_Qtot = new TH1D("hframe_Qtot", "", 1000,0.001,10);
}
