# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PairingStatus1Code
from . import ReconciliationStatus1Code
from . import ReconciliationStatus2Code
from . import TradeRepositoryReportingType1Code
from . import YesNoIndicator

class ReconciliationCategory5(base_types._BaseFieldType):

	__slots__ = ["_FrthrMod", "_Pairg", "_Rcncltn", "_RptgTp", "_Rvvd", "_ValtnRcncltn"]
	@property
	def FrthrMod(self):
		return self._FrthrMod

	@FrthrMod.setter
	def FrthrMod(self, value):
		self._FrthrMod = value if value is not None else base_types.UninitialisedField(self, 'FrthrMod', YesNoIndicator, False)

	@FrthrMod.deleter
	def FrthrMod(self):
		del self._FrthrMod
		self._FrthrMod = base_types.UninitialisedField(self, 'FrthrMod', YesNoIndicator, False)

	@property
	def Pairg(self):
		return self._Pairg

	@Pairg.setter
	def Pairg(self, value):
		self._Pairg = value if value is not None else base_types.UninitialisedField(self, 'Pairg', PairingStatus1Code, False)

	@Pairg.deleter
	def Pairg(self):
		del self._Pairg
		self._Pairg = base_types.UninitialisedField(self, 'Pairg', PairingStatus1Code, False)

	@property
	def Rcncltn(self):
		return self._Rcncltn

	@Rcncltn.setter
	def Rcncltn(self, value):
		self._Rcncltn = value if value is not None else base_types.UninitialisedField(self, 'Rcncltn', ReconciliationStatus1Code, False)

	@Rcncltn.deleter
	def Rcncltn(self):
		del self._Rcncltn
		self._Rcncltn = base_types.UninitialisedField(self, 'Rcncltn', ReconciliationStatus1Code, False)

	@property
	def RptgTp(self):
		return self._RptgTp

	@RptgTp.setter
	def RptgTp(self, value):
		self._RptgTp = value if value is not None else base_types.UninitialisedField(self, 'RptgTp', TradeRepositoryReportingType1Code, False)

	@RptgTp.deleter
	def RptgTp(self):
		del self._RptgTp
		self._RptgTp = base_types.UninitialisedField(self, 'RptgTp', TradeRepositoryReportingType1Code, False)

	@property
	def Rvvd(self):
		return self._Rvvd

	@Rvvd.setter
	def Rvvd(self, value):
		self._Rvvd = value if value is not None else base_types.UninitialisedField(self, 'Rvvd', YesNoIndicator, False)

	@Rvvd.deleter
	def Rvvd(self):
		del self._Rvvd
		self._Rvvd = base_types.UninitialisedField(self, 'Rvvd', YesNoIndicator, False)

	@property
	def ValtnRcncltn(self):
		return self._ValtnRcncltn

	@ValtnRcncltn.setter
	def ValtnRcncltn(self, value):
		self._ValtnRcncltn = value if value is not None else base_types.UninitialisedField(self, 'ValtnRcncltn', ReconciliationStatus2Code, False)

	@ValtnRcncltn.deleter
	def ValtnRcncltn(self):
		del self._ValtnRcncltn
		self._ValtnRcncltn = base_types.UninitialisedField(self, 'ValtnRcncltn', ReconciliationStatus2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrthrMod', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pairg', type=PairingStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcncltn', type=ReconciliationStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgTp', type=TradeRepositoryReportingType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rvvd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnRcncltn', type=ReconciliationStatus2Code, min=1, max=1, mutex_group=None, array=False),
	))