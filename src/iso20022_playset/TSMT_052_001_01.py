from . import base_types
from .RoleAndBaselineRejectionNotificationV01 import RoleAndBaselineRejectionNotificationV01

class TSMT_052_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RoleAndBaselnRjctnNtfctn"]
		@property
		def RoleAndBaselnRjctnNtfctn(self):
			return self._RoleAndBaselnRjctnNtfctn

		@RoleAndBaselnRjctnNtfctn.setter
		def RoleAndBaselnRjctnNtfctn(self, value):
			self._RoleAndBaselnRjctnNtfctn = value if type(value) != auto else self.make_default("RoleAndBaselnRjctnNtfctn")

		@RoleAndBaselnRjctnNtfctn.deleter
		def RoleAndBaselnRjctnNtfctn(self):
			del self._RoleAndBaselnRjctnNtfctn
			self._RoleAndBaselnRjctnNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RoleAndBaselnRjctnNtfctn', type=RoleAndBaselineRejectionNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))

