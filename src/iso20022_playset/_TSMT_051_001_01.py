from . import base_types
from ._RoleAndBaselineAcceptanceNotificationV01 import RoleAndBaselineAcceptanceNotificationV01

class TSMT_051_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RoleAndBaselnAccptncNtfctn"]
		@property
		def RoleAndBaselnAccptncNtfctn(self):
			return self._RoleAndBaselnAccptncNtfctn

		@RoleAndBaselnAccptncNtfctn.setter
		def RoleAndBaselnAccptncNtfctn(self, value):
			self._RoleAndBaselnAccptncNtfctn = value if type(value) != base_types.auto else self.make_default("RoleAndBaselnAccptncNtfctn")

		@RoleAndBaselnAccptncNtfctn.deleter
		def RoleAndBaselnAccptncNtfctn(self):
			del self._RoleAndBaselnAccptncNtfctn
			self._RoleAndBaselnAccptncNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RoleAndBaselnAccptncNtfctn', type=RoleAndBaselineAcceptanceNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))

