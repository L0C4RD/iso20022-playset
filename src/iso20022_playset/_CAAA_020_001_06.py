from . import base_types
from ._TransactionAdviceV06 import TransactionAdviceV06

class CAAA_020_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_TxAdvc"]
		@property
		def TxAdvc(self):
			return self._TxAdvc

		@TxAdvc.setter
		def TxAdvc(self, value):
			self._TxAdvc = value if type(value) != base_types.auto else self.make_default("TxAdvc")

		@TxAdvc.deleter
		def TxAdvc(self):
			del self._TxAdvc
			self._TxAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TxAdvc', type=TransactionAdviceV06, min=1, max=1, mutex_group=None, array=False),
		))

