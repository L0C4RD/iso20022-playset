from . import base_types
from .Number import Number
from .MICIdentifier import MICIdentifier
from .Max35Text import Max35Text
from .ISODate import ISODate
from .ISINOct2015Identifier import ISINOct2015Identifier
from .TransactionsBin2 import TransactionsBin2
from .TrueFalseIndicator import TrueFalseIndicator

class TransparencyDataReport15(base_types._BaseFieldType):

	__slots__ = ["_NbTxs", "_Id", "_TradgVn", "_AggtdQttvData", "_RptgDt", "_Sspnsn", "_TechRcrdId"]
	@property
	def NbTxs(self):
		return self._NbTxs

	@NbTxs.setter
	def NbTxs(self, value):
		self._NbTxs = value if type(value) != auto else self.make_default("NbTxs")

	@NbTxs.deleter
	def NbTxs(self):
		del self._NbTxs
		self._NbTxs = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if type(value) != auto else self.make_default("TradgVn")

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = None

	@property
	def AggtdQttvData(self):
		return self._AggtdQttvData

	@AggtdQttvData.setter
	def AggtdQttvData(self, value):
		self._AggtdQttvData = value if type(value) != auto else self.make_default("AggtdQttvData")

	@AggtdQttvData.deleter
	def AggtdQttvData(self):
		del self._AggtdQttvData
		self._AggtdQttvData = None

	@property
	def RptgDt(self):
		return self._RptgDt

	@RptgDt.setter
	def RptgDt(self, value):
		self._RptgDt = value if type(value) != auto else self.make_default("RptgDt")

	@RptgDt.deleter
	def RptgDt(self):
		del self._RptgDt
		self._RptgDt = None

	@property
	def Sspnsn(self):
		return self._Sspnsn

	@Sspnsn.setter
	def Sspnsn(self, value):
		self._Sspnsn = value if type(value) != auto else self.make_default("Sspnsn")

	@Sspnsn.deleter
	def Sspnsn(self):
		del self._Sspnsn
		self._Sspnsn = None

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if type(value) != auto else self.make_default("TechRcrdId")

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbTxs', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVn', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AggtdQttvData', type=TransactionsBin2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sspnsn', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

