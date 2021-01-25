% skript for WRC-curve clustering analysis / Samuli 22.6.2016
% uses Statistical Toolbox clustering functions

clear; close all
inpath='c:\Projects\HydrologisetOminaisuudet\Data\\';

infile='WRCdata_from_python.dat';

%read raw data
wrcdata=readtable([inpath infile], 'Delimiter',';','ReadVariableNames',false, 'HeaderLines',1, 'FileEncoding', 'utf-8');
psi_m=[0.01 0.3 1 5 10 33 98.1 1500]; %kPa

theta_m=table2array(wrcdata(:,11:18))/100.0; %vol. water cont. m3/m3
Org=table2array(wrcdata(:,10))/100.0; %organic fraction
Bd=table2array(wrcdata(:,8)); %bulk denstiy g/cm3

%vanGenuchten 4-parameter fit coefficients

% datafile looks like this:
% ;thetaS;thetaR;alpha;n;resid;NrIter
% 0;0.917332812651;0.0451831494062;4.98494861481;1.25851804116;0.0133521306486;23.0
% 1;0.530772402052;0.0;10.0;1.21792705327;0.00244280916269;40.0
% 2;0.959374891056;0.0198112748537;4.4423245361;1.3852249046;0.0200713651931;25.0
% 3;0.718307978596;0.0;10.0;1.18802872989;0.00967358801619;30.0
% 4;0.894914829235;0.0842161811786;10.0;1.39585853445;0.0133821854928;100.0

infile='WRC_vanG4p.dat';
vanG4=readtable([inpath infile], 'Delimiter',';','ReadVariableNames',false, 'HeaderLines',1, 'FileEncoding', 'utf-8');
vanG4=table2array(vanG4);
g=find(vanG4(:,7)<200); %iteration numbers
%get params
P=vanG4(:,2:5); %th_sat th_res alpha n

% %vanGenuchten 5-parameter fit coefficients
% infile='WRC_vanG5p.dat';
% vanG5=readtable([inpath infile], 'Delimiter',';','ReadVariableNames',false, 'HeaderLines',1, 'FileEncoding', 'utf-8');
% vanG5=table2array(vanG5);
% g=find(vanG5(:,8)<100); %iteration numbers
% %get params
% P=vanG5(:,2:6); %th_sat th_res alpha n m

% infile='WRC_Campbell.dat';
% camp=readtable([inpath infile], 'Delimiter',';','ReadVariableNames',false, 'HeaderLines',1, 'FileEncoding', 'utf-8');
% camp=table2array(camp);
% g=find(camp(:,6)<100); %iteration numbers
% %get params
% P=camp(:,2:4); %th_sat th_res alpha n

%--- find rows in P where we have fit coefficients AND know Bd and Org fraction
f=find(isnan(P(:,1))==0 & isnan(Bd)==0 & isnan(Org)==0);

%rows where iterno<200 and criteria above is filled
ff=intersect(f,g);
%subset of P
P=P(ff,:);

%M=P;
%M(:,6)=Bd(ff);
%M(:,5)=Org(ff); 

%normalize parameter values, see help zscore    
Z=zscore(P,[],1); 

%th_sat=vanG4(:,2); th_res=vanG4(:,3); alpha=vanG4(:,4); n=vanG4(:,5); sse=vanG4(:,6); iterNo=vanG4(:,7);

% load vanG4 model predictions (these have saved from Python); could
% calculate here from models + parameter values also
vanG=csvread([inpath 'vanG4fit.dat'],1,0);
x=logspace(-2,3.2,100);

f=find(vanG(:,2)>0); 
vanG=vanG(ff,2:end);
vanGz=zscore(vanG,[],1);

%% test clustering data by 'P'
%see help clusterdata
close all
rng default;  % For reproducibility
eva = evalclusters(Z,'kmeans','CalinskiHarabasz','KList',[1:20])
% Y=pdist(P,'euclidean'); %compute euclidian distances
% Z=linkage(Y); %linkages
% %plot hierarchical clusters
% dendrogram(Z)
hc=clusterdata(Z,'maxclust',15,'distance','cityblock');
kc=kmeans(Z,8,'distance','sqeuclidean', 'emptyaction', 'drop');
%kcp=kmeans(P,20);


%scatter3(P(f,1), P(f,2), P(f,3),50,kc,'filled')

% plot curves

cmap = colormap(colorcube);
figure(100);
clf;
for k=1:8,
    figure(100);
    subplot(3,3,k);
    semilogx(x,vanG(kc==k,:),'-','color',cmap(k,:)); hold on
    title(['Cluster: ' num2str(k)])
    ylim([0 1]);    xlim([0.99*min(x), 1.01*max(x)])
    xlabel('kPa'); ylabel('Th (m^3m^{-3})')

    subplot(3,3,9);
    semilogx(x,mean(vanG(kc==k,:)),'-','color',cmap(k,:),'linewidth',1); hold on
    ylim([0 1]);    xlim([0.99*min(x), 1.01*max(x)])
    xlabel('kPa'); ylabel('Th (m^3m^{-3})'); title('Cluster means')
    
    figure(200);
    %subplot(3,3,9);
    semilogx(x,mean(vanG(kc==k,:)),'-','color',cmap(k,:)); hold on
    %semilogx(x,median(vanG(kc==k,:)),'--','color',cmap(k,:)); hold on
    ylim([0 1]);    xlim([0.99*min(x), 1.01*max(x)])
    xlabel('kPa'); ylabel('Th (m^3m^{-3})'); title('Cluster means')

    figure(400);
    subplot(3,3,9);
    semilogx(x,mean(vanG(kc==k,:)),'-','color',cmap(k,:),'linewidth',1); hold on
    %semilogx(x,median(vanG(kc==k,:)),'--','color',cmap(k,:)); hold on
    ylim([0 1]); xlim([0.99*min(x), 1.01*max(x)])
    xlabel('kPa'); ylabel('Th (m^3m^{-3})'); title('Cluster means');
   
%     figure(300);
%     subplot(121);
%     plot(k,Org(kc==k),'o','color',cmap(k,:)); hold on;
%     ylabel('Org fraction')
% 
%     subplot(122);
%     plot(k,Bd(kc==k),'o','color',cmap(k,:)); hold on;
%     ylabel('Bd g/cm^3')
end
figure(400);
subplot(3,3,9);
legend('1','2','3','4','5','6','7','8')
%boxplots

figure(400);

subplot(3,3,1);
boxplot(P(:,1),kc); ylabel('Th_s'); xlabel('Cluster'); title('vanG param')
subplot(3,3,2);
boxplot(P(:,2),kc); ylabel('Th_r'); xlabel('Cluster'); title('vanG param')

subplot(3,3,3);
boxplot(P(:,3),kc); ylabel('alpha'); xlabel('Cluster'); title('vanG param')
subplot(3,3,4);
boxplot(P(:,4),kc); ylabel('n'); xlabel('Cluster'); title('vanG param')

subplot(3,3,5);
boxplot(Bd(ff),kc); ylabel('Bd g/cm^3'); xlabel('Cluster'); title('meas')

subplot(3,3,6);
boxplot(Org(ff),kc); ylabel('Org (-)'); xlabel('Cluster'); title('meas')

subplot(3,3,7);
boxplot(theta_m(ff,6),kc); ylabel('FC (-33 kPa)'); xlabel('Cluster'); title('meas') 

subplot(3,3,8);
boxplot(theta_m(ff,8),kc); ylabel('WP (-1500 kPa)'); xlabel('Cluster'); title('meas')
