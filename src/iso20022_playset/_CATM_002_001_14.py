# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ManagementPlanReplacementV14

class CATM_002_001_14():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catm.002.001.14"
		_docname = "catm.002.001.14"

		__slots__ = ["_MgmtPlanRplcmnt"]
		@property
		def MgmtPlanRplcmnt(self):
			return self._MgmtPlanRplcmnt

		@MgmtPlanRplcmnt.setter
		def MgmtPlanRplcmnt(self, value):
			self._MgmtPlanRplcmnt = value if value is not None else base_types.UninitialisedField(self, 'MgmtPlanRplcmnt', ManagementPlanReplacementV14, False)

		@MgmtPlanRplcmnt.deleter
		def MgmtPlanRplcmnt(self):
			del self._MgmtPlanRplcmnt
			self._MgmtPlanRplcmnt = base_types.UninitialisedField(self, 'MgmtPlanRplcmnt', ManagementPlanReplacementV14, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='MgmtPlanRplcmnt', type=ManagementPlanReplacementV14, min=1, max=1, mutex_group=None, array=False),
		))