from . import base_types
from ._AccountHoldingInformationV09 import AccountHoldingInformationV09

class SESE_018_001_09():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctHldgInf"]
		@property
		def AcctHldgInf(self):
			return self._AcctHldgInf

		@AcctHldgInf.setter
		def AcctHldgInf(self, value):
			self._AcctHldgInf = value if type(value) != base_types.auto else self.make_default("AcctHldgInf")

		@AcctHldgInf.deleter
		def AcctHldgInf(self):
			del self._AcctHldgInf
			self._AcctHldgInf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctHldgInf', type=AccountHoldingInformationV09, min=1, max=1, mutex_group=None, array=False),
		))

