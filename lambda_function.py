import boto3
import os
import time

ec2 = boto3.client("ec2")
route53 = boto3.client("route53")

INSTANCE_ID = os.environ["INSTANCE_ID"]
HOSTED_ZONE_ID = os.environ["HOSTED_ZONE_ID"]
RECORD_NAME = os.environ["RECORD_NAME"]


def get_instance_public_ip(instance_id):

    response = ec2.describe_instances(
        InstanceIds=[instance_id]
    )

    reservations = response["Reservations"]
    instance = reservations[0]["Instances"][0]

    return instance.get("PublicIpAddress")


def update_route53_record(public_ip):

    route53.change_resource_record_sets(
        HostedZoneId=HOSTED_ZONE_ID,
        ChangeBatch={
            "Comment": "Update EC2 public IP",
            "Changes": [
                {
                    "Action": "UPSERT",
                    "ResourceRecordSet": {
                        "Name": RECORD_NAME,
                        "Type": "A",
                        "TTL": 60,
                        "ResourceRecords": [
                            {
                                "Value": public_ip
                            }
                        ]
                    }
                }
            ]
        }
    )


def delete_route53_record(public_ip):

    route53.change_resource_record_sets(
        HostedZoneId=HOSTED_ZONE_ID,
        ChangeBatch={
            "Comment": "Delete EC2 public IP record",
            "Changes": [
                {
                    "Action": "DELETE",
                    "ResourceRecordSet": {
                        "Name": RECORD_NAME,
                        "Type": "A",
                        "TTL": 60,
                        "ResourceRecords": [
                            {
                                "Value": public_ip
                            }
                        ]
                    }
                }
            ]
        }
    )


def lambda_handler(event, context):

    action = event.get("action")

    if action == "start":

        # Start EC2
        ec2.start_instances(
            InstanceIds=[INSTANCE_ID]
        )

        print("Starting EC2 instance...")

        # Wait until running
        waiter = ec2.get_waiter("instance_running")
        waiter.wait(InstanceIds=[INSTANCE_ID])

        print("EC2 instance is running")

        # Small delay for public IP assignment
        time.sleep(15)

        # Get new public IP
        public_ip = get_instance_public_ip(INSTANCE_ID)

        print(f"New Public IP: {public_ip}")

        # Update Route53
        update_route53_record(public_ip)

        print("Route53 record updated")

    elif action == "stop":

        # Get current public IP before stopping
        public_ip = get_instance_public_ip(INSTANCE_ID)

        print(f"Current Public IP: {public_ip}")

        # Delete Route53 record
        if public_ip:
            delete_route53_record(public_ip)
            print("Route53 record deleted")

        # Stop EC2
        ec2.stop_instances(
            InstanceIds=[INSTANCE_ID]
        )

        print("EC2 instance stopped")

    return {
        "status": "done",
        "action": action
    }
