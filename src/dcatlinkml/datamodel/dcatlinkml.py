# Auto generated from dcatlinkml.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-05-02T13:34:38
# Schema: DCATap_LinkML_Template
#
# id: https://ndfi4cat.de/linkml/tests/DCATap
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

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
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DCATAP_LINKML_TEMPLATE_FROM_NFDI4CAT = CurieNamespace('DCATap_LinkML_Template_from_NFDI4Cat', 'https://ndfi4cat.de/linkml/tests/DCATap')
ADMS = CurieNamespace('adms', 'http://www.w3.org/ns/adms')
CC = CurieNamespace('cc', 'http://creativecommons.org/ns')
DC = CurieNamespace('dc', 'http://purl.org/dc/elements/1.1/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCATAP = CurieNamespace('dcatap', 'http://data.europa.eu/r5r/')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LCON = CurieNamespace('lcon', 'http://www.w3.org/ns/locn')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
ODRL = CurieNamespace('odrl', 'http://www.w3.org/ns/odrl/2/')
ORG = CurieNamespace('org', 'http://www.w3.org/ns/org')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SH = CurieNamespace('sh', 'http://www.w3.org/ns/shacl')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SPDX = CurieNamespace('spdx', 'http://spdx.org/rdf/terms')
TIME = CurieNamespace('time', 'http://www.w3.org/2006/time')
VCARD = CurieNamespace('vcard', 'http://www.w3.org/2006/vcard/ns')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'https://ndfi4cat.de/linkml/tests/DCATap/')


# Types

# Class references



