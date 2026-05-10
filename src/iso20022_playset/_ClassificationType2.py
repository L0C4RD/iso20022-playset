from . import base_types
from .ExternalFinancialInstrumentProductType1Code import ExternalFinancialInstrumentProductType1Code
from .CFIOct2015Identifier import CFIOct2015Identifier
from .GenericIdentification36 import GenericIdentification36

class ClassificationType2(base_types._BaseFieldType):

	__slots__ = ["_AltrnClssfctn", "_ClssfctnFinInstrm", "_FinInstrmPdctTpCd"]
	@property
	def AltrnClssfctn(self):
		return self._AltrnClssfctn

	@AltrnClssfctn.setter
	def AltrnClssfctn(self, value):
		self._AltrnClssfctn = value if type(value) != base_types.auto else self.make_default("AltrnClssfctn")

	@AltrnClssfctn.deleter
	def AltrnClssfctn(self):
		del self._AltrnClssfctn
		self._AltrnClssfctn = None

	@property
	def ClssfctnFinInstrm(self):
		return self._ClssfctnFinInstrm

	@ClssfctnFinInstrm.setter
	def ClssfctnFinInstrm(self, value):
		self._ClssfctnFinInstrm = value if type(value) != base_types.auto else self.make_default("ClssfctnFinInstrm")

	@ClssfctnFinInstrm.deleter
	def ClssfctnFinInstrm(self):
		del self._ClssfctnFinInstrm
		self._ClssfctnFinInstrm = None

	@property
	def FinInstrmPdctTpCd(self):
		return self._FinInstrmPdctTpCd

	@FinInstrmPdctTpCd.setter
	def FinInstrmPdctTpCd(self, value):
		self._FinInstrmPdctTpCd = value if type(value) != base_types.auto else self.make_default("FinInstrmPdctTpCd")

	@FinInstrmPdctTpCd.deleter
	def FinInstrmPdctTpCd(self):
		del self._FinInstrmPdctTpCd
		self._FinInstrmPdctTpCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrnClssfctn', type=GenericIdentification36, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClssfctnFinInstrm', type=CFIOct2015Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmPdctTpCd', type=ExternalFinancialInstrumentProductType1Code, min=0, max=1, mutex_group=None, array=False),
	))

