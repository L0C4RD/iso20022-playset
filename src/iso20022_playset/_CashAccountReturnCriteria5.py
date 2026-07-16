# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashBalanceReturnCriteria2
from . import RequestedIndicator

class CashAccountReturnCriteria5(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnrInd", "_AcctSvcrInd", "_BilBalRtrCrit", "_BilLmtInd", "_CcyInd", "_MulBalRtrCrit", "_MulLmtInd", "_NmInd", "_StgOrdrInd", "_TpInd"]
	@property
	def AcctOwnrInd(self):
		return self._AcctOwnrInd

	@AcctOwnrInd.setter
	def AcctOwnrInd(self, value):
		self._AcctOwnrInd = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnrInd', RequestedIndicator, False)

	@AcctOwnrInd.deleter
	def AcctOwnrInd(self):
		del self._AcctOwnrInd
		self._AcctOwnrInd = base_types.UninitialisedField(self, 'AcctOwnrInd', RequestedIndicator, False)

	@property
	def AcctSvcrInd(self):
		return self._AcctSvcrInd

	@AcctSvcrInd.setter
	def AcctSvcrInd(self, value):
		self._AcctSvcrInd = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcrInd', RequestedIndicator, False)

	@AcctSvcrInd.deleter
	def AcctSvcrInd(self):
		del self._AcctSvcrInd
		self._AcctSvcrInd = base_types.UninitialisedField(self, 'AcctSvcrInd', RequestedIndicator, False)

	@property
	def BilBalRtrCrit(self):
		return self._BilBalRtrCrit

	@BilBalRtrCrit.setter
	def BilBalRtrCrit(self, value):
		self._BilBalRtrCrit = value if value is not None else base_types.UninitialisedField(self, 'BilBalRtrCrit', CashBalanceReturnCriteria2, False)

	@BilBalRtrCrit.deleter
	def BilBalRtrCrit(self):
		del self._BilBalRtrCrit
		self._BilBalRtrCrit = base_types.UninitialisedField(self, 'BilBalRtrCrit', CashBalanceReturnCriteria2, False)

	@property
	def BilLmtInd(self):
		return self._BilLmtInd

	@BilLmtInd.setter
	def BilLmtInd(self, value):
		self._BilLmtInd = value if value is not None else base_types.UninitialisedField(self, 'BilLmtInd', RequestedIndicator, False)

	@BilLmtInd.deleter
	def BilLmtInd(self):
		del self._BilLmtInd
		self._BilLmtInd = base_types.UninitialisedField(self, 'BilLmtInd', RequestedIndicator, False)

	@property
	def CcyInd(self):
		return self._CcyInd

	@CcyInd.setter
	def CcyInd(self, value):
		self._CcyInd = value if value is not None else base_types.UninitialisedField(self, 'CcyInd', RequestedIndicator, False)

	@CcyInd.deleter
	def CcyInd(self):
		del self._CcyInd
		self._CcyInd = base_types.UninitialisedField(self, 'CcyInd', RequestedIndicator, False)

	@property
	def MulBalRtrCrit(self):
		return self._MulBalRtrCrit

	@MulBalRtrCrit.setter
	def MulBalRtrCrit(self, value):
		self._MulBalRtrCrit = value if value is not None else base_types.UninitialisedField(self, 'MulBalRtrCrit', CashBalanceReturnCriteria2, False)

	@MulBalRtrCrit.deleter
	def MulBalRtrCrit(self):
		del self._MulBalRtrCrit
		self._MulBalRtrCrit = base_types.UninitialisedField(self, 'MulBalRtrCrit', CashBalanceReturnCriteria2, False)

	@property
	def MulLmtInd(self):
		return self._MulLmtInd

	@MulLmtInd.setter
	def MulLmtInd(self, value):
		self._MulLmtInd = value if value is not None else base_types.UninitialisedField(self, 'MulLmtInd', RequestedIndicator, False)

	@MulLmtInd.deleter
	def MulLmtInd(self):
		del self._MulLmtInd
		self._MulLmtInd = base_types.UninitialisedField(self, 'MulLmtInd', RequestedIndicator, False)

	@property
	def NmInd(self):
		return self._NmInd

	@NmInd.setter
	def NmInd(self, value):
		self._NmInd = value if value is not None else base_types.UninitialisedField(self, 'NmInd', RequestedIndicator, False)

	@NmInd.deleter
	def NmInd(self):
		del self._NmInd
		self._NmInd = base_types.UninitialisedField(self, 'NmInd', RequestedIndicator, False)

	@property
	def StgOrdrInd(self):
		return self._StgOrdrInd

	@StgOrdrInd.setter
	def StgOrdrInd(self, value):
		self._StgOrdrInd = value if value is not None else base_types.UninitialisedField(self, 'StgOrdrInd', RequestedIndicator, False)

	@StgOrdrInd.deleter
	def StgOrdrInd(self):
		del self._StgOrdrInd
		self._StgOrdrInd = base_types.UninitialisedField(self, 'StgOrdrInd', RequestedIndicator, False)

	@property
	def TpInd(self):
		return self._TpInd

	@TpInd.setter
	def TpInd(self, value):
		self._TpInd = value if value is not None else base_types.UninitialisedField(self, 'TpInd', RequestedIndicator, False)

	@TpInd.deleter
	def TpInd(self):
		del self._TpInd
		self._TpInd = base_types.UninitialisedField(self, 'TpInd', RequestedIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BilBalRtrCrit', type=CashBalanceReturnCriteria2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BilLmtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MulBalRtrCrit', type=CashBalanceReturnCriteria2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MulLmtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgOrdrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))