@dataclass
class DcatDataset(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Dataset"]
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "dcat_Dataset"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/DcatDataset")

    dct_description: Union[Union[dict, "RdfsLiteral"], List[Union[dict, "RdfsLiteral"]]] = None
    dct_title: Union[Union[dict, "RdfsLiteral"], List[Union[dict, "RdfsLiteral"]]] = None
    dct_contactPoint: Optional[Union[Union[dict, "VcardKind"], List[Union[dict, "VcardKind"]]]] = empty_list()
    dct_keyword: Optional[Union[Union[dict, "RdfsLiteral"], List[Union[dict, "RdfsLiteral"]]]] = empty_list()
    dct_theme: Optional[Union[Union[dict, "SkosConcept"], List[Union[dict, "SkosConcept"]]]] = empty_list()
    adms_identifier: Optional[Union[Union[dict, "AdmsIdentifier"], List[Union[dict, "AdmsIdentifier"]]]] = empty_list()
    adms_versionNotes: Optional[Union[Union[dict, "RdfsLiteral"], List[Union[dict, "RdfsLiteral"]]]] = empty_list()
    dcat_landingPage: Optional[Union[Union[dict, "FoafDocument"], List[Union[dict, "FoafDocument"]]]] = empty_list()
    dcat_qualifiedRelation: Optional[Union[Union[dict, "DcatRelationship"], List[Union[dict, "DcatRelationship"]]]] = empty_list()
    dcat_spatialResolutionInMeters: Optional[Union[Union[dict, "XsdDecimal"], List[Union[dict, "XsdDecimal"]]]] = empty_list()
    dcat_temporalResolution: Optional[Union[Union[dict, "XsdDuration"], List[Union[dict, "XsdDuration"]]]] = empty_list()
    dcat_version: Optional[Union[Union[dict, "RdfsLiteral"], List[Union[dict, "RdfsLiteral"]]]] = empty_list()
    dct_accessRights: Optional[Union[dict, "DctFrequency"]] = None
    dct_accuralPeriodicity: Optional[Union[dict, "DctFrequency"]] = None
    dct_conformsTo: Optional[Union[Union[dict, "DctStandard"], List[Union[dict, "DctStandard"]]]] = empty_list()
    dct_identifier: Optional[Union[Union[dict, "RdfsLiteral"], List[Union[dict, "RdfsLiteral"]]]] = empty_list()
    dct_isReferencedBy: Optional[Union[Union[dict, "RdfsResource"], List[Union[dict, "RdfsResource"]]]] = empty_list()
    dct_issued: Optional[str] = None
    dct_language: Optional[Union[Union[dict, "DctLinguisticSystem"], List[Union[dict, "DctLinguisticSystem"]]]] = empty_list()
    dct_modified: Optional[str] = None
    dct_provenance: Optional[Union[Union[dict, "DctProvenanceStatement"], List[Union[dict, "DctProvenanceStatement"]]]] = empty_list()
    dct_relation: Optional[Union[Union[dict, "RdfsResource"], List[Union[dict, "RdfsResource"]]]] = empty_list()
    dct_type: Optional[Union[dict, "SkosConcept"]] = None
    foaf_page: Optional[Union[Union[dict, "FoafDocument"], List[Union[dict, "FoafDocument"]]]] = empty_list()
    owl_versionInfo: Optional[Union[dict, "RdfsLiteral"]] = None
    prov_qualifiedAttribution: Optional[Union[Union[dict, "ProvAttribution"], List[Union[dict, "ProvAttribution"]]]] = empty_list()
    prov_wasGeneratedBy: Optional[Union[Union[dict, "ProvActivity"], List[Union[dict, "ProvActivity"]]]] = empty_list()
    dcat_themeTaxonomy: Optional[Union[Union[dict, "SkosConcept"], List[Union[dict, "SkosConcept"]]]] = empty_list()
    dct_spatial: Optional[Union[Union[dict, "DctLocation"], List[Union[dict, "DctLocation"]]]] = empty_list()
    dct_temporal: Optional[Union[Union[dict, "DctPeriodOfTime"], List[Union[dict, "DctPeriodOfTime"]]]] = empty_list()
    dct_publisher: Optional[Union[dict, "FoafAgent"]] = None
    dcat_distribution: Optional[Union[Union[dict, "DcatDistribution"], List[Union[dict, "DcatDistribution"]]]] = empty_list()
    dcat_hasVersion: Optional[Union[Union[dict, "DcatDataset"], List[Union[dict, "DcatDataset"]]]] = empty_list()
    dcat_isVersionOf: Optional[Union[Union[dict, "DcatDataset"], List[Union[dict, "DcatDataset"]]]] = empty_list()
    dct_source: Optional[Union[Union[dict, "DcatDataset"], List[Union[dict, "DcatDataset"]]]] = empty_list()
    adms_sample: Optional[Union[Union[dict, "DcatDistribution"], List[Union[dict, "DcatDistribution"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.dct_description):
            self.MissingRequiredField("dct_description")
        if not isinstance(self.dct_description, list):
            self.dct_description = [self.dct_description] if self.dct_description is not None else []
        self.dct_description = [v if isinstance(v, RdfsLiteral) else RdfsLiteral(**as_dict(v)) for v in self.dct_description]

        if self._is_empty(self.dct_title):
            self.MissingRequiredField("dct_title")
        if not isinstance(self.dct_title, list):
            self.dct_title = [self.dct_title] if self.dct_title is not None else []
        self.dct_title = [v if isinstance(v, RdfsLiteral) else RdfsLiteral(**as_dict(v)) for v in self.dct_title]

        if not isinstance(self.dct_contactPoint, list):
            self.dct_contactPoint = [self.dct_contactPoint] if self.dct_contactPoint is not None else []
        self.dct_contactPoint = [v if isinstance(v, VcardKind) else VcardKind(**as_dict(v)) for v in self.dct_contactPoint]

        if not isinstance(self.dct_keyword, list):
            self.dct_keyword = [self.dct_keyword] if self.dct_keyword is not None else []
        self.dct_keyword = [v if isinstance(v, RdfsLiteral) else RdfsLiteral(**as_dict(v)) for v in self.dct_keyword]

        if not isinstance(self.dct_theme, list):
            self.dct_theme = [self.dct_theme] if self.dct_theme is not None else []
        self.dct_theme = [v if isinstance(v, SkosConcept) else SkosConcept(**as_dict(v)) for v in self.dct_theme]

        if not isinstance(self.adms_identifier, list):
            self.adms_identifier = [self.adms_identifier] if self.adms_identifier is not None else []
        self.adms_identifier = [v if isinstance(v, AdmsIdentifier) else AdmsIdentifier(**as_dict(v)) for v in self.adms_identifier]

        if not isinstance(self.adms_versionNotes, list):
            self.adms_versionNotes = [self.adms_versionNotes] if self.adms_versionNotes is not None else []
        self.adms_versionNotes = [v if isinstance(v, RdfsLiteral) else RdfsLiteral(**as_dict(v)) for v in self.adms_versionNotes]

        if not isinstance(self.dcat_landingPage, list):
            self.dcat_landingPage = [self.dcat_landingPage] if self.dcat_landingPage is not None else []
        self.dcat_landingPage = [v if isinstance(v, FoafDocument) else FoafDocument(**as_dict(v)) for v in self.dcat_landingPage]

        if not isinstance(self.dcat_qualifiedRelation, list):
            self.dcat_qualifiedRelation = [self.dcat_qualifiedRelation] if self.dcat_qualifiedRelation is not None else []
        self.dcat_qualifiedRelation = [v if isinstance(v, DcatRelationship) else DcatRelationship(**as_dict(v)) for v in self.dcat_qualifiedRelation]

        if not isinstance(self.dcat_spatialResolutionInMeters, list):
            self.dcat_spatialResolutionInMeters = [self.dcat_spatialResolutionInMeters] if self.dcat_spatialResolutionInMeters is not None else []
        self.dcat_spatialResolutionInMeters = [v if isinstance(v, XsdDecimal) else XsdDecimal(**as_dict(v)) for v in self.dcat_spatialResolutionInMeters]

        if not isinstance(self.dcat_temporalResolution, list):
            self.dcat_temporalResolution = [self.dcat_temporalResolution] if self.dcat_temporalResolution is not None else []
        self.dcat_temporalResolution = [v if isinstance(v, XsdDuration) else XsdDuration(**as_dict(v)) for v in self.dcat_temporalResolution]

        if not isinstance(self.dcat_version, list):
            self.dcat_version = [self.dcat_version] if self.dcat_version is not None else []
        self.dcat_version = [v if isinstance(v, RdfsLiteral) else RdfsLiteral(**as_dict(v)) for v in self.dcat_version]

        if self.dct_accessRights is not None and not isinstance(self.dct_accessRights, DctFrequency):
            self.dct_accessRights = DctFrequency()

        if self.dct_accuralPeriodicity is not None and not isinstance(self.dct_accuralPeriodicity, DctFrequency):
            self.dct_accuralPeriodicity = DctFrequency()

        if not isinstance(self.dct_conformsTo, list):
            self.dct_conformsTo = [self.dct_conformsTo] if self.dct_conformsTo is not None else []
        self.dct_conformsTo = [v if isinstance(v, DctStandard) else DctStandard(**as_dict(v)) for v in self.dct_conformsTo]

        if not isinstance(self.dct_identifier, list):
            self.dct_identifier = [self.dct_identifier] if self.dct_identifier is not None else []
        self.dct_identifier = [v if isinstance(v, RdfsLiteral) else RdfsLiteral(**as_dict(v)) for v in self.dct_identifier]

        if not isinstance(self.dct_isReferencedBy, list):
            self.dct_isReferencedBy = [self.dct_isReferencedBy] if self.dct_isReferencedBy is not None else []
        self.dct_isReferencedBy = [v if isinstance(v, RdfsResource) else RdfsResource(**as_dict(v)) for v in self.dct_isReferencedBy]

        if self.dct_issued is not None and not isinstance(self.dct_issued, str):
            self.dct_issued = str(self.dct_issued)

        if not isinstance(self.dct_language, list):
            self.dct_language = [self.dct_language] if self.dct_language is not None else []
        self.dct_language = [v if isinstance(v, DctLinguisticSystem) else DctLinguisticSystem(**as_dict(v)) for v in self.dct_language]

        if self.dct_modified is not None and not isinstance(self.dct_modified, str):
            self.dct_modified = str(self.dct_modified)

        if not isinstance(self.dct_provenance, list):
            self.dct_provenance = [self.dct_provenance] if self.dct_provenance is not None else []
        self.dct_provenance = [v if isinstance(v, DctProvenanceStatement) else DctProvenanceStatement(**as_dict(v)) for v in self.dct_provenance]

        if not isinstance(self.dct_relation, list):
            self.dct_relation = [self.dct_relation] if self.dct_relation is not None else []
        self.dct_relation = [v if isinstance(v, RdfsResource) else RdfsResource(**as_dict(v)) for v in self.dct_relation]

        if self.dct_type is not None and not isinstance(self.dct_type, SkosConcept):
            self.dct_type = SkosConcept()

        if not isinstance(self.foaf_page, list):
            self.foaf_page = [self.foaf_page] if self.foaf_page is not None else []
        self.foaf_page = [v if isinstance(v, FoafDocument) else FoafDocument(**as_dict(v)) for v in self.foaf_page]

        if self.owl_versionInfo is not None and not isinstance(self.owl_versionInfo, RdfsLiteral):
            self.owl_versionInfo = RdfsLiteral()

        if not isinstance(self.prov_qualifiedAttribution, list):
            self.prov_qualifiedAttribution = [self.prov_qualifiedAttribution] if self.prov_qualifiedAttribution is not None else []
        self.prov_qualifiedAttribution = [v if isinstance(v, ProvAttribution) else ProvAttribution(**as_dict(v)) for v in self.prov_qualifiedAttribution]

        if not isinstance(self.prov_wasGeneratedBy, list):
            self.prov_wasGeneratedBy = [self.prov_wasGeneratedBy] if self.prov_wasGeneratedBy is not None else []
        self.prov_wasGeneratedBy = [v if isinstance(v, ProvActivity) else ProvActivity(**as_dict(v)) for v in self.prov_wasGeneratedBy]

        if not isinstance(self.dcat_themeTaxonomy, list):
            self.dcat_themeTaxonomy = [self.dcat_themeTaxonomy] if self.dcat_themeTaxonomy is not None else []
        self.dcat_themeTaxonomy = [v if isinstance(v, SkosConcept) else SkosConcept(**as_dict(v)) for v in self.dcat_themeTaxonomy]

        if not isinstance(self.dct_spatial, list):
            self.dct_spatial = [self.dct_spatial] if self.dct_spatial is not None else []
        self.dct_spatial = [v if isinstance(v, DctLocation) else DctLocation(**as_dict(v)) for v in self.dct_spatial]

        if not isinstance(self.dct_temporal, list):
            self.dct_temporal = [self.dct_temporal] if self.dct_temporal is not None else []
        self.dct_temporal = [v if isinstance(v, DctPeriodOfTime) else DctPeriodOfTime(**as_dict(v)) for v in self.dct_temporal]

        if self.dct_publisher is not None and not isinstance(self.dct_publisher, FoafAgent):
            self.dct_publisher = FoafAgent(**as_dict(self.dct_publisher))

        self._normalize_inlined_as_dict(slot_name="dcat_distribution", slot_type=DcatDistribution, key_name="dcat_accessURL", keyed=False)

        self._normalize_inlined_as_dict(slot_name="dcat_hasVersion", slot_type=DcatDataset, key_name="dct_description", keyed=False)

        self._normalize_inlined_as_dict(slot_name="dcat_isVersionOf", slot_type=DcatDataset, key_name="dct_description", keyed=False)

        self._normalize_inlined_as_dict(slot_name="dct_source", slot_type=DcatDataset, key_name="dct_description", keyed=False)

        self._normalize_inlined_as_dict(slot_name="adms_sample", slot_type=DcatDistribution, key_name="dcat_accessURL", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class DcatDistribution(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Distribution"]
    class_class_curie: ClassVar[str] = "dcat:Distribution"
    class_name: ClassVar[str] = "dcat_Distribution"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/DcatDistribution")

    dcat_accessURL: Union[Union[dict, "RdfsResource"], List[Union[dict, "RdfsResource"]]] = None
    dcatap_availability: Optional[Union[dict, "SkosConcept"]] = None
    dct_description: Optional[Union[Union[dict, "RdfsLiteral"], List[Union[dict, "RdfsLiteral"]]]] = empty_list()
    dct_format: Optional[Union[dict, "DctMediaTypeOrExtent"]] = None
    adms_status: Optional[Union[dict, "SkosConcept"]] = None
    dcat_byteSize: Optional[Union[dict, "XsdNonNegativInteger"]] = None
    dcat_compressFormat: Optional[Union[dict, "DctMediaType"]] = None
    dcat_downloadURL: Optional[Union[Union[dict, "RdfsResource"], List[Union[dict, "RdfsResource"]]]] = empty_list()
    dcat_mediaType: Optional[Union[dict, "DctMediaType"]] = None
    dcat_packageFormat: Optional[Union[dict, "DctMediaType"]] = None
    dcat_spatialResolutionInMeters: Optional[Union[Union[dict, "XsdDecimal"], List[Union[dict, "XsdDecimal"]]]] = empty_list()
    dcat_temporalResolution: Optional[Union[Union[dict, "XsdDuration"], List[Union[dict, "XsdDuration"]]]] = empty_list()
    dct_conformsTo: Optional[Union[Union[dict, "DctStandard"], List[Union[dict, "DctStandard"]]]] = empty_list()
    dct_issued: Optional[str] = None
    dct_language: Optional[Union[Union[dict, "DctLinguisticSystem"], List[Union[dict, "DctLinguisticSystem"]]]] = empty_list()
    dct_modified: Optional[str] = None
    dct_rights: Optional[Union[dict, "DctRightsStatement"]] = None
    dct_title: Optional[Union[Union[dict, "RdfsLiteral"], List[Union[dict, "RdfsLiteral"]]]] = empty_list()
    foaf_page: Optional[Union[Union[dict, "FoafDocument"], List[Union[dict, "FoafDocument"]]]] = empty_list()
    odrl_hasPolicy: Optional[Union[dict, "OdrlHasPolicy"]] = None
    spdx_checksum: Optional[Union[dict, "SpdxChecksum"]] = None
    dct_license: Optional[Union[dict, "DctLicenseDocument"]] = None
    dcat_accessesService: Optional[Union[Union[dict, "DcatDataService"], List[Union[dict, "DcatDataService"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.dcat_accessURL):
            self.MissingRequiredField("dcat_accessURL")
        if not isinstance(self.dcat_accessURL, list):
            self.dcat_accessURL = [self.dcat_accessURL] if self.dcat_accessURL is not None else []
        self.dcat_accessURL = [v if isinstance(v, RdfsResource) else RdfsResource(**as_dict(v)) for v in self.dcat_accessURL]

        if self.dcatap_availability is not None and not isinstance(self.dcatap_availability, SkosConcept):
            self.dcatap_availability = SkosConcept()

        if not isinstance(self.dct_description, list):
            self.dct_description = [self.dct_description] if self.dct_description is not None else []
        self.dct_description = [v if isinstance(v, RdfsLiteral) else RdfsLiteral(**as_dict(v)) for v in self.dct_description]

        if self.dct_format is not None and not isinstance(self.dct_format, DctMediaTypeOrExtent):
            self.dct_format = DctMediaTypeOrExtent()

        if self.adms_status is not None and not isinstance(self.adms_status, SkosConcept):
            self.adms_status = SkosConcept()

        if self.dcat_byteSize is not None and not isinstance(self.dcat_byteSize, XsdNonNegativInteger):
            self.dcat_byteSize = XsdNonNegativInteger()

        if self.dcat_compressFormat is not None and not isinstance(self.dcat_compressFormat, DctMediaType):
            self.dcat_compressFormat = DctMediaType()

        if not isinstance(self.dcat_downloadURL, list):
            self.dcat_downloadURL = [self.dcat_downloadURL] if self.dcat_downloadURL is not None else []
        self.dcat_downloadURL = [v if isinstance(v, RdfsResource) else RdfsResource(**as_dict(v)) for v in self.dcat_downloadURL]

        if self.dcat_mediaType is not None and not isinstance(self.dcat_mediaType, DctMediaType):
            self.dcat_mediaType = DctMediaType()

        if self.dcat_packageFormat is not None and not isinstance(self.dcat_packageFormat, DctMediaType):
            self.dcat_packageFormat = DctMediaType()

        if not isinstance(self.dcat_spatialResolutionInMeters, list):
            self.dcat_spatialResolutionInMeters = [self.dcat_spatialResolutionInMeters] if self.dcat_spatialResolutionInMeters is not None else []
        self.dcat_spatialResolutionInMeters = [v if isinstance(v, XsdDecimal) else XsdDecimal(**as_dict(v)) for v in self.dcat_spatialResolutionInMeters]

        if not isinstance(self.dcat_temporalResolution, list):
            self.dcat_temporalResolution = [self.dcat_temporalResolution] if self.dcat_temporalResolution is not None else []
        self.dcat_temporalResolution = [v if isinstance(v, XsdDuration) else XsdDuration(**as_dict(v)) for v in self.dcat_temporalResolution]

        if not isinstance(self.dct_conformsTo, list):
            self.dct_conformsTo = [self.dct_conformsTo] if self.dct_conformsTo is not None else []
        self.dct_conformsTo = [v if isinstance(v, DctStandard) else DctStandard(**as_dict(v)) for v in self.dct_conformsTo]

        if self.dct_issued is not None and not isinstance(self.dct_issued, str):
            self.dct_issued = str(self.dct_issued)

        if not isinstance(self.dct_language, list):
            self.dct_language = [self.dct_language] if self.dct_language is not None else []
        self.dct_language = [v if isinstance(v, DctLinguisticSystem) else DctLinguisticSystem(**as_dict(v)) for v in self.dct_language]

        if self.dct_modified is not None and not isinstance(self.dct_modified, str):
            self.dct_modified = str(self.dct_modified)

        if self.dct_rights is not None and not isinstance(self.dct_rights, DctRightsStatement):
            self.dct_rights = DctRightsStatement()

        if not isinstance(self.dct_title, list):
            self.dct_title = [self.dct_title] if self.dct_title is not None else []
        self.dct_title = [v if isinstance(v, RdfsLiteral) else RdfsLiteral(**as_dict(v)) for v in self.dct_title]

        if not isinstance(self.foaf_page, list):
            self.foaf_page = [self.foaf_page] if self.foaf_page is not None else []
        self.foaf_page = [v if isinstance(v, FoafDocument) else FoafDocument(**as_dict(v)) for v in self.foaf_page]

        if self.odrl_hasPolicy is not None and not isinstance(self.odrl_hasPolicy, OdrlHasPolicy):
            self.odrl_hasPolicy = OdrlHasPolicy()

        if self.spdx_checksum is not None and not isinstance(self.spdx_checksum, SpdxChecksum):
            self.spdx_checksum = SpdxChecksum()

        if self.dct_license is not None and not isinstance(self.dct_license, DctLicenseDocument):
            self.dct_license = DctLicenseDocument(**as_dict(self.dct_license))

        self._normalize_inlined_as_dict(slot_name="dcat_accessesService", slot_type=DcatDataService, key_name="dcat_endpointURL", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class DcatCatalog(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Catalog"]
    class_class_curie: ClassVar[str] = "dcat:Catalog"
    class_name: ClassVar[str] = "dcat_Catalog"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/DcatCatalog")

    dct_description: Union[Union[dict, "RdfsLiteral"], List[Union[dict, "RdfsLiteral"]]] = None
    dct_title: Union[Union[dict, "RdfsLiteral"], List[Union[dict, "RdfsLiteral"]]] = None
    dct_publisher: Union[dict, "FoafAgent"] = None
    dcat_themeTaxonomy: Optional[Union[Union[dict, "SkosConcept"], List[Union[dict, "SkosConcept"]]]] = empty_list()
    dct_issued: Optional[str] = None
    dct_language: Optional[Union[Union[dict, "DctLinguisticSystem"], List[Union[dict, "DctLinguisticSystem"]]]] = empty_list()
    dct_modified: Optional[str] = None
    foaf_homepage: Optional[Union[dict, "FoafDocument"]] = None
    dct_rights: Optional[Union[dict, "DctRightsStatement"]] = None
    dct_license: Optional[Union[dict, "DctLicenseDocument"]] = None
    dcat_service: Optional[Union[Union[dict, "DcatDataService"], List[Union[dict, "DcatDataService"]]]] = empty_list()
    dct_spatial: Optional[Union[Union[dict, "DctLocation"], List[Union[dict, "DctLocation"]]]] = empty_list()
    dcat_dataset: Optional[Union[Union[dict, DcatDataset], List[Union[dict, DcatDataset]]]] = empty_list()
    dcat_catalog: Optional[Union[Union[dict, "DcatCatalog"], List[Union[dict, "DcatCatalog"]]]] = empty_list()
    dct_hasPart: Optional[Union[Union[dict, "DcatCatalog"], List[Union[dict, "DcatCatalog"]]]] = empty_list()
    dct_isPart: Optional[Union[dict, "DcatCatalog"]] = None
    dct_temporal: Optional[Union[Union[dict, "DctPeriodOfTime"], List[Union[dict, "DctPeriodOfTime"]]]] = empty_list()
    dcat_record: Optional[Union[Union[dict, "DcatCatalogRecord"], List[Union[dict, "DcatCatalogRecord"]]]] = empty_list()
    dct_creator: Optional[Union[dict, "FoafAgent"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.dct_description):
            self.MissingRequiredField("dct_description")
        if not isinstance(self.dct_description, list):
            self.dct_description = [self.dct_description] if self.dct_description is not None else []
        self.dct_description = [v if isinstance(v, RdfsLiteral) else RdfsLiteral(**as_dict(v)) for v in self.dct_description]

        if self._is_empty(self.dct_title):
            self.MissingRequiredField("dct_title")
        if not isinstance(self.dct_title, list):
            self.dct_title = [self.dct_title] if self.dct_title is not None else []
        self.dct_title = [v if isinstance(v, RdfsLiteral) else RdfsLiteral(**as_dict(v)) for v in self.dct_title]

        if self._is_empty(self.dct_publisher):
            self.MissingRequiredField("dct_publisher")
        if not isinstance(self.dct_publisher, FoafAgent):
            self.dct_publisher = FoafAgent(**as_dict(self.dct_publisher))

        if not isinstance(self.dcat_themeTaxonomy, list):
            self.dcat_themeTaxonomy = [self.dcat_themeTaxonomy] if self.dcat_themeTaxonomy is not None else []
        self.dcat_themeTaxonomy = [v if isinstance(v, SkosConcept) else SkosConcept(**as_dict(v)) for v in self.dcat_themeTaxonomy]

        if self.dct_issued is not None and not isinstance(self.dct_issued, str):
            self.dct_issued = str(self.dct_issued)

        if not isinstance(self.dct_language, list):
            self.dct_language = [self.dct_language] if self.dct_language is not None else []
        self.dct_language = [v if isinstance(v, DctLinguisticSystem) else DctLinguisticSystem(**as_dict(v)) for v in self.dct_language]

        if self.dct_modified is not None and not isinstance(self.dct_modified, str):
            self.dct_modified = str(self.dct_modified)

        if self.foaf_homepage is not None and not isinstance(self.foaf_homepage, FoafDocument):
            self.foaf_homepage = FoafDocument()

        if self.dct_rights is not None and not isinstance(self.dct_rights, DctRightsStatement):
            self.dct_rights = DctRightsStatement()

        if self.dct_license is not None and not isinstance(self.dct_license, DctLicenseDocument):
            self.dct_license = DctLicenseDocument(**as_dict(self.dct_license))

        self._normalize_inlined_as_dict(slot_name="dcat_service", slot_type=DcatDataService, key_name="dcat_endpointURL", keyed=False)

        if not isinstance(self.dct_spatial, list):
            self.dct_spatial = [self.dct_spatial] if self.dct_spatial is not None else []
        self.dct_spatial = [v if isinstance(v, DctLocation) else DctLocation(**as_dict(v)) for v in self.dct_spatial]

        self._normalize_inlined_as_dict(slot_name="dcat_dataset", slot_type=DcatDataset, key_name="dct_description", keyed=False)

        self._normalize_inlined_as_dict(slot_name="dcat_catalog", slot_type=DcatCatalog, key_name="dct_description", keyed=False)

        self._normalize_inlined_as_dict(slot_name="dct_hasPart", slot_type=DcatCatalog, key_name="dct_description", keyed=False)

        if self.dct_isPart is not None and not isinstance(self.dct_isPart, DcatCatalog):
            self.dct_isPart = DcatCatalog(**as_dict(self.dct_isPart))

        if not isinstance(self.dct_temporal, list):
            self.dct_temporal = [self.dct_temporal] if self.dct_temporal is not None else []
        self.dct_temporal = [v if isinstance(v, DctPeriodOfTime) else DctPeriodOfTime(**as_dict(v)) for v in self.dct_temporal]

        self._normalize_inlined_as_dict(slot_name="dcat_record", slot_type=DcatCatalogRecord, key_name="dct_modified", keyed=False)

        if self.dct_creator is not None and not isinstance(self.dct_creator, FoafAgent):
            self.dct_creator = FoafAgent(**as_dict(self.dct_creator))

        super().__post_init__(**kwargs)


@dataclass
class DctLicenseDocument(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["LicenseDocument"]
    class_class_curie: ClassVar[str] = "dct:LicenseDocument"
    class_name: ClassVar[str] = "dct_LicenseDocument"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/DctLicenseDocument")

    dct_type: Optional[Union[Union[dict, "SkosConcept"], List[Union[dict, "SkosConcept"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.dct_type, list):
            self.dct_type = [self.dct_type] if self.dct_type is not None else []
        self.dct_type = [v if isinstance(v, SkosConcept) else SkosConcept(**as_dict(v)) for v in self.dct_type]

        super().__post_init__(**kwargs)


@dataclass
class DcatDataService(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["DataService"]
    class_class_curie: ClassVar[str] = "dcat:DataService"
    class_name: ClassVar[str] = "dcat_DataService"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/DcatDataService")

    dcat_endpointURL: Union[Union[dict, "RdfsResource"], List[Union[dict, "RdfsResource"]]] = None
    dct_title: Union[Union[dict, "RdfsLiteral"], List[Union[dict, "RdfsLiteral"]]] = None
    dcat_endpointDescription: Optional[Union[Union[dict, "RdfsResource"], List[Union[dict, "RdfsResource"]]]] = empty_list()
    dct_accessRights: Optional[Union[dict, "DctRightsStatement"]] = None
    dct_description: Optional[Union[Union[dict, "RdfsLiteral"], List[Union[dict, "RdfsLiteral"]]]] = empty_list()
    dct_format: Optional[Union[Union[dict, "DctMediaTypeOrExtent"], List[Union[dict, "DctMediaTypeOrExtent"]]]] = empty_list()
    dcat_servesDataset: Optional[Union[Union[dict, DcatDataset], List[Union[dict, DcatDataset]]]] = empty_list()
    dct_license: Optional[Union[dict, DctLicenseDocument]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.dcat_endpointURL):
            self.MissingRequiredField("dcat_endpointURL")
        if not isinstance(self.dcat_endpointURL, list):
            self.dcat_endpointURL = [self.dcat_endpointURL] if self.dcat_endpointURL is not None else []
        self.dcat_endpointURL = [v if isinstance(v, RdfsResource) else RdfsResource(**as_dict(v)) for v in self.dcat_endpointURL]

        if self._is_empty(self.dct_title):
            self.MissingRequiredField("dct_title")
        if not isinstance(self.dct_title, list):
            self.dct_title = [self.dct_title] if self.dct_title is not None else []
        self.dct_title = [v if isinstance(v, RdfsLiteral) else RdfsLiteral(**as_dict(v)) for v in self.dct_title]

        if not isinstance(self.dcat_endpointDescription, list):
            self.dcat_endpointDescription = [self.dcat_endpointDescription] if self.dcat_endpointDescription is not None else []
        self.dcat_endpointDescription = [v if isinstance(v, RdfsResource) else RdfsResource(**as_dict(v)) for v in self.dcat_endpointDescription]

        if self.dct_accessRights is not None and not isinstance(self.dct_accessRights, DctRightsStatement):
            self.dct_accessRights = DctRightsStatement()

        if not isinstance(self.dct_description, list):
            self.dct_description = [self.dct_description] if self.dct_description is not None else []
        self.dct_description = [v if isinstance(v, RdfsLiteral) else RdfsLiteral(**as_dict(v)) for v in self.dct_description]

        if not isinstance(self.dct_format, list):
            self.dct_format = [self.dct_format] if self.dct_format is not None else []
        self.dct_format = [v if isinstance(v, DctMediaTypeOrExtent) else DctMediaTypeOrExtent(**as_dict(v)) for v in self.dct_format]

        self._normalize_inlined_as_dict(slot_name="dcat_servesDataset", slot_type=DcatDataset, key_name="dct_description", keyed=False)

        if self.dct_license is not None and not isinstance(self.dct_license, DctLicenseDocument):
            self.dct_license = DctLicenseDocument(**as_dict(self.dct_license))

        super().__post_init__(**kwargs)


@dataclass
class DcatCatalogRecord(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["CatalogRecord"]
    class_class_curie: ClassVar[str] = "dcat:CatalogRecord"
    class_name: ClassVar[str] = "dcat_CatalogRecord"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/DcatCatalogRecord")

    dct_modified: str = None
    foaf_primaryTopic: Union[dict, "DcatResource"] = None
    adms_status: Optional[Union[dict, "SkosConcept"]] = None
    dct_conformsTo: Optional[Union[Union[dict, "DctStandard"], List[Union[dict, "DctStandard"]]]] = empty_list()
    dct_issued: Optional[str] = None
    dct_description: Optional[Union[Union[dict, "RdfsLiteral"], List[Union[dict, "RdfsLiteral"]]]] = empty_list()
    dct_language: Optional[Union[Union[dict, "DctLinguisticSystem"], List[Union[dict, "DctLinguisticSystem"]]]] = empty_list()
    dct_title: Optional[Union[Union[dict, "RdfsLiteral"], List[Union[dict, "RdfsLiteral"]]]] = empty_list()
    dct_source: Optional[Union[dict, "DcatCatalogRecord"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.dct_modified):
            self.MissingRequiredField("dct_modified")
        if not isinstance(self.dct_modified, str):
            self.dct_modified = str(self.dct_modified)

        if self._is_empty(self.foaf_primaryTopic):
            self.MissingRequiredField("foaf_primaryTopic")
        if not isinstance(self.foaf_primaryTopic, DcatResource):
            self.foaf_primaryTopic = DcatResource()

        if self.adms_status is not None and not isinstance(self.adms_status, SkosConcept):
            self.adms_status = SkosConcept()

        if not isinstance(self.dct_conformsTo, list):
            self.dct_conformsTo = [self.dct_conformsTo] if self.dct_conformsTo is not None else []
        self.dct_conformsTo = [v if isinstance(v, DctStandard) else DctStandard(**as_dict(v)) for v in self.dct_conformsTo]

        if self.dct_issued is not None and not isinstance(self.dct_issued, str):
            self.dct_issued = str(self.dct_issued)

        if not isinstance(self.dct_description, list):
            self.dct_description = [self.dct_description] if self.dct_description is not None else []
        self.dct_description = [v if isinstance(v, RdfsLiteral) else RdfsLiteral(**as_dict(v)) for v in self.dct_description]

        if not isinstance(self.dct_language, list):
            self.dct_language = [self.dct_language] if self.dct_language is not None else []
        self.dct_language = [v if isinstance(v, DctLinguisticSystem) else DctLinguisticSystem(**as_dict(v)) for v in self.dct_language]

        if not isinstance(self.dct_title, list):
            self.dct_title = [self.dct_title] if self.dct_title is not None else []
        self.dct_title = [v if isinstance(v, RdfsLiteral) else RdfsLiteral(**as_dict(v)) for v in self.dct_title]

        if self.dct_source is not None and not isinstance(self.dct_source, DcatCatalogRecord):
            self.dct_source = DcatCatalogRecord(**as_dict(self.dct_source))

        super().__post_init__(**kwargs)


@dataclass
class DctLocation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["Location"]
    class_class_curie: ClassVar[str] = "dct:Location"
    class_name: ClassVar[str] = "dct_Location"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/DctLocation")

    dcat_bbox: Optional[Union[dict, "RdfsLiteral"]] = None
    dcat_centroid: Optional[Union[dict, "RdfsLiteral"]] = None
    lcon_geometry: Optional[Union[dict, "LconGeometry"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.dcat_bbox is not None and not isinstance(self.dcat_bbox, RdfsLiteral):
            self.dcat_bbox = RdfsLiteral()

        if self.dcat_centroid is not None and not isinstance(self.dcat_centroid, RdfsLiteral):
            self.dcat_centroid = RdfsLiteral()

        if self.lcon_geometry is not None and not isinstance(self.lcon_geometry, LconGeometry):
            self.lcon_geometry = LconGeometry()

        super().__post_init__(**kwargs)


@dataclass
class DctPeriodOfTime(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["PeriodOfTime"]
    class_class_curie: ClassVar[str] = "dct:PeriodOfTime"
    class_name: ClassVar[str] = "dct_PeriodOfTime"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/DctPeriodOfTime")

    dcat_endDate: Optional[str] = None
    dcat_startDate: Optional[str] = None
    time_hasBeginning: Optional[str] = None
    time_hasEnd: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.dcat_endDate is not None and not isinstance(self.dcat_endDate, str):
            self.dcat_endDate = str(self.dcat_endDate)

        if self.dcat_startDate is not None and not isinstance(self.dcat_startDate, str):
            self.dcat_startDate = str(self.dcat_startDate)

        if self.time_hasBeginning is not None and not isinstance(self.time_hasBeginning, str):
            self.time_hasBeginning = str(self.time_hasBeginning)

        if self.time_hasEnd is not None and not isinstance(self.time_hasEnd, str):
            self.time_hasEnd = str(self.time_hasEnd)

        super().__post_init__(**kwargs)


@dataclass
class FoafAgent(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF["agent"]
    class_class_curie: ClassVar[str] = "foaf:agent"
    class_name: ClassVar[str] = "foaf_agent"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/FoafAgent")

    foaf_name: Union[Union[dict, "RdfsLiteral"], List[Union[dict, "RdfsLiteral"]]] = None
    dct_type: Optional[Union[dict, "SkosConcept"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.foaf_name):
            self.MissingRequiredField("foaf_name")
        if not isinstance(self.foaf_name, list):
            self.foaf_name = [self.foaf_name] if self.foaf_name is not None else []
        self.foaf_name = [v if isinstance(v, RdfsLiteral) else RdfsLiteral(**as_dict(v)) for v in self.foaf_name]

        if self.dct_type is not None and not isinstance(self.dct_type, SkosConcept):
            self.dct_type = SkosConcept()

        super().__post_init__(**kwargs)


@dataclass
class DatasetinSeries(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCATAP["DatasetinSeries"]
    class_class_curie: ClassVar[str] = "dcatap:DatasetinSeries"
    class_name: ClassVar[str] = "DatasetinSeries"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/DatasetinSeries")

    dct_description: Union[Union[dict, "RdfsLiteral"], List[Union[dict, "RdfsLiteral"]]] = None
    dct_title: Union[Union[dict, "RdfsLiteral"], List[Union[dict, "RdfsLiteral"]]] = None
    dct_accuralPeriodicity: Optional[Union[Union[dict, "DctFrequency"], List[Union[dict, "DctFrequency"]]]] = empty_list()
    dcat_prev: Optional[Union[Union[dict, "DatasetinSeries"], List[Union[dict, "DatasetinSeries"]]]] = empty_list()
    dcat_next: Optional[Union[Union[dict, "DatasetinSeries"], List[Union[dict, "DatasetinSeries"]]]] = empty_list()
    dcat_inSeries: Optional[Union[Union[dict, "DcatDatasetSeries"], List[Union[dict, "DcatDatasetSeries"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.dct_description):
            self.MissingRequiredField("dct_description")
        if not isinstance(self.dct_description, list):
            self.dct_description = [self.dct_description] if self.dct_description is not None else []
        self.dct_description = [v if isinstance(v, RdfsLiteral) else RdfsLiteral(**as_dict(v)) for v in self.dct_description]

        if self._is_empty(self.dct_title):
            self.MissingRequiredField("dct_title")
        if not isinstance(self.dct_title, list):
            self.dct_title = [self.dct_title] if self.dct_title is not None else []
        self.dct_title = [v if isinstance(v, RdfsLiteral) else RdfsLiteral(**as_dict(v)) for v in self.dct_title]

        if not isinstance(self.dct_accuralPeriodicity, list):
            self.dct_accuralPeriodicity = [self.dct_accuralPeriodicity] if self.dct_accuralPeriodicity is not None else []
        self.dct_accuralPeriodicity = [v if isinstance(v, DctFrequency) else DctFrequency(**as_dict(v)) for v in self.dct_accuralPeriodicity]

        self._normalize_inlined_as_dict(slot_name="dcat_prev", slot_type=DatasetinSeries, key_name="dct_description", keyed=False)

        self._normalize_inlined_as_dict(slot_name="dcat_next", slot_type=DatasetinSeries, key_name="dct_description", keyed=False)

        self._normalize_inlined_as_dict(slot_name="dcat_inSeries", slot_type=DcatDatasetSeries, key_name="dct_description", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class DcatDatasetSeries(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["DatasetSeries"]
    class_class_curie: ClassVar[str] = "dcat:DatasetSeries"
    class_name: ClassVar[str] = "dcat_DatasetSeries"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/DcatDatasetSeries")

    dct_description: Union[Union[dict, "RdfsLiteral"], List[Union[dict, "RdfsLiteral"]]] = None
    dct_title: Union[Union[dict, "RdfsLiteral"], List[Union[dict, "RdfsLiteral"]]] = None
    dcat_contactPoint: Optional[Union[Union[dict, "VcardKind"], List[Union[dict, "VcardKind"]]]] = empty_list()
    dct_accuralPeriodicity: Optional[Union[dict, "DctFrequency"]] = None
    dct_issued: Optional[str] = None
    dct_modified: Optional[str] = None
    dct_spatial: Optional[Union[Union[dict, DctLocation], List[Union[dict, DctLocation]]]] = empty_list()
    dct_temporal: Optional[Union[Union[dict, DctPeriodOfTime], List[Union[dict, DctPeriodOfTime]]]] = empty_list()
    dct_publisher: Optional[Union[dict, FoafAgent]] = None
    dcat_seriesMember: Optional[Union[Union[dict, DatasetinSeries], List[Union[dict, DatasetinSeries]]]] = empty_list()
    dcat_first: Optional[Union[Union[dict, DatasetinSeries], List[Union[dict, DatasetinSeries]]]] = empty_list()
    dcat_last: Optional[Union[Union[dict, DatasetinSeries], List[Union[dict, DatasetinSeries]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.dct_description):
            self.MissingRequiredField("dct_description")
        if not isinstance(self.dct_description, list):
            self.dct_description = [self.dct_description] if self.dct_description is not None else []
        self.dct_description = [v if isinstance(v, RdfsLiteral) else RdfsLiteral(**as_dict(v)) for v in self.dct_description]

        if self._is_empty(self.dct_title):
            self.MissingRequiredField("dct_title")
        if not isinstance(self.dct_title, list):
            self.dct_title = [self.dct_title] if self.dct_title is not None else []
        self.dct_title = [v if isinstance(v, RdfsLiteral) else RdfsLiteral(**as_dict(v)) for v in self.dct_title]

        if not isinstance(self.dcat_contactPoint, list):
            self.dcat_contactPoint = [self.dcat_contactPoint] if self.dcat_contactPoint is not None else []
        self.dcat_contactPoint = [v if isinstance(v, VcardKind) else VcardKind(**as_dict(v)) for v in self.dcat_contactPoint]

        if self.dct_accuralPeriodicity is not None and not isinstance(self.dct_accuralPeriodicity, DctFrequency):
            self.dct_accuralPeriodicity = DctFrequency()

        if self.dct_issued is not None and not isinstance(self.dct_issued, str):
            self.dct_issued = str(self.dct_issued)

        if self.dct_modified is not None and not isinstance(self.dct_modified, str):
            self.dct_modified = str(self.dct_modified)

        if not isinstance(self.dct_spatial, list):
            self.dct_spatial = [self.dct_spatial] if self.dct_spatial is not None else []
        self.dct_spatial = [v if isinstance(v, DctLocation) else DctLocation(**as_dict(v)) for v in self.dct_spatial]

        if not isinstance(self.dct_temporal, list):
            self.dct_temporal = [self.dct_temporal] if self.dct_temporal is not None else []
        self.dct_temporal = [v if isinstance(v, DctPeriodOfTime) else DctPeriodOfTime(**as_dict(v)) for v in self.dct_temporal]

        if self.dct_publisher is not None and not isinstance(self.dct_publisher, FoafAgent):
            self.dct_publisher = FoafAgent(**as_dict(self.dct_publisher))

        self._normalize_inlined_as_dict(slot_name="dcat_seriesMember", slot_type=DatasetinSeries, key_name="dct_description", keyed=False)

        self._normalize_inlined_as_dict(slot_name="dcat_first", slot_type=DatasetinSeries, key_name="dct_description", keyed=False)

        self._normalize_inlined_as_dict(slot_name="dcat_last", slot_type=DatasetinSeries, key_name="dct_description", keyed=False)

        super().__post_init__(**kwargs)


class DcatResource(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Resource"]
    class_class_curie: ClassVar[str] = "dcat:Resource"
    class_name: ClassVar[str] = "dcat_Resource"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/DcatResource")


class RdfsLiteral(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDFS["Literal"]
    class_class_curie: ClassVar[str] = "rdfs:Literal"
    class_name: ClassVar[str] = "rdfs_Literal"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/RdfsLiteral")


class VcardKind(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VCARD["Kind"]
    class_class_curie: ClassVar[str] = "vcard:Kind"
    class_name: ClassVar[str] = "vcard_Kind"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/VcardKind")


class SkosConcept(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS["Concept"]
    class_class_curie: ClassVar[str] = "skos:Concept"
    class_name: ClassVar[str] = "skos_Concept"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/SkosConcept")


class AdmsIdentifier(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ADMS["identifier"]
    class_class_curie: ClassVar[str] = "adms:identifier"
    class_name: ClassVar[str] = "adms_Identifier"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/AdmsIdentifier")


class FoafDocument(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF["Document"]
    class_class_curie: ClassVar[str] = "foaf:Document"
    class_name: ClassVar[str] = "foaf_Document"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/FoafDocument")


class DcatRelationship(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Relationship"]
    class_class_curie: ClassVar[str] = "dcat:Relationship"
    class_name: ClassVar[str] = "dcat_Relationship"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/DcatRelationship")


class XsdDecimal(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = XSD["decimal"]
    class_class_curie: ClassVar[str] = "xsd:decimal"
    class_name: ClassVar[str] = "xsd_decimal"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/XsdDecimal")


class XsdDuration(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = XSD["duration"]
    class_class_curie: ClassVar[str] = "xsd:duration"
    class_name: ClassVar[str] = "xsd_duration"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/XsdDuration")


class DctFrequency(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["Frequency"]
    class_class_curie: ClassVar[str] = "dct:Frequency"
    class_name: ClassVar[str] = "dct_Frequency"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/DctFrequency")


class DctStandard(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["Standard"]
    class_class_curie: ClassVar[str] = "dct:Standard"
    class_name: ClassVar[str] = "dct_Standard"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/DctStandard")


class RdfsResource(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDFS["Resource"]
    class_class_curie: ClassVar[str] = "rdfs:Resource"
    class_name: ClassVar[str] = "rdfs_Resource"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/RdfsResource")


class DctLinguisticSystem(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["LinguisticSystem"]
    class_class_curie: ClassVar[str] = "dct:LinguisticSystem"
    class_name: ClassVar[str] = "dct_LinguisticSystem"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/DctLinguisticSystem")


class DctProvenanceStatement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["ProvenanceStatement"]
    class_class_curie: ClassVar[str] = "dct:ProvenanceStatement"
    class_name: ClassVar[str] = "dct_ProvenanceStatement"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/DctProvenanceStatement")


class ProvAttribution(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Attribution"]
    class_class_curie: ClassVar[str] = "prov:Attribution"
    class_name: ClassVar[str] = "prov_Attribution"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/ProvAttribution")


class ProvActivity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Activity"]
    class_class_curie: ClassVar[str] = "prov:Activity"
    class_name: ClassVar[str] = "prov_Activity"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/ProvActivity")


class DctMediaTypeOrExtent(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["MediaTypeOrExtent"]
    class_class_curie: ClassVar[str] = "dct:MediaTypeOrExtent"
    class_name: ClassVar[str] = "dct_MediaTypeOrExtent"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/DctMediaTypeOrExtent")


class XsdNonNegativInteger(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = XSD["nonNegativeInteger"]
    class_class_curie: ClassVar[str] = "xsd:nonNegativeInteger"
    class_name: ClassVar[str] = "xsd_nonNegativInteger"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/XsdNonNegativInteger")


class DctMediaType(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["MediaType"]
    class_class_curie: ClassVar[str] = "dct:MediaType"
    class_name: ClassVar[str] = "dct_MediaType"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/DctMediaType")


class DctRightsStatement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["RightsStatement"]
    class_class_curie: ClassVar[str] = "dct:RightsStatement"
    class_name: ClassVar[str] = "dct_RightsStatement"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/DctRightsStatement")


class OdrlHasPolicy(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODRL["hasPolicy"]
    class_class_curie: ClassVar[str] = "odrl:hasPolicy"
    class_name: ClassVar[str] = "odrl_hasPolicy"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/OdrlHasPolicy")


class SpdxChecksum(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX["Checksum"]
    class_class_curie: ClassVar[str] = "spdx:Checksum"
    class_name: ClassVar[str] = "spdx_Checksum"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/SpdxChecksum")


class LconGeometry(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LCON["Geometry"]
    class_class_curie: ClassVar[str] = "lcon:Geometry"
    class_name: ClassVar[str] = "lcon_Geometry"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/LconGeometry")


class XsdDate(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = XSD["date"]
    class_class_curie: ClassVar[str] = "xsd:date"
    class_name: ClassVar[str] = "xsd_date"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/XsdDate")


class XsdDateTime(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = XSD["dateTime"]
    class_class_curie: ClassVar[str] = "xsd:dateTime"
    class_name: ClassVar[str] = "xsd_dateTime"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/XsdDateTime")


class XsdGYear(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = XSD["gYear"]
    class_class_curie: ClassVar[str] = "xsd:gYear"
    class_name: ClassVar[str] = "xsd_gYear"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/XsdGYear")


class XsdGYearMonth(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = XSD["gYearMonth"]
    class_class_curie: ClassVar[str] = "xsd:gYearMonth"
    class_name: ClassVar[str] = "xsd_gYearMonth"
    class_model_uri: ClassVar[URIRef] = URIRef("https://ndfi4cat.de/linkml/tests/DCATap/XsdGYearMonth")


# Enumerations


# Slots
class slots:
    pass

slots.dcatDataset__dct_description = Slot(uri=DCAT.description, name="dcatDataset__dct_description", curie=DCAT.curie('description'),
                   model_uri=DEFAULT_.dcatDataset__dct_description, domain=None, range=Union[Union[dict, RdfsLiteral], List[Union[dict, RdfsLiteral]]])

slots.dcatDataset__dct_title = Slot(uri=DCT.title, name="dcatDataset__dct_title", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.dcatDataset__dct_title, domain=None, range=Union[Union[dict, RdfsLiteral], List[Union[dict, RdfsLiteral]]])

slots.dcatDataset__dct_contactPoint = Slot(uri=DCT.contactPoint, name="dcatDataset__dct_contactPoint", curie=DCT.curie('contactPoint'),
                   model_uri=DEFAULT_.dcatDataset__dct_contactPoint, domain=None, range=Optional[Union[Union[dict, VcardKind], List[Union[dict, VcardKind]]]])

slots.dcatDataset__dct_keyword = Slot(uri=DCT.keyword, name="dcatDataset__dct_keyword", curie=DCT.curie('keyword'),
                   model_uri=DEFAULT_.dcatDataset__dct_keyword, domain=None, range=Optional[Union[Union[dict, RdfsLiteral], List[Union[dict, RdfsLiteral]]]])

slots.dcatDataset__dct_theme = Slot(uri=DCT.theme, name="dcatDataset__dct_theme", curie=DCT.curie('theme'),
                   model_uri=DEFAULT_.dcatDataset__dct_theme, domain=None, range=Optional[Union[Union[dict, SkosConcept], List[Union[dict, SkosConcept]]]])

slots.dcatDataset__adms_identifier = Slot(uri=ADMS.identifier, name="dcatDataset__adms_identifier", curie=ADMS.curie('identifier'),
                   model_uri=DEFAULT_.dcatDataset__adms_identifier, domain=None, range=Optional[Union[Union[dict, AdmsIdentifier], List[Union[dict, AdmsIdentifier]]]])

slots.dcatDataset__adms_versionNotes = Slot(uri=ADMS.versionNotes, name="dcatDataset__adms_versionNotes", curie=ADMS.curie('versionNotes'),
                   model_uri=DEFAULT_.dcatDataset__adms_versionNotes, domain=None, range=Optional[Union[Union[dict, RdfsLiteral], List[Union[dict, RdfsLiteral]]]])

slots.dcatDataset__dcat_landingPage = Slot(uri=DCAT.landingPage, name="dcatDataset__dcat_landingPage", curie=DCAT.curie('landingPage'),
                   model_uri=DEFAULT_.dcatDataset__dcat_landingPage, domain=None, range=Optional[Union[Union[dict, FoafDocument], List[Union[dict, FoafDocument]]]])

slots.dcatDataset__dcat_qualifiedRelation = Slot(uri=DCAT.qualifiedRelation, name="dcatDataset__dcat_qualifiedRelation", curie=DCAT.curie('qualifiedRelation'),
                   model_uri=DEFAULT_.dcatDataset__dcat_qualifiedRelation, domain=None, range=Optional[Union[Union[dict, DcatRelationship], List[Union[dict, DcatRelationship]]]])

slots.dcatDataset__dcat_spatialResolutionInMeters = Slot(uri=DCAT.spatialResolutionInMeters, name="dcatDataset__dcat_spatialResolutionInMeters", curie=DCAT.curie('spatialResolutionInMeters'),
                   model_uri=DEFAULT_.dcatDataset__dcat_spatialResolutionInMeters, domain=None, range=Optional[Union[Union[dict, XsdDecimal], List[Union[dict, XsdDecimal]]]])

slots.dcatDataset__dcat_temporalResolution = Slot(uri=DCAT.temporalResolution, name="dcatDataset__dcat_temporalResolution", curie=DCAT.curie('temporalResolution'),
                   model_uri=DEFAULT_.dcatDataset__dcat_temporalResolution, domain=None, range=Optional[Union[Union[dict, XsdDuration], List[Union[dict, XsdDuration]]]])

slots.dcatDataset__dcat_version = Slot(uri=DCAT.version, name="dcatDataset__dcat_version", curie=DCAT.curie('version'),
                   model_uri=DEFAULT_.dcatDataset__dcat_version, domain=None, range=Optional[Union[Union[dict, RdfsLiteral], List[Union[dict, RdfsLiteral]]]])

slots.dcatDataset__dct_accessRights = Slot(uri=DCT.accessRights, name="dcatDataset__dct_accessRights", curie=DCT.curie('accessRights'),
                   model_uri=DEFAULT_.dcatDataset__dct_accessRights, domain=None, range=Optional[Union[dict, DctFrequency]])

slots.dcatDataset__dct_accuralPeriodicity = Slot(uri=DCT.accuralPeriodicity, name="dcatDataset__dct_accuralPeriodicity", curie=DCT.curie('accuralPeriodicity'),
                   model_uri=DEFAULT_.dcatDataset__dct_accuralPeriodicity, domain=None, range=Optional[Union[dict, DctFrequency]])

slots.dcatDataset__dct_conformsTo = Slot(uri=DCT.conformsTo, name="dcatDataset__dct_conformsTo", curie=DCT.curie('conformsTo'),
                   model_uri=DEFAULT_.dcatDataset__dct_conformsTo, domain=None, range=Optional[Union[Union[dict, DctStandard], List[Union[dict, DctStandard]]]])

slots.dcatDataset__dct_identifier = Slot(uri=DCT.identifier, name="dcatDataset__dct_identifier", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.dcatDataset__dct_identifier, domain=None, range=Optional[Union[Union[dict, RdfsLiteral], List[Union[dict, RdfsLiteral]]]])

slots.dcatDataset__dct_isReferencedBy = Slot(uri=DCT.isReferencedBy, name="dcatDataset__dct_isReferencedBy", curie=DCT.curie('isReferencedBy'),
                   model_uri=DEFAULT_.dcatDataset__dct_isReferencedBy, domain=None, range=Optional[Union[Union[dict, RdfsResource], List[Union[dict, RdfsResource]]]])

slots.dcatDataset__dct_issued = Slot(uri=DCT.issued, name="dcatDataset__dct_issued", curie=DCT.curie('issued'),
                   model_uri=DEFAULT_.dcatDataset__dct_issued, domain=None, range=Optional[str])

slots.dcatDataset__dct_language = Slot(uri=DCT.language, name="dcatDataset__dct_language", curie=DCT.curie('language'),
                   model_uri=DEFAULT_.dcatDataset__dct_language, domain=None, range=Optional[Union[Union[dict, DctLinguisticSystem], List[Union[dict, DctLinguisticSystem]]]])

slots.dcatDataset__dct_modified = Slot(uri=DCT.modified, name="dcatDataset__dct_modified", curie=DCT.curie('modified'),
                   model_uri=DEFAULT_.dcatDataset__dct_modified, domain=None, range=Optional[str])

slots.dcatDataset__dct_provenance = Slot(uri=DCT.provenance, name="dcatDataset__dct_provenance", curie=DCT.curie('provenance'),
                   model_uri=DEFAULT_.dcatDataset__dct_provenance, domain=None, range=Optional[Union[Union[dict, DctProvenanceStatement], List[Union[dict, DctProvenanceStatement]]]])

slots.dcatDataset__dct_relation = Slot(uri=DCT.relation, name="dcatDataset__dct_relation", curie=DCT.curie('relation'),
                   model_uri=DEFAULT_.dcatDataset__dct_relation, domain=None, range=Optional[Union[Union[dict, RdfsResource], List[Union[dict, RdfsResource]]]])

slots.dcatDataset__dct_type = Slot(uri=DCT.type, name="dcatDataset__dct_type", curie=DCT.curie('type'),
                   model_uri=DEFAULT_.dcatDataset__dct_type, domain=None, range=Optional[Union[dict, SkosConcept]])

slots.dcatDataset__foaf_page = Slot(uri=FOAF.page, name="dcatDataset__foaf_page", curie=FOAF.curie('page'),
                   model_uri=DEFAULT_.dcatDataset__foaf_page, domain=None, range=Optional[Union[Union[dict, FoafDocument], List[Union[dict, FoafDocument]]]])

slots.dcatDataset__owl_versionInfo = Slot(uri=OWL.versionInfo, name="dcatDataset__owl_versionInfo", curie=OWL.curie('versionInfo'),
                   model_uri=DEFAULT_.dcatDataset__owl_versionInfo, domain=None, range=Optional[Union[dict, RdfsLiteral]])

slots.dcatDataset__prov_qualifiedAttribution = Slot(uri=PROV.qualifiedAttribution, name="dcatDataset__prov_qualifiedAttribution", curie=PROV.curie('qualifiedAttribution'),
                   model_uri=DEFAULT_.dcatDataset__prov_qualifiedAttribution, domain=None, range=Optional[Union[Union[dict, ProvAttribution], List[Union[dict, ProvAttribution]]]])

slots.dcatDataset__prov_wasGeneratedBy = Slot(uri=PROV.wasGeneratedBy, name="dcatDataset__prov_wasGeneratedBy", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=DEFAULT_.dcatDataset__prov_wasGeneratedBy, domain=None, range=Optional[Union[Union[dict, ProvActivity], List[Union[dict, ProvActivity]]]])

slots.dcatDataset__dcat_themeTaxonomy = Slot(uri=DCAT.themeTaxonomy, name="dcatDataset__dcat_themeTaxonomy", curie=DCAT.curie('themeTaxonomy'),
                   model_uri=DEFAULT_.dcatDataset__dcat_themeTaxonomy, domain=None, range=Optional[Union[Union[dict, SkosConcept], List[Union[dict, SkosConcept]]]])

slots.dcatDataset__dct_spatial = Slot(uri=DCT.spatial, name="dcatDataset__dct_spatial", curie=DCT.curie('spatial'),
                   model_uri=DEFAULT_.dcatDataset__dct_spatial, domain=None, range=Optional[Union[Union[dict, DctLocation], List[Union[dict, DctLocation]]]])

slots.dcatDataset__dct_temporal = Slot(uri=DCT.temporal, name="dcatDataset__dct_temporal", curie=DCT.curie('temporal'),
                   model_uri=DEFAULT_.dcatDataset__dct_temporal, domain=None, range=Optional[Union[Union[dict, DctPeriodOfTime], List[Union[dict, DctPeriodOfTime]]]])

slots.dcatDataset__dct_publisher = Slot(uri=DCT.publisher, name="dcatDataset__dct_publisher", curie=DCT.curie('publisher'),
                   model_uri=DEFAULT_.dcatDataset__dct_publisher, domain=None, range=Optional[Union[dict, FoafAgent]])

slots.dcatDataset__dcat_distribution = Slot(uri=DCAT.distribution, name="dcatDataset__dcat_distribution", curie=DCAT.curie('distribution'),
                   model_uri=DEFAULT_.dcatDataset__dcat_distribution, domain=None, range=Optional[Union[Union[dict, DcatDistribution], List[Union[dict, DcatDistribution]]]])

slots.dcatDataset__dcat_hasVersion = Slot(uri=DCAT.hasVersion, name="dcatDataset__dcat_hasVersion", curie=DCAT.curie('hasVersion'),
                   model_uri=DEFAULT_.dcatDataset__dcat_hasVersion, domain=None, range=Optional[Union[Union[dict, DcatDataset], List[Union[dict, DcatDataset]]]])

slots.dcatDataset__dcat_isVersionOf = Slot(uri=DCAT.isVersionOf, name="dcatDataset__dcat_isVersionOf", curie=DCAT.curie('isVersionOf'),
                   model_uri=DEFAULT_.dcatDataset__dcat_isVersionOf, domain=None, range=Optional[Union[Union[dict, DcatDataset], List[Union[dict, DcatDataset]]]])

slots.dcatDataset__dct_source = Slot(uri=DCT.source, name="dcatDataset__dct_source", curie=DCT.curie('source'),
                   model_uri=DEFAULT_.dcatDataset__dct_source, domain=None, range=Optional[Union[Union[dict, DcatDataset], List[Union[dict, DcatDataset]]]])

slots.dcatDataset__adms_sample = Slot(uri=ADMS.sample, name="dcatDataset__adms_sample", curie=ADMS.curie('sample'),
                   model_uri=DEFAULT_.dcatDataset__adms_sample, domain=None, range=Optional[Union[Union[dict, DcatDistribution], List[Union[dict, DcatDistribution]]]])

slots.dcatDistribution__dcat_accessURL = Slot(uri=DCAT.accessURL, name="dcatDistribution__dcat_accessURL", curie=DCAT.curie('accessURL'),
                   model_uri=DEFAULT_.dcatDistribution__dcat_accessURL, domain=None, range=Union[Union[dict, RdfsResource], List[Union[dict, RdfsResource]]])

slots.dcatDistribution__dcatap_availability = Slot(uri=DCATAP.availability, name="dcatDistribution__dcatap_availability", curie=DCATAP.curie('availability'),
                   model_uri=DEFAULT_.dcatDistribution__dcatap_availability, domain=None, range=Optional[Union[dict, SkosConcept]])

slots.dcatDistribution__dct_description = Slot(uri=DCAT.description, name="dcatDistribution__dct_description", curie=DCAT.curie('description'),
                   model_uri=DEFAULT_.dcatDistribution__dct_description, domain=None, range=Optional[Union[Union[dict, RdfsLiteral], List[Union[dict, RdfsLiteral]]]])

slots.dcatDistribution__dct_format = Slot(uri=DCT.format, name="dcatDistribution__dct_format", curie=DCT.curie('format'),
                   model_uri=DEFAULT_.dcatDistribution__dct_format, domain=None, range=Optional[Union[dict, DctMediaTypeOrExtent]])

slots.dcatDistribution__adms_status = Slot(uri=ADMS.status, name="dcatDistribution__adms_status", curie=ADMS.curie('status'),
                   model_uri=DEFAULT_.dcatDistribution__adms_status, domain=None, range=Optional[Union[dict, SkosConcept]])

slots.dcatDistribution__dcat_byteSize = Slot(uri=DCAT.byteSize, name="dcatDistribution__dcat_byteSize", curie=DCAT.curie('byteSize'),
                   model_uri=DEFAULT_.dcatDistribution__dcat_byteSize, domain=None, range=Optional[Union[dict, XsdNonNegativInteger]])

slots.dcatDistribution__dcat_compressFormat = Slot(uri=DCAT.compressFormat, name="dcatDistribution__dcat_compressFormat", curie=DCAT.curie('compressFormat'),
                   model_uri=DEFAULT_.dcatDistribution__dcat_compressFormat, domain=None, range=Optional[Union[dict, DctMediaType]])

slots.dcatDistribution__dcat_downloadURL = Slot(uri=DCAT.downloadURL, name="dcatDistribution__dcat_downloadURL", curie=DCAT.curie('downloadURL'),
                   model_uri=DEFAULT_.dcatDistribution__dcat_downloadURL, domain=None, range=Optional[Union[Union[dict, RdfsResource], List[Union[dict, RdfsResource]]]])

slots.dcatDistribution__dcat_mediaType = Slot(uri=DCAT.compressFormat, name="dcatDistribution__dcat_mediaType", curie=DCAT.curie('compressFormat'),
                   model_uri=DEFAULT_.dcatDistribution__dcat_mediaType, domain=None, range=Optional[Union[dict, DctMediaType]])

slots.dcatDistribution__dcat_packageFormat = Slot(uri=DCAT.packageFormat, name="dcatDistribution__dcat_packageFormat", curie=DCAT.curie('packageFormat'),
                   model_uri=DEFAULT_.dcatDistribution__dcat_packageFormat, domain=None, range=Optional[Union[dict, DctMediaType]])

slots.dcatDistribution__dcat_spatialResolutionInMeters = Slot(uri=DCAT.spatialResolutionInMeters, name="dcatDistribution__dcat_spatialResolutionInMeters", curie=DCAT.curie('spatialResolutionInMeters'),
                   model_uri=DEFAULT_.dcatDistribution__dcat_spatialResolutionInMeters, domain=None, range=Optional[Union[Union[dict, XsdDecimal], List[Union[dict, XsdDecimal]]]])

slots.dcatDistribution__dcat_temporalResolution = Slot(uri=DCAT.temporalResolution, name="dcatDistribution__dcat_temporalResolution", curie=DCAT.curie('temporalResolution'),
                   model_uri=DEFAULT_.dcatDistribution__dcat_temporalResolution, domain=None, range=Optional[Union[Union[dict, XsdDuration], List[Union[dict, XsdDuration]]]])

slots.dcatDistribution__dct_conformsTo = Slot(uri=DCT.conformsTo, name="dcatDistribution__dct_conformsTo", curie=DCT.curie('conformsTo'),
                   model_uri=DEFAULT_.dcatDistribution__dct_conformsTo, domain=None, range=Optional[Union[Union[dict, DctStandard], List[Union[dict, DctStandard]]]])

slots.dcatDistribution__dct_issued = Slot(uri=DCT.issued, name="dcatDistribution__dct_issued", curie=DCT.curie('issued'),
                   model_uri=DEFAULT_.dcatDistribution__dct_issued, domain=None, range=Optional[str])

slots.dcatDistribution__dct_language = Slot(uri=DCT.language, name="dcatDistribution__dct_language", curie=DCT.curie('language'),
                   model_uri=DEFAULT_.dcatDistribution__dct_language, domain=None, range=Optional[Union[Union[dict, DctLinguisticSystem], List[Union[dict, DctLinguisticSystem]]]])

slots.dcatDistribution__dct_modified = Slot(uri=DCT.modified, name="dcatDistribution__dct_modified", curie=DCT.curie('modified'),
                   model_uri=DEFAULT_.dcatDistribution__dct_modified, domain=None, range=Optional[str])

slots.dcatDistribution__dct_rights = Slot(uri=DCT.rights, name="dcatDistribution__dct_rights", curie=DCT.curie('rights'),
                   model_uri=DEFAULT_.dcatDistribution__dct_rights, domain=None, range=Optional[Union[dict, DctRightsStatement]])

slots.dcatDistribution__dct_title = Slot(uri=DCT.title, name="dcatDistribution__dct_title", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.dcatDistribution__dct_title, domain=None, range=Optional[Union[Union[dict, RdfsLiteral], List[Union[dict, RdfsLiteral]]]])

slots.dcatDistribution__foaf_page = Slot(uri=FOAF.page, name="dcatDistribution__foaf_page", curie=FOAF.curie('page'),
                   model_uri=DEFAULT_.dcatDistribution__foaf_page, domain=None, range=Optional[Union[Union[dict, FoafDocument], List[Union[dict, FoafDocument]]]])

slots.dcatDistribution__odrl_hasPolicy = Slot(uri=ODRL.hasPolicy, name="dcatDistribution__odrl_hasPolicy", curie=ODRL.curie('hasPolicy'),
                   model_uri=DEFAULT_.dcatDistribution__odrl_hasPolicy, domain=None, range=Optional[Union[dict, OdrlHasPolicy]])

slots.dcatDistribution__spdx_checksum = Slot(uri=SPDX.checksum, name="dcatDistribution__spdx_checksum", curie=SPDX.curie('checksum'),
                   model_uri=DEFAULT_.dcatDistribution__spdx_checksum, domain=None, range=Optional[Union[dict, SpdxChecksum]])

slots.dcatDistribution__dct_license = Slot(uri=DCT.license, name="dcatDistribution__dct_license", curie=DCT.curie('license'),
                   model_uri=DEFAULT_.dcatDistribution__dct_license, domain=None, range=Optional[Union[dict, DctLicenseDocument]])

slots.dcatDistribution__dcat_accessesService = Slot(uri=DCAT.accessesService, name="dcatDistribution__dcat_accessesService", curie=DCAT.curie('accessesService'),
                   model_uri=DEFAULT_.dcatDistribution__dcat_accessesService, domain=None, range=Optional[Union[Union[dict, DcatDataService], List[Union[dict, DcatDataService]]]])

slots.dcatCatalog__dct_description = Slot(uri=DCAT.description, name="dcatCatalog__dct_description", curie=DCAT.curie('description'),
                   model_uri=DEFAULT_.dcatCatalog__dct_description, domain=None, range=Union[Union[dict, RdfsLiteral], List[Union[dict, RdfsLiteral]]])

slots.dcatCatalog__dct_title = Slot(uri=DCT.title, name="dcatCatalog__dct_title", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.dcatCatalog__dct_title, domain=None, range=Union[Union[dict, RdfsLiteral], List[Union[dict, RdfsLiteral]]])

slots.dcatCatalog__dcat_themeTaxonomy = Slot(uri=DCAT.themeTaxonomy, name="dcatCatalog__dcat_themeTaxonomy", curie=DCAT.curie('themeTaxonomy'),
                   model_uri=DEFAULT_.dcatCatalog__dcat_themeTaxonomy, domain=None, range=Optional[Union[Union[dict, SkosConcept], List[Union[dict, SkosConcept]]]])

slots.dcatCatalog__dct_issued = Slot(uri=DCT.issued, name="dcatCatalog__dct_issued", curie=DCT.curie('issued'),
                   model_uri=DEFAULT_.dcatCatalog__dct_issued, domain=None, range=Optional[str])

slots.dcatCatalog__dct_language = Slot(uri=DCT.language, name="dcatCatalog__dct_language", curie=DCT.curie('language'),
                   model_uri=DEFAULT_.dcatCatalog__dct_language, domain=None, range=Optional[Union[Union[dict, DctLinguisticSystem], List[Union[dict, DctLinguisticSystem]]]])

slots.dcatCatalog__dct_modified = Slot(uri=DCT.modified, name="dcatCatalog__dct_modified", curie=DCT.curie('modified'),
                   model_uri=DEFAULT_.dcatCatalog__dct_modified, domain=None, range=Optional[str])

slots.dcatCatalog__foaf_homepage = Slot(uri=FOAF.homepage, name="dcatCatalog__foaf_homepage", curie=FOAF.curie('homepage'),
                   model_uri=DEFAULT_.dcatCatalog__foaf_homepage, domain=None, range=Optional[Union[dict, FoafDocument]])

slots.dcatCatalog__dct_rights = Slot(uri=DCT.rights, name="dcatCatalog__dct_rights", curie=DCT.curie('rights'),
                   model_uri=DEFAULT_.dcatCatalog__dct_rights, domain=None, range=Optional[Union[dict, DctRightsStatement]])

slots.dcatCatalog__dct_publisher = Slot(uri=DCT.publisher, name="dcatCatalog__dct_publisher", curie=DCT.curie('publisher'),
                   model_uri=DEFAULT_.dcatCatalog__dct_publisher, domain=None, range=Union[dict, FoafAgent])

slots.dcatCatalog__dct_license = Slot(uri=DCT.license, name="dcatCatalog__dct_license", curie=DCT.curie('license'),
                   model_uri=DEFAULT_.dcatCatalog__dct_license, domain=None, range=Optional[Union[dict, DctLicenseDocument]])

slots.dcatCatalog__dcat_service = Slot(uri=DCAT.service, name="dcatCatalog__dcat_service", curie=DCAT.curie('service'),
                   model_uri=DEFAULT_.dcatCatalog__dcat_service, domain=None, range=Optional[Union[Union[dict, DcatDataService], List[Union[dict, DcatDataService]]]])

slots.dcatCatalog__dct_spatial = Slot(uri=DCT.spatial, name="dcatCatalog__dct_spatial", curie=DCT.curie('spatial'),
                   model_uri=DEFAULT_.dcatCatalog__dct_spatial, domain=None, range=Optional[Union[Union[dict, DctLocation], List[Union[dict, DctLocation]]]])

slots.dcatCatalog__dcat_dataset = Slot(uri=DCAT.dataset, name="dcatCatalog__dcat_dataset", curie=DCAT.curie('dataset'),
                   model_uri=DEFAULT_.dcatCatalog__dcat_dataset, domain=None, range=Optional[Union[Union[dict, DcatDataset], List[Union[dict, DcatDataset]]]])

slots.dcatCatalog__dcat_catalog = Slot(uri=DCAT.catalog, name="dcatCatalog__dcat_catalog", curie=DCAT.curie('catalog'),
                   model_uri=DEFAULT_.dcatCatalog__dcat_catalog, domain=None, range=Optional[Union[Union[dict, DcatCatalog], List[Union[dict, DcatCatalog]]]])

slots.dcatCatalog__dct_hasPart = Slot(uri=DCT.hasPart, name="dcatCatalog__dct_hasPart", curie=DCT.curie('hasPart'),
                   model_uri=DEFAULT_.dcatCatalog__dct_hasPart, domain=None, range=Optional[Union[Union[dict, DcatCatalog], List[Union[dict, DcatCatalog]]]])

slots.dcatCatalog__dct_isPart = Slot(uri=DCT.isPart, name="dcatCatalog__dct_isPart", curie=DCT.curie('isPart'),
                   model_uri=DEFAULT_.dcatCatalog__dct_isPart, domain=None, range=Optional[Union[dict, DcatCatalog]])

slots.dcatCatalog__dct_temporal = Slot(uri=DCT.temporal, name="dcatCatalog__dct_temporal", curie=DCT.curie('temporal'),
                   model_uri=DEFAULT_.dcatCatalog__dct_temporal, domain=None, range=Optional[Union[Union[dict, DctPeriodOfTime], List[Union[dict, DctPeriodOfTime]]]])

slots.dcatCatalog__dcat_record = Slot(uri=DCAT.record, name="dcatCatalog__dcat_record", curie=DCAT.curie('record'),
                   model_uri=DEFAULT_.dcatCatalog__dcat_record, domain=None, range=Optional[Union[Union[dict, DcatCatalogRecord], List[Union[dict, DcatCatalogRecord]]]])

slots.dcatCatalog__dct_creator = Slot(uri=DCT.creator, name="dcatCatalog__dct_creator", curie=DCT.curie('creator'),
                   model_uri=DEFAULT_.dcatCatalog__dct_creator, domain=None, range=Optional[Union[dict, FoafAgent]])

slots.dctLicenseDocument__dct_type = Slot(uri=DCT.type, name="dctLicenseDocument__dct_type", curie=DCT.curie('type'),
                   model_uri=DEFAULT_.dctLicenseDocument__dct_type, domain=None, range=Optional[Union[Union[dict, SkosConcept], List[Union[dict, SkosConcept]]]])

slots.dcatDataService__dcat_endpointURL = Slot(uri=DCAT.endpointURL, name="dcatDataService__dcat_endpointURL", curie=DCAT.curie('endpointURL'),
                   model_uri=DEFAULT_.dcatDataService__dcat_endpointURL, domain=None, range=Union[Union[dict, RdfsResource], List[Union[dict, RdfsResource]]])

slots.dcatDataService__dct_title = Slot(uri=DCT.title, name="dcatDataService__dct_title", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.dcatDataService__dct_title, domain=None, range=Union[Union[dict, RdfsLiteral], List[Union[dict, RdfsLiteral]]])

slots.dcatDataService__dcat_endpointDescription = Slot(uri=DCAT.endpointDescription, name="dcatDataService__dcat_endpointDescription", curie=DCAT.curie('endpointDescription'),
                   model_uri=DEFAULT_.dcatDataService__dcat_endpointDescription, domain=None, range=Optional[Union[Union[dict, RdfsResource], List[Union[dict, RdfsResource]]]])

slots.dcatDataService__dct_accessRights = Slot(uri=DCT.accessRights, name="dcatDataService__dct_accessRights", curie=DCT.curie('accessRights'),
                   model_uri=DEFAULT_.dcatDataService__dct_accessRights, domain=None, range=Optional[Union[dict, DctRightsStatement]])

slots.dcatDataService__dct_description = Slot(uri=DCAT.description, name="dcatDataService__dct_description", curie=DCAT.curie('description'),
                   model_uri=DEFAULT_.dcatDataService__dct_description, domain=None, range=Optional[Union[Union[dict, RdfsLiteral], List[Union[dict, RdfsLiteral]]]])

slots.dcatDataService__dct_format = Slot(uri=DCT.format, name="dcatDataService__dct_format", curie=DCT.curie('format'),
                   model_uri=DEFAULT_.dcatDataService__dct_format, domain=None, range=Optional[Union[Union[dict, DctMediaTypeOrExtent], List[Union[dict, DctMediaTypeOrExtent]]]])

slots.dcatDataService__dcat_servesDataset = Slot(uri=DCAT.servesDataset, name="dcatDataService__dcat_servesDataset", curie=DCAT.curie('servesDataset'),
                   model_uri=DEFAULT_.dcatDataService__dcat_servesDataset, domain=None, range=Optional[Union[Union[dict, DcatDataset], List[Union[dict, DcatDataset]]]])

slots.dcatDataService__dct_license = Slot(uri=DCT.license, name="dcatDataService__dct_license", curie=DCT.curie('license'),
                   model_uri=DEFAULT_.dcatDataService__dct_license, domain=None, range=Optional[Union[dict, DctLicenseDocument]])

slots.dcatCatalogRecord__dct_modified = Slot(uri=DCT.modified, name="dcatCatalogRecord__dct_modified", curie=DCT.curie('modified'),
                   model_uri=DEFAULT_.dcatCatalogRecord__dct_modified, domain=None, range=str)

slots.dcatCatalogRecord__adms_status = Slot(uri=ADMS.status, name="dcatCatalogRecord__adms_status", curie=ADMS.curie('status'),
                   model_uri=DEFAULT_.dcatCatalogRecord__adms_status, domain=None, range=Optional[Union[dict, SkosConcept]])

slots.dcatCatalogRecord__dct_conformsTo = Slot(uri=DCT.conformsTo, name="dcatCatalogRecord__dct_conformsTo", curie=DCT.curie('conformsTo'),
                   model_uri=DEFAULT_.dcatCatalogRecord__dct_conformsTo, domain=None, range=Optional[Union[Union[dict, DctStandard], List[Union[dict, DctStandard]]]])

slots.dcatCatalogRecord__dct_issued = Slot(uri=DCT.issued, name="dcatCatalogRecord__dct_issued", curie=DCT.curie('issued'),
                   model_uri=DEFAULT_.dcatCatalogRecord__dct_issued, domain=None, range=Optional[str])

slots.dcatCatalogRecord__dct_description = Slot(uri=DCAT.description, name="dcatCatalogRecord__dct_description", curie=DCAT.curie('description'),
                   model_uri=DEFAULT_.dcatCatalogRecord__dct_description, domain=None, range=Optional[Union[Union[dict, RdfsLiteral], List[Union[dict, RdfsLiteral]]]])

slots.dcatCatalogRecord__dct_language = Slot(uri=DCT.language, name="dcatCatalogRecord__dct_language", curie=DCT.curie('language'),
                   model_uri=DEFAULT_.dcatCatalogRecord__dct_language, domain=None, range=Optional[Union[Union[dict, DctLinguisticSystem], List[Union[dict, DctLinguisticSystem]]]])

slots.dcatCatalogRecord__dct_title = Slot(uri=DCT.title, name="dcatCatalogRecord__dct_title", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.dcatCatalogRecord__dct_title, domain=None, range=Optional[Union[Union[dict, RdfsLiteral], List[Union[dict, RdfsLiteral]]]])

slots.dcatCatalogRecord__foaf_primaryTopic = Slot(uri=FOAF.primaryTopic, name="dcatCatalogRecord__foaf_primaryTopic", curie=FOAF.curie('primaryTopic'),
                   model_uri=DEFAULT_.dcatCatalogRecord__foaf_primaryTopic, domain=None, range=Union[dict, DcatResource])

slots.dcatCatalogRecord__dct_source = Slot(uri=DCT.source, name="dcatCatalogRecord__dct_source", curie=DCT.curie('source'),
                   model_uri=DEFAULT_.dcatCatalogRecord__dct_source, domain=None, range=Optional[Union[dict, DcatCatalogRecord]])

slots.dctLocation__dcat_bbox = Slot(uri=DCAT.bbox, name="dctLocation__dcat_bbox", curie=DCAT.curie('bbox'),
                   model_uri=DEFAULT_.dctLocation__dcat_bbox, domain=None, range=Optional[Union[dict, RdfsLiteral]])

slots.dctLocation__dcat_centroid = Slot(uri=DCAT.centroid, name="dctLocation__dcat_centroid", curie=DCAT.curie('centroid'),
                   model_uri=DEFAULT_.dctLocation__dcat_centroid, domain=None, range=Optional[Union[dict, RdfsLiteral]])

slots.dctLocation__lcon_geometry = Slot(uri=LCON.geometry, name="dctLocation__lcon_geometry", curie=LCON.curie('geometry'),
                   model_uri=DEFAULT_.dctLocation__lcon_geometry, domain=None, range=Optional[Union[dict, LconGeometry]])

slots.dctPeriodOfTime__dcat_endDate = Slot(uri=DCAT.endDate, name="dctPeriodOfTime__dcat_endDate", curie=DCAT.curie('endDate'),
                   model_uri=DEFAULT_.dctPeriodOfTime__dcat_endDate, domain=None, range=Optional[str])

slots.dctPeriodOfTime__dcat_startDate = Slot(uri=DCAT.startDate, name="dctPeriodOfTime__dcat_startDate", curie=DCAT.curie('startDate'),
                   model_uri=DEFAULT_.dctPeriodOfTime__dcat_startDate, domain=None, range=Optional[str])

slots.dctPeriodOfTime__time_hasBeginning = Slot(uri=TIME.hasBeginning, name="dctPeriodOfTime__time_hasBeginning", curie=TIME.curie('hasBeginning'),
                   model_uri=DEFAULT_.dctPeriodOfTime__time_hasBeginning, domain=None, range=Optional[str])

slots.dctPeriodOfTime__time_hasEnd = Slot(uri=TIME.hasEnd, name="dctPeriodOfTime__time_hasEnd", curie=TIME.curie('hasEnd'),
                   model_uri=DEFAULT_.dctPeriodOfTime__time_hasEnd, domain=None, range=Optional[str])

slots.foafAgent__foaf_name = Slot(uri=FOAF.name, name="foafAgent__foaf_name", curie=FOAF.curie('name'),
                   model_uri=DEFAULT_.foafAgent__foaf_name, domain=None, range=Union[Union[dict, RdfsLiteral], List[Union[dict, RdfsLiteral]]])

slots.foafAgent__dct_type = Slot(uri=DCT.type, name="foafAgent__dct_type", curie=DCT.curie('type'),
                   model_uri=DEFAULT_.foafAgent__dct_type, domain=None, range=Optional[Union[dict, SkosConcept]])

slots.datasetinSeries__dct_description = Slot(uri=DCAT.description, name="datasetinSeries__dct_description", curie=DCAT.curie('description'),
                   model_uri=DEFAULT_.datasetinSeries__dct_description, domain=None, range=Union[Union[dict, RdfsLiteral], List[Union[dict, RdfsLiteral]]])

slots.datasetinSeries__dct_title = Slot(uri=DCT.title, name="datasetinSeries__dct_title", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.datasetinSeries__dct_title, domain=None, range=Union[Union[dict, RdfsLiteral], List[Union[dict, RdfsLiteral]]])

slots.datasetinSeries__dct_accuralPeriodicity = Slot(uri=DCT.accuralPeriodicity, name="datasetinSeries__dct_accuralPeriodicity", curie=DCT.curie('accuralPeriodicity'),
                   model_uri=DEFAULT_.datasetinSeries__dct_accuralPeriodicity, domain=None, range=Optional[Union[Union[dict, DctFrequency], List[Union[dict, DctFrequency]]]])

slots.datasetinSeries__dcat_prev = Slot(uri=DCAT.prev, name="datasetinSeries__dcat_prev", curie=DCAT.curie('prev'),
                   model_uri=DEFAULT_.datasetinSeries__dcat_prev, domain=None, range=Optional[Union[Union[dict, DatasetinSeries], List[Union[dict, DatasetinSeries]]]])

slots.datasetinSeries__dcat_next = Slot(uri=DCAT.next, name="datasetinSeries__dcat_next", curie=DCAT.curie('next'),
                   model_uri=DEFAULT_.datasetinSeries__dcat_next, domain=None, range=Optional[Union[Union[dict, DatasetinSeries], List[Union[dict, DatasetinSeries]]]])

slots.datasetinSeries__dcat_inSeries = Slot(uri=DCAT.inSeries, name="datasetinSeries__dcat_inSeries", curie=DCAT.curie('inSeries'),
                   model_uri=DEFAULT_.datasetinSeries__dcat_inSeries, domain=None, range=Optional[Union[Union[dict, DcatDatasetSeries], List[Union[dict, DcatDatasetSeries]]]])

slots.dcatDatasetSeries__dct_description = Slot(uri=DCAT.description, name="dcatDatasetSeries__dct_description", curie=DCAT.curie('description'),
                   model_uri=DEFAULT_.dcatDatasetSeries__dct_description, domain=None, range=Union[Union[dict, RdfsLiteral], List[Union[dict, RdfsLiteral]]])

slots.dcatDatasetSeries__dct_title = Slot(uri=DCT.title, name="dcatDatasetSeries__dct_title", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.dcatDatasetSeries__dct_title, domain=None, range=Union[Union[dict, RdfsLiteral], List[Union[dict, RdfsLiteral]]])

slots.dcatDatasetSeries__dcat_contactPoint = Slot(uri=DCAT.contactPoint, name="dcatDatasetSeries__dcat_contactPoint", curie=DCAT.curie('contactPoint'),
                   model_uri=DEFAULT_.dcatDatasetSeries__dcat_contactPoint, domain=None, range=Optional[Union[Union[dict, VcardKind], List[Union[dict, VcardKind]]]])

slots.dcatDatasetSeries__dct_accuralPeriodicity = Slot(uri=DCT.accuralPeriodicity, name="dcatDatasetSeries__dct_accuralPeriodicity", curie=DCT.curie('accuralPeriodicity'),
                   model_uri=DEFAULT_.dcatDatasetSeries__dct_accuralPeriodicity, domain=None, range=Optional[Union[dict, DctFrequency]])

slots.dcatDatasetSeries__dct_issued = Slot(uri=DCT.issued, name="dcatDatasetSeries__dct_issued", curie=DCT.curie('issued'),
                   model_uri=DEFAULT_.dcatDatasetSeries__dct_issued, domain=None, range=Optional[str])

slots.dcatDatasetSeries__dct_modified = Slot(uri=DCT.modified, name="dcatDatasetSeries__dct_modified", curie=DCT.curie('modified'),
                   model_uri=DEFAULT_.dcatDatasetSeries__dct_modified, domain=None, range=Optional[str])

slots.dcatDatasetSeries__dct_spatial = Slot(uri=DCT.spatial, name="dcatDatasetSeries__dct_spatial", curie=DCT.curie('spatial'),
                   model_uri=DEFAULT_.dcatDatasetSeries__dct_spatial, domain=None, range=Optional[Union[Union[dict, DctLocation], List[Union[dict, DctLocation]]]])

slots.dcatDatasetSeries__dct_temporal = Slot(uri=DCT.temporal, name="dcatDatasetSeries__dct_temporal", curie=DCT.curie('temporal'),
                   model_uri=DEFAULT_.dcatDatasetSeries__dct_temporal, domain=None, range=Optional[Union[Union[dict, DctPeriodOfTime], List[Union[dict, DctPeriodOfTime]]]])

slots.dcatDatasetSeries__dct_publisher = Slot(uri=DCT.publisher, name="dcatDatasetSeries__dct_publisher", curie=DCT.curie('publisher'),
                   model_uri=DEFAULT_.dcatDatasetSeries__dct_publisher, domain=None, range=Optional[Union[dict, FoafAgent]])

slots.dcatDatasetSeries__dcat_seriesMember = Slot(uri=DCAT.seriesMember, name="dcatDatasetSeries__dcat_seriesMember", curie=DCAT.curie('seriesMember'),
                   model_uri=DEFAULT_.dcatDatasetSeries__dcat_seriesMember, domain=None, range=Optional[Union[Union[dict, DatasetinSeries], List[Union[dict, DatasetinSeries]]]])

slots.dcatDatasetSeries__dcat_first = Slot(uri=DCAT.first, name="dcatDatasetSeries__dcat_first", curie=DCAT.curie('first'),
                   model_uri=DEFAULT_.dcatDatasetSeries__dcat_first, domain=None, range=Optional[Union[Union[dict, DatasetinSeries], List[Union[dict, DatasetinSeries]]]])

slots.dcatDatasetSeries__dcat_last = Slot(uri=DCAT.last, name="dcatDatasetSeries__dcat_last", curie=DCAT.curie('last'),
                   model_uri=DEFAULT_.dcatDatasetSeries__dcat_last, domain=None, range=Optional[Union[Union[dict, DatasetinSeries], List[Union[dict, DatasetinSeries]]]])