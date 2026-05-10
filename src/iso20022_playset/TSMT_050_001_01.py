from . import base_types
from .RoleAndBaselineRejectionV01 import RoleAndBaselineRejectionV01

class TSMT_050_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RoleAndBaselnRjctn"]
		@property
		def RoleAndBaselnRjctn(self):
			return self._RoleAndBaselnRjctn

		@RoleAndBaselnRjctn.setter
		def RoleAndBaselnRjctn(self, value):
			self._RoleAndBaselnRjctn = value if type(value) != auto else self.make_default("RoleAndBaselnRjctn")

		@RoleAndBaselnRjctn.deleter
		def RoleAndBaselnRjctn(self):
			del self._RoleAndBaselnRjctn
			self._RoleAndBaselnRjctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RoleAndBaselnRjctn', type=RoleAndBaselineRejectionV01, min=1, max=1, mutex_group=None, array=False),
		))

