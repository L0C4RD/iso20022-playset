import base_types
import ReconciliationStatus2Code
import PairingStatus1Code
import YesNoIndicator
import ReconciliationStatus1Code
import TradeRepositoryReportingType1Code

class ReconciliationCategory5(base_types._BaseFieldType):

	__slots__ = ["_Rvvd", "_Pairg", "_RptgTp", "_ValtnRcncltn", "_FrthrMod", "_Rcncltn"]
	@property
	def Rvvd(self):
		return self._Rvvd

	@Rvvd.setter
	def Rvvd(self, value):
		self._Rvvd = value if type(value) != auto else self.make_default("Rvvd")

	@Rvvd.deleter
	def Rvvd(self):
		del self._Rvvd
		self._Rvvd = None

	@property
	def Pairg(self):
		return self._Pairg

	@Pairg.setter
	def Pairg(self, value):
		self._Pairg = value if type(value) != auto else self.make_default("Pairg")

	@Pairg.deleter
	def Pairg(self):
		del self._Pairg
		self._Pairg = None

	@property
	def RptgTp(self):
		return self._RptgTp

	@RptgTp.setter
	def RptgTp(self, value):
		self._RptgTp = value if type(value) != auto else self.make_default("RptgTp")

	@RptgTp.deleter
	def RptgTp(self):
		del self._RptgTp
		self._RptgTp = None

	@property
	def ValtnRcncltn(self):
		return self._ValtnRcncltn

	@ValtnRcncltn.setter
	def ValtnRcncltn(self, value):
		self._ValtnRcncltn = value if type(value) != auto else self.make_default("ValtnRcncltn")

	@ValtnRcncltn.deleter
	def ValtnRcncltn(self):
		del self._ValtnRcncltn
		self._ValtnRcncltn = None

	@property
	def FrthrMod(self):
		return self._FrthrMod

	@FrthrMod.setter
	def FrthrMod(self, value):
		self._FrthrMod = value if type(value) != auto else self.make_default("FrthrMod")

	@FrthrMod.deleter
	def FrthrMod(self):
		del self._FrthrMod
		self._FrthrMod = None

	@property
	def Rcncltn(self):
		return self._Rcncltn

	@Rcncltn.setter
	def Rcncltn(self, value):
		self._Rcncltn = value if type(value) != auto else self.make_default("Rcncltn")

	@Rcncltn.deleter
	def Rcncltn(self):
		del self._Rcncltn
		self._Rcncltn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rvvd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pairg', type=PairingStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgTp', type=TradeRepositoryReportingType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnRcncltn', type=ReconciliationStatus2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrthrMod', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcncltn', type=ReconciliationStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))

