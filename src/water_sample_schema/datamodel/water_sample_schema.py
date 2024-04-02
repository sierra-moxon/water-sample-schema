# Auto generated from water_sample_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-04-02T15:43:07
# Schema: water-sample-schema
#
# id: https://w3id.org/sierra-moxon/water-sample-schema
# description: Sample LinkML project setup for 2024 paper figures
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
from linkml_runtime.linkml_model.types import Float, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
WATER_SAMPLE_SCHEMA = CurieNamespace('water_sample_schema', 'https://w3id.org/sierra-moxon/water-sample-schema/')
DEFAULT_ = WATER_SAMPLE_SCHEMA


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class BioSampleId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = WATER_SAMPLE_SCHEMA.NamedThing

    id: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class BioSample(NamedThing):
    """
    A hypothetical collection of attributes that represent a sample of water from a specific location and depth with
    associated bacterial composition.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = WATER_SAMPLE_SCHEMA["BioSample"]
    class_class_curie: ClassVar[str] = "water_sample_schema:BioSample"
    class_name: ClassVar[str] = "BioSample"
    class_model_uri: ClassVar[URIRef] = WATER_SAMPLE_SCHEMA.BioSample

    id: Union[str, BioSampleId] = None
    depth: Optional[float] = None
    sample_type: Optional[Union[str, URIorCURIE]] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    bacteria: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BioSampleId):
            self.id = BioSampleId(self.id)

        if self.depth is not None and not isinstance(self.depth, float):
            self.depth = float(self.depth)

        if self.sample_type is not None and not isinstance(self.sample_type, URIorCURIE):
            self.sample_type = URIorCURIE(self.sample_type)

        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if not isinstance(self.bacteria, list):
            self.bacteria = [self.bacteria] if self.bacteria is not None else []
        self.bacteria = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.bacteria]

        super().__post_init__(**kwargs)


@dataclass
class BioSampleCollection(YAMLRoot):
    """
    A holder for BioSample objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = WATER_SAMPLE_SCHEMA["BioSampleCollection"]
    class_class_curie: ClassVar[str] = "water_sample_schema:BioSampleCollection"
    class_name: ClassVar[str] = "BioSampleCollection"
    class_model_uri: ClassVar[URIRef] = WATER_SAMPLE_SCHEMA.BioSampleCollection

    entries: Optional[Union[Dict[Union[str, BioSampleId], Union[dict, BioSample]], List[Union[dict, BioSample]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=BioSample, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class SampleTypeEnum(EnumDefinitionImpl):
    """
    The type of sample
    """
    _defn = EnumDefinition(
        name="SampleTypeEnum",
        description="The type of sample",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=WATER_SAMPLE_SCHEMA.id, domain=None, range=URIRef)

slots.depth = Slot(uri=WATER_SAMPLE_SCHEMA.depth, name="depth", curie=WATER_SAMPLE_SCHEMA.curie('depth'),
                   model_uri=WATER_SAMPLE_SCHEMA.depth, domain=None, range=Optional[float])

slots.latitude = Slot(uri=WATER_SAMPLE_SCHEMA.latitude, name="latitude", curie=WATER_SAMPLE_SCHEMA.curie('latitude'),
                   model_uri=WATER_SAMPLE_SCHEMA.latitude, domain=None, range=Optional[float],
                   pattern=re.compile(r'^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?)$'))

slots.longitude = Slot(uri=WATER_SAMPLE_SCHEMA.longitude, name="longitude", curie=WATER_SAMPLE_SCHEMA.curie('longitude'),
                   model_uri=WATER_SAMPLE_SCHEMA.longitude, domain=None, range=Optional[float],
                   pattern=re.compile(r'^[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$'))

slots.sample_type = Slot(uri=WATER_SAMPLE_SCHEMA.sample_type, name="sample_type", curie=WATER_SAMPLE_SCHEMA.curie('sample_type'),
                   model_uri=WATER_SAMPLE_SCHEMA.sample_type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.bacteria = Slot(uri=WATER_SAMPLE_SCHEMA.bacteria, name="bacteria", curie=WATER_SAMPLE_SCHEMA.curie('bacteria'),
                   model_uri=WATER_SAMPLE_SCHEMA.bacteria, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]],
                   pattern=re.compile(r'^NCBITaxon:\d+$'))

slots.bioSampleCollection__entries = Slot(uri=WATER_SAMPLE_SCHEMA.entries, name="bioSampleCollection__entries", curie=WATER_SAMPLE_SCHEMA.curie('entries'),
                   model_uri=WATER_SAMPLE_SCHEMA.bioSampleCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, BioSampleId], Union[dict, BioSample]], List[Union[dict, BioSample]]]])