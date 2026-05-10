import base_types
import DocumentAmount1
import DocumentAdjustment1

class RemittanceAmount4(base_types._BaseFieldType):

	__slots__ = ["_AdjstmntAmtAndRsn", "_RmtAmtAndTp"]
	@property
	def AdjstmntAmtAndRsn(self):
		return self._AdjstmntAmtAndRsn

	@AdjstmntAmtAndRsn.setter
	def AdjstmntAmtAndRsn(self, value):
		self._AdjstmntAmtAndRsn = value if type(value) != auto else self.make_default("AdjstmntAmtAndRsn")

	@AdjstmntAmtAndRsn.deleter
	def AdjstmntAmtAndRsn(self):
		del self._AdjstmntAmtAndRsn
		self._AdjstmntAmtAndRsn = None

	@property
	def RmtAmtAndTp(self):
		return self._RmtAmtAndTp

	@RmtAmtAndTp.setter
	def RmtAmtAndTp(self, value):
		self._RmtAmtAndTp = value if type(value) != auto else self.make_default("RmtAmtAndTp")

	@RmtAmtAndTp.deleter
	def RmtAmtAndTp(self):
		del self._RmtAmtAndTp
		self._RmtAmtAndTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdjstmntAmtAndRsn', type=DocumentAdjustment1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RmtAmtAndTp', type=DocumentAmount1, min=0, max=None, mutex_group=None, array=True),
	))

