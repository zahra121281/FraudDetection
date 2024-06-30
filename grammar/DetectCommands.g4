grammar DetectCommands;

start : setting load_data command EOF ;


setting : 'Setting' url username pass NewLine;
url:'url=' STRING;
username:'username=' STRING;
pass:'pass=' Pass;

load_data: 'LoadData' path NewLine;
command: 'Detect' ( detect_customer | detect_terminal | detect_date_range | detect_degree_limit ) NewLine;
detect_customer: 'customer' start_date end_date  limit  ;
detect_terminal: 'terminal' start_date  end_date  limit  ;
detect_date_range: 'name3' start_date end_date ;
detect_degree_limit: 'name4' degree limit ;
start_date:'startdate='DATE;
end_date:'enddate='DATE;
limit:'limit='NUMBER ;
degree:'degree='NUMBER;
path:STRING;



STRING: '"' ~["]* '"';
NewLine :'\n';
NUMBER: DIGIT+;
DATE: (DIGIT DIGIT DIGIT DIGIT) '-'DIGIT DIGIT '-' DIGIT DIGIT;
Pass : ALPHANUM ((DIGIT LETTER) | (LETTER DIGIT) ) ALPHANUM;
fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Z];
fragment ALPHANUM : [a-zA-Z0-9]*;

WS: [ \t\r\n]+ -> skip;