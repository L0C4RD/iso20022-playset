import base_types
import SupplementaryData1
import SettlementInternaliser1
import IssuerCSDReport1
import SettlementInternaliserReportHeader1

class SettlementInternaliserReportV01(base_types._BaseFieldType):

	__slots__ = ["_SttlmIntlr", "_SplmtryData", "_RptHdr", "_IssrCSD"]
	@property
	def SttlmIntlr(self):
		return self._SttlmIntlr

	@SttlmIntlr.setter
	def SttlmIntlr(self, value):
		self._SttlmIntlr = value if type(value) != auto else self.make_default("SttlmIntlr")

	@SttlmIntlr.deleter
	def SttlmIntlr(self):
		del self._SttlmIntlr
		self._SttlmIntlr = None

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
	def RptHdr(self):
		return self._RptHdr

	@RptHdr.setter
	def RptHdr(self, value):
		self._RptHdr = value if type(value) != auto else self.make_default("RptHdr")

	@RptHdr.deleter
	def RptHdr(self):
		del self._RptHdr
		self._RptHdr = None

	@property
	def IssrCSD(self):
		return self._IssrCSD

	@IssrCSD.setter
	def IssrCSD(self, value):
		self._IssrCSD = value if type(value) != auto else self.make_default("IssrCSD")

	@IssrCSD.deleter
	def IssrCSD(self):
		del self._IssrCSD
		self._IssrCSD = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SttlmIntlr', type=SettlementInternaliser1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptHdr', type=SettlementInternaliserReportHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrCSD', type=IssuerCSDReport1, min=1, max=None, mutex_group=None, array=True),
	))

