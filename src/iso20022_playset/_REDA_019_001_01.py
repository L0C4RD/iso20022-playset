from . import base_types
from ._SecuritiesAccountQueryV01 import SecuritiesAccountQueryV01

class REDA_019_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesAcctQry"]
		@property
		def SctiesAcctQry(self):
			return self._SctiesAcctQry

		@SctiesAcctQry.setter
		def SctiesAcctQry(self, value):
			self._SctiesAcctQry = value if type(value) != base_types.auto else self.make_default("SctiesAcctQry")

		@SctiesAcctQry.deleter
		def SctiesAcctQry(self):
			del self._SctiesAcctQry
			self._SctiesAcctQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAcctQry', type=SecuritiesAccountQueryV01, min=1, max=1, mutex_group=None, array=False),
		))

