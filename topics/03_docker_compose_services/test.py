import yaml

with open("./topics/03_docker_compose_services/compose.yaml") as stream:
    try:
        a = yaml.safe_load(stream)
        print(a["services"]["model_endpoint1"]["ports"])
        print(123)

    except yaml.YAMLError as exc:
        print(exc)
