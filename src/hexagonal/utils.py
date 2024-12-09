import logging
import re

DATE_FRANCAISE_RE = re.compile(r"^(?P<jour>\d{2})/(?P<mois>\d{2})/(?P<annee>\d{4})$")

logger = logging.getLogger(__name__)


def date_francaise_vers_iso(d):
    if not d:
        return ""
    if m := DATE_FRANCAISE_RE.match(d):
        parts = m.groupdict()
        return f"{parts['annee']}-{parts['mois']}-{parts['jour']}"
    else:
        logger.warning(f"Date non valide: {d}")
        return ""
