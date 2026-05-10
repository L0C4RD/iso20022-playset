from . import base_types
from .Pagination1 import Pagination1
from .SupplementaryData1 import SupplementaryData1
from .MessageHeader1 import MessageHeader1
from .SecuritiesAccountStatement2 import SecuritiesAccountStatement2

class SecuritiesAccountActivityAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_SplmtryData", "_Pgntn", "_SctiesAcctActvty"]
	@property
	def MsgHdr(self):
		return self._MsgHdr

	@MsgHdr.setter
	def MsgHdr(self, value):
		self._MsgHdr = value if type(value) != auto else self.make_default("MsgHdr")

	@MsgHdr.deleter
	def MsgHdr(self):
		del self._MsgHdr
		self._MsgHdr = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	@property
	def SctiesAcctActvty(self):
		return self._SctiesAcctActvty

	@SctiesAcctActvty.setter
	def SctiesAcctActvty(self, value):
		self._SctiesAcctActvty = value if type(value) != auto else self.make_default("SctiesAcctActvty")

	@SctiesAcctActvty.deleter
	def SctiesAcctActvty(self):
		del self._SctiesAcctActvty
		self._SctiesAcctActvty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesAcctActvty', type=SecuritiesAccountStatement2, min=1, max=1, mutex_group=None, array=False),
	))

