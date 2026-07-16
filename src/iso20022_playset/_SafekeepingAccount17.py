# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountSubLevel24
from . import FinancialInstrumentQuantity18Choice
from . import Max35Text
from . import PartyIdentification195Choice

class SafekeepingAccount17(base_types._BaseFieldType):

	__slots__ = ["_AcctSubLvl", "_AcctSvcr", "_SfkpgAcct", "_ShrhldgBalOnClntAcct", "_ShrhldgBalOnOwnAcct", "_TtlShrhldgBal"]
	@property
	def AcctSubLvl(self):
		return self._AcctSubLvl

	@AcctSubLvl.setter
	def AcctSubLvl(self, value):
		self._AcctSubLvl = value if value is not None else base_types.UninitialisedField(self, 'AcctSubLvl', AccountSubLevel24, False)

	@AcctSubLvl.deleter
	def AcctSubLvl(self):
		del self._AcctSubLvl
		self._AcctSubLvl = base_types.UninitialisedField(self, 'AcctSubLvl', AccountSubLevel24, False)

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcr', PartyIdentification195Choice, False)

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = base_types.UninitialisedField(self, 'AcctSvcr', PartyIdentification195Choice, False)

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', Max35Text, False)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', Max35Text, False)

	@property
	def ShrhldgBalOnClntAcct(self):
		return self._ShrhldgBalOnClntAcct

	@ShrhldgBalOnClntAcct.setter
	def ShrhldgBalOnClntAcct(self, value):
		self._ShrhldgBalOnClntAcct = value if value is not None else base_types.UninitialisedField(self, 'ShrhldgBalOnClntAcct', FinancialInstrumentQuantity18Choice, False)

	@ShrhldgBalOnClntAcct.deleter
	def ShrhldgBalOnClntAcct(self):
		del self._ShrhldgBalOnClntAcct
		self._ShrhldgBalOnClntAcct = base_types.UninitialisedField(self, 'ShrhldgBalOnClntAcct', FinancialInstrumentQuantity18Choice, False)

	@property
	def ShrhldgBalOnOwnAcct(self):
		return self._ShrhldgBalOnOwnAcct

	@ShrhldgBalOnOwnAcct.setter
	def ShrhldgBalOnOwnAcct(self, value):
		self._ShrhldgBalOnOwnAcct = value if value is not None else base_types.UninitialisedField(self, 'ShrhldgBalOnOwnAcct', FinancialInstrumentQuantity18Choice, False)

	@ShrhldgBalOnOwnAcct.deleter
	def ShrhldgBalOnOwnAcct(self):
		del self._ShrhldgBalOnOwnAcct
		self._ShrhldgBalOnOwnAcct = base_types.UninitialisedField(self, 'ShrhldgBalOnOwnAcct', FinancialInstrumentQuantity18Choice, False)

	@property
	def TtlShrhldgBal(self):
		return self._TtlShrhldgBal

	@TtlShrhldgBal.setter
	def TtlShrhldgBal(self, value):
		self._TtlShrhldgBal = value if value is not None else base_types.UninitialisedField(self, 'TtlShrhldgBal', FinancialInstrumentQuantity18Choice, False)

	@TtlShrhldgBal.deleter
	def TtlShrhldgBal(self):
		del self._TtlShrhldgBal
		self._TtlShrhldgBal = base_types.UninitialisedField(self, 'TtlShrhldgBal', FinancialInstrumentQuantity18Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctSubLvl', type=AccountSubLevel24, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification195Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrhldgBalOnClntAcct', type=FinancialInstrumentQuantity18Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrhldgBalOnOwnAcct', type=FinancialInstrumentQuantity18Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlShrhldgBal', type=FinancialInstrumentQuantity18Choice, min=1, max=1, mutex_group=None, array=False),
	))