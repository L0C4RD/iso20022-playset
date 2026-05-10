from . import base_types
import SettlementTotalData1Choice

class SettlementFailsInstrument2(base_types._BaseFieldType):

	__slots__ = ["_Bd", "_OthrTrfblScties", "_XchgTraddFnds", "_SvrgnDebt", "_Eqty", "_MnyMktInstrm", "_CllctvInvstmtUdrtkgs", "_EmssnAllwnc", "_Othr"]
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
	def XchgTraddFnds(self):
		return self._XchgTraddFnds

	@XchgTraddFnds.setter
	def XchgTraddFnds(self, value):
		self._XchgTraddFnds = value if type(value) != auto else self.make_default("XchgTraddFnds")

	@XchgTraddFnds.deleter
	def XchgTraddFnds(self):
		del self._XchgTraddFnds
		self._XchgTraddFnds = None

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
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bd', type=SettlementTotalData1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTrfblScties', type=SettlementTotalData1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgTraddFnds', type=SettlementTotalData1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvrgnDebt', type=SettlementTotalData1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Eqty', type=SettlementTotalData1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MnyMktInstrm', type=SettlementTotalData1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CllctvInvstmtUdrtkgs', type=SettlementTotalData1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmssnAllwnc', type=SettlementTotalData1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=SettlementTotalData1Choice, min=1, max=1, mutex_group=None, array=False),
	))

