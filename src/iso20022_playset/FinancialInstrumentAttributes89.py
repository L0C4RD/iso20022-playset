from . import base_types
from .PhysicalTransferType4Code import PhysicalTransferType4Code
from .ContractSize1 import ContractSize1
from .GenericIdentification165 import GenericIdentification165
from .ActiveCurrencyCode import ActiveCurrencyCode

class FinancialInstrumentAttributes89(base_types._BaseFieldType):

	__slots__ = ["_CtrctSz", "_UndrlygId", "_DlvryTp", "_PricCcy"]
	@property
	def CtrctSz(self):
		return self._CtrctSz

	@CtrctSz.setter
	def CtrctSz(self, value):
		self._CtrctSz = value if type(value) != base_types.auto else self.make_default("CtrctSz")

	@CtrctSz.deleter
	def CtrctSz(self):
		del self._CtrctSz
		self._CtrctSz = None

	@property
	def UndrlygId(self):
		return self._UndrlygId

	@UndrlygId.setter
	def UndrlygId(self, value):
		self._UndrlygId = value if type(value) != base_types.auto else self.make_default("UndrlygId")

	@UndrlygId.deleter
	def UndrlygId(self):
		del self._UndrlygId
		self._UndrlygId = None

	@property
	def DlvryTp(self):
		return self._DlvryTp

	@DlvryTp.setter
	def DlvryTp(self, value):
		self._DlvryTp = value if type(value) != base_types.auto else self.make_default("DlvryTp")

	@DlvryTp.deleter
	def DlvryTp(self):
		del self._DlvryTp
		self._DlvryTp = None

	@property
	def PricCcy(self):
		return self._PricCcy

	@PricCcy.setter
	def PricCcy(self, value):
		self._PricCcy = value if type(value) != base_types.auto else self.make_default("PricCcy")

	@PricCcy.deleter
	def PricCcy(self):
		del self._PricCcy
		self._PricCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrctSz', type=ContractSize1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygId', type=GenericIdentification165, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryTp', type=PhysicalTransferType4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
	))

