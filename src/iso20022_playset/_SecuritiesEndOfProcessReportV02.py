# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ConfirmationParties7
from . import Pagination1
from . import PartyIdentificationAndAccount220
from . import Report6
from . import SupplementaryData1

class SecuritiesEndOfProcessReportV02(base_types._BaseFieldType):

	__slots__ = ["_ConfPties", "_Invstr", "_Pgntn", "_RptGnlDtls", "_SplmtryData"]
	@property
	def ConfPties(self):
		return self._ConfPties

	@ConfPties.setter
	def ConfPties(self, value):
		self._ConfPties = value if value is not None else base_types.UninitialisedField(self, 'ConfPties', ConfirmationParties7, True)

	@ConfPties.deleter
	def ConfPties(self):
		del self._ConfPties
		self._ConfPties = base_types.UninitialisedField(self, 'ConfPties', ConfirmationParties7, True)

	@property
	def Invstr(self):
		return self._Invstr

	@Invstr.setter
	def Invstr(self, value):
		self._Invstr = value if value is not None else base_types.UninitialisedField(self, 'Invstr', PartyIdentificationAndAccount220, True)

	@Invstr.deleter
	def Invstr(self):
		del self._Invstr
		self._Invstr = base_types.UninitialisedField(self, 'Invstr', PartyIdentificationAndAccount220, True)

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if value is not None else base_types.UninitialisedField(self, 'Pgntn', Pagination1, True)

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = base_types.UninitialisedField(self, 'Pgntn', Pagination1, True)

	@property
	def RptGnlDtls(self):
		return self._RptGnlDtls

	@RptGnlDtls.setter
	def RptGnlDtls(self, value):
		self._RptGnlDtls = value if value is not None else base_types.UninitialisedField(self, 'RptGnlDtls', Report6, False)

	@RptGnlDtls.deleter
	def RptGnlDtls(self):
		del self._RptGnlDtls
		self._RptGnlDtls = base_types.UninitialisedField(self, 'RptGnlDtls', Report6, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ConfPties', type=ConfirmationParties7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Invstr', type=PartyIdentificationAndAccount220, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptGnlDtls', type=Report6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))