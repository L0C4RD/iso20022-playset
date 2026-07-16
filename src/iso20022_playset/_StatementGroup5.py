# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BillingStatement5
from . import Contact13
from . import Max35Text
from . import PartyIdentification273

class StatementGroup5(base_types._BaseFieldType):

	__slots__ = ["_BllgStmt", "_GrpId", "_Rcvr", "_RcvrIndvCtct", "_Sndr", "_SndrIndvCtct"]
	@property
	def BllgStmt(self):
		return self._BllgStmt

	@BllgStmt.setter
	def BllgStmt(self, value):
		self._BllgStmt = value if value is not None else base_types.UninitialisedField(self, 'BllgStmt', BillingStatement5, True)

	@BllgStmt.deleter
	def BllgStmt(self):
		del self._BllgStmt
		self._BllgStmt = base_types.UninitialisedField(self, 'BllgStmt', BillingStatement5, True)

	@property
	def GrpId(self):
		return self._GrpId

	@GrpId.setter
	def GrpId(self, value):
		self._GrpId = value if value is not None else base_types.UninitialisedField(self, 'GrpId', Max35Text, False)

	@GrpId.deleter
	def GrpId(self):
		del self._GrpId
		self._GrpId = base_types.UninitialisedField(self, 'GrpId', Max35Text, False)

	@property
	def Rcvr(self):
		return self._Rcvr

	@Rcvr.setter
	def Rcvr(self, value):
		self._Rcvr = value if value is not None else base_types.UninitialisedField(self, 'Rcvr', PartyIdentification273, False)

	@Rcvr.deleter
	def Rcvr(self):
		del self._Rcvr
		self._Rcvr = base_types.UninitialisedField(self, 'Rcvr', PartyIdentification273, False)

	@property
	def RcvrIndvCtct(self):
		return self._RcvrIndvCtct

	@RcvrIndvCtct.setter
	def RcvrIndvCtct(self, value):
		self._RcvrIndvCtct = value if value is not None else base_types.UninitialisedField(self, 'RcvrIndvCtct', Contact13, True)

	@RcvrIndvCtct.deleter
	def RcvrIndvCtct(self):
		del self._RcvrIndvCtct
		self._RcvrIndvCtct = base_types.UninitialisedField(self, 'RcvrIndvCtct', Contact13, True)

	@property
	def Sndr(self):
		return self._Sndr

	@Sndr.setter
	def Sndr(self, value):
		self._Sndr = value if value is not None else base_types.UninitialisedField(self, 'Sndr', PartyIdentification273, False)

	@Sndr.deleter
	def Sndr(self):
		del self._Sndr
		self._Sndr = base_types.UninitialisedField(self, 'Sndr', PartyIdentification273, False)

	@property
	def SndrIndvCtct(self):
		return self._SndrIndvCtct

	@SndrIndvCtct.setter
	def SndrIndvCtct(self, value):
		self._SndrIndvCtct = value if value is not None else base_types.UninitialisedField(self, 'SndrIndvCtct', Contact13, True)

	@SndrIndvCtct.deleter
	def SndrIndvCtct(self):
		del self._SndrIndvCtct
		self._SndrIndvCtct = base_types.UninitialisedField(self, 'SndrIndvCtct', Contact13, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BllgStmt', type=BillingStatement5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrpId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcvr', type=PartyIdentification273, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvrIndvCtct', type=Contact13, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sndr', type=PartyIdentification273, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndrIndvCtct', type=Contact13, min=0, max=2, mutex_group=None, array=True),
	))