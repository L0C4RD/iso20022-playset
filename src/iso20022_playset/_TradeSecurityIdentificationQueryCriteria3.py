# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentContractType2Code
from . import ISINQueryCriteria1
from . import Operation3Code
from . import SecurityIdentificationQuery4Choice
from . import SecurityIdentificationQueryCriteria1
from . import UPIQueryCriteria1

class TradeSecurityIdentificationQueryCriteria3(base_types._BaseFieldType):

	__slots__ = ["_CtrctTp", "_ISIN", "_Id", "_Oprtr", "_UndrlygInstrmId", "_UnqPdctIdr"]
	@property
	def CtrctTp(self):
		return self._CtrctTp

	@CtrctTp.setter
	def CtrctTp(self, value):
		self._CtrctTp = value if value is not None else base_types.UninitialisedField(self, 'CtrctTp', FinancialInstrumentContractType2Code, True)

	@CtrctTp.deleter
	def CtrctTp(self):
		del self._CtrctTp
		self._CtrctTp = base_types.UninitialisedField(self, 'CtrctTp', FinancialInstrumentContractType2Code, True)

	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if value is not None else base_types.UninitialisedField(self, 'ISIN', ISINQueryCriteria1, True)

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = base_types.UninitialisedField(self, 'ISIN', ISINQueryCriteria1, True)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', SecurityIdentificationQueryCriteria1, True)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', SecurityIdentificationQueryCriteria1, True)

	@property
	def Oprtr(self):
		return self._Oprtr

	@Oprtr.setter
	def Oprtr(self, value):
		self._Oprtr = value if value is not None else base_types.UninitialisedField(self, 'Oprtr', Operation3Code, False)

	@Oprtr.deleter
	def Oprtr(self):
		del self._Oprtr
		self._Oprtr = base_types.UninitialisedField(self, 'Oprtr', Operation3Code, False)

	@property
	def UndrlygInstrmId(self):
		return self._UndrlygInstrmId

	@UndrlygInstrmId.setter
	def UndrlygInstrmId(self, value):
		self._UndrlygInstrmId = value if value is not None else base_types.UninitialisedField(self, 'UndrlygInstrmId', SecurityIdentificationQuery4Choice, True)

	@UndrlygInstrmId.deleter
	def UndrlygInstrmId(self):
		del self._UndrlygInstrmId
		self._UndrlygInstrmId = base_types.UninitialisedField(self, 'UndrlygInstrmId', SecurityIdentificationQuery4Choice, True)

	@property
	def UnqPdctIdr(self):
		return self._UnqPdctIdr

	@UnqPdctIdr.setter
	def UnqPdctIdr(self, value):
		self._UnqPdctIdr = value if value is not None else base_types.UninitialisedField(self, 'UnqPdctIdr', UPIQueryCriteria1, True)

	@UnqPdctIdr.deleter
	def UnqPdctIdr(self):
		del self._UnqPdctIdr
		self._UnqPdctIdr = base_types.UninitialisedField(self, 'UnqPdctIdr', UPIQueryCriteria1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrctTp', type=FinancialInstrumentContractType2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ISIN', type=ISINQueryCriteria1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=SecurityIdentificationQueryCriteria1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Oprtr', type=Operation3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygInstrmId', type=SecurityIdentificationQuery4Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UnqPdctIdr', type=UPIQueryCriteria1, min=0, max=None, mutex_group=None, array=True),
	))