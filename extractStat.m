function extractStat()


%str = fileread('WiFiDemo.txt');
%expr = '[^\n]*Signals transmitted[^\n]*';
%matches = regexp(str, expr, 'match');
%disp(matches)
fid = fopen('STAT_FILE_FOR_SCENARIO_WITH_1AP.txt');

tline = fgetl(fid);

substring1 = "Signals transmitted (signals) = ";
substring2 = "Time spent transmitting (seconds) = ";
signalarray = [];
    tokenarray = [];
    timearray = [];
while ischar(tline)
    
    if contains(tline,substring1) == 1
        U1 = strfind (tline, 'Signals transmitted (signals) = ');
        length = strlength(substring1);
        token1 = strtok(tline);
        tok1 = uint32(str2num(token1));
        tokenarray = [tokenarray, tok1];
        signal = tline(U1+length:end);
        signals = str2double(signal);
        signalarray = [signalarray, signals];
        sprintf('%s     %f', tline);
    %    disp(tline)
    end
    
    if contains(tline,substring2) == 1
        U2 = strfind (tline, 'Time spent transmitting (seconds) = ');
        length = strlength(substring2);
        %token2 = strtok(tline)
        times = tline(U2+length:end);
        time = str2double (times);
        timearray = [timearray, time];
        sprintf('%s     %f', tline);
    %    disp(tline)
    end
    tline = fgetl(fid);
end
tokenarray;
signalarray;
timearray;
throughputarray = [];
size(tokenarray, 2);
for i = 1 : size(tokenarray, 2)
    throughput(i) = signalarray(i)/timearray(i);
    throughputarray = [throughputarray, throughput(i)]; 
end
throughputarray;
farray = [tokenarray; signalarray; timearray];
ftarray = [tokenarray; throughputarray];

finalarray = transpose(farray)
finalthroughputarray = transpose(ftarray)
fclose(fid);

%myfile = fopen('throughputfile.txt','a+');
dlmwrite ('throughputfile.txt', finalthroughputarray, 'delimiter', '\t', 'precision', 4, 'newline', 'pc');
        
end