from . import base_types
from .ContentInformationType10 import ContentInformationType10
from .DetailedAmount16 import DetailedAmount16
from .Max70Text import Max70Text
from .CardAccount21 import CardAccount21
from .ATMDepositedMedia4 import ATMDepositedMedia4

class ATMDepositComponent1(base_types._BaseFieldType):

	__slots__ = ["_PrtctdAcctData", "_DpstdMdia", "_AcctData", "_DtldReqdAmt", "_SubDpstId"]
	@property
	def PrtctdAcctData(self):
		return self._PrtctdAcctData

	@PrtctdAcctData.setter
	def PrtctdAcctData(self, value):
		self._PrtctdAcctData = value if type(value) != base_types.auto else self.make_default("PrtctdAcctData")

	@PrtctdAcctData.deleter
	def PrtctdAcctData(self):
		del self._PrtctdAcctData
		self._PrtctdAcctData = None

	@property
	def DpstdMdia(self):
		return self._DpstdMdia

	@DpstdMdia.setter
	def DpstdMdia(self, value):
		self._DpstdMdia = value if type(value) != base_types.auto else self.make_default("DpstdMdia")

	@DpstdMdia.deleter
	def DpstdMdia(self):
		del self._DpstdMdia
		self._DpstdMdia = None

	@property
	def AcctData(self):
		return self._AcctData

	@AcctData.setter
	def AcctData(self, value):
		self._AcctData = value if type(value) != base_types.auto else self.make_default("AcctData")

	@AcctData.deleter
	def AcctData(self):
		del self._AcctData
		self._AcctData = None

	@property
	def DtldReqdAmt(self):
		return self._DtldReqdAmt

	@DtldReqdAmt.setter
	def DtldReqdAmt(self, value):
		self._DtldReqdAmt = value if type(value) != base_types.auto else self.make_default("DtldReqdAmt")

	@DtldReqdAmt.deleter
	def DtldReqdAmt(self):
		del self._DtldReqdAmt
		self._DtldReqdAmt = None

	@property
	def SubDpstId(self):
		return self._SubDpstId

	@SubDpstId.setter
	def SubDpstId(self, value):
		self._SubDpstId = value if type(value) != base_types.auto else self.make_default("SubDpstId")

	@SubDpstId.deleter
	def SubDpstId(self):
		del self._SubDpstId
		self._SubDpstId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtctdAcctData', type=ContentInformationType10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DpstdMdia', type=ATMDepositedMedia4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctData', type=CardAccount21, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtldReqdAmt', type=DetailedAmount16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubDpstId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))

