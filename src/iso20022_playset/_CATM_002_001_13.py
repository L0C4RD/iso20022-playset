# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ManagementPlanReplacementV13 import ManagementPlanReplacementV13

class CATM_002_001_13():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:catm.002.001.13",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_MgmtPlanRplcmnt"]
		@property
		def MgmtPlanRplcmnt(self):
			return self._MgmtPlanRplcmnt

		@MgmtPlanRplcmnt.setter
		def MgmtPlanRplcmnt(self, value):
			self._MgmtPlanRplcmnt = value if type(value) != base_types.auto else self.make_default("MgmtPlanRplcmnt")

		@MgmtPlanRplcmnt.deleter
		def MgmtPlanRplcmnt(self):
			del self._MgmtPlanRplcmnt
			self._MgmtPlanRplcmnt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MgmtPlanRplcmnt', type=ManagementPlanReplacementV13, min=1, max=1, mutex_group=None, array=False),
		))