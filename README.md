# What is this
This is a junction of Nifi and Nifi Registry servers put together in containers to facilitate and speed up the development of CI/CD pipeline features.


## Assumptions
You know what you're doing and do not need someone to hold your hand while using this implementation


## Concepts

There are 2 groups of instances. nifi & nifi_registry AND nifi_second_cluster & nifi_registry_second_cluster. They are meant to be independent to simulate different environments, say non-prod and prod. Additionally, all commands are triggered from the nifi container just because I didn't want to create another container to be used as the "CI/CD agent box".



#Set-up
### 1 - Download the nifi-toolkit-1.10.0 to the nifi/volume folder so that it can be volumed inside the container for API usage.

### 2 - Update the variable NIFI_REGISTRY_COMMAND_PREFIX inside the Properties.py file in the ci_cd_nifi_registry/scripts/resources folder OR make the "cli.sh" reacheable through the command line (PATH variable)

#Start-up
### 1 - On the nifi_registry folder run "docker-compose up"

### 2 - Once the containers are running. Give them 30 seconds or so and then run the set_up.sh script in the nifi_cluster/utils folder. This will create 1 bucket, 1 flow file and 3 versions in each NIFI registry and push the process groups to the their respective NIFI instances