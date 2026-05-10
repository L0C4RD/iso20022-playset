from . import base_types
from .SecurityIdentification19 import SecurityIdentification19
from .Quantity51Choice import Quantity51Choice
from .DateAndDateTime2Choice import DateAndDateTime2Choice
from .CreditDebitCode import CreditDebitCode

class SecuritiesOption80(base_types._BaseFieldType):

	__slots__ = ["_OrgnlPstngDt", "_PstngQty", "_FinInstrmId", "_CdtDbtInd", "_PstngDt"]
	@property
	def OrgnlPstngDt(self):
		return self._OrgnlPstngDt

	@OrgnlPstngDt.setter
	def OrgnlPstngDt(self, value):
		self._OrgnlPstngDt = value if type(value) != auto else self.make_default("OrgnlPstngDt")

	@OrgnlPstngDt.deleter
	def OrgnlPstngDt(self):
		del self._OrgnlPstngDt
		self._OrgnlPstngDt = None

	@property
	def PstngQty(self):
		return self._PstngQty

	@PstngQty.setter
	def PstngQty(self, value):
		self._PstngQty = value if type(value) != auto else self.make_default("PstngQty")

	@PstngQty.deleter
	def PstngQty(self):
		del self._PstngQty
		self._PstngQty = None

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
	def PstngDt(self):
		return self._PstngDt

	@PstngDt.setter
	def PstngDt(self, value):
		self._PstngDt = value if type(value) != auto else self.make_default("PstngDt")

	@PstngDt.deleter
	def PstngDt(self):
		del self._PstngDt
		self._PstngDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlPstngDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngQty', type=Quantity51Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
	))

