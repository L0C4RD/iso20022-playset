# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import SecuritiesTransactionPrice2Choice

class OrderPriceData2(base_types._BaseFieldType):

	__slots__ = ["_AddtlLmtPric", "_CcyScndLeg", "_LmtPric", "_PggdPric", "_StopPric"]
	@property
	def AddtlLmtPric(self):
		return self._AddtlLmtPric

	@AddtlLmtPric.setter
	def AddtlLmtPric(self, value):
		self._AddtlLmtPric = value if value is not None else base_types.UninitialisedField(self, 'AddtlLmtPric', SecuritiesTransactionPrice2Choice, False)

	@AddtlLmtPric.deleter
	def AddtlLmtPric(self):
		del self._AddtlLmtPric
		self._AddtlLmtPric = base_types.UninitialisedField(self, 'AddtlLmtPric', SecuritiesTransactionPrice2Choice, False)

	@property
	def CcyScndLeg(self):
		return self._CcyScndLeg

	@CcyScndLeg.setter
	def CcyScndLeg(self, value):
		self._CcyScndLeg = value if value is not None else base_types.UninitialisedField(self, 'CcyScndLeg', ActiveOrHistoricCurrencyCode, False)

	@CcyScndLeg.deleter
	def CcyScndLeg(self):
		del self._CcyScndLeg
		self._CcyScndLeg = base_types.UninitialisedField(self, 'CcyScndLeg', ActiveOrHistoricCurrencyCode, False)

	@property
	def LmtPric(self):
		return self._LmtPric

	@LmtPric.setter
	def LmtPric(self, value):
		self._LmtPric = value if value is not None else base_types.UninitialisedField(self, 'LmtPric', SecuritiesTransactionPrice2Choice, False)

	@LmtPric.deleter
	def LmtPric(self):
		del self._LmtPric
		self._LmtPric = base_types.UninitialisedField(self, 'LmtPric', SecuritiesTransactionPrice2Choice, False)

	@property
	def PggdPric(self):
		return self._PggdPric

	@PggdPric.setter
	def PggdPric(self, value):
		self._PggdPric = value if value is not None else base_types.UninitialisedField(self, 'PggdPric', SecuritiesTransactionPrice2Choice, False)

	@PggdPric.deleter
	def PggdPric(self):
		del self._PggdPric
		self._PggdPric = base_types.UninitialisedField(self, 'PggdPric', SecuritiesTransactionPrice2Choice, False)

	@property
	def StopPric(self):
		return self._StopPric

	@StopPric.setter
	def StopPric(self, value):
		self._StopPric = value if value is not None else base_types.UninitialisedField(self, 'StopPric', SecuritiesTransactionPrice2Choice, False)

	@StopPric.deleter
	def StopPric(self):
		del self._StopPric
		self._StopPric = base_types.UninitialisedField(self, 'StopPric', SecuritiesTransactionPrice2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlLmtPric', type=SecuritiesTransactionPrice2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyScndLeg', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LmtPric', type=SecuritiesTransactionPrice2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PggdPric', type=SecuritiesTransactionPrice2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StopPric', type=SecuritiesTransactionPrice2Choice, min=0, max=1, mutex_group=None, array=False),
	))