# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISINOct2015Identifier
from . import ISODate
from . import MICIdentifier
from . import Max35Text
from . import Number
from . import TransactionsBin2
from . import TrueFalseIndicator

class TransparencyDataReport15(base_types._BaseFieldType):

	__slots__ = ["_AggtdQttvData", "_Id", "_NbTxs", "_RptgDt", "_Sspnsn", "_TechRcrdId", "_TradgVn"]
	@property
	def AggtdQttvData(self):
		return self._AggtdQttvData

	@AggtdQttvData.setter
	def AggtdQttvData(self, value):
		self._AggtdQttvData = value if value is not None else base_types.UninitialisedField(self, 'AggtdQttvData', TransactionsBin2, True)

	@AggtdQttvData.deleter
	def AggtdQttvData(self):
		del self._AggtdQttvData
		self._AggtdQttvData = base_types.UninitialisedField(self, 'AggtdQttvData', TransactionsBin2, True)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', ISINOct2015Identifier, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', ISINOct2015Identifier, False)

	@property
	def NbTxs(self):
		return self._NbTxs

	@NbTxs.setter
	def NbTxs(self, value):
		self._NbTxs = value if value is not None else base_types.UninitialisedField(self, 'NbTxs', Number, False)

	@NbTxs.deleter
	def NbTxs(self):
		del self._NbTxs
		self._NbTxs = base_types.UninitialisedField(self, 'NbTxs', Number, False)

	@property
	def RptgDt(self):
		return self._RptgDt

	@RptgDt.setter
	def RptgDt(self, value):
		self._RptgDt = value if value is not None else base_types.UninitialisedField(self, 'RptgDt', ISODate, False)

	@RptgDt.deleter
	def RptgDt(self):
		del self._RptgDt
		self._RptgDt = base_types.UninitialisedField(self, 'RptgDt', ISODate, False)

	@property
	def Sspnsn(self):
		return self._Sspnsn

	@Sspnsn.setter
	def Sspnsn(self, value):
		self._Sspnsn = value if value is not None else base_types.UninitialisedField(self, 'Sspnsn', TrueFalseIndicator, False)

	@Sspnsn.deleter
	def Sspnsn(self):
		del self._Sspnsn
		self._Sspnsn = base_types.UninitialisedField(self, 'Sspnsn', TrueFalseIndicator, False)

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if value is not None else base_types.UninitialisedField(self, 'TechRcrdId', Max35Text, False)

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = base_types.UninitialisedField(self, 'TechRcrdId', Max35Text, False)

	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if value is not None else base_types.UninitialisedField(self, 'TradgVn', MICIdentifier, False)

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = base_types.UninitialisedField(self, 'TradgVn', MICIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AggtdQttvData', type=TransactionsBin2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbTxs', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sspnsn', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVn', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
	))