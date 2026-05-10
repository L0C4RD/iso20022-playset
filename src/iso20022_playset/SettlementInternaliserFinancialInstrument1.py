from . import base_types
import InternalisationData1

class SettlementInternaliserFinancialInstrument1(base_types._BaseFieldType):

	__slots__ = ["_XchgTradgFnds", "_Bd", "_Eqty", "_SvrgnDebt", "_CllctvInvstmtUdrtkgs", "_MnyMktInstrm", "_EmssnAllwnc", "_OthrTrfblScties", "_OthrFinInstrms"]
	@property
	def XchgTradgFnds(self):
		return self._XchgTradgFnds

	@XchgTradgFnds.setter
	def XchgTradgFnds(self, value):
		self._XchgTradgFnds = value if type(value) != auto else self.make_default("XchgTradgFnds")

	@XchgTradgFnds.deleter
	def XchgTradgFnds(self):
		del self._XchgTradgFnds
		self._XchgTradgFnds = None

	@property
	def Bd(self):
		return self._Bd

	@Bd.setter
	def Bd(self, value):
		self._Bd = value if type(value) != auto else self.make_default("Bd")

	@Bd.deleter
	def Bd(self):
		del self._Bd
		self._Bd = None

	@property
	def Eqty(self):
		return self._Eqty

	@Eqty.setter
	def Eqty(self, value):
		self._Eqty = value if type(value) != auto else self.make_default("Eqty")

	@Eqty.deleter
	def Eqty(self):
		del self._Eqty
		self._Eqty = None

	@property
	def SvrgnDebt(self):
		return self._SvrgnDebt

	@SvrgnDebt.setter
	def SvrgnDebt(self, value):
		self._SvrgnDebt = value if type(value) != auto else self.make_default("SvrgnDebt")

	@SvrgnDebt.deleter
	def SvrgnDebt(self):
		del self._SvrgnDebt
		self._SvrgnDebt = None

	@property
	def CllctvInvstmtUdrtkgs(self):
		return self._CllctvInvstmtUdrtkgs

	@CllctvInvstmtUdrtkgs.setter
	def CllctvInvstmtUdrtkgs(self, value):
		self._CllctvInvstmtUdrtkgs = value if type(value) != auto else self.make_default("CllctvInvstmtUdrtkgs")

	@CllctvInvstmtUdrtkgs.deleter
	def CllctvInvstmtUdrtkgs(self):
		del self._CllctvInvstmtUdrtkgs
		self._CllctvInvstmtUdrtkgs = None

	@property
	def MnyMktInstrm(self):
		return self._MnyMktInstrm

	@MnyMktInstrm.setter
	def MnyMktInstrm(self, value):
		self._MnyMktInstrm = value if type(value) != auto else self.make_default("MnyMktInstrm")

	@MnyMktInstrm.deleter
	def MnyMktInstrm(self):
		del self._MnyMktInstrm
		self._MnyMktInstrm = None

	@property
	def EmssnAllwnc(self):
		return self._EmssnAllwnc

	@EmssnAllwnc.setter
	def EmssnAllwnc(self, value):
		self._EmssnAllwnc = value if type(value) != auto else self.make_default("EmssnAllwnc")

	@EmssnAllwnc.deleter
	def EmssnAllwnc(self):
		del self._EmssnAllwnc
		self._EmssnAllwnc = None

	@property
	def OthrTrfblScties(self):
		return self._OthrTrfblScties

	@OthrTrfblScties.setter
	def OthrTrfblScties(self, value):
		self._OthrTrfblScties = value if type(value) != auto else self.make_default("OthrTrfblScties")

	@OthrTrfblScties.deleter
	def OthrTrfblScties(self):
		del self._OthrTrfblScties
		self._OthrTrfblScties = None

	@property
	def OthrFinInstrms(self):
		return self._OthrFinInstrms

	@OthrFinInstrms.setter
	def OthrFinInstrms(self, value):
		self._OthrFinInstrms = value if type(value) != auto else self.make_default("OthrFinInstrms")

	@OthrFinInstrms.deleter
	def OthrFinInstrms(self):
		del self._OthrFinInstrms
		self._OthrFinInstrms = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='XchgTradgFnds', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bd', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Eqty', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvrgnDebt', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CllctvInvstmtUdrtkgs', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MnyMktInstrm', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmssnAllwnc', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTrfblScties', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrFinInstrms', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
	))

