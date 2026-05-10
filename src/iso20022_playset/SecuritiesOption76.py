import base_types
import SecurityIdentification19
import CreditDebitCode
import Quantity6Choice
import DateFormat58Choice

class SecuritiesOption76(base_types._BaseFieldType):

	__slots__ = ["_CdtDbtInd", "_PmtDt", "_FinInstrmId", "_EntitldQty"]
	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	@property
	def PmtDt(self):
		return self._PmtDt

	@PmtDt.setter
	def PmtDt(self, value):
		self._PmtDt = value if type(value) != auto else self.make_default("PmtDt")

	@PmtDt.deleter
	def PmtDt(self):
		del self._PmtDt
		self._PmtDt = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def EntitldQty(self):
		return self._EntitldQty

	@EntitldQty.setter
	def EntitldQty(self, value):
		self._EntitldQty = value if type(value) != auto else self.make_default("EntitldQty")

	@EntitldQty.deleter
	def EntitldQty(self):
		del self._EntitldQty
		self._EntitldQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDt', type=DateFormat58Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EntitldQty', type=Quantity6Choice, min=1, max=1, mutex_group=None, array=False),
	))

