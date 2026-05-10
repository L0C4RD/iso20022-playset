from . import base_types
import RoleAndBaselineAcceptanceV01

class TSMT_049_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RoleAndBaselnAccptnc"]
		@property
		def RoleAndBaselnAccptnc(self):
			return self._RoleAndBaselnAccptnc

		@RoleAndBaselnAccptnc.setter
		def RoleAndBaselnAccptnc(self, value):
			self._RoleAndBaselnAccptnc = value if type(value) != auto else self.make_default("RoleAndBaselnAccptnc")

		@RoleAndBaselnAccptnc.deleter
		def RoleAndBaselnAccptnc(self):
			del self._RoleAndBaselnAccptnc
			self._RoleAndBaselnAccptnc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RoleAndBaselnAccptnc', type=RoleAndBaselineAcceptanceV01, min=1, max=1, mutex_group=None, array=False),
		))

