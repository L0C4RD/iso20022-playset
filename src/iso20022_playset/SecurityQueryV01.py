import base_types
import GenericIdentification1
import MessageHeader1
import SupplementaryData1
import SecuritiesSearchCriteria4
import SecuritiesReturnCriteria1

class SecurityQueryV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_SmlSetRtrCrit", "_MsgHdr", "_SchCrit", "_ReqTp"]
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
	def SmlSetRtrCrit(self):
		return self._SmlSetRtrCrit

	@SmlSetRtrCrit.setter
	def SmlSetRtrCrit(self, value):
		self._SmlSetRtrCrit = value if type(value) != auto else self.make_default("SmlSetRtrCrit")

	@SmlSetRtrCrit.deleter
	def SmlSetRtrCrit(self):
		del self._SmlSetRtrCrit
		self._SmlSetRtrCrit = None

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
	def SchCrit(self):
		return self._SchCrit

	@SchCrit.setter
	def SchCrit(self, value):
		self._SchCrit = value if type(value) != auto else self.make_default("SchCrit")

	@SchCrit.deleter
	def SchCrit(self):
		del self._SchCrit
		self._SchCrit = None

	@property
	def ReqTp(self):
		return self._ReqTp

	@ReqTp.setter
	def ReqTp(self, value):
		self._ReqTp = value if type(value) != auto else self.make_default("ReqTp")

	@ReqTp.deleter
	def ReqTp(self):
		del self._ReqTp
		self._ReqTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SmlSetRtrCrit', type=SecuritiesReturnCriteria1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchCrit', type=SecuritiesSearchCriteria4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqTp', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
	))

