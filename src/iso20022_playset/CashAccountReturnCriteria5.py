import base_types
import RequestedIndicator
import CashBalanceReturnCriteria2

class CashAccountReturnCriteria5(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnrInd", "_MulBalRtrCrit", "_MulLmtInd", "_BilBalRtrCrit", "_StgOrdrInd", "_CcyInd", "_NmInd", "_TpInd", "_AcctSvcrInd", "_BilLmtInd"]
	@property
	def AcctOwnrInd(self):
		return self._AcctOwnrInd

	@AcctOwnrInd.setter
	def AcctOwnrInd(self, value):
		self._AcctOwnrInd = value if type(value) != auto else self.make_default("AcctOwnrInd")

	@AcctOwnrInd.deleter
	def AcctOwnrInd(self):
		del self._AcctOwnrInd
		self._AcctOwnrInd = None

	@property
	def MulBalRtrCrit(self):
		return self._MulBalRtrCrit

	@MulBalRtrCrit.setter
	def MulBalRtrCrit(self, value):
		self._MulBalRtrCrit = value if type(value) != auto else self.make_default("MulBalRtrCrit")

	@MulBalRtrCrit.deleter
	def MulBalRtrCrit(self):
		del self._MulBalRtrCrit
		self._MulBalRtrCrit = None

	@property
	def MulLmtInd(self):
		return self._MulLmtInd

	@MulLmtInd.setter
	def MulLmtInd(self, value):
		self._MulLmtInd = value if type(value) != auto else self.make_default("MulLmtInd")

	@MulLmtInd.deleter
	def MulLmtInd(self):
		del self._MulLmtInd
		self._MulLmtInd = None

	@property
	def BilBalRtrCrit(self):
		return self._BilBalRtrCrit

	@BilBalRtrCrit.setter
	def BilBalRtrCrit(self, value):
		self._BilBalRtrCrit = value if type(value) != auto else self.make_default("BilBalRtrCrit")

	@BilBalRtrCrit.deleter
	def BilBalRtrCrit(self):
		del self._BilBalRtrCrit
		self._BilBalRtrCrit = None

	@property
	def StgOrdrInd(self):
		return self._StgOrdrInd

	@StgOrdrInd.setter
	def StgOrdrInd(self, value):
		self._StgOrdrInd = value if type(value) != auto else self.make_default("StgOrdrInd")

	@StgOrdrInd.deleter
	def StgOrdrInd(self):
		del self._StgOrdrInd
		self._StgOrdrInd = None

	@property
	def CcyInd(self):
		return self._CcyInd

	@CcyInd.setter
	def CcyInd(self, value):
		self._CcyInd = value if type(value) != auto else self.make_default("CcyInd")

	@CcyInd.deleter
	def CcyInd(self):
		del self._CcyInd
		self._CcyInd = None

	@property
	def NmInd(self):
		return self._NmInd

	@NmInd.setter
	def NmInd(self, value):
		self._NmInd = value if type(value) != auto else self.make_default("NmInd")

	@NmInd.deleter
	def NmInd(self):
		del self._NmInd
		self._NmInd = None

	@property
	def TpInd(self):
		return self._TpInd

	@TpInd.setter
	def TpInd(self, value):
		self._TpInd = value if type(value) != auto else self.make_default("TpInd")

	@TpInd.deleter
	def TpInd(self):
		del self._TpInd
		self._TpInd = None

	@property
	def AcctSvcrInd(self):
		return self._AcctSvcrInd

	@AcctSvcrInd.setter
	def AcctSvcrInd(self, value):
		self._AcctSvcrInd = value if type(value) != auto else self.make_default("AcctSvcrInd")

	@AcctSvcrInd.deleter
	def AcctSvcrInd(self):
		del self._AcctSvcrInd
		self._AcctSvcrInd = None

	@property
	def BilLmtInd(self):
		return self._BilLmtInd

	@BilLmtInd.setter
	def BilLmtInd(self, value):
		self._BilLmtInd = value if type(value) != auto else self.make_default("BilLmtInd")

	@BilLmtInd.deleter
	def BilLmtInd(self):
		del self._BilLmtInd
		self._BilLmtInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MulBalRtrCrit', type=CashBalanceReturnCriteria2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MulLmtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BilBalRtrCrit', type=CashBalanceReturnCriteria2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgOrdrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BilLmtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))

