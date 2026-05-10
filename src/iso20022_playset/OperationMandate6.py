from . import base_types
from .PartyAndAuthorisation6 import PartyAndAuthorisation6
from .Max35Text import Max35Text
from .BankTransactionCodeStructure4 import BankTransactionCodeStructure4
from .Modification1Code import Modification1Code
from .ISODate import ISODate
from .Max15PlusSignedNumericText import Max15PlusSignedNumericText
from .YesNoIndicator import YesNoIndicator
from .Channel2Choice import Channel2Choice

class OperationMandate6(base_types._BaseFieldType):

	__slots__ = ["_EndDt", "_SgntrOrdrInd", "_Id", "_ReqrdSgntrNb", "_AplblChanl", "_ModCd", "_MndtHldr", "_BkOpr", "_StartDt"]
	@property
	def EndDt(self):
		return self._EndDt

	@EndDt.setter
	def EndDt(self, value):
		self._EndDt = value if type(value) != base_types.auto else self.make_default("EndDt")

	@EndDt.deleter
	def EndDt(self):
		del self._EndDt
		self._EndDt = None

	@property
	def SgntrOrdrInd(self):
		return self._SgntrOrdrInd

	@SgntrOrdrInd.setter
	def SgntrOrdrInd(self, value):
		self._SgntrOrdrInd = value if type(value) != base_types.auto else self.make_default("SgntrOrdrInd")

	@SgntrOrdrInd.deleter
	def SgntrOrdrInd(self):
		del self._SgntrOrdrInd
		self._SgntrOrdrInd = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def ReqrdSgntrNb(self):
		return self._ReqrdSgntrNb

	@ReqrdSgntrNb.setter
	def ReqrdSgntrNb(self, value):
		self._ReqrdSgntrNb = value if type(value) != base_types.auto else self.make_default("ReqrdSgntrNb")

	@ReqrdSgntrNb.deleter
	def ReqrdSgntrNb(self):
		del self._ReqrdSgntrNb
		self._ReqrdSgntrNb = None

	@property
	def AplblChanl(self):
		return self._AplblChanl

	@AplblChanl.setter
	def AplblChanl(self, value):
		self._AplblChanl = value if type(value) != base_types.auto else self.make_default("AplblChanl")

	@AplblChanl.deleter
	def AplblChanl(self):
		del self._AplblChanl
		self._AplblChanl = None

	@property
	def ModCd(self):
		return self._ModCd

	@ModCd.setter
	def ModCd(self, value):
		self._ModCd = value if type(value) != base_types.auto else self.make_default("ModCd")

	@ModCd.deleter
	def ModCd(self):
		del self._ModCd
		self._ModCd = None

	@property
	def MndtHldr(self):
		return self._MndtHldr

	@MndtHldr.setter
	def MndtHldr(self, value):
		self._MndtHldr = value if type(value) != base_types.auto else self.make_default("MndtHldr")

	@MndtHldr.deleter
	def MndtHldr(self):
		del self._MndtHldr
		self._MndtHldr = None

	@property
	def BkOpr(self):
		return self._BkOpr

	@BkOpr.setter
	def BkOpr(self, value):
		self._BkOpr = value if type(value) != base_types.auto else self.make_default("BkOpr")

	@BkOpr.deleter
	def BkOpr(self):
		del self._BkOpr
		self._BkOpr = None

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if type(value) != base_types.auto else self.make_default("StartDt")

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EndDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgntrOrdrInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqrdSgntrNb', type=Max15PlusSignedNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AplblChanl', type=Channel2Choice, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ModCd', type=Modification1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtHldr', type=PartyAndAuthorisation6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BkOpr', type=BankTransactionCodeStructure4, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StartDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

