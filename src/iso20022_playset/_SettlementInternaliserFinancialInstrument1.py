# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InternalisationData1

class SettlementInternaliserFinancialInstrument1(base_types._BaseFieldType):

	__slots__ = ["_Bd", "_CllctvInvstmtUdrtkgs", "_EmssnAllwnc", "_Eqty", "_MnyMktInstrm", "_OthrFinInstrms", "_OthrTrfblScties", "_SvrgnDebt", "_XchgTradgFnds"]
	@property
	def Bd(self):
		return self._Bd

	@Bd.setter
	def Bd(self, value):
		self._Bd = value if value is not None else base_types.UninitialisedField(self, 'Bd', InternalisationData1, False)

	@Bd.deleter
	def Bd(self):
		del self._Bd
		self._Bd = base_types.UninitialisedField(self, 'Bd', InternalisationData1, False)

	@property
	def CllctvInvstmtUdrtkgs(self):
		return self._CllctvInvstmtUdrtkgs

	@CllctvInvstmtUdrtkgs.setter
	def CllctvInvstmtUdrtkgs(self, value):
		self._CllctvInvstmtUdrtkgs = value if value is not None else base_types.UninitialisedField(self, 'CllctvInvstmtUdrtkgs', InternalisationData1, False)

	@CllctvInvstmtUdrtkgs.deleter
	def CllctvInvstmtUdrtkgs(self):
		del self._CllctvInvstmtUdrtkgs
		self._CllctvInvstmtUdrtkgs = base_types.UninitialisedField(self, 'CllctvInvstmtUdrtkgs', InternalisationData1, False)

	@property
	def EmssnAllwnc(self):
		return self._EmssnAllwnc

	@EmssnAllwnc.setter
	def EmssnAllwnc(self, value):
		self._EmssnAllwnc = value if value is not None else base_types.UninitialisedField(self, 'EmssnAllwnc', InternalisationData1, False)

	@EmssnAllwnc.deleter
	def EmssnAllwnc(self):
		del self._EmssnAllwnc
		self._EmssnAllwnc = base_types.UninitialisedField(self, 'EmssnAllwnc', InternalisationData1, False)

	@property
	def Eqty(self):
		return self._Eqty

	@Eqty.setter
	def Eqty(self, value):
		self._Eqty = value if value is not None else base_types.UninitialisedField(self, 'Eqty', InternalisationData1, False)

	@Eqty.deleter
	def Eqty(self):
		del self._Eqty
		self._Eqty = base_types.UninitialisedField(self, 'Eqty', InternalisationData1, False)

	@property
	def MnyMktInstrm(self):
		return self._MnyMktInstrm

	@MnyMktInstrm.setter
	def MnyMktInstrm(self, value):
		self._MnyMktInstrm = value if value is not None else base_types.UninitialisedField(self, 'MnyMktInstrm', InternalisationData1, False)

	@MnyMktInstrm.deleter
	def MnyMktInstrm(self):
		del self._MnyMktInstrm
		self._MnyMktInstrm = base_types.UninitialisedField(self, 'MnyMktInstrm', InternalisationData1, False)

	@property
	def OthrFinInstrms(self):
		return self._OthrFinInstrms

	@OthrFinInstrms.setter
	def OthrFinInstrms(self, value):
		self._OthrFinInstrms = value if value is not None else base_types.UninitialisedField(self, 'OthrFinInstrms', InternalisationData1, False)

	@OthrFinInstrms.deleter
	def OthrFinInstrms(self):
		del self._OthrFinInstrms
		self._OthrFinInstrms = base_types.UninitialisedField(self, 'OthrFinInstrms', InternalisationData1, False)

	@property
	def OthrTrfblScties(self):
		return self._OthrTrfblScties

	@OthrTrfblScties.setter
	def OthrTrfblScties(self, value):
		self._OthrTrfblScties = value if value is not None else base_types.UninitialisedField(self, 'OthrTrfblScties', InternalisationData1, False)

	@OthrTrfblScties.deleter
	def OthrTrfblScties(self):
		del self._OthrTrfblScties
		self._OthrTrfblScties = base_types.UninitialisedField(self, 'OthrTrfblScties', InternalisationData1, False)

	@property
	def SvrgnDebt(self):
		return self._SvrgnDebt

	@SvrgnDebt.setter
	def SvrgnDebt(self, value):
		self._SvrgnDebt = value if value is not None else base_types.UninitialisedField(self, 'SvrgnDebt', InternalisationData1, False)

	@SvrgnDebt.deleter
	def SvrgnDebt(self):
		del self._SvrgnDebt
		self._SvrgnDebt = base_types.UninitialisedField(self, 'SvrgnDebt', InternalisationData1, False)

	@property
	def XchgTradgFnds(self):
		return self._XchgTradgFnds

	@XchgTradgFnds.setter
	def XchgTradgFnds(self, value):
		self._XchgTradgFnds = value if value is not None else base_types.UninitialisedField(self, 'XchgTradgFnds', InternalisationData1, False)

	@XchgTradgFnds.deleter
	def XchgTradgFnds(self):
		del self._XchgTradgFnds
		self._XchgTradgFnds = base_types.UninitialisedField(self, 'XchgTradgFnds', InternalisationData1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bd', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CllctvInvstmtUdrtkgs', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmssnAllwnc', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Eqty', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MnyMktInstrm', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrFinInstrms', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTrfblScties', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvrgnDebt', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgTradgFnds', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
	))