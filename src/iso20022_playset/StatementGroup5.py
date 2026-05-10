import base_types
import BillingStatement5
import PartyIdentification273
import Contact13
import Max35Text

class StatementGroup5(base_types._BaseFieldType):

	__slots__ = ["_BllgStmt", "_RcvrIndvCtct", "_SndrIndvCtct", "_GrpId", "_Rcvr", "_Sndr"]
	@property
	def BllgStmt(self):
		return self._BllgStmt

	@BllgStmt.setter
	def BllgStmt(self, value):
		self._BllgStmt = value if type(value) != auto else self.make_default("BllgStmt")

	@BllgStmt.deleter
	def BllgStmt(self):
		del self._BllgStmt
		self._BllgStmt = None

	@property
	def RcvrIndvCtct(self):
		return self._RcvrIndvCtct

	@RcvrIndvCtct.setter
	def RcvrIndvCtct(self, value):
		self._RcvrIndvCtct = value if type(value) != auto else self.make_default("RcvrIndvCtct")

	@RcvrIndvCtct.deleter
	def RcvrIndvCtct(self):
		del self._RcvrIndvCtct
		self._RcvrIndvCtct = None

	@property
	def SndrIndvCtct(self):
		return self._SndrIndvCtct

	@SndrIndvCtct.setter
	def SndrIndvCtct(self, value):
		self._SndrIndvCtct = value if type(value) != auto else self.make_default("SndrIndvCtct")

	@SndrIndvCtct.deleter
	def SndrIndvCtct(self):
		del self._SndrIndvCtct
		self._SndrIndvCtct = None

	@property
	def GrpId(self):
		return self._GrpId

	@GrpId.setter
	def GrpId(self, value):
		self._GrpId = value if type(value) != auto else self.make_default("GrpId")

	@GrpId.deleter
	def GrpId(self):
		del self._GrpId
		self._GrpId = None

	@property
	def Rcvr(self):
		return self._Rcvr

	@Rcvr.setter
	def Rcvr(self, value):
		self._Rcvr = value if type(value) != auto else self.make_default("Rcvr")

	@Rcvr.deleter
	def Rcvr(self):
		del self._Rcvr
		self._Rcvr = None

	@property
	def Sndr(self):
		return self._Sndr

	@Sndr.setter
	def Sndr(self, value):
		self._Sndr = value if type(value) != auto else self.make_default("Sndr")

	@Sndr.deleter
	def Sndr(self):
		del self._Sndr
		self._Sndr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BllgStmt', type=BillingStatement5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcvrIndvCtct', type=Contact13, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='SndrIndvCtct', type=Contact13, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrpId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcvr', type=PartyIdentification273, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sndr', type=PartyIdentification273, min=1, max=1, mutex_group=None, array=False),
	))

