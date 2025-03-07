#!/usr/bin/env python3

import os
import sys
import json

def cleanup_old_versions(layer_name, versions_to_delete):
    for version in versions_to_delete:
        print(f"aws lambda delete-layer-version --layer-name {layer_name} --version-number {version['Version']}")
        os.system(f"aws lambda delete-layer-version --layer-name {layer_name} --version-number {version['Version']}")

versions = json.loads(os.popen(f"aws lambda list-layer-versions --layer-name lambda_monitoring").read())

if len(versions['LayerVersions']) >1:
    cleanup_old_versions(layer['LayerName'], versions['LayerVersions'][1:])
