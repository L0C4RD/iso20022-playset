from . import base_types
from ._ReturnAccountV10 import ReturnAccountV10

class CAMT_004_001_10():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RtrAcct"]
		@property
		def RtrAcct(self):
			return self._RtrAcct

		@RtrAcct.setter
		def RtrAcct(self, value):
			self._RtrAcct = value if type(value) != base_types.auto else self.make_default("RtrAcct")

		@RtrAcct.deleter
		def RtrAcct(self):
			del self._RtrAcct
			self._RtrAcct = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrAcct', type=ReturnAccountV10, min=1, max=1, mutex_group=None, array=False),
		))

