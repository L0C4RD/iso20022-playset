# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BasketQuery1
from . import ISINOct2015Identifier
from . import Max52Text
from . import NotAvailable1Code
from . import NotReported1Code
from . import SecurityIdentification20Choice

class SecurityIdentificationQuery4Choice(base_types._BaseFieldType):

	__slots__ = ["_AltrntvInstrmId", "_Bskt", "_ISIN", "_Indx", "_NotAvlbl", "_NotRptd", "_UnqPdctIdr"]
	@property
	def AltrntvInstrmId(self):
		return self._AltrntvInstrmId

	@AltrntvInstrmId.setter
	def AltrntvInstrmId(self, value):
		self._AltrntvInstrmId = value if value is not None else base_types.UninitialisedField(self, 'AltrntvInstrmId', Max52Text, True)

	@AltrntvInstrmId.deleter
	def AltrntvInstrmId(self):
		del self._AltrntvInstrmId
		self._AltrntvInstrmId = base_types.UninitialisedField(self, 'AltrntvInstrmId', Max52Text, True)

	@property
	def Bskt(self):
		return self._Bskt

	@Bskt.setter
	def Bskt(self, value):
		self._Bskt = value if value is not None else base_types.UninitialisedField(self, 'Bskt', BasketQuery1, True)

	@Bskt.deleter
	def Bskt(self):
		del self._Bskt
		self._Bskt = base_types.UninitialisedField(self, 'Bskt', BasketQuery1, True)

	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if value is not None else base_types.UninitialisedField(self, 'ISIN', ISINOct2015Identifier, True)

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = base_types.UninitialisedField(self, 'ISIN', ISINOct2015Identifier, True)

	@property
	def Indx(self):
		return self._Indx

	@Indx.setter
	def Indx(self, value):
		self._Indx = value if value is not None else base_types.UninitialisedField(self, 'Indx', SecurityIdentification20Choice, True)

	@Indx.deleter
	def Indx(self):
		del self._Indx
		self._Indx = base_types.UninitialisedField(self, 'Indx', SecurityIdentification20Choice, True)

	@property
	def NotAvlbl(self):
		return self._NotAvlbl

	@NotAvlbl.setter
	def NotAvlbl(self, value):
		self._NotAvlbl = value if value is not None else base_types.UninitialisedField(self, 'NotAvlbl', NotAvailable1Code, False)

	@NotAvlbl.deleter
	def NotAvlbl(self):
		del self._NotAvlbl
		self._NotAvlbl = base_types.UninitialisedField(self, 'NotAvlbl', NotAvailable1Code, False)

	@property
	def NotRptd(self):
		return self._NotRptd

	@NotRptd.setter
	def NotRptd(self, value):
		self._NotRptd = value if value is not None else base_types.UninitialisedField(self, 'NotRptd', NotReported1Code, False)

	@NotRptd.deleter
	def NotRptd(self):
		del self._NotRptd
		self._NotRptd = base_types.UninitialisedField(self, 'NotRptd', NotReported1Code, False)

	@property
	def UnqPdctIdr(self):
		return self._UnqPdctIdr

	@UnqPdctIdr.setter
	def UnqPdctIdr(self, value):
		self._UnqPdctIdr = value if value is not None else base_types.UninitialisedField(self, 'UnqPdctIdr', Max52Text, True)

	@UnqPdctIdr.deleter
	def UnqPdctIdr(self):
		del self._UnqPdctIdr
		self._UnqPdctIdr = base_types.UninitialisedField(self, 'UnqPdctIdr', Max52Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrntvInstrmId', type=Max52Text, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Bskt', type=BasketQuery1, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Indx', type=SecurityIdentification20Choice, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='NotAvlbl', type=NotAvailable1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotRptd', type=NotReported1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UnqPdctIdr', type=Max52Text, min=1, max=None, mutex_group=1, array=True),
	))