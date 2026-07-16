# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BankTransactionCodeStructure4
from . import Channel2Choice
from . import ISODate
from . import Max15PlusSignedNumericText
from . import Max35Text
from . import PartyAndAuthorisation7
from . import YesNoIndicator

class OperationMandate7(base_types._BaseFieldType):

	__slots__ = ["_AplblChanl", "_BkOpr", "_EndDt", "_Id", "_MndtHldr", "_ReqrdSgntrNb", "_SgntrOrdrInd", "_StartDt"]
	@property
	def AplblChanl(self):
		return self._AplblChanl

	@AplblChanl.setter
	def AplblChanl(self, value):
		self._AplblChanl = value if value is not None else base_types.UninitialisedField(self, 'AplblChanl', Channel2Choice, True)

	@AplblChanl.deleter
	def AplblChanl(self):
		del self._AplblChanl
		self._AplblChanl = base_types.UninitialisedField(self, 'AplblChanl', Channel2Choice, True)

	@property
	def BkOpr(self):
		return self._BkOpr

	@BkOpr.setter
	def BkOpr(self, value):
		self._BkOpr = value if value is not None else base_types.UninitialisedField(self, 'BkOpr', BankTransactionCodeStructure4, True)

	@BkOpr.deleter
	def BkOpr(self):
		del self._BkOpr
		self._BkOpr = base_types.UninitialisedField(self, 'BkOpr', BankTransactionCodeStructure4, True)

	@property
	def EndDt(self):
		return self._EndDt

	@EndDt.setter
	def EndDt(self, value):
		self._EndDt = value if value is not None else base_types.UninitialisedField(self, 'EndDt', ISODate, False)

	@EndDt.deleter
	def EndDt(self):
		del self._EndDt
		self._EndDt = base_types.UninitialisedField(self, 'EndDt', ISODate, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def MndtHldr(self):
		return self._MndtHldr

	@MndtHldr.setter
	def MndtHldr(self, value):
		self._MndtHldr = value if value is not None else base_types.UninitialisedField(self, 'MndtHldr', PartyAndAuthorisation7, True)

	@MndtHldr.deleter
	def MndtHldr(self):
		del self._MndtHldr
		self._MndtHldr = base_types.UninitialisedField(self, 'MndtHldr', PartyAndAuthorisation7, True)

	@property
	def ReqrdSgntrNb(self):
		return self._ReqrdSgntrNb

	@ReqrdSgntrNb.setter
	def ReqrdSgntrNb(self, value):
		self._ReqrdSgntrNb = value if value is not None else base_types.UninitialisedField(self, 'ReqrdSgntrNb', Max15PlusSignedNumericText, False)

	@ReqrdSgntrNb.deleter
	def ReqrdSgntrNb(self):
		del self._ReqrdSgntrNb
		self._ReqrdSgntrNb = base_types.UninitialisedField(self, 'ReqrdSgntrNb', Max15PlusSignedNumericText, False)

	@property
	def SgntrOrdrInd(self):
		return self._SgntrOrdrInd

	@SgntrOrdrInd.setter
	def SgntrOrdrInd(self, value):
		self._SgntrOrdrInd = value if value is not None else base_types.UninitialisedField(self, 'SgntrOrdrInd', YesNoIndicator, False)

	@SgntrOrdrInd.deleter
	def SgntrOrdrInd(self):
		del self._SgntrOrdrInd
		self._SgntrOrdrInd = base_types.UninitialisedField(self, 'SgntrOrdrInd', YesNoIndicator, False)

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if value is not None else base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AplblChanl', type=Channel2Choice, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BkOpr', type=BankTransactionCodeStructure4, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EndDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtHldr', type=PartyAndAuthorisation7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqrdSgntrNb', type=Max15PlusSignedNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgntrOrdrInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))