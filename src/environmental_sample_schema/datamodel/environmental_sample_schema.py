# Auto generated from environmental_sample_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-25T11:15:52
# Schema: environmental-sample-schema
#
# id: https://w3id.org/environmental-sample-schema
# description: Environmental Sample LinkML project
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Float

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ENVIRONMENTAL_SAMPLE_SCHEMA = CurieNamespace('environmental_sample_schema', 'https://w3id.org/water-sample-schema/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = ENVIRONMENTAL_SAMPLE_SCHEMA


# Types

# Class references



@dataclass
class EnvironmentalSample(YAMLRoot):
    """
    A hypothetical collection of attributes that represent a sample from a specific  location.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ENVIRONMENTAL_SAMPLE_SCHEMA["EnvironmentalSample"]
    class_class_curie: ClassVar[str] = "environmental_sample_schema:EnvironmentalSample"
    class_name: ClassVar[str] = "EnvironmentalSample"
    class_model_uri: ClassVar[URIRef] = ENVIRONMENTAL_SAMPLE_SCHEMA.EnvironmentalSample

    analysis_type: Optional[Union[str, "AnalysisTypeEnum"]] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        super().__post_init__(**kwargs)


# Enumerations
class AnalysisTypeEnum(EnumDefinitionImpl):
    """
    The type of sample
    """
    _defn = EnumDefinition(
        name="AnalysisTypeEnum",
        description="The type of sample",
    )

# Slots
class slots:
    pass

slots.analysis_type = Slot(uri=ENVIRONMENTAL_SAMPLE_SCHEMA.analysis_type, name="analysis_type", curie=ENVIRONMENTAL_SAMPLE_SCHEMA.curie('analysis_type'),
                   model_uri=ENVIRONMENTAL_SAMPLE_SCHEMA.analysis_type, domain=None, range=Optional[Union[str, "AnalysisTypeEnum"]])

slots.latitude = Slot(uri=ENVIRONMENTAL_SAMPLE_SCHEMA.latitude, name="latitude", curie=ENVIRONMENTAL_SAMPLE_SCHEMA.curie('latitude'),
                   model_uri=ENVIRONMENTAL_SAMPLE_SCHEMA.latitude, domain=None, range=Optional[float],
                   pattern=re.compile(r'^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?)$'))

slots.longitude = Slot(uri=ENVIRONMENTAL_SAMPLE_SCHEMA.longitude, name="longitude", curie=ENVIRONMENTAL_SAMPLE_SCHEMA.curie('longitude'),
                   model_uri=ENVIRONMENTAL_SAMPLE_SCHEMA.longitude, domain=None, range=Optional[float],
                   pattern=re.compile(r'^[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$'))