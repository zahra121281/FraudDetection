grammar DetectCommands;

start : setting load_terminal load_customer load_transaction commands EOF ;


setting : 'Setting' url username pass dbname NewLine*;
url:'url=' STRING;
username:'username=' STRING;
pass:'pass=' Pass;
dbname:'Databasename=' STRING;

load_terminal: 'LoadTerminal' path  NewLine*;
load_customer: 'LoadCustomer' path  NewLine*;
load_transaction: 'LoadTransaction' path  NewLine*;
path:STRING;

commands: command+;
command: 'Detect' ( detect_customer | detect_terminal | detect_date_range | detect_degree_limit ) NewLine*;
detect_customer: 'customer' start_date end_date  limit  ;
detect_terminal: 'terminal' start_date  end_date  limit  ;
detect_date_range: 'transactions_of_each_period' start_date end_date ;
detect_degree_limit: 'cc_relationship_with_degree' degree limit ;
start_date:'startdate='DATE;
end_date:'enddate='DATE;
limit:'limit='NUMBER ;
degree:'degree='NUMBER;




STRING: '"' ~["]* '"';
NUMBER: DIGIT+;
DATE: (DIGIT DIGIT DIGIT DIGIT) '-'DIGIT DIGIT '-' DIGIT DIGIT;
Pass : ALPHANUM+ (CHARACTER | ALPHANUM)*;
fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Z];
fragment ALPHANUM : [a-zA-Z0-9];
fragment CHARACTER :  '@' | '-' | '.';

WS: [ \t\r]+ -> skip;
NewLine : '\n';

