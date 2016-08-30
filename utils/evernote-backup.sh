file=~/Documents/backup/evernote-musings-2015-12-10.enex

general_pattern='s/([0-9]+).*<pattern>(.*)<\/pattern>.*/\1 :: \2/'
general_command=`ag "<pattern>" $file | sed -E $general_pattern`
$general_command

pattern_title=`echo $general_pattern | sed -E 's/pattern/title/g'`
results_title=`ag '<title>' $file | sed -E $pattern_title`

pattern_updated=`echo $general_pattern | sed -E 's/pattern/updated/g'`
results_updated=`ag '<updated>' $file | sed -E $pattern_updated`

results=`{echo $results_title && echo $results_updated}`
echo $results | sort -n | awk -F':: ' '{print $2}' | paste -s -d '\t\n' -
