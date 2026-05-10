from . import base_types
import MessageHeader7
import SupplementaryData1
import ResendSearchCriteria2

class ResendRequestV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_RsndSchCrit", "_MsgHdr"]
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
	def RsndSchCrit(self):
		return self._RsndSchCrit

	@RsndSchCrit.setter
	def RsndSchCrit(self, value):
		self._RsndSchCrit = value if type(value) != auto else self.make_default("RsndSchCrit")

	@RsndSchCrit.deleter
	def RsndSchCrit(self):
		del self._RsndSchCrit
		self._RsndSchCrit = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RsndSchCrit', type=ResendSearchCriteria2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader7, min=1, max=1, mutex_group=None, array=False),
	))

