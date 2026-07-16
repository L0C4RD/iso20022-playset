# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SettlementFailsDailyTransactionType1Choice

class SettlementFailsDailyInstrument3(base_types._BaseFieldType):

	__slots__ = ["_Bd", "_CllctvInvstmtUdrtkgs", "_EmssnAllwnc", "_Eqty", "_MnyMktInstrm", "_Othr", "_OthrTrfblScties", "_SvrgnDebt", "_XchgTraddFnds"]
	@property
	def Bd(self):
		return self._Bd

	@Bd.setter
	def Bd(self, value):
		self._Bd = value if value is not None else base_types.UninitialisedField(self, 'Bd', SettlementFailsDailyTransactionType1Choice, False)

	@Bd.deleter
	def Bd(self):
		del self._Bd
		self._Bd = base_types.UninitialisedField(self, 'Bd', SettlementFailsDailyTransactionType1Choice, False)

	@property
	def CllctvInvstmtUdrtkgs(self):
		return self._CllctvInvstmtUdrtkgs

	@CllctvInvstmtUdrtkgs.setter
	def CllctvInvstmtUdrtkgs(self, value):
		self._CllctvInvstmtUdrtkgs = value if value is not None else base_types.UninitialisedField(self, 'CllctvInvstmtUdrtkgs', SettlementFailsDailyTransactionType1Choice, False)

	@CllctvInvstmtUdrtkgs.deleter
	def CllctvInvstmtUdrtkgs(self):
		del self._CllctvInvstmtUdrtkgs
		self._CllctvInvstmtUdrtkgs = base_types.UninitialisedField(self, 'CllctvInvstmtUdrtkgs', SettlementFailsDailyTransactionType1Choice, False)

	@property
	def EmssnAllwnc(self):
		return self._EmssnAllwnc

	@EmssnAllwnc.setter
	def EmssnAllwnc(self, value):
		self._EmssnAllwnc = value if value is not None else base_types.UninitialisedField(self, 'EmssnAllwnc', SettlementFailsDailyTransactionType1Choice, False)

	@EmssnAllwnc.deleter
	def EmssnAllwnc(self):
		del self._EmssnAllwnc
		self._EmssnAllwnc = base_types.UninitialisedField(self, 'EmssnAllwnc', SettlementFailsDailyTransactionType1Choice, False)

	@property
	def Eqty(self):
		return self._Eqty

	@Eqty.setter
	def Eqty(self, value):
		self._Eqty = value if value is not None else base_types.UninitialisedField(self, 'Eqty', SettlementFailsDailyTransactionType1Choice, False)

	@Eqty.deleter
	def Eqty(self):
		del self._Eqty
		self._Eqty = base_types.UninitialisedField(self, 'Eqty', SettlementFailsDailyTransactionType1Choice, False)

	@property
	def MnyMktInstrm(self):
		return self._MnyMktInstrm

	@MnyMktInstrm.setter
	def MnyMktInstrm(self, value):
		self._MnyMktInstrm = value if value is not None else base_types.UninitialisedField(self, 'MnyMktInstrm', SettlementFailsDailyTransactionType1Choice, False)

	@MnyMktInstrm.deleter
	def MnyMktInstrm(self):
		del self._MnyMktInstrm
		self._MnyMktInstrm = base_types.UninitialisedField(self, 'MnyMktInstrm', SettlementFailsDailyTransactionType1Choice, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', SettlementFailsDailyTransactionType1Choice, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', SettlementFailsDailyTransactionType1Choice, False)

	@property
	def OthrTrfblScties(self):
		return self._OthrTrfblScties

	@OthrTrfblScties.setter
	def OthrTrfblScties(self, value):
		self._OthrTrfblScties = value if value is not None else base_types.UninitialisedField(self, 'OthrTrfblScties', SettlementFailsDailyTransactionType1Choice, False)

	@OthrTrfblScties.deleter
	def OthrTrfblScties(self):
		del self._OthrTrfblScties
		self._OthrTrfblScties = base_types.UninitialisedField(self, 'OthrTrfblScties', SettlementFailsDailyTransactionType1Choice, False)

	@property
	def SvrgnDebt(self):
		return self._SvrgnDebt

	@SvrgnDebt.setter
	def SvrgnDebt(self, value):
		self._SvrgnDebt = value if value is not None else base_types.UninitialisedField(self, 'SvrgnDebt', SettlementFailsDailyTransactionType1Choice, False)

	@SvrgnDebt.deleter
	def SvrgnDebt(self):
		del self._SvrgnDebt
		self._SvrgnDebt = base_types.UninitialisedField(self, 'SvrgnDebt', SettlementFailsDailyTransactionType1Choice, False)

	@property
	def XchgTraddFnds(self):
		return self._XchgTraddFnds

	@XchgTraddFnds.setter
	def XchgTraddFnds(self, value):
		self._XchgTraddFnds = value if value is not None else base_types.UninitialisedField(self, 'XchgTraddFnds', SettlementFailsDailyTransactionType1Choice, False)

	@XchgTraddFnds.deleter
	def XchgTraddFnds(self):
		del self._XchgTraddFnds
		self._XchgTraddFnds = base_types.UninitialisedField(self, 'XchgTraddFnds', SettlementFailsDailyTransactionType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bd', type=SettlementFailsDailyTransactionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CllctvInvstmtUdrtkgs', type=SettlementFailsDailyTransactionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmssnAllwnc', type=SettlementFailsDailyTransactionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Eqty', type=SettlementFailsDailyTransactionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MnyMktInstrm', type=SettlementFailsDailyTransactionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=SettlementFailsDailyTransactionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTrfblScties', type=SettlementFailsDailyTransactionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvrgnDebt', type=SettlementFailsDailyTransactionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgTraddFnds', type=SettlementFailsDailyTransactionType1Choice, min=1, max=1, mutex_group=None, array=False),
	))