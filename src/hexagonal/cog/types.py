from enum import IntEnum, StrEnum


class TypeCommune(StrEnum):
    COMMUNE = "COM"
    COMMUNE_ASSOCIEE = "COMA"
    COMMUNE_DELEGUEE = "COMD"
    ARRONDISSEMENT_PLM = "ARM"


class TypeMouvement(IntEnum):
    CHANGEMENT_DE_NOM = 10
    CREATION = 20
    RETABLISSEMENT = 21
    SUPPRESSION = 30
    FUSION_SIMPLE = 31
    CREATION_COMMUNE_NOUVELLE = 32
    FUSION_ASSOCIATION = 33
    TRANSFORMATION_FUSION_ASSOCIATION_EN_FUSION_SIMPLE = 34
    SUPPRESSION_COMMUNE_DELEGUEE = 35
    CHANGEMENT_DE_DEPARTEMENT = 41
    TRANSFERT_DE_CHEF_LIEU = 50
    TRANSFORMATION_COMMUNE_ASSOCIEE_EN_COMMUNE_DELEGUEE = 70
    RETABLISSEMENT_COMMUNE_DELEGUEE = 71


class TypeCanton(StrEnum):
    CANTON = "C"
    CANTON_VILLE = "V"
    CANTON_FICTIF = "N"


LABELS_TYPE_MOUVEMENT = {
    TypeMouvement.CHANGEMENT_DE_NOM: "changement de nom",
    TypeMouvement.CREATION: "création",
    TypeMouvement.RETABLISSEMENT: "rétablissement",
    TypeMouvement.SUPPRESSION: "suppression",
    TypeMouvement.FUSION_SIMPLE: "fusion simple",
    TypeMouvement.CREATION_COMMUNE_NOUVELLE: "création d'une commune nouvelle",
    TypeMouvement.FUSION_ASSOCIATION: "fusion-association",
    TypeMouvement.TRANSFORMATION_FUSION_ASSOCIATION_EN_FUSION_SIMPLE: "transformation d'une fusion-association en fusion simple",
    TypeMouvement.SUPPRESSION_COMMUNE_DELEGUEE: "suppression d'une commune déléguée",
    TypeMouvement.CHANGEMENT_DE_DEPARTEMENT: "changement de département",
    TypeMouvement.TRANSFERT_DE_CHEF_LIEU: "transfert de chef-lieu",
    TypeMouvement.TRANSFORMATION_COMMUNE_ASSOCIEE_EN_COMMUNE_DELEGUEE: "transformation d'une commune associée en commune déléguée",
    TypeMouvement.RETABLISSEMENT_COMMUNE_DELEGUEE: "rétablissement d'une commune déléguée",
}
