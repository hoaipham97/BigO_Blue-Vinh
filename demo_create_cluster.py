import sys
from google.cloud import storage
from google.cloud import dataproc_v1 as dataproc
from google.cloud.dataproc_v1.gapic.transports import cluster_controller_grpc_transport
from google.cloud.dataproc_v1.gapic.transports import job_controller_grpc_transport
import click

@click.command()



project_id = 'momovn-dev'
region = 'us-central1'
cluster_name = 'hoai-test'
bucket_name = ''
filename = ''
#Create dataproc client to create, submit job and delete cluster
dataproc_cluster_client = dataproc.ClusterControllerClient(
    client_options={"api_endpoint": f"{region}-dataproc.googleapis.com:443"}
)

job_transport = job_controller_grpc_transport.JobControllerGrpcTransport(address="{}-dataproc.googleapis.com:443".format(region))
dataproc_job_client = dataproc.JobControllerClient(job_transport)

def create_cluster(project_id, region, cluster_name):
    cluster = {
        "project_id": project_id,
        "cluster_name": cluster_name,
        "config": {
            "master_config": {"num_instances": 1, "machine_type_uri": "n1-standard-4"},
            "worker_config": {"num_instances": 2, "machine_type_uri": "n1-standard-4"},
        },
    }

    operation = dataproc_cluster_client.create_cluster(
        request={"project_id": project_id, "region": region, "cluster": cluster}
    )
    result = operation.result()
    print(f"Cluster created successfully: {result.cluster_name}")




def delete_cluster(project, region, cluster):
    print("Tearing down cluster.")
    result = dataproc_cluster_client.delete_cluster(
        request={"project_id": project, "region": region, "cluster_name": cluster}
    )
    print(f"Cluster deleted successfully")
    return result


def submit_spark_job(project, region, cluster_name, bucket_name, filename):
    job_details = {
        "placement": {"cluster_name": cluster_name},
        "pyspark_job": {
            "main_python_file_uri": "gs://enki-mask-dev/HOAI_TEST/jobs/hermes_location_parser_deploy.jar".format(bucket_name, filename)
        },
    }

    result = dataproc_cluster_client.submit_job(
        request={"project_id": project, "region": region, "job": job_details, "async"}
    )
    aa = dataproc.JobControllerClient.list_jobs(request={"project_id": project, "region": region})
    job_id = result.reference.job_id
    print("Submitted job ID {}.".format(job_id))
    return job_id


def download_output(project, cluster_id, output_bucket, job_id):
    print("Downloading output file.")
    client = storage.Client(project=project)
    bucket = client.get_bucket(output_bucket)
    output_blob = "google-cloud-dataproc-metainfo/{}/jobs/{}/driveroutput.000000000".format(
        cluster_id, job_id
    )
    return bucket.blob(output_blob).download_as_string()


def submit_job_with_async(project, cluster_id, output_bucket, job_id):



if __name__ == "__main__":
    create_cluster(project_id, region, cluster_name)
    # delete_cluster(project_id, region, cluster_name)

    # job_id = submit_spark_job(dataproc_job_client, project_id, region, cluster_name, bucket_name, spark_filename)
    # output = download_output(project_id, cluster_id, output_bucket, job_id)
    # print("Received job output {}".format(output))

