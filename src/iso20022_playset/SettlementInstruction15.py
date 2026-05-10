import base_types
import ClearingSystemIdentification3Choice
import BranchAndFinancialInstitutionIdentification8
import SettlementMethod1Code
import CashAccount40

class SettlementInstruction15(base_types._BaseFieldType):

	__slots__ = ["_InstgRmbrsmntAgtAcct", "_ThrdRmbrsmntAgt", "_SttlmAcct", "_InstgRmbrsmntAgt", "_SttlmMtd", "_ClrSys", "_ThrdRmbrsmntAgtAcct", "_InstdRmbrsmntAgtAcct", "_InstdRmbrsmntAgt"]
	@property
	def InstgRmbrsmntAgtAcct(self):
		return self._InstgRmbrsmntAgtAcct

	@InstgRmbrsmntAgtAcct.setter
	def InstgRmbrsmntAgtAcct(self, value):
		self._InstgRmbrsmntAgtAcct = value if type(value) != auto else self.make_default("InstgRmbrsmntAgtAcct")

	@InstgRmbrsmntAgtAcct.deleter
	def InstgRmbrsmntAgtAcct(self):
		del self._InstgRmbrsmntAgtAcct
		self._InstgRmbrsmntAgtAcct = None

	@property
	def ThrdRmbrsmntAgt(self):
		return self._ThrdRmbrsmntAgt

	@ThrdRmbrsmntAgt.setter
	def ThrdRmbrsmntAgt(self, value):
		self._ThrdRmbrsmntAgt = value if type(value) != auto else self.make_default("ThrdRmbrsmntAgt")

	@ThrdRmbrsmntAgt.deleter
	def ThrdRmbrsmntAgt(self):
		del self._ThrdRmbrsmntAgt
		self._ThrdRmbrsmntAgt = None

	@property
	def SttlmAcct(self):
		return self._SttlmAcct

	@SttlmAcct.setter
	def SttlmAcct(self, value):
		self._SttlmAcct = value if type(value) != auto else self.make_default("SttlmAcct")

	@SttlmAcct.deleter
	def SttlmAcct(self):
		del self._SttlmAcct
		self._SttlmAcct = None

	@property
	def InstgRmbrsmntAgt(self):
		return self._InstgRmbrsmntAgt

	@InstgRmbrsmntAgt.setter
	def InstgRmbrsmntAgt(self, value):
		self._InstgRmbrsmntAgt = value if type(value) != auto else self.make_default("InstgRmbrsmntAgt")

	@InstgRmbrsmntAgt.deleter
	def InstgRmbrsmntAgt(self):
		del self._InstgRmbrsmntAgt
		self._InstgRmbrsmntAgt = None

	@property
	def SttlmMtd(self):
		return self._SttlmMtd

	@SttlmMtd.setter
	def SttlmMtd(self, value):
		self._SttlmMtd = value if type(value) != auto else self.make_default("SttlmMtd")

	@SttlmMtd.deleter
	def SttlmMtd(self):
		del self._SttlmMtd
		self._SttlmMtd = None

	@property
	def ClrSys(self):
		return self._ClrSys

	@ClrSys.setter
	def ClrSys(self, value):
		self._ClrSys = value if type(value) != auto else self.make_default("ClrSys")

	@ClrSys.deleter
	def ClrSys(self):
		del self._ClrSys
		self._ClrSys = None

	@property
	def ThrdRmbrsmntAgtAcct(self):
		return self._ThrdRmbrsmntAgtAcct

	@ThrdRmbrsmntAgtAcct.setter
	def ThrdRmbrsmntAgtAcct(self, value):
		self._ThrdRmbrsmntAgtAcct = value if type(value) != auto else self.make_default("ThrdRmbrsmntAgtAcct")

	@ThrdRmbrsmntAgtAcct.deleter
	def ThrdRmbrsmntAgtAcct(self):
		del self._ThrdRmbrsmntAgtAcct
		self._ThrdRmbrsmntAgtAcct = None

	@property
	def InstdRmbrsmntAgtAcct(self):
		return self._InstdRmbrsmntAgtAcct

	@InstdRmbrsmntAgtAcct.setter
	def InstdRmbrsmntAgtAcct(self, value):
		self._InstdRmbrsmntAgtAcct = value if type(value) != auto else self.make_default("InstdRmbrsmntAgtAcct")

	@InstdRmbrsmntAgtAcct.deleter
	def InstdRmbrsmntAgtAcct(self):
		del self._InstdRmbrsmntAgtAcct
		self._InstdRmbrsmntAgtAcct = None

	@property
	def InstdRmbrsmntAgt(self):
		return self._InstdRmbrsmntAgt

	@InstdRmbrsmntAgt.setter
	def InstdRmbrsmntAgt(self, value):
		self._InstdRmbrsmntAgt = value if type(value) != auto else self.make_default("InstdRmbrsmntAgt")

	@InstdRmbrsmntAgt.deleter
	def InstdRmbrsmntAgt(self):
		del self._InstdRmbrsmntAgt
		self._InstdRmbrsmntAgt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstgRmbrsmntAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrdRmbrsmntAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgRmbrsmntAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmMtd', type=SettlementMethod1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrSys', type=ClearingSystemIdentification3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrdRmbrsmntAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdRmbrsmntAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdRmbrsmntAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
	))

