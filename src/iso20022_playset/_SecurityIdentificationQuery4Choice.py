from . import base_types
from ._ISINOct2015Identifier import ISINOct2015Identifier
from ._BasketQuery1 import BasketQuery1
from ._SecurityIdentification20Choice import SecurityIdentification20Choice
from ._NotAvailable1Code import NotAvailable1Code
from ._NotReported1Code import NotReported1Code
from ._Max52Text import Max52Text

class SecurityIdentificationQuery4Choice(base_types._BaseFieldType):

	__slots__ = ["_UnqPdctIdr", "_NotRptd", "_Bskt", "_AltrntvInstrmId", "_ISIN", "_NotAvlbl", "_Indx"]
	@property
	def AltrntvInstrmId(self):
		return self._AltrntvInstrmId

	@AltrntvInstrmId.setter
	def AltrntvInstrmId(self, value):
		self._AltrntvInstrmId = value if type(value) != base_types.auto else self.make_default("AltrntvInstrmId")

	@AltrntvInstrmId.deleter
	def AltrntvInstrmId(self):
		del self._AltrntvInstrmId
		self._AltrntvInstrmId = None

	@property
	def Bskt(self):
		return self._Bskt

	@Bskt.setter
	def Bskt(self, value):
		self._Bskt = value if type(value) != base_types.auto else self.make_default("Bskt")

	@Bskt.deleter
	def Bskt(self):
		del self._Bskt
		self._Bskt = None

	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if type(value) != base_types.auto else self.make_default("ISIN")

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = None

	@property
	def Indx(self):
		return self._Indx

	@Indx.setter
	def Indx(self, value):
		self._Indx = value if type(value) != base_types.auto else self.make_default("Indx")

	@Indx.deleter
	def Indx(self):
		del self._Indx
		self._Indx = None

	@property
	def NotAvlbl(self):
		return self._NotAvlbl

	@NotAvlbl.setter
	def NotAvlbl(self, value):
		self._NotAvlbl = value if type(value) != base_types.auto else self.make_default("NotAvlbl")

	@NotAvlbl.deleter
	def NotAvlbl(self):
		del self._NotAvlbl
		self._NotAvlbl = None

	@property
	def NotRptd(self):
		return self._NotRptd

	@NotRptd.setter
	def NotRptd(self, value):
		self._NotRptd = value if type(value) != base_types.auto else self.make_default("NotRptd")

	@NotRptd.deleter
	def NotRptd(self):
		del self._NotRptd
		self._NotRptd = None

	@property
	def UnqPdctIdr(self):
		return self._UnqPdctIdr

	@UnqPdctIdr.setter
	def UnqPdctIdr(self, value):
		self._UnqPdctIdr = value if type(value) != base_types.auto else self.make_default("UnqPdctIdr")

	@UnqPdctIdr.deleter
	def UnqPdctIdr(self):
		del self._UnqPdctIdr
		self._UnqPdctIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrntvInstrmId', type=Max52Text, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Bskt', type=BasketQuery1, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Indx', type=SecurityIdentification20Choice, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='NotAvlbl', type=NotAvailable1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotRptd', type=NotReported1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UnqPdctIdr', type=Max52Text, min=1, max=None, mutex_group=1, array=True),
	))

