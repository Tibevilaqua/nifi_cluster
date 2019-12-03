# ci_cd_nifi_registry

## Purpose
Facilitate the promotion of NIFI flows from non-production servers to production servers through copying Buckets, Flows and Version from to former to the latter to facilitate the overall CI/CD deployment process so that application teams can have visibility, traceability, speed and confidence during their deployment process.

### Interfaces

#### CreateBucket
Creates a bucket

#### CreateFlow
Creates a flow assuming that the bucket already exists

#### CreatePromoteVersionController
Promotes a version from the Nifi Registry flow to the Nifi Registry destination. This process creates a Bucket and a Flow in case it does not exist.

## Future tasks to be implemented

1 - Improve the performance of the ci/cd pipeline by implementing a in memory nearby cache (HashMap would do) intead of issuing toolkit commands all the time. i.e. get bucket, get version, etc.

2 - Add variable replacement feature for flows that contain variables.

3 - Implement getBucket description for the bucket creation feature. This way, the new bucket will have the same description as the old bucket when it's copied from one registry to another.

4 - Implement getFlow description for the flow creation feature. This way, the new flow will have the same description as the old flow when it's copied from one registry to another.


