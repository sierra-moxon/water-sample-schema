from pathlib import Path
from linkml.utils.schemaloader import SchemaLoader
from linkml.generators.linkmlgen import LinkmlGenerator
from linkml_runtime.dumpers import yaml_dumper
from linkml_map.session import Session
# Path to your YAML file
from pprint import pprint
schema_path = Path("../schema/environmental_sample_schema.yaml")

lmg = LinkmlGenerator(schema_path)
schema_definition = lmg.schema

session = Session()
session.set_source_schema(schema_definition)


session.set_object_transformer("""
class_derivations:
  Specimen:
    populated_from: BioSample
    slot_derivations:
      depth: 
        populated_from: depth
      sample_type:
        populated_from: sample_type
      location:
        expr: "'lat: ' + {latitude} + ' ' + 'long: ' + {family_name}"
      species_collected:
        populated_from: bacteria
        
      id:
        populated_from: id
""")


pprint(session.target_schema)
