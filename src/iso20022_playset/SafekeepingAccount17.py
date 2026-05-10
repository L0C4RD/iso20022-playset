import base_types
import FinancialInstrumentQuantity18Choice
import AccountSubLevel24
import PartyIdentification195Choice
import Max35Text

class SafekeepingAccount17(base_types._BaseFieldType):

	__slots__ = ["_ShrhldgBalOnClntAcct", "_AcctSubLvl", "_SfkpgAcct", "_TtlShrhldgBal", "_AcctSvcr", "_ShrhldgBalOnOwnAcct"]
	@property
	def ShrhldgBalOnClntAcct(self):
		return self._ShrhldgBalOnClntAcct

	@ShrhldgBalOnClntAcct.setter
	def ShrhldgBalOnClntAcct(self, value):
		self._ShrhldgBalOnClntAcct = value if type(value) != auto else self.make_default("ShrhldgBalOnClntAcct")

	@ShrhldgBalOnClntAcct.deleter
	def ShrhldgBalOnClntAcct(self):
		del self._ShrhldgBalOnClntAcct
		self._ShrhldgBalOnClntAcct = None

	@property
	def AcctSubLvl(self):
		return self._AcctSubLvl

	@AcctSubLvl.setter
	def AcctSubLvl(self, value):
		self._AcctSubLvl = value if type(value) != auto else self.make_default("AcctSubLvl")

	@AcctSubLvl.deleter
	def AcctSubLvl(self):
		del self._AcctSubLvl
		self._AcctSubLvl = None

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	@property
	def TtlShrhldgBal(self):
		return self._TtlShrhldgBal

	@TtlShrhldgBal.setter
	def TtlShrhldgBal(self, value):
		self._TtlShrhldgBal = value if type(value) != auto else self.make_default("TtlShrhldgBal")

	@TtlShrhldgBal.deleter
	def TtlShrhldgBal(self):
		del self._TtlShrhldgBal
		self._TtlShrhldgBal = None

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if type(value) != auto else self.make_default("AcctSvcr")

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = None

	@property
	def ShrhldgBalOnOwnAcct(self):
		return self._ShrhldgBalOnOwnAcct

	@ShrhldgBalOnOwnAcct.setter
	def ShrhldgBalOnOwnAcct(self, value):
		self._ShrhldgBalOnOwnAcct = value if type(value) != auto else self.make_default("ShrhldgBalOnOwnAcct")

	@ShrhldgBalOnOwnAcct.deleter
	def ShrhldgBalOnOwnAcct(self):
		del self._ShrhldgBalOnOwnAcct
		self._ShrhldgBalOnOwnAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ShrhldgBalOnClntAcct', type=FinancialInstrumentQuantity18Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSubLvl', type=AccountSubLevel24, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlShrhldgBal', type=FinancialInstrumentQuantity18Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification195Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrhldgBalOnOwnAcct', type=FinancialInstrumentQuantity18Choice, min=1, max=1, mutex_group=None, array=False),
	))

