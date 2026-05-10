from . import base_types
from .CardPaymentServiceType2Code import CardPaymentServiceType2Code
from .Max35Text import Max35Text
from .ExternalCardTransactionCategory1Code import ExternalCardTransactionCategory1Code
from .CardSequenceNumberRange1 import CardSequenceNumberRange1
from .DateOrDateTimePeriod1Choice import DateOrDateTimePeriod1Choice

class CardAggregated2(base_types._BaseFieldType):

	__slots__ = ["_AddtlSvc", "_TxCtgy", "_SeqNbRg", "_SaleRcncltnId", "_TxDtRg"]
	@property
	def AddtlSvc(self):
		return self._AddtlSvc

	@AddtlSvc.setter
	def AddtlSvc(self, value):
		self._AddtlSvc = value if type(value) != auto else self.make_default("AddtlSvc")

	@AddtlSvc.deleter
	def AddtlSvc(self):
		del self._AddtlSvc
		self._AddtlSvc = None

	@property
	def TxCtgy(self):
		return self._TxCtgy

	@TxCtgy.setter
	def TxCtgy(self, value):
		self._TxCtgy = value if type(value) != auto else self.make_default("TxCtgy")

	@TxCtgy.deleter
	def TxCtgy(self):
		del self._TxCtgy
		self._TxCtgy = None

	@property
	def SeqNbRg(self):
		return self._SeqNbRg

	@SeqNbRg.setter
	def SeqNbRg(self, value):
		self._SeqNbRg = value if type(value) != auto else self.make_default("SeqNbRg")

	@SeqNbRg.deleter
	def SeqNbRg(self):
		del self._SeqNbRg
		self._SeqNbRg = None

	@property
	def SaleRcncltnId(self):
		return self._SaleRcncltnId

	@SaleRcncltnId.setter
	def SaleRcncltnId(self, value):
		self._SaleRcncltnId = value if type(value) != auto else self.make_default("SaleRcncltnId")

	@SaleRcncltnId.deleter
	def SaleRcncltnId(self):
		del self._SaleRcncltnId
		self._SaleRcncltnId = None

	@property
	def TxDtRg(self):
		return self._TxDtRg

	@TxDtRg.setter
	def TxDtRg(self, value):
		self._TxDtRg = value if type(value) != auto else self.make_default("TxDtRg")

	@TxDtRg.deleter
	def TxDtRg(self):
		del self._TxDtRg
		self._TxDtRg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlSvc', type=CardPaymentServiceType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxCtgy', type=ExternalCardTransactionCategory1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNbRg', type=CardSequenceNumberRange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleRcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtRg', type=DateOrDateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
	))

