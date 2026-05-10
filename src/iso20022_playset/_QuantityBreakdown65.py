from . import base_types
from ._FinancialInstrumentQuantity36Choice import FinancialInstrumentQuantity36Choice
from ._GenericIdentification39 import GenericIdentification39
from ._GenericIdentification47 import GenericIdentification47

class QuantityBreakdown65(base_types._BaseFieldType):

	__slots__ = ["_SctiesSubBalTp", "_LotNb", "_LotQty"]
	@property
	def LotNb(self):
		return self._LotNb

	@LotNb.setter
	def LotNb(self, value):
		self._LotNb = value if type(value) != base_types.auto else self.make_default("LotNb")

	@LotNb.deleter
	def LotNb(self):
		del self._LotNb
		self._LotNb = None

	@property
	def LotQty(self):
		return self._LotQty

	@LotQty.setter
	def LotQty(self, value):
		self._LotQty = value if type(value) != base_types.auto else self.make_default("LotQty")

	@LotQty.deleter
	def LotQty(self):
		del self._LotQty
		self._LotQty = None

	@property
	def SctiesSubBalTp(self):
		return self._SctiesSubBalTp

	@SctiesSubBalTp.setter
	def SctiesSubBalTp(self, value):
		self._SctiesSubBalTp = value if type(value) != base_types.auto else self.make_default("SctiesSubBalTp")

	@SctiesSubBalTp.deleter
	def SctiesSubBalTp(self):
		del self._SctiesSubBalTp
		self._SctiesSubBalTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LotNb', type=GenericIdentification39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotQty', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesSubBalTp', type=GenericIdentification47, min=0, max=1, mutex_group=None, array=False),
	))

