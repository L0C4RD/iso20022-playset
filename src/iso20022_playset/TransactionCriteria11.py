from . import base_types
import ReportIndicator1Code
import TransactionReturnCriteria5
import Max35Text
import TransactionSearchCriteria11

class TransactionCriteria11(base_types._BaseFieldType):

	__slots__ = ["_NewQryNm", "_RtrCrit", "_StmtRpt", "_SchCrit"]
	@property
	def NewQryNm(self):
		return self._NewQryNm

	@NewQryNm.setter
	def NewQryNm(self, value):
		self._NewQryNm = value if type(value) != auto else self.make_default("NewQryNm")

	@NewQryNm.deleter
	def NewQryNm(self):
		del self._NewQryNm
		self._NewQryNm = None

	@property
	def RtrCrit(self):
		return self._RtrCrit

	@RtrCrit.setter
	def RtrCrit(self, value):
		self._RtrCrit = value if type(value) != auto else self.make_default("RtrCrit")

	@RtrCrit.deleter
	def RtrCrit(self):
		del self._RtrCrit
		self._RtrCrit = None

	@property
	def StmtRpt(self):
		return self._StmtRpt

	@StmtRpt.setter
	def StmtRpt(self, value):
		self._StmtRpt = value if type(value) != auto else self.make_default("StmtRpt")

	@StmtRpt.deleter
	def StmtRpt(self):
		del self._StmtRpt
		self._StmtRpt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='NewQryNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrCrit', type=TransactionReturnCriteria5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtRpt', type=ReportIndicator1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchCrit', type=TransactionSearchCriteria11, min=0, max=None, mutex_group=None, array=True),
	))

