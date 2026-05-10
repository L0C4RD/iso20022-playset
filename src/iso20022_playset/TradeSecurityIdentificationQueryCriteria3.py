import base_types
import ISINQueryCriteria1
import FinancialInstrumentContractType2Code
import SecurityIdentificationQueryCriteria1
import Operation3Code
import SecurityIdentificationQuery4Choice
import UPIQueryCriteria1

class TradeSecurityIdentificationQueryCriteria3(base_types._BaseFieldType):

	__slots__ = ["_ISIN", "_CtrctTp", "_Id", "_Oprtr", "_UndrlygInstrmId", "_UnqPdctIdr"]
	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if type(value) != auto else self.make_default("ISIN")

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = None

	@property
	def CtrctTp(self):
		return self._CtrctTp

	@CtrctTp.setter
	def CtrctTp(self, value):
		self._CtrctTp = value if type(value) != auto else self.make_default("CtrctTp")

	@CtrctTp.deleter
	def CtrctTp(self):
		del self._CtrctTp
		self._CtrctTp = None

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
	def Oprtr(self):
		return self._Oprtr

	@Oprtr.setter
	def Oprtr(self, value):
		self._Oprtr = value if type(value) != auto else self.make_default("Oprtr")

	@Oprtr.deleter
	def Oprtr(self):
		del self._Oprtr
		self._Oprtr = None

	@property
	def UndrlygInstrmId(self):
		return self._UndrlygInstrmId

	@UndrlygInstrmId.setter
	def UndrlygInstrmId(self, value):
		self._UndrlygInstrmId = value if type(value) != auto else self.make_default("UndrlygInstrmId")

	@UndrlygInstrmId.deleter
	def UndrlygInstrmId(self):
		del self._UndrlygInstrmId
		self._UndrlygInstrmId = None

	@property
	def UnqPdctIdr(self):
		return self._UnqPdctIdr

	@UnqPdctIdr.setter
	def UnqPdctIdr(self, value):
		self._UnqPdctIdr = value if type(value) != auto else self.make_default("UnqPdctIdr")

	@UnqPdctIdr.deleter
	def UnqPdctIdr(self):
		del self._UnqPdctIdr
		self._UnqPdctIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ISIN', type=ISINQueryCriteria1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrctTp', type=FinancialInstrumentContractType2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=SecurityIdentificationQueryCriteria1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Oprtr', type=Operation3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygInstrmId', type=SecurityIdentificationQuery4Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UnqPdctIdr', type=UPIQueryCriteria1, min=0, max=None, mutex_group=None, array=True),
	))

