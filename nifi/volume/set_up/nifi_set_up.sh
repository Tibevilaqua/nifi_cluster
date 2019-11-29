export PATH=$PATH:/opt/volumes/nifi-toolkit-1.10.0/bin/

bucketName="ci-cd-test-1"
flowName="ci-cd-test-flow-1"
nifi_registry_ip=$(host nifi_registry | awk '{print $4}')
nifi_registry_second_cluster_ip=$(host nifi_registry_second_cluster | awk '{print $4}')


execute(){
	nifiRegistryIp=$1
	nifiIp=$2

	## Create bucket & flow
	cli.sh registry create-bucket -bn $bucketName -u http://$nifiRegistryIp:18080

	bucketId=$(cli.sh registry list-buckets -u http://$nifiRegistryIp:18080 | grep $bucketName | awk '{print $3}')

	cli.sh registry create-flow -b $bucketId -fn $flowName -u http://$nifiRegistryIp:18080

	cli.sh nifi create-reg-client --registryClientUrl http://$nifiRegistryIp:18080 --registryClientName nifi_registry -u http://$nifiIp:8080

	#Import versions to flow

	flowId=$(cli.sh registry list-flows -u http://$nifiRegistryIp:18080 -b $bucketId | grep $flowName | awk '{print $3}')

	cli.sh registry import-flow-version -u http://$nifiRegistryIp:18080 -f $flowId  -i fv1.json
	cli.sh registry import-flow-version -u http://$nifiRegistryIp:18080 -f $flowId  -i fv2.json
	cli.sh registry import-flow-version -u http://$nifiRegistryIp:18080 -f $flowId  -i fv3.json

	cli.sh nifi pg-import -b $bucketId -f $flowId -fv 3 -u http://$nifiIp:8080
}


execute $nifi_registry_ip nifi
execute $nifi_registry_second_cluster_ip nifi_second_cluster
