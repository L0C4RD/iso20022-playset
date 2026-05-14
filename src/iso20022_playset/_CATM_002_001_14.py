from . import base_types
from ._ManagementPlanReplacementV14 import ManagementPlanReplacementV14

class CATM_002_001_14():

	class Document(base_types._BaseFieldType):

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
			base_types.FieldEntry(name='MgmtPlanRplcmnt', type=ManagementPlanReplacementV14, min=1, max=1, mutex_group=None, array=False),
		))

