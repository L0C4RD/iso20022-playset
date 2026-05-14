# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ConfirmationParties7 import ConfirmationParties7
from ._Pagination1 import Pagination1
from ._PartyIdentificationAndAccount220 import PartyIdentificationAndAccount220
from ._Report6 import Report6
from ._SupplementaryData1 import SupplementaryData1

class SecuritiesEndOfProcessReportV02(base_types._BaseFieldType):

	__slots__ = ["_ConfPties", "_Invstr", "_Pgntn", "_RptGnlDtls", "_SplmtryData"]
	@property
	def ConfPties(self):
		return self._ConfPties

	@ConfPties.setter
	def ConfPties(self, value):
		self._ConfPties = value if type(value) != base_types.auto else self.make_default("ConfPties")

	@ConfPties.deleter
	def ConfPties(self):
		del self._ConfPties
		self._ConfPties = None

	@property
	def Invstr(self):
		return self._Invstr

	@Invstr.setter
	def Invstr(self, value):
		self._Invstr = value if type(value) != base_types.auto else self.make_default("Invstr")

	@Invstr.deleter
	def Invstr(self):
		del self._Invstr
		self._Invstr = None

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != base_types.auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	@property
	def RptGnlDtls(self):
		return self._RptGnlDtls

	@RptGnlDtls.setter
	def RptGnlDtls(self, value):
		self._RptGnlDtls = value if type(value) != base_types.auto else self.make_default("RptGnlDtls")

	@RptGnlDtls.deleter
	def RptGnlDtls(self):
		del self._RptGnlDtls
		self._RptGnlDtls = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ConfPties', type=ConfirmationParties7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Invstr', type=PartyIdentificationAndAccount220, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptGnlDtls', type=Report6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))