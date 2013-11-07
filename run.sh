#!/bin/sh
 
###############################################
 
jobname="word count"
hadoop_in=" ** path-to-hdfs-file ** "
hadoop_out=" ** path-to-hdfs-file ** "
 
###############################################
 
currentPath=`pwd`;
mapper=$currentPath"/mapper.py"
reducer=$currentPath"/reducer.py"
 
###############################################
 
options="-D mapred.reduce.tasks=30"
options=$options" -D mapred.job.priority=NORMAL"
options=$options" -file ** path-to-dic.json **"
 
###############################################
 
echo "remove hdfs file: \""$hadoop_out"\" ?[y/n]"
read ANS
 
if [ $ANS = 'y' -o $ANS = 'yes' ]; then
	hadoop fs -rmr ${hadoop_out}
	hadoop jar /home/hadoop/hadoop/contrib/streaming/hadoop-streaming-1.1.2.jar  -D mapred.job.name="${jobname}" ${options} -file ${mapper} -mapper ${mapper} -file ${reducer} -reducer ${reducer} -input ${hadoop_in} -output ${hadoop_out}
fi